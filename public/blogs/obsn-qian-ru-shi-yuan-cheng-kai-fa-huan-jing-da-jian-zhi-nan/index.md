> 来源：Obsidian/30-项目与实践/项目说明/嵌入式-智能家居/VS Code 嵌入式 Linux 远程开发环境搭建指南.md

# VS Code 嵌入式 Linux 远程开发指南 (SFTP + Makefile 方案)

适用硬件：STM32MP157 开发板 (FSMP1A) 或其他 Linux 开发板

适用环境：Windows PC (主机) + VS Code

## 1. 方案概述

本方案采用 **“本地编写 + 自动同步 + 板端编译”** 的模式，完美解决了嵌入式开发中跨平台编译环境配置难、代码同步繁琐的问题。

- **本地 (Windows)**：使用 VS Code 享受高效的代码补全、语法高亮和文件管理。
- **传输 (SFTP)**：利用插件实时监听文件变化，毫秒级自动同步代码到开发板。
- **远端 (开发板)**：利用板载 GCC 编译器直接编译，无需在 PC 端配置复杂的交叉编译链。

---

## 2. 环境准备

1. **VS Code 插件安装**：
   - 在扩展商店搜索并安装 **SFTP** (推荐 `liximomo.sftp` 或 `Natizyskunk.sftp`)。
   - (可选) **C/C++** (Microsoft) 用于语法高亮。

2. **网络连接**：
   - 确保开发板已联网，并知晓其 IP 地址 (例如: `10.239.146.97`)。
   - 确保能通过终端 SSH 连上板子。

---

## 3. 核心配置步骤 (一次性配置)

在项目根目录下创建 `.vscode` 文件夹（如果没有），并配置以下三个关键文件。

### 3.1 配置 SSH 免密登录 (极大提升效率)

为了避免每次编译都要输密码，请先在 PC 端配置公钥认证。

1. 在 VS Code 终端 (PowerShell) 生成密钥（一路回车）：

```shell
ssh-keygen -t rsa
```

1. 将公钥发送给开发板（替换为您的板子 IP）：

```shell
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh root@10.239.146.97 "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

### 3.2 配置自动同步 (`.vscode/sftp.json`)

此配置解决了“VS Code 自动保存导致频繁上传”的问题，开启了防抖动监听。

```JSON
{
    "name": "FSMP1A_Board",
    "host": "10.239.146.97",  // 【注意】板子IP变动后需修改此处
    "protocol": "sftp",
    "port": 22,
    "username": "root",
    // "password": "hqyj",    // 配置免密登录后，这行可以删除
    "remotePath": "/root/code", // 板子上存放代码的路径
    "uploadOnSave": false,    // 关闭保存即上传
    "watcher": {              // 开启监听模式
        "files": "**/*",
        "autoUpload": true,
        "delay": 1000         // 【防抖】停止打字 1秒 后才上传
    },
    "ignore": [".vscode", ".git", ".DS_Store", "app"] // 忽略不需要上传的文件
}
```

### 3.3 配置自动化任务 (`.vscode/tasks.json`)

此配置将 `Ctrl + Shift + B` 快捷键映射为“在板子上执行 Make 编译”。

```JSON
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Remote Build", // 任务名称
            "type": "shell",
            "command": "ssh",
            "args": [
                "root@10.239.146.97", // 【注意】IP需与 sftp.json 一致
                "cd /root/code && make" // 进入目录并编译 (只编译不运行)
            ],
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
```

### 3.4 配置通用 Makefile (`Makefile`)

在项目根目录新建 `Makefile` 文件，实现“不管有多少个 .c 文件都能自动编译”。

```Makefile
# 定义编译器
CC = gcc
# 定义输出程序名
TARGET = app
# 自动寻找当前目录下所有的 .c 文件
SRCS = $(wildcard *.c)

# 默认目标
all:
	$(CC) $(SRCS) -o $(TARGET)

# 清理目标
clean:
	rm -f $(TARGET)
```

### 3.5 最终文件目录

## ![vscode_project_file_structure](/blogs/obsn-qian-ru-shi-yuan-cheng-kai-fa-huan-jing-da-jian-zhi-nan/vscode_project_file_structure.png)

## 4. 开发工作流 (日常使用)

配置完成后，您的日常开发步骤如下：

1. **编写代码**：在 VS Code 中新建或修改 `.c` 文件 (如 `fan_control.c`)。
2. **自动同步**：写完代码停顿 1 秒，观察左下角状态栏，显示 `Uploading...` 即代表代码已同步到板子。
3. **一键编译**：按下快捷键 **`Ctrl + Shift + B`**。
   - 下方终端会自动弹出，显示编译结果。
   - _成功_：无报错。
   - _失败_：根据报错信息修改代码，重复步骤 1。

4. **运行程序**：
   - 在下方 SSH 终端中输入：`./app`
   - 观察硬件现象（如风扇转动、LED 亮灭）。

---

## 5. 常见问题排查 (FAQ)

| **问题现象**                        | **可能原因**     | **解决方法**                                                           |
| ----------------------------------- | ---------------- | ---------------------------------------------------------------------- |
| **编译提示 `No such file`**         | 文件还没传过去   | 右键文件 -> 选择 "SFTP: Upload" 强制上传一次。                         |
| **一直提示输入密码**                | SSH 免密没配置好 | 检查步骤 3.1，或检查 `sftp.json` 里是否还有密码字段。                  |
| **连接超时 (Timeout)**              | **板子 IP 变了** | 输入 `ifconfig` 查看板子新 IP，更新 `sftp.json` 和 `tasks.json`。      |
| **风扇/蜂鸣器停不下来**             | 程序异常退出     | 在终端手动输入命令关闭，例如 `echo 0 > /sys/class/hwmon/hwmon1/pwm1`。 |
| **编译警告 `implicit declaration`** | 缺头文件         | 检查代码开头是否加了 `#include <stdio.h>` 或 `<unistd.h>`。            |

---

### 下一步建议

既然您已经打通了这套流程，建议您：

1. **保持工程整洁**：每次开始新实验前，可以运行 `make clean` 清理旧文件。

2. **备份配置**：将 `.vscode` 文件夹备份，以后新建项目时直接复制过去，改改 IP 就能用。
