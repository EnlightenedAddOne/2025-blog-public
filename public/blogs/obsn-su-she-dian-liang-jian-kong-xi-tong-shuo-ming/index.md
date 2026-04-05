# 宿舍电量监控系统说明

> 来源：Obsidian/30-项目与实践/项目说明/宿舍电量监控系统/宿舍电量监控系统说明.md

## Cookie手动获取教程

### 电脑端

#### 方法1:提取链接后缀(推荐)

1. 使用Chrome浏览器访问下面连接进行登录 [统一身份认证](http://ids.lit.edu.cn/authserver/login?service=http%3A%2F%2Fzhyd.sec.lit.edu.cn%2Fzhyd%2Fsydl%2Findex)

![login_page_url](/blogs/obsn-su-she-dian-liang-jian-kong-xi-tong-shuo-ming/login_page_url.png)

成功登录界面

![login_success_page](/blogs/obsn-su-she-dian-liang-jian-kong-xi-tong-shuo-ming/login_success_page.png)

2. 复制其中的 `JSESSIONID=xxxxxxxxx` 部分
   ![cookie_from_url_suffix](/blogs/obsn-su-she-dian-liang-jian-kong-xi-tong-shuo-ming/cookie_from_url_suffix.png)

#### 方法2:使用开发者工具

1. 参考方法一进行登录
2. 按 F12 打开开发者工具

![browser_dev_tools_f12](/blogs/obsn-su-she-dian-liang-jian-kong-xi-tong-shuo-ming/browser_dev_tools_f12.png)

3. 切换到 **Network(网络)** 选项卡
   ![dev_tools_network_tab](/blogs/obsn-su-she-dian-liang-jian-kong-xi-tong-shuo-ming/dev_tools_network_tab.png)

4. 刷新页面(F5)
5. 点击任意请求,在右侧找到 **Request Headers(请求头)**
6. 找到 `Cookie:` 字段
7. 复制其中的 `JSESSIONID=xxxxxxxxx` 部分

![cookie_from_headers](/blogs/obsn-su-she-dian-liang-jian-kong-xi-tong-shuo-ming/cookie_from_headers.png)

### 手机端

使用 **电脑端的方法一** 获取，手机端浏览器一般无法使用开发者工具
