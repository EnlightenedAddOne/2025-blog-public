> 来源：Obsidian/20-技术知识库/docker部署/Fastapi项目部署.md

**项目目录**

```
fastapi-docker_learn\
│
├── app/              # 应用程序主文件夹
│   ├── __init__.py   # Python包初始化文件
│   └── main.py       # FastAPI应用主文件
├── Dockerfile        # Docker容器配置文件
├── requirements.txt  # Python依赖项列表
```

# 1.创建requirements.txt

```
pip freeze > requirements.txt
#列出所需的库到requirements.txt文件
```

# 2.创建Dockerfile

```
#从官方Python基础镜像开始。
FROM python:3.12-slim

#将当前工作目录设置为/code。这是我们放置requirements.txt文件和app目录的位置。
WORKDIR /code

#将符合要求的文件复制到/code目录中。
 #首先仅复制requirements.txt文件，而不复制其余代码。
 #由于此文件不经常更改，Docker 将检测到它并在这一步中使用缓存，从而为下一步启用缓存。
COPY ./requirements.txt /code/requirements.txt

#安装需求文件中的包依赖项。
 # #--no-cache-dir 选项告诉 pip 不要在本地保存下载的包，因为只有当 pip 再次运行以安装相同的包时才会这样，但在与容器一起工作时情况并非如此。
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#将“./app”目录复制到“/code”目录中。
 # #由于其中包含更改最频繁的所有代码，因此 Docker 缓存不会轻易用于此操作或任何后续步骤。
 # #因此，将其放在Dockerfile接近最后的位置非常重要，以优化容器镜像的构建时间。
COPY ./app /code/app

# 暴露应用运行的端口
EXPOSE 8000
#设置命令来运行 uvicorn 服务器。
 # #CMD 接受一个字符串列表，每个字符串都是你在命令行中输入的内容，并用空格分隔。
 # #该命令将从 当前工作目录 运行，即你上面使用WORKDIR /code设置的同一/code目录。
 # #因为程序将从/code启动，并且其中包含你的代码的目录./app，所以Uvicorn将能够从app.main中查看并importapp。
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

# 3.构建 Docker 镜像

首先，您需要构建 Docker 镜像。在项目根目录下执行以下命令：

```bash
docker build -t fastapi-docker_learn .
```

这个命令会根据您的 Dockerfile 构建一个名为 fastapi-docker_learn 的镜像。

# 4. 运行 Docker 容器

构建完成后，您可以运行容器：

```bash
docker run -d --name fastapi-app -p 8000:8000 fastapi-docker_learn
```

这个命令会：

- -d : 在后台运行容器
- --name fastapi-app : 将容器命名为 "fastapi-app"
- -p 8000:8000 : 将主机的 8000 端口映射到容器的 8000 端口
- fastapi-docker_learn : 使用我们刚刚构建的镜像

# 5. 管理容器

如果需要停止容器：

```bash
docker stop fastapi-app
```

如果需要重新启动容器：

```bash
docker start fastapi-app
```

如果需要删除容器：

```bash
docker rm fastapi-app
```
