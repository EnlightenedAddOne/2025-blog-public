> 来源：Obsidian/20-技术知识库/环境配置/WSL下安装Ubuntu并使用VScode编写C语言程序.md

# 前言

---

由于课程 Linux C需要，需要在 Linux 系统下运行C 语言程序，在老师的建议下使用wsl 在window 系统下运行 Ubuntu 系统，同时为了方便代码的编写将使用VS code 进行代码编写。

# WSL 简介

Windows Subsystem for Linux（简称WSL），Windows下的Linux子系统，是一个在Windows 10上能够运行原生Linux二进制可执行文件（ELF格式）的兼容层。它是由微软与Canonical公司合作开发，其目标是使纯正的Ubuntu、Debian等映像能下载和解压到用户的本地计算机，并且映像内的工具和实用工具能在此子系统上原生运行。
详情请访问 [微软官方文档](https://docs.microsoft.com/zh-cn/windows/wsl/)]

# 下载 Ubuntu

## 1. 启用 wsl 功能

打开开始菜单，在搜索栏中输入 `启用或关闭 Windows 功能`，在弹出的窗口中勾选 `虚拟机平台` 和 `适用于 Linux 的 Windows 子系统`，确定之后重启系统。
![alt text](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315105.png)

重启之后搜索栏中输入 `CMD`，打开命令提示符。

![alt text](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315106.png)

打开后在终端输入：

```
wsl.exe --update
```

![cmd1 1](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315107.png)

如图，即可安装 WSL 相关的组件，这一步可能需要几分钟的时间。

## 2. 安装Ubuntu

打开 **Microsoft Store**，搜索 **Ubuntu** 并下载。

![store](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315108.png)

下载完成后在底部搜索栏中输入 **Ubuntu**，并打开

![Ubuntu1](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315109.png)

打开后稍等片刻，会提示你输入用户名和密码

![Ubuntu2](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315110.png)

如图，这一步提示你输入用户名和密码，注意：**在你输入密码时它是不会显示的，同时需要记好你的密码，否则只能再删掉重下！！！**

当你输入完账号和密码后 Ubuntu 系统就已经安装好了

![Ubuntu3](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315111.png)

此时在 `此电脑` 里会多出一个 `Linux` 的图标 ![Ubuntu.4](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315112.png)

# C 语言程序编写

## 1. 编译环境配置

在编译 C 语言程序时需要用到 gcc，所以我们需要打开 `Ubuntu` ，运行以下命令，进行环境配置

```
sudo apt-get install build-essential
```

输入此代码后，会让你输入密码，输入之后即可下载。

下载之后，可输入

```
gcc -v
```

来检测是否安装成功

## 2. 一些需要用到的 Linux 命令

在进行 C 语言程序的编译运行之前，我们需要知道一些基本的 Linux 命令

2.1 切换目录（cd）

```
cd              //切换到home目录
cd xx(文件夹名)  //切换到本目录下的名为xx的文件目录，如果目录不存在报错
cd /xxx/xx/x    //可以输入完整的路径，直接切换到目标目录，输入过程中可以使用tab键快速补全
```

2.2 查看目录（ls）

```
ls         //查看当前目录下的所有目录和文件
ls -a      //查看当前目录下的所有目录和文件（包括隐藏的文件）
ls -l      //列表查看当前目录下的所有目录和文件（列表查看，显示更多信息），与命令"ll"效果一样
```

2.3 编译 C 语言文件（gcc）

```
gcc C语言文件  //可使用Tab键进行自动路径补全，编译成功后会出现一个a.out文件
```

2.4 运行编译结果

```
./a.out    //运行后会输出上次编译的C语言结果
```

2.5 查看当前目录（pwd）

```
pwd         //显示当前位置路径
```

2.6 新增文件（touch）

```
touch a.txt          //在当前目录下创建名为a的txt文件
```

2.7 新增文件夹（mkdir）

```
mkdir 文件夹名
```

## 3. 使用其他编译器编写代码

打开 `Ubuntu` ，运行以下命令，创建一个用于存放代码的文件夹

```
mkdir 文件夹名
```

然后你的 `Linux\Ubuntu\home\User` 路径下就会出现一个你刚刚创建的文件夹，将你写好的 C 语言代码放在这里。
之后，打开 Ubuntu，使用 cd 命令进入此文件，再用 gcc 命令编译 C 语言文件，最后使用 `./out` 命令输出结果。

此操作个人认为在编写时比较麻烦，下面将介绍一种个人比较喜欢的编写方案。

## 4 .使用 VS code + WSL

首先下载 [Download Visual Studio Code](https://code.visualstudio.com/download)

下载完成后打开 VS code 点击扩展选项

![VS1](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315113.png)

然后搜索 wsl 并下载

![wsl](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315114.png)

安装完后，重启 VS code ，点击左下角的 WSL 连接 Ubuntu（此处我已经连上了）
![wsl2](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/202505302315115.png)
之后就可以在 VS code 中创建 C 语言文件，并在下方终端界面运行指令，实现代码的编译运行。第一次创建 C 语言文件还会提示你下载 C 语言的配置文件。（若没出现终端界面可同时按下 Ctrl + ~ 键）

## 参考文档

[Windows Subsystem for Linux (WSL) 最新详细安装教程-CSDN博客](https://blog.csdn.net/wangtcCSDN/article/details/137950545)
[wsl2安装与 gcc环境搭建\_wsl gcc-CSDN博客](https://blog.csdn.net/qq_41783470/article/details/120496916)
[通过VScode的远程连接 WSL，配置Linux平台python开发环境\_vscode wsl-CSDN博客](https://blog.csdn.net/mmc02/article/details/136142015)
