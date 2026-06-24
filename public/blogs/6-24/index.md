> 架构：旧安卓手机（执行端）+ 树莓派（控制端，DietPi/ARM64）+ ALAS（开源自动化脚本）+ Docker（最终运行形态）
> 本文记录从零开始的完整可行路径，以及过程中踩过的所有坑——尤其是 Python 3.13 在 ARM64 上的依赖地狱，希望能帮后来者少走弯路。

---

## 一、最终架构（The Golden Setup）

| 组件 | 选型 |
| --- | --- |
| 宿主机系统 | DietPi（基于 Debian 的精简版 Linux） |
| 硬件架构 | ARM64（树莓派） |
| 运行引擎 | Docker 容器 `littlemio/alas:latest`（社区编译的 ARM64 专属版） |
| 被控设备 | 实体安卓旧手机，USB 数据线直连 |
| 配置持久化 | 宿主机目录 `/root/AzurLaneAutoScript` 通过 `-v` 挂载进容器 |

**核心结论：在树莓派上部署 ALAS，不要纠结原生 Python 虚拟环境，直接用 Docker。** 原生路线最终会在 OCR 依赖的 `mxnet`（深度学习框架）上彻底卡死——官方从未发布过 ARM64 版本的 MXNet。这条路线唯一的价值是探明了"此路不通"，下面会说明为什么，但如果你只想要能跑的步骤，请直接跳到第三章。

![](/blogs/6-24/0dab68887388aa5a.jpg)

---

## 二、原理简述

- ALAS（Azur Lane Auto Script）通过 ADB 截图 + 模板匹配（OpenCV）识别游戏画面，再通过 ADB 模拟点击操作手机。
- 图像识别严格基于 **16:9（1280×720）** 比例开发，手机原生分辨率（尤其是异形屏，如 2400×1080）会导致识别错位甚至直接拒绝工作。
- 文字识别（OCR，用于读取委托、资源数量等文字）依赖 `cnocr`，而 `cnocr` 又强制依赖深度学习框架 `mxnet`。这是后续 ARM64 翻车的根源。

---

## 三、推荐部署步骤（精简版，跳过试错弯路）

### 阶段 1：旧手机准备

1. 清理后台应用，仅保留游戏本体和必要系统组件，保证内存/存储充足。
2. 开启开发者模式：`设置 → 关于手机 → 连续点击版本号 7 次`。
3. 开启 **USB 调试**；如果是小米/vivo/OPPO 等深度定制系统，**必须额外开启"USB调试（安全设置）/允许模拟点击"**，否则 ALAS 只能看画面、无法模拟点击。
4. 屏幕休眠设为"永不"，或开启"充电时屏幕不休眠"。

### 阶段 2：树莓派基础环境

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install adb git screen -y
```

> DietPi 等精简系统默认可能没装 `screen`，建议直接一起装上，用于后续后台挂起任务。

### 阶段 3：建立 ADB 连接

```bash
# 数据线连接手机后执行
adb devices
```

手机上会弹出调试授权弹窗，勾选"始终允许使用这台计算机调试"。再次执行 `adb devices`，看到设备号后跟 `device`（不是 `unauthorized`）即为连接成功，记下这串设备序列号。

### 阶段 4：修正手机分辨率（关键，避免后续识别失败）

```bash
# 先记录原始参数，方便日后恢复
adb shell wm size
adb shell wm density

# 强制改为标准 16:9（720P）
adb shell wm size 720x1280
adb shell wm density 320
```

执行后手机画面会闪烁或出现黑边，这是正常现象。**修改后必须在手机上彻底杀掉游戏后台并重新打开**，让游戏以新分辨率渲染。

如需恢复原状：

```bash
adb shell wm size reset
adb shell wm density reset
```

### 阶段 5：部署 ALAS（直接用 Docker，跳过原生环境）

```bash
# 安装 Docker（树莓派常见 docker.io 安装不完整，建议直接用官方脚本）
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

