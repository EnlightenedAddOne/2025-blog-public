# 【新】安装小雅Alist

> 来源：Obsidian/20-技术知识库/树莓派/【新】安装小雅Alist.md

使用一键安装脚本

```
bash -c "$(curl --insecure -fsSL https://ddsrem.com/xiaoya_install.sh))"
```

即可快速配置xiaoya环境

注意当执行到这一步时，记下这个密码，到时候登录需要
![Pasted image 20250910212841](/blogs/obsn-xin-an-zhuang-xiao-ya/Pasted image 20250910212841.png)

执行结束后会显示如下信息，但此时使用 `用户密码: guest/admin` 登录小雅`http://ip:5678` 时会显示密码错误好像，反正我是登录不上。
解决办法是：重启xiaoya容器，然后使用上面的`强制登入用户名、密码`进行登录
`
![Pasted image 20250910213015](/blogs/obsn-xin-an-zhuang-xiao-ya/Pasted image 20250910213015.png)

参考链接：[飞牛部署小雅Alist-Tvbox，畅快看4K影视,飞牛影视刮削 - 应用中心 飞牛私有云论坛 fnOS](https://club.fnnas.com/forum.php?mod=viewthread&tid=7389)
