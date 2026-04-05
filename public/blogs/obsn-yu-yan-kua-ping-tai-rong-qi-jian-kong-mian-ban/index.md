> 来源：Obsidian/30-项目与实践/项目说明/GO项目/Go语言-跨平台容器监控面板.md

# 🌐 MINI PORTAINER GLOBAL 跨端容器监控面板

## 📑 项目简介

MINI PORTAINER GLOBAL 是一套基于 Go 语言原生 Docker SDK 和 Vue3 编写的分布式监控与调度系统。

相比于传统的臃肿监控方案，本项目彻底摒弃了复杂的内网穿透（如 FRP、Tailscale），采用极其优雅的 **“心跳夹带（Heartbeat Piggybacking）”与信箱模式** ，完美实现了公网服务器对家庭内网设备（如 Raspberry Pi）的反向控制与日志拉取。编译产物体积极小（单文件十几MB），零环境依赖。

---

## ✨ 核心特性

- **⚡ 异构多端支持**：通过 Go 强大的交叉编译，完美兼容 x86 云服务器 (Linux/amd64) 与树莓派等 ARM 嵌入式设备 (Linux/arm64)。
- **🛡️ NAT 穿透免配**：边缘 Agent 主动采用 HTTP POST 轮询上报，利用云端 HTTP 响应“夹带”控制指令，无视任何家庭路由器防火墙。
- **📊 硬件与容器双擎监控**：实时读取底层 `/sys/class/thermal` 与 `/proc/meminfo`，结合 Docker SDK，全景展示 CPU 温度、内存占用及容器启停状态。
- **🕹️ 远程快照日志**：无需长连接，一键下发指令，边缘节点自动截取容器末尾 200 行干净日志并回传展示。
- **🎨 极客级暗黑大屏**：前端采用前后端分离架构，基于 Vue 3 + Ionicons + 原生 CSS 手搓，支持中英双语无缝切换、3秒无感动态刷新与内存进度条动画。
- **后台守护运行**：全面拥抱 Linux Systemd，实现进程保活、开机自启与标准日志托管。

---

## 🏗️ 技术架构与通信模型

本项目分为三大核心模块：**边缘执行节点 (Agent)**、**云端主控室 (Server)** 和 **前端大屏 (Web UI)**。

### 核心通信机制：信箱模式 (心跳指令下发)

为了解决内网设备无法被公网主动访问的痛点，系统采用以下流转逻辑：

1. **主动上报 (Push)**：Agent 每 5 秒将本机硬件和容器状态打包为 JSON，POST 发送给 Server。
2. **指令入匣 (Queue)**：用户在前端点击操作（如停止 `jiuguan` 容器），指令通过 API 存入 Server 内存的“该节点专属信箱”。
3. **顺手牵羊 (Piggybacking)**：Agent 下一次上报数据时，Server 在 HTTP 响应的 Body 中将信箱里的指令（如 `{"action": "stop", "container_id": "xxx"}`）下发给 Agent。
4. **边缘执行 (Execute)**：Agent 解析指令，调用底层 Docker SDK 启停容器或截取日志。

---

## 📂 目录结构

```Plaintext
📦 MiniPortainer-Project
 ┣ 📂 mini-portainer-agent        # 边缘节点探针 (部署于树莓派/各服务器)
 ┃ ┣ 📜 main.go                   # 核心上报、指令解析与 Docker 交互逻辑
 ┃ ┣ 📜 go.mod
 ┃ ┗ 📜 go.sum
 ┣ 📂 mini-portainer-server       # 云端 API 与静态服务器 (部署于阿里云)
 ┃ ┣ 📂 static                    # 前端静态资源
 ┃ ┃ ┣ 📜 index.html              # 页面骨架与弹窗 DOM
 ┃ ┃ ┣ 📜 app.js                  # Vue 3 核心逻辑、i18n 字典与轮询请求
 ┃ ┃ ┗ 📜 style.css               # 赛博暗黑风样式表
 ┃ ┣ 📜 main.go                   # 内存信箱、API 路由分发
 ┃ ┣ 📜 go.mod
 ┃ ┗ 📜 go.sum
```

---

## 🚀 编译与部署指南

### 1. 跨平台交叉编译 (在 Windows 开发机执行)

**针对云服务器 (Linux x86_64 / amd64):**

```PowerShell
# 编译 Server 端
$env:GOOS="linux"; $env:GOARCH="amd64"; go build -o server_linux main.go
# 编译 Agent 端 (云服务器自监控)
$env:GOOS="linux"; $env:GOARCH="amd64"; go build -o agent_aliyun main.go
```

**针对树莓派 3B (Linux ARM64):**

```PowerShell
# 编译边缘 Agent
$env:GOOS="linux"; $env:GOARCH="arm64"; go build -o agent_pi64 main.go
```

_编译完成后，使用 SFTP 将二进制文件和 `static` 文件夹上传至对应服务器。_

### 2. Systemd 守护进程配置 (在服务器/树莓派终端执行)

为了保证程序后台运行及开机自启，采用 `systemctl` 管理。

**云端 Server 服务 (`/etc/systemd/system/mini-server.service`):**

```Ini, TOML
[Unit]
Description=Mini Portainer Cloud Server
After=network.target

[Service]
Type=simple
WorkingDirectory=/root/MiniPortainer/   # 注意修改路径  ExecStart=/root/MiniPortainer/server_linux   # 注意修改路径
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

**边缘 Agent 服务 (`/etc/systemd/system/mini-agent.service`):**

_(注意修改为对应设备的绝对路径及执行文件名)_

```Ini, TOML
[Unit]
Description=Mini Portainer Agent
After=network.target docker.service

[Service]
Type=simple
WorkingDirectory=/root/project/MiniPortainer/   # 注意修改路径
ExecStart=/root/project/MiniPortainer/agent_pi64   # 注意修改路径
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

### 3. 服务启停命令

```Bash
# 重载系统配置
systemctl daemon-reload

# 启动并设置开机自启
systemctl enable --now mini-server
systemctl enable --now mini-agent

# 查看实时日志
journalctl -u mini-server -f
journalctl -u mini-agent -f

systemctl stop mini-server    # 停止
systemctl start mini-server   # 启动
systemctl restart mini-server # 重启
systemctl status mini-server  # 查看运行状态（有没有报错，是不是绿色的 active）

systemctl disable mini-agent  # 取消开机自启
```

---

## 💻 接口列表参考 (API Reference)

- `POST /api/report?node={name}`：Agent 上报节点状态，返回待执行指令。
- `GET /api/data`：前端拉取全盘节点快照数据。
- `POST /api/command?node={name}&action={action}&id={id}`：前端下发操作指令（入匣）。
- `POST /api/logs/submit?node={name}&id={id}`：Agent 回传提取后的容器 200 行快照日志。
- `GET /api/logs?node={name}&id={id}`：前端轮询提取暂存的日志文本。