# 拉取并启动 ARM64 专属版 ALAS 容器
sudo docker run -d \
  --name alas-arm \
  --network host \
  --restart always \
  -e TZ=Asia/Shanghai \
  -v /root/AzurLaneAutoScript:/app/AzurLaneAutoScript \
  littlemio/alas:latest
```

如果拉取镜像时卡在 `context deadline exceeded`（国内直连 Docker Hub 不稳定），给 Docker 配置国内镜像加速：

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [
    "https://dockerpull.com",
    "https://docker.1panel.live",
    "https://docker.m.daocloud.io"
  ]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

再重新执行 `docker run` 命令即可（之前下载的层会复用缓存，很快）。

看到终端输出一长串容器 ID，即代表部署成功。

### 阶段 6：在 ALAS 网页面板中绑定设备

1. 等待 1～2 分钟让容器完成首次解压启动。
2. 浏览器访问 `http://树莓派局域网IP:22267`。
3. 在【模拟器设置】中，将默认的 `auto` 改为手机的 ADB 设备序列号（USB 直连一般就是设备的真实 Serial，例如 `AGRHVB3421000992`）。
4. 确保手机停在游戏主界面，点击"获取游戏截图"。看到清晰无黑边的 16:9 画面即为成功。
5. 左侧菜单勾选需要的日常任务，点击"启动"。

### 阶段 7（可选）：无线 ADB

如果不想一直插数据线：

```bash
# 数据线仍连接时执行
adb tcpip 5555
# 拔线后
adb connect 手机IP:5555
```

注意事项：

- 建议在路由器后台为手机绑定静态 IP（DHCP 预留），否则 IP 变化后需要重新填写设备地址。
- 手机断电重启后，无线调试端口会失效，需要重新插线执行一次 `adb tcpip 5555`。

---

## 四、日常维护命令

```bash
sudo docker logs -f alas-arm      # 实时查看运行日志
sudo docker stop alas-arm         # 停止
sudo docker start alas-arm        # 启动
sudo docker restart alas-arm      # 重启
```

容器加了 `--restart always`，树莓派断电重启后会自动拉起，无需任何人工干预。

---

## 五、踩坑记录（完整版，供排查参考）

这部分记录了在走向 Docker 方案之前，原生 Python 环境踩过的全部坑。如果你打算尝试原生部署（不推荐，但可能想了解原理），或者用 Docker 后依然遇到类似报错，可以对照排查。

### 坑 1：`pip3 install` 报 `externally-managed-environment`

**原因**：PEP 668 规范下，新版 Debian/DietPi 默认锁定全局 pip 安装权限。
**解法**：用虚拟环境隔离依赖（`sudo apt install python3-venv -y && python3 -m venv venv && source venv/bin/activate`），或简单粗暴加 `--break-system-packages` 参数。

### 坑 2：apt 镜像源 404 Not Found

**原因**：本地软件包索引与镜像站不同步。
**解法**：`sudo apt update`（必要时加 `--fix-missing`）后重试。

### 坑 3：编译 PyAV 报 `pkg-config is required`

**原因**：树莓派 ARM64 + Python 3.13 没有现成预编译包，pip 现场编译源码，但缺少编译工具链和 FFmpeg 开发头文件。
**解法**：`sudo apt install pkg-config build-essential libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev -y`

### 坑 4：SSH 断开导致长时间编译任务中断

**解法**：用 `screen` 创建持久虚拟终端（`screen -S alas`，挂起用 `Ctrl+A` 再按 `D`，恢复用 `screen -r alas`），或用 `nohup ... > log 2>&1 &` 后台运行并 `tail -f` 查看日志。

### 坑 5：底层 C 扩展包持续编译失败（根本性问题）

