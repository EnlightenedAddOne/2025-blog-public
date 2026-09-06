> 来源：Obsidian/20-技术知识库/树莓派/夸克网盘自动签到脚本部署.md

# 夸克网盘自动签到：抓包攻坚与树莓派部署

## 📌 项目背景与脚本选型

- **初始参考项目**：[Cp0204 / quark-auto-save (Wiki 参考)](https://github.com/Cp0204/quark-auto-save/wiki/%E4%BD%BF%E7%94%A8%E6%8A%80%E5%B7%A7%E9%9B%86%E9%94%A6#%E6%AF%8F%E6%97%A5%E7%AD%BE%E5%88%B0%E9%A2%86%E7%A9%BA%E9%97%B4)
    - _选型说明_：最开始尝试使用该项目，但其逻辑或配置方式与实际个人需求不够匹配。
- **最终采用脚本**：[BNDou / Auto_Check_In (checkIn_Quark.py)](https://github.com/BNDou/Auto_Check_In/blob/main/checkIn_Quark.py)
    - _选型说明_：受上述原项目启发改编的 V 2 版本，纯净且适配移动端新接口，只需提取核心参数即可运行，更契合轻量化部署需求。
- **运行环境**：树莓派 (DietPi 系统) + Python 3 + Cron 定时任务。
- **抓包工具**：Charles Proxy (需配置手机端 CA 证书并开启 SSL 代理)。

## 🔍 核心难点：抓包过程与接口参数定位

本次部署耗时最长的环节在于获取签到所需的核心参数（`kps`、`sign`、`vcode`）。由于夸克 APP 接口进行了更新，导致旧版教程的方法失效，以下是完整的排障与定位过程。

### 1. 踩坑与常规思路失效

- **旧版教程指引**：在 Charles 中过滤 `capacity`，寻找 `/1/clouddrive/capacity/growth/info` 接口，并从 Query String (URL 问号后面的部分) 中提取明文参数。
- **实际现象**：Charles 已经能成功解密 `drive-m.quark.cn` 域名的 HTTPS 流量，但无论怎么点击签到，都**无法搜到带有 `capacity` 的接口**，在其他请求的 URL 中也找不到这三个参数。

### 2. 破局：利用 Charles 全局搜索定位新参数

既然旧接口被废弃，思路转变为"只找参数，不挑接口"（因为任意携带身份验证的请求都会包含这些参数）。

- **操作步骤**：
    1. 彻底杀掉手机端夸克 APP 进程，点击 Charles 垃圾桶 🗑 清空所有历史请求，保证环境干净。
    2. 打开 Charles 的**全局搜索** (Edit -> Find)，搜索关键字 `kps=`，勾选在 `Request` 的 Headers 和 Query String 中查找。
    3. 手机重新打开夸克，进入网盘随便浏览并点击签到页。
    4. 通过搜索结果发现，夸克更新了安全机制，**参数已经从 URL 明文迁移到了 Request Headers (请求头) 中**，并且变量名加上了 `x-u-` 前缀。
- **最终成功提取**（以 `/auth/identity/get` 接口为例，在 Headers 中找到）：
    - `x-u-kps-wg` 对应所需参数 **`kps`**
    - `x-u-sign-wg` 对应所需参数 **`sign`**
    - `x-u-vcode` 对应所需参数 **`vcode`**
![file-20260808154626832](/blogs/quark-checkin/file-20260808154626832.png)
### 3. 备用抓包方案（脚本注释提供，本次未测试）

原脚本头部注释中提供了另一种获取参数的方法。本次实践虽然没有采用这种方式，但记录于此作为日后备用方案：

> **流程**：
>
> ① 开启抓包，手机端访问夸克**抽奖页**。
>
> ② 寻找 URL 为 `[https://drive-m.quark.cn/1/clouddrive/act/growth/reward](https://drive-m.quark.cn/1/clouddrive/act/growth/reward)` 的请求。
>
> ③ 复制整段 URL（该链接后直接附带了 `kps`、`sign`、`vcode` 参数）。
>
> ④ 直接将整段 URL 赋值给环境变量，如：`user=张三; url=https://...`

## 🛠 树莓派 (DietPi) 部署与环境排障

在拿到参数后，转移至 DietPi 系统进行部署时，遇到了几个典型的 Linux 系统级坑点：

### 问题 1：Crontab 环境变量丢失与路径报错

- **现象**：直接将 Python 命令写入 Cron 容易导致找不到环境变量 `COOKIE_QUARK`，且偶尔出现文件路径找不到的情况。
- **解决方式**：使用 `.sh` 启动脚本 (Wrapper Script) 进行封装。
    - 在脚本内部先 `export` 环境变量。
    - 必须使用**绝对路径**（如 `cd /root/quark-auto-save`）代替 `~`，避免 Cron 后台执行时运行目录混乱。

### 问题 2：DietPi 的 Cron 服务默认处于挂起状态

- **现象**：配置好 `crontab -e` 后，到达设定时间脚本并未执行，日志未生成。
- **排查**：输入 `systemctl status cron`，发现状态为 `Active: inactive (dead)`，且 `preset: disabled`。DietPi 为节省资源默认关闭了此服务。
- **解决方式**：手动激活并开启自启。

```bash
systemctl enable cron
systemctl start cron
```

### 问题 3：误导性的代码报错

- **现象**：日志虽然显示 `✅ 今日已签到...`，但末尾带有一段红色报错 `NameError: name 'send' is not defined`。
- **原因**：主脚本底部包含针对微信/TG 的推送逻辑，但我并未下载配套的 `utils` 通知模块，导致流程最后一步报错。
- **解决方式**：核心签到逻辑在报错前已跑通，不影响实际结果。若需清爽日志，直接 `nano` 编辑 Python 文件，将底部的 `try...except` 发送通知代码用 `#` 注释掉即可。

## 📂 最终配置文件归档

### 1. 启动脚本 (`run_quark.sh`)

路径：`/root/quark-auto-save/run_quark.sh`

```bash
#!/bin/bash

# 注入抓包获取的三个核心参数
export COOKIE_QUARK="user=我的夸克; kps=抓包获取的值; sign=抓包获取的值; vcode=抓包获取的值"

# 必须切换到绝对路径
cd /root/quark-auto-save

# 执行 Python 脚本，标准输出与错误均追加到日志中
/usr/bin/python3 checkIn_Quark.py >> run.log 2>&1
```

_(注：需要使用 `chmod +x run_quark.sh` 赋予执行权限)_

### 2. 定时任务配置 (`crontab -e`)

```bash
# 每天早上 9:00 自动执行签到启动脚本
0 9 * * * /bin/bash /root/quark-auto-save/run_quark.sh
```

_(注意：Crontab 文件的最后一行必须敲击回车保留一个空白行，否则最后一行规则可能不被系统执行。)_
