> 来源：Obsidian/30-项目与实践/项目说明/图书管理系统说明/服务器部署.md

# 一、前期准备

## 1. 申请一个服务器

以腾讯云服务器为例

访问：[轻量应用服务器Lighthouse*香港轻量服务器*海外轻量服务器-腾讯云](https://cloud.tencent.com/product/lighthouse?Is=sdk-topnav) 申请一个服务器，新用户可以免费使用一个月。

在申请时会让你选择服务器系统，这里我使用的是`Ubuntu22.04-Docker26-1NZ1` 它自带腾讯的docker镜像

申请成功后可以在[站内信 - 控制台](https://console.cloud.tencent.com/message) 内看到创建成功的消息，里面有远程连接的用户名和密码
![Pasted image 20250803122232](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513358.png)

然后前往[服务器 - 轻量云 - 控制台](https://console.cloud.tencent.com/lighthouse/instance/index?rid=1)启动服务器
![Pasted image 20250803122842](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513359.png)
![Pasted image 20250803123121](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513360.png)

登录服务器，可以直接点击上图中的`登录` 或者使用远程连接工具，我使用的是`Xshell` ,打开Xhell后点击`新建会话` ，填写下面内容连接即可
![Pasted image 20250803123533](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513361.png)![Pasted image 20250803123612](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513362.png)
成功连接
![Pasted image 20250803123841](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513363.png)

## 2.后端配置

修改`application.properties`文件中的数据库配置
"填入你的服务器ip" 下面的 `library` 是数据库名称
![Pasted image 20250803124957](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513365.png)

使用`Maven`打成jar包，点击最左侧的M选择`package`
![Pasted image 20250803125157](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513366.png)

等待一会就会新出现一个名为`target`的文件夹，里面的后缀为`jar`的文件就是我们需要的
![Pasted image 20250803125518](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513367.png)

## 3.前端配置

若未初始化，先使用`pnpn i`初始化前端代码

修改`.env` `.env.development` `.env.production` 使用相对路径，避免跨域请求失败
![Pasted image 20250803132453](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513368.png)

修改完毕之后运行`pnpm build` 打包文件，完成后会看到目录内出现了一个`dist`的文件夹

# 二、docker配置

## 1.安装Docker和Docker Compose

我选择的这个系统已经提前下载好了Docker和Docker Compose，故这一步可以跳过。

检测是否已安装

```shell
docker --version
docker-compose --version
```

若返回对应的版本号，说明安装完成
![Pasted image 20250803133843](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513369.png)

如未提前安装，请自行搜索 `Ubuntu 安装 Docker、Docker Compose` 记得还要配置镜像，否则由于网络原因镜可能无法下载

## 2.设置文件目录

新建一个文件夹存放我们之前打包好的前后端文件，这个文件夹配置好之后要传到服务器上

![Pasted image 20250803134921](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513370.png)
文件夹结构

```
# []包裹的文件需要我们手动创建
# dist 和 library-0.0.1-SNAPSHOT.jar是我们打包生成的文件
# package.json 和 pnpm-lock.yaml 在前端代码根目录里，复制过来
book-management/
├── [docker-compose.yml]         # Docker Compose 编排文件
├── frontend/                    # 前端项目
│   ├── [Dockerfile]             # 前端 Docker 构建文件
│   ├── [nginx.conf]             # Nginx 配置
│   ├── package.json             # 前端依赖配置
│   ├── pnpm-lock.yaml           # 依赖锁定文件
│   └── dist/                    # 构建输出的静态资源
└── backend/                     # 后端项目
    ├── [Dockerfile]             # 后端 Docker 构建文件
    └── library-0.0.1-SNAPSHOT.jar  # 后端可执行 Jar 包
```

## 3.docker代码编写

### 1.后端

#### Dockerfile

```Dockerfile
FROM eclipse-temurin:17-jre-alpine

# 安装 curl 用于健康检查
RUN apk add --no-cache curl

WORKDIR /app

# 复制jar包
COPY library-0.0.1-SNAPSHOT.jar app.jar

# 暴露端口
EXPOSE 8080

# 启动应用
ENTRYPOINT ["java", "-jar", "app.jar"]

```

### 2.前端

#### Dockerfile

```Dockerfile
# 直接使用 nginx 提供静态文件服务
FROM nginx:alpine

# 复制已构建好的静态文件
COPY dist/ /usr/share/nginx/html/

# 复制nginx配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

#### nginx

```nginx
server {
    listen 80;
    server_name localhost;

    root /usr/share/nginx/html;
    index index.html;

    # 前端路由
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API代理 - 增强CORS支持
    location /api/ {
        proxy_pass http://backend:8080/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Content-Type application/json;

        # CORS设置
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
        add_header Access-Control-Allow-Headers "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization";

        # 处理预检请求
        if ($request_method = 'OPTIONS') {
            add_header Access-Control-Allow-Origin *;
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
            add_header Access-Control-Allow-Headers "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization";
            add_header Access-Control-Max-Age 1728000;
            add_header Content-Type 'text/plain; charset=utf-8';
            add_header Content-Length 0;
            return 204;
        }
    }

    # 静态资源缓存
    location ~* \.(js|css|png|jpg|jpeg|gif|ico|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}

```

### 根目录

#### docker-compose.yml

```yml
services:
  database:
    image: mysql:8.0
    container_name: book-database
    environment:
      - MYSQL_ROOT_PASSWORD=0128
      - MYSQL_DATABASE=library
      - MYSQL_USER=book_app_user
      - MYSQL_PASSWORD=SecurePassword123!
    volumes:
      - db_data:/var/lib/mysql
    restart: unless-stopped
    networks:
      - book-network
    ports:
      - '3306:3306' # 添加端口映射
    healthcheck:
      test: ['CMD', 'mysqladmin', 'ping', '-h', 'localhost']
      timeout: 20s
      retries: 10
  frontend:
    build: ./frontend
    container_name: book-frontend
    ports:
      - '80:80'
    restart: unless-stopped
    networks:
      - book-network
    depends_on:
      - backend

  backend:
    build: ./backend
    container_name: book-backend
    environment:
      - SPRING_PROFILES_ACTIVE=prod
      - SPRING_DATASOURCE_URL=jdbc:mysql://database:3306/library
      - SPRING_DATASOURCE_USERNAME=book_app_user
      - SPRING_DATASOURCE_PASSWORD=SecurePassword123!
    restart: unless-stopped
    networks:
      - book-network
    depends_on:
      database:
        condition: service_healthy

volumes:
  db_data:

networks:
  book-network:
    driver: bridge
```

# 三、服务器配置

## 1.文件上传服务器

将上一步配置好的文件夹压缩为zip文件，打开Xshell，点击Xftp
![Pasted image 20250803142354](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513371.png)

新建文件夹，然后将zip文件拖入对应文件夹
![Pasted image 20250803142459](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513372.png)

在服务上安装解压缩程序

```bash
sudo apt update
sudo apt install unzip -y
```

解压 zip 文件

```
unzip file.zip
```

## 2.docker部署

解压后进入项目文件夹，执行docker命令

```docker
docker-compose up -d
```

等待文件下载完毕，若无报错，查看服务状态

```
# 查看服务状态
docker-compose ps
```

若也正常，打卡浏览器，输入你的服务器IP看是否正常加载

## 3.导入sql数据

打开数据库操作工具，这里使用的是idea自带的数据库工具

![Pasted image 20250803144347](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513373.png)![Pasted image 20250803144533](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513374.png)
打开sql文件，选择刚才连接的数据源，然后执行SQL代码，即可载入数据

![Pasted image 20250803145039](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513375.png)

# 四、结束

演示视频：[图书管理系统演示视频\_哔哩哔哩\_bilibili](https://www.bilibili.com/video/BV1uhguzJEYH/?spm_id_from=333.1387.homepage.video_card.click&vd_source=e88731727a722c629c5950e91da85296)

![Pasted image 20250803150832](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513376.png)
![Pasted image 20250803150921](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513377.png)
![Pasted image 20250803150941](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513378.png)
![Pasted image 20250803150956](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513379.png)
![Pasted image 20250803151010](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513380.png)
![Pasted image 20250803151020](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513381.png)
![Pasted image 20250803151150](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508031513382.png)

---

参考文档：
[超详细Docker部署SpringBoot+Vue项目（三更博客项目部署）\_三更博客部署-CSDN博客](https://blog.csdn.net/qq_52030824/article/details/127982206)
[如何从零将vue+springboot项目打包部署到云服务器（亲测，图文教程超详细！！）\_spring boot vue 部署 图解-CSDN博客](https://blog.csdn.net/xiguagaizi88/article/details/111272195)