**现象**：`av`、`opencv-python`、`lxml`、`gevent`、`cffi`、`pyzmq`、`jellyfish`、`lz4`、`matplotlib`、`numpy`、`Pillow`、`PyYAML`、`pycryptodome`、`msgpack` 等十几个包先后报错，错误类型五花八门：
- `ModuleNotFoundError: No module named 'distutils'`（Python 3.13 彻底移除了 distutils）
- `No module named 'pipes'`（pyzmq 依赖的旧内置模块被删除）
- `Cargo, the Rust package manager, is not installed`（jellyfish 需要本地 Rust 编译环境）
- `AttributeError: 'build_ext' object has no attribute 'cython_sources'`（PyYAML 旧版打包脚本不兼容新 setuptools）
- `SafeConfigParser` 被移除（matplotlib 旧版）

**根本原因**：ALAS 官方 `requirements.txt` 锁定的全部是 2021～2022 年的老版本依赖，而 DietPi 上的 Python 3.13 是发布不久的新版本，标准库做了大量"瘦身"删除，新旧版本之间存在明显代沟。这些包大多含 C/C++/Rust 底层代码，在 ARM64 上又没有现成的预编译 wheel，只能现场编译，而编译脚本本身就是为老 Python 写的。

**统一解法（"系统包接管大法"）**：
1. 用 `sudo apt install python3-xxx` 让系统的 apt 源直接安装这些库的预编译版本（ARM64 官方仓库通常有适配版）。
2. 用 `sed -i '/^包名/d' requirements.txt` 把这些包从需求清单中删除，避免 pip 再去尝试编译它们。
3. 对于像 `cffi` 这种被删除后可能引发链式兼容问题的包，额外执行 `pip3 install setuptools` 打补丁。
4. 全部跑完后用国内镜像源加速剩余纯 Python 包：`pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt`

**易错点**：
- `sed` 默认区分大小写，多次因为 `Pillow` vs `pillow`、`PyYAML` vs `pyyaml` 大小写不一致导致"漏网之鱼"——建议直接用 `sed -i '/^[Pp]illow/d'` 或加 `/Id`（忽略大小写）参数。
- 终端里连续粘贴多行命令时，如果没有用 `&&` 连接或换行执行，**实际上只会执行第一行**，后面的命令会被忽略——这是导致"删了好像没删"的常见原因。

### 坑 6：`cnocr` 死锁旧版 numpy 引发链式崩溃

**现象**：即使已经用 apt 装好新版 numpy，`cnocr` 仍要求 `numpy<1.20.0`，导致 pip 试图下载老版本源码编译，再次失败。
**解法**：把 `cnocr`、`mxnet`、`gluoncv` 三个互相绑定的机器学习包从清单中删除，单独用 `--no-deps`（不安装依赖）参数强制安装：
```bash
pip3 install cnocr==1.2.2 mxnet==1.6.0 gluoncv==0.6.0 --no-deps -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 坑 7：`requests`/`urllib3` 太旧导致启动闪退

**现象**：核心依赖装完后 `python3 gui.py` 仍闪退，报错指向网络库内部接口缺失。
**原因**：`urllib3==1.22` 是 2017 年的版本，与 Python 3.13 不兼容。
**解法**：直接升级到最新版（这两个库接口早已稳定，升级不影响 ALAS 功能）：
```bash
pip3 install --upgrade requests urllib3 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 坑 8：`uiautomator2` 报 `ImportError: cannot import name 'formatargspec'`

