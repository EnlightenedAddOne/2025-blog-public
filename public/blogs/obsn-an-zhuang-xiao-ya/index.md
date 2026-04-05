> 来源：Obsidian/20-技术知识库/树莓派/安装小雅Alist.md

注意：安装小雅Alist之前需要先安装Alist。

Alist可以在宝塔面板的docker界面一键安装

---

# 安装小雅

在宝塔面板-->Docker-->线上镜像，搜索*xiaoyaliu* ，拉取

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709791.png)

安装完之后，即可看到

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709792.png)
![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709793.png)

# 配置小雅

## 任务目标

我们需要获得有关阿里云盘的三条数据，并将其放入小雅对应的文件夹里

| 内容                 | 对应文件名                  | 获取方式                                                                                                                                                                                                                             |
| -------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| tocken               | mytoken.txt                 | [阿里云盘 / 分享 \| AList文档](https://alist.nn.ci/zh/guide/drivers/aliyundrive.html)                                                                                                                                                |
| refresh_token        | myopentoken.txt             | [阿里云盘 Open \| AList文档](https://alist.nn.ci/zh/guide/drivers/aliyundrive_open.html)                                                                                                                                             |
| 转存目录的 folder id | temp_transfer_folder_id.txt | 先转存这个[阿里云盘分享](https://www.aliyundrive.com/s/rP9gP3h9asE)到自己网盘。然后参考[阿里云盘 / 分享 \| AList文档](https://alist.nn.ci/zh/guide/drivers/aliyundrive.html#%E5%88%B7%E6%96%B0%E4%BB%A4%E7%89%8C)获得自己的folder id |

## 文件配置

将得到的数据存储到对应的txt文件内，之后打开小雅容器对应目录，创建*data*
文件夹，将三个txt文件放入

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709794.png)

创建*data* 文件夹

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709795.png)

将三个文件传入，其余文件在容器运行后会自动生成

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709797.png)

至此，小雅基本已经完成配置，启动容器，查看日志是否成功启动

## 定时清理小雅缓存文件

由于小雅本质是将别人阿里云盘的文件先转存到自己的阿里云盘内再进行播放，如此当时间久了就会是云盘空间不足，我们可以手动清理，当然也可以使用插件，进行自动清理

搜索*xiaoyakeeper* 拉取镜像，等待安装完成即可

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709798.png)

# 本地访问小雅

## 准备配置信息

```

小雅的ip地址：192.168.28.38:5678  （例子）

协议：WebDAV协议

账户：guest

密码：guest_Api789
```

## 电脑Potpalyer访问

打开PotPlayer播放器，点击“新建专辑”

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709799.png)

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709800.png)

最后，点击确定。

## 手机ES文件浏览器访问

选择*我的网络* 添加*webdav服务器* ，填写信息

![](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202508041709801.png)

---

参考资料：

- [如何低成本搭建一个docker 轻服务器 随时随地访问小雅影音库 OrangePi Zero3 ｜免费内网穿透 bilibili](https://www.bilibili.com/video/BV1ND421T7nB/?spm_id_from=333.1387.favlist.content.click&vd_source=e88731727a722c629c5950e91da85296)
- [用Docker单独安装xiaoya-alist_docker 小雅-CSDN博客](https://blog.csdn.net/wbsu2004/article/details/138304477)
- [如何设置xiaoya的docker](https://xiaoyaliu.notion.site/xiaoya-docker-69404af849504fa5bcf9f2dd5ecaa75f)（小雅官方文档，可能需要加速访问）
- [Home | AList文档](https://alist.nn.ci/zh/)（Alist官方文档）
