> 来源：Obsidian/20-技术知识库/树莓派/树莓派无显示器进行ssh连接.md

# 系统烧录

- 1.使用官方镜像烧录工具

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041722694.png)

- 2.选择自己的树莓派型号、操作系统和SD卡
- 3.设置用户账号密码和WiFi
  **注意：** 用户账户尽量避免使用 _root_ 和 _admin_
- 4.开启远程ssh连接，允许使用账号密码登录

# 使用远程连接工具连接

## 查找树莓派IP

打开路由器后台查看，若连接的是手机热点，打开手机设置里的个人热点查看。

## SSH 连接

打开远程连接工具，这里以 _Xshell_ 为例

点击 _新建会话_ 输入上面得到的树莓派IP

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041722696.png)

在*用户身份验证* 输入之前设置的账号密码，点击连接

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041722697.png)

## 设置root用户的密码

在ssh连接时必须先使用普通用户密码进行连接，之后使用命令进行权限切换时输入root的密码切换为root权限

- 设置root密码

```bash
sudo passwd 或者 sudo passwd root
Password： 你当前用户的密码
Enter new UNIX password： 设置是 root 用户的密码
Retype new UNIX password：重复以上 root 用户的密码
```

- 切换root用户

```bash
su -
```