**原因**：依赖的 `wrapt` 旧版本调用了 Python 3.11 之后被删除的 `inspect.formatargspec`。
**解法**：`pip3 install --upgrade wrapt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 坑 9：ALAS 启动时自动拉取原始 requirements.txt 导致死循环

**原因**：ALAS 检测到 GitHub 上有更新时，会自动重新下载官方原始的 `requirements.txt`（也就是把刚才删掉的那些坑全部还原），并尝试重新安装。
**解法**：编辑 `config/deploy.yaml`，将 `InstallDependencies: true` 改为 `InstallDependencies: false`，彻底关闭启动时的依赖自检/安装。

### 坑 10：ALAS 识别成网易 MuMu 模拟器而非真机

**现象**：报错 `device '127.0.0.1:16384' not found`，`127.0.0.1:16384` 是 MuMu 模拟器专属端口。
**原因**：网页面板【模拟器 Serial】填写有误或被自动检测覆盖。
**解法**：手动在面板中将 Serial 严格填写为手机的真实设备号（不要留空格，不要是 `auto`），模拟器类型选择"Phone"或保持自动检测。

### 坑 11：修改分辨率后 ALAS 仍报 `Resolution not supported: 2400x1080`

**原因**：`atx-agent`（ALAS 在手机端的截图代理插件）在分辨率修改前就已启动并缓存了旧的分辨率信息，不会自动刷新。
**解法**：
```bash
adb shell /data/local/tmp/atx-agent server --stop
```
如果该命令无效，直接重启手机即可——`wm size` 修改的分辨率是持久化的，重启后依然生效，同时会清空所有卡死的后台插件。

### 坑 12：终极卡点 —— `OSError: libmxnet.so: cannot open shared object file`

**这是原生 Python 路线的死刑判决**。

**原因**：ALAS 的 OCR 依赖 `mxnet` 深度学习框架，但 **官方从未发布过适配 ARM64 架构的 MXNet 二进制包**。之前通过 pip 装上的 mxnet 实际上是 x86_64（电脑端）架构的二进制文件，树莓派的 ARM64 处理器根本无法加载执行。

**解法**：放弃原生环境，转向 ALAS 社区编译的 ARM64 专属 Docker 镜像（`littlemio/alas:latest`），里面已经包含手工编译好的 ARM64 版 MXNet 及全部依赖。之前在 `/root/AzurLaneAutoScript` 目录下做的所有配置（ADB 序列号、`deploy.yaml` 设置等）可以通过 `-v` 挂载无缝继承，无需重新配置。

### 坑 13：`docker.io` 安装后命令不可用

**原因**：DietPi 等精简系统通过 apt 安装的 `docker.io` 有时未正确配置核心运行文件。
**解法**：用官方一键安装脚本重装：`curl -fsSL https://get.docker.com | sh`

### 坑 14：Docker 官方安装脚本 `Connection reset by peer`

**原因**：脚本默认连接境外 `download.docker.com`，国内网络环境下连接被重置。
**解法**：使用阿里云镜像参数：`curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun`

### 坑 15：拉取镜像卡在 `context deadline exceeded`

**原因**：大文件（本例中核心层约 233.5MB）下载到 100% 后，向 Docker Hub 做最终校验/通信时超时，国内直连 Docker Hub 不稳定。
**解法**：配置国内镜像加速源（见第三章阶段 5），重启 Docker 服务后重新拉取，缓存会被复用，很快完成。

---

## 六、硬件层面的长期运行注意事项（24/7 挂机必读）

- **散热**：长时间运行游戏极易发热降频甚至死机，建议拆除手机后盖或加装半导体散热背夹。
- **电池防鼓包**：手机长期满电插着充电器会导致电池鼓包甚至起火风险，几种应对方案：
  - 已 Root 的手机可用 `Battery Charge Limit` 类模块，将电量锁定在 50%～60% 循环；
  - 用支持智能协议的插座做定时通断电（如充 1 小时断 2 小时），让电池保持有放电过程；
  - 进阶方案：拆除电池，改用稳压直流电源（如 4.2V）直接供电主板，实现真正"去电池化"长期运行（需要一定动手能力，涉及拆机改线，风险自负）。

---

## 七、小结

整个部署过程本质上是一场 **"2021 年代的 Python 依赖清单" vs "2026 年的 Python 3.13 + ARM64 树莓派"** 的代沟战争。核心经验可以归纳为三条：

1. **遇到底层编译报错（C/C++/Rust 扩展包），第一反应是让系统的包管理器（apt）代劳，而不是死磕 pip 编译。**
2. **遇到 ARM64 架构上没有官方二进制支持的重型框架（如本例的 MXNet），不要恋战，直接切换到社区维护的 Docker 镜像。**
3. **ALAS 这类长期挂机脚本要善用 `screen`/`nohup` 做后台持久化，最终落地到 Docker 后用 `--restart always` 彻底解放双手。**
