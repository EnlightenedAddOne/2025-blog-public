项目简介：
	前端：Vue
	后端：Python-flask框架

---
# 本地docker结构搭建
## vue项目打包
- 使用在终端执行以下命令
```bash
# 进入Vue项目目录
cd d:\PROJECT\Python\test01\front-end\vue-font

# 构建项目
npm run build
```
- 构建完成后，会在项目目录下生成一个 dist 文件夹，里面包含了所有构建好的静态文件。

## 编写Dockerfile文件
- 分别在前后端项目文件目录下编写Dockerfile文件
```
Project\
 |
 |__flask_end\
 |      |
 |      |__app.py
 |      |__Dockerfile
 |      |__requirements.txt
 |
 |__vue_font\
 |      |
 |      |__src\
 |      |    |
 |      |    |__App.vue
 |      |
 |      |__Dockerfile
 |
 |__docker-compose.yml
```

## 压缩上传

将**Project**文件夹压缩，然后上传至服务器

# 服务器操作

注意：需要先配置好服务器环境，例如*nginx、docker、docker-compose、mysql等*
Linux命令查询网站：[Linux命令大全(手册)](https://www.linuxcool.com/)

---
## 新建项目目录

```
mkdir 文件名
```

将在本地的项目压缩包传到创建好的文件夹内

## 解压

```
unzip  压缩包.zip
```

## 构建Docker镜像

- 解压完后进入项目目录
- 构建Docker镜像
```
docker compose build
```
- 启动docker
```
docker compose up -d     # -d 参数 后台运行
```
- 停止命令
```
docker compose down
```

- 其他调试用到的docker命令
> 查看运行中的容器：docker compose ps
> 查看容器日志：docker compose logs -f





