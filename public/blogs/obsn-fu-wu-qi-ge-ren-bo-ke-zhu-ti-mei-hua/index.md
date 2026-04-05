> 来源：Obsidian/20-技术知识库/服务器/ClawCloud服务器+WordPress个人博客+Argon主题美化.md

「ClawCloud Run」推出了注册 180 天以上的 GitHub 账号终身每月免费送$5 美金额度的福利活动，而 WordPress $ 0.06/Day ，相当于是永久免费的个人博客了。

[Claw Cloud工作台](https://ap-northeast-1.run.claw.cloud/)

---

# 在ClawCloud服务器上安装WordPress

访问 [ClawCloud 官网](https://claw.cloud/) ，注册 ClawCloud，使用 **GitHub** 账号登录，进入主界面

![](attachments/Pasted%20image%2020250502182845.png)

点击 **App Store** 下载**WordPress**

![](attachments/Pasted%20image%2020250502183227.png)

然后，返回主页面打开**App Launchpad** 就可以看到刚下载好的WordPress

![](attachments/Pasted%20image%2020250502183422.png)

点击公网地址，访问WordPress，设置一下WordPress的账号密码

![](attachments/Pasted%20image%2020250502183520.png)

# 配置 WordPress

由于PHP限制最多只能上传2M的文件，导致我们无法上传主题，所以我们需要修改一下配置

---

在电脑上新建一个名为 **php.ini** 的文件，在里面写入下面内容

```ini
# 512M可根据自己的需求更改
upload_max_filesize = 512M
post_max_size = 512M
memory_limit = 512M
```

然后打开WordPress所在目录，将该文件传进去。

![](attachments/Pasted%20image%2020250502184855.png)![](attachments/Pasted%20image%2020250502185443.png)

然后重启 WordPress ，在媒体库可以看到我们当前允许上传的文件大小

![](attachments/Pasted%20image%2020250502185612.png)

# 安装Argon并配置

在GitHub上下载Argon [📖 Argon - 一个轻盈、简洁的 WordPress 主题](https://github.com/solstice23/argon-theme)

在 外观-->主题-->上传主题 选择刚才下载的压缩包，安装

![](attachments/Pasted%20image%2020250502201838.png)

具体美化过程请参考：[Argon主题博客美化 – Echo小窝](https://www.liveout.cn/25/)
