> 来源：Obsidian/20-技术知识库/网络/Edgetunnel CF Pages 全流程部署.md

> 摘要
> 本文记录我借助 **Cloudflare Pages** 与**免费域名（dpDNS / FreeDomain）**部署 **cmliu/edgetunnel** 节点的完整实操过程，覆盖 Fork 仓库、Pages 接入、环境变量、KV 绑定、自定义域名解析，以及一路踩到的 **522 超时、Nginx 伪装页、变量不生效、CF 名称服务器无效** 等问题排查。本文技术细节以官方仓库 [cmliu/edgetunnel](https://github.com/cmliu/edgetunnel) 为准。

> 版本说明
> 本笔记对应 **edgetunnel 2.1**。作者仓库仍在持续更新，部署前请以 README 最新内容为准。

---

## 一、项目简介

**cmliu/edgetunnel** 是一个基于 **Cloudflare Workers/Pages** 平台的边缘隧道方案，支持：

- 🛡️ 协议：**VLESS**、**Trojan**、**Shadowsocks**
- 🎛️ 内置**可视化管理后台**（实时改配置、看日志、看流量）
- 📦 部署灵活：Workers / Pages（GitHub 连接 或 ZIP 上传）均可
- 🔗 内置订阅生成与混淆转换，适配 Clash、Sing-box、Surge 等主流客户端
- ⚡ 支持自定义 ProxyIP、SOCKS5/HTTP 链式代理、优选 API

- **核心链路**：客户端 → CF 边缘节点 → Worker/Pagess 脚本（反代）→ 上游 ProxyIP → 目标网站。
- **官方演示站**：`https://EDT-Pages.github.io/admin`

---

## 二、部署前置准备

| 类型 | 内容 |
| --- | --- |
| GitHub 账号 | 用于 Fork `cmliu/edgetunnel` 仓库 |
| Cloudflare 账号 | 用于部署 Pages 并接管 DNS |
| 免费域名 | dpDNS（`*.dpdns.org`）、FreeDomain（`*.qzz.io` 等） |
| 优选 IP | 来自 `LancelotRar/best-cf-ips`，用于配置反代 IP |
| 客户端 | 支持 VLESS/Trojan/SS 的代理客户端 |

### 参考教程

> 先看视频再动手，能少踩很多坑
> - 主教程：[《CF 新服务条款解读 & edgetunnel 最新教程》](https://www.youtube.com/watch?v=tKe9xUuFODA&t=474s)
> - 备选：[kuL4xR2Co9A](https://www.youtube.com/watch?v=kuL4xR2Co9A)、[iYiH-PjfGYw](https://www.youtube.com/watch?v=iYiH-PjfGYw&t=418s)
> - 官方详细教程：<https://cmliussss.com/p/edt2/>
> - 文字教程：[wandou.eu.org](https://wandou.eu.org/archives/410)、[fastly.blog.cmliussss.com edt2](https://fastly.blog.cmliussss.com/p/edt2/)
>
>   ![00-教程封面](/blogs/edgetunnel-cf/00-cover.jpg)

---

## 三、CF Pages 部署（GitHub 方式）

> 官方提供三种部署方式：**① Workers**、**② Pages ZIP 上传**、**③ Pages + GitHub**。我采用第 ③ 种（Fork 后连接 Git）。

### 1. Fork 仓库并连接

1. 打开 <https://github.com/cmliu/edgetunnel>，点 **Fork** 到自己的 GitHub 账号（顺手点个 ⭐ Star）。
2. 进入 Cloudflare 控制台 → **Workers 和 Pages** → **Pages** → **创建项目** → **连接到 Git**。
3. 选择刚 Fork 的 `edgetunnel` 仓库 → **开始设置**。
4. 构建命令、输出目录保持默认（无需构建）→ **保存并部署**。

### 2. 配置环境变量（关键）

官方环境变量清单如下（**仅 `ADMIN` 必填**）：

| 变量名 | 必填 | 示例 | 说明 |
| --- | --- | --- | --- |
| **ADMIN** | ✅ | `123456` | 后台管理面板登录密码 |
| KEY | ❌ | `CMLiussss` | 快速订阅路径密钥，访问 `/CMLiussss` 直接拿节点 |
| UUID | ❌ | `90cd4a77-141a-43c9-991b-08263cfe9c10` | 强制固定 UUID，**必须是 UUIDv4 标准格式** |
| PROXYIP | ❌ | `proxyip.cmliussss.net:443` | 全局自定义反代 IP |
| URL | ❌ | `https://cloudflare-error-page-3th.pages.dev` | 默认主页伪装地址（可填网页 URL 或 `1101`） |
| GO2SOCKS5 | ❌ | `blog.cmliussss.com`,`*.ip111.cn` | 强制走 SOCKS5 的域名名单 |
| DEBUG | ❌ | `1` 或 `true` | 开发者模式（开启调试日志） |
| OFF_LOG | ❌ | `1` 或 `true` | 关闭 KV 日志记录 |
| BEST_SUB | ❌ | `1` 或 `true` | 开启优选订阅生成器 |
| TCP_CONCURRENT_DIAL | ❌ | `2` | TCP 并发拨号数（默认 2） |
| PROXY_CONCURRENT_DIAL | ❌ | `1` | 反代并发拨号数（默认 1） |

> 我这次踩的第一个坑：变量名用错了
> 我当时误以为「进入管理页的密码」变量名叫 `UUID`，于是只配置了 `UUID=addone`。但官方**管理后台的登录密码变量名是 `ADMIN`**，`UUID` 只是可选变量，且值必须是 UUIDv4 格式（如 `90cd4a77-141a-43c9-991b-08263cfe9c10`），不能随便填 `addone` 这种字符串。
>
> **正确做法**：至少配置 `ADMIN`（后台密码）；如需固定节点 UUID 再额外配 `UUID`（UUIDv4 格式）。

### 3. 绑定 KV 命名空间（我漏掉的关键一步）

1. 进入 Pages 项目 → **设置** → **绑定** → **添加** → **KV 命名空间**。
2. 新建或选择一个命名空间。
3. **变量名称必须填 `KV`**，保存后重试部署。

> 千万别漏 KV
> `KV` 用于持久化日志与配置，变量名写错（如 `kv`、`KVStore`）会导致功能异常。这一步我在最初部署时**完全漏掉了**，是导致后续行为异常的原因之一。

---

## 四、自定义域接入

### 1. 在 Pages 后台设置自定义域

进入 Pages 项目 → **自定义域** → **设置自定义域**：

- 填入你的次级域名，例如 `qifei.addone.dpdns.org`。
- ⚠️ **不要使用根域名**（例如分配的是 `addone.dpdns.org`，就填 `qifei.addone.dpdns.org`）。

### 2. 在 DNS 服务商添加 CNAME（指向 edgetunnel.pages.dev）

官方要求 CNAME **指向 `edgetunnel.pages.dev`**（仓库主域），不是你自己 Pages 项目生成的随机 `xxx.pages.dev`：

| 类型 | 名称 | 内容 | 代理状态 |
| --- | --- | --- | --- |
| CNAME | `qifei.addone.dpdns.org` | `edgetunnel.pages.dev` | ✅ 已代理（小黄云点亮） |

![02-CF-DNS-小黄云配置](/blogs/edgetunnel-cf/02-CF-DNS-dns-proxy-config.png)

> 我这次踩的第二个坑：CNAME 指错了
> 我当时填的是自己 Pages 项目生成的 `addone-qifei.pages.dev`，而官方要求统一指向 `edgetunnel.pages.dev`。虽然也能通，但应按官方规范填写。
>
> **关键**：无论如何，**小黄云必须点亮（代理状态 = 已代理）**。小黄云是灰的，流量就不经过 CF 边缘，直接解析真实 IP，往往不可达 → 立刻 522。

> 证书生效
> 添加自定义域后，CF 会下发 TLS 证书，需等待几分钟，状态变 **活跃（Active）** 才算生效。

![03-Pages-自定义域-活跃](/blogs/edgetunnel-cf/03-Pages-custom-domain-active.png)

### 3. 访问后台

部署并绑定域名后，访问：

```
https://你的域名/admin
```

输入 `ADMIN` 变量里设置的密码即可登录管理后台（在后台里看订阅链接、改配置、看日志）。

---

## 五、522 错误排查实战

### 1. 现象

部署后访问 `https://qifei.addone.dpdns.org`，返回 Cloudflare 522 错误页：

![01-522错误首现](/blogs/edgetunnel-cf/01-error-522.png)

- **You（浏览器）**：Working ✅
- **Tokyo（CF 边缘节点）**：Working ✅
- **Host（源站）**：Error ❌

> 含义
> 浏览器 ↔ Cloudflare 是通的，但 Cloudflare 回源到 Worker/源站时**迟迟得不到响应**，于是超时。

### 2. 排查路径（4 个常见原因）

| # | 原因 | 检查位置 | 解决办法 |
| --- | --- | --- | --- |
| 1 | 自定义域未初始化 | Pages → 自定义域 | 等 3–5 分钟，等证书生效 |
| 2 | 环境变量 / KV 未生效 | Pages → 部署记录 | 重新部署（见下文） |
| 3 | DNS 小黄云未点亮 | CF DNS 记录页 | 开启 Proxy（小黄云变橙） |
| 4 | 上游 ProxyIP 失效 | 订阅链接 `?proxyip=` | 更换可用反代 IP |

> 排除法经验
> 本次 DNS 已显示"已代理"，故先排除 DNS；往下查 Pages 自定义域状态 → 变量/KV 生效 → ProxyIP。

### 3. 真正的根因：变量未生效（需重新部署）

即便变量名、值都对，**CF Pages 的环境变量在新增/修改后，必须重新部署一次才会生效**，否则运行的还是旧构建。

> 重新部署步骤
> 1. Pages 项目 → **部署** 选项卡。
> 2. **GitHub 同步部署**：点最新部署记录右侧 `...` → **重试部署**。
> 3. **ZIP 上传部署**：点右上角 **创建部署** → 重新上传 `main.zip`。
> 4. 等新部署状态变 **成功**。
> 5. 重新访问 `https://你的域名/admin`。

---

## 六、Nginx 伪装页与后台入口

### 1. 现象

访问根域名 `https://qifei.addone.dpdns.org`，出现 "Welcome to nginx!" 页面：

![04-Nginx伪装页](/blogs/edgetunnel-cf/04-nginx-page.png)

### 2. 这是「防探测伪装」，不是报错

- 脚本默认对外返回一个**伪装页**，隐藏代理服务的存在。
- 默认伪装地址由 **`URL` 环境变量**控制（可填网页 URL，或填 `1101` 使用 CF 默认错误页）。
- 而**真正的管理后台在 `/admin` 路径**。

> 我这次踩的第三个坑：把入口当成了 /UUID
> 我当时误以为入口是 `域名/<UUID>`，所以去访问 `qifei.addone.dpdns.org/addone`，结果自然还是 Nginx 伪装页（`/addone` 根本不是一个合法路径）。
>
> **正确入口是 `域名/admin`**，登录密码是 `ADMIN` 变量的值。

### 3. 访问 /admin 仍是伪装页？

若访问 `/admin` 仍异常，通常是 `ADMIN` 变量或 `KV` 未真正生效 —— 执行一次「重试部署」即可（见上一节）。

![06-加UUID后仍Nginx伪装页](/blogs/edgetunnel-cf/06-still-nginx-page.png)

---

## 七、CF 接管 NS 与注册商修改（zaddone.qzz.io）

### 1. 在 Cloudflare 添加第二个域

为获得第二个反代域名，我又通过 **DigitalPlat FreeDomain** 注册了免费域名 `zaddone.qzz.io` 并加入 Cloudflare，结果提示「名称服务器无效」：

![07-CF-NS无效提示](/blogs/edgetunnel-cf/07-ns-invalid.png)

三个域名里只有 `addone.dcdn.org` 的 NS 有效，`addone.me` 和 `zaddone.qzz.io` 均无效：

![08-三个域名NS状态](/blogs/edgetunnel-cf/08-three-domains-ns-status.png)

### 2. 在注册商（DigitalPlat）修改 NS

> 原理
> CF 接管域名 = 把域名的 DNS 服务器指向 CF 分配的 `*.ns.cloudflare.com`。**修改的是域名在注册商处的 NS 记录**，不是在 CF 内部改。

1. 进入 DigitalPlat 域名管理后台：

   ![09-DigitalPlat域名管理](/blogs/edgetunnel-cf/09-domain-manage.png)

2. CF 引导页给出需要填写的两条 NS：

   ![10-CF-接管NS指引](/blogs/edgetunnel-cf/10-takeover-ns-guide.png)

3. 回到注册商「名称服务器」选项卡，将默认 NS 替换为 CF 分配的两条：
   - **NAME SERVER 1**：`trey.ns.cloudflare.com`
   - **NAME SERVER 2**：`savanna.ns.cloudflare.com`

   ![11-注册商填CF-NS](/blogs/edgetunnel-cf/11-registrar-fill-cf-ns.png)

> 我这次踩的第四个坑：域名拼写错位
> 我把 `zaddone.qzz.io`（带 z）的 NS 误填到了 `addone.qzz.io`（漏了 z）的位置，导致 NS 永远无效。**修改 NS 前务必反复核对域名拼写完全一致。**

> 生效延迟
> 全球 DNS 缓存刷新需要时间，通常 **15–30 分钟**。改完后回 CF 域名页点 **检查名称服务器（Check nameservers）** 强制 CF 立刻检测。

### 3. NS 生效后的下一步

CF 检测到 NS 已指向自己后，会进入接管前的最后一步：

![12-Cloudflare接管页清理DNS](/blogs/edgetunnel-cf/12-cleanup-dns.jpg)

---

## 八、清理默认 DNS 记录

1. CF 自动扫到的 A / AAAA 记录（如 `172.67.192.24`）是注册商自带的**默认停放页 IP**，对新注册免费域名是"出厂配置"。
2. **建议全部删除**：这些记录对节点无用，留着可能和节点路由冲突。
3. 逐条删除，清空全部 8 条 A/AAAA 记录。
4. 点页面底部 **继续前往激活**，完成域名接管。
5. 之后在 Pages 后台绑定 `zaddone.qzz.io` 自定义域时，CF 会自动生成指向 Pages 的 CNAME，无需手写。

---

## 九、PATH 路径动态切换与优选 IP

### 1. PATH 路径切换底层代理

edgetunnel 支持通过 URL 路径动态指定底层代理：

```
# 指定 ProxyIP
/proxyip=proxyip.cmliussss.net
/?proxyip=proxyip.cmliussss.net

# 指定 SOCKS5
/socks5=user:password@127.0.0.1:1080
/socks://dXNlcjpwYXNzd29yZA==@127.0.0.1:1080

# 指定 HTTP 代理
/http=user:password@127.0.0.1:1080
```

### 2. 优选 IP（best-cf-ips）

- 仓库：<https://github.com/LancelotRar/best-cf-ips>
- 可在订阅链接加 `?proxyip=` 或 `PROXYIP` 变量指定反代 IP。
- 建议结合延迟测试挑选合适的 Cloudflare IP 段。

### 3. 客户端适配

| 平台 | 推荐客户端 |
| --- | --- |
| Windows | v2rayN、Hiddify、FlClash、mihomo-party、Clash Verge Rev |
| Android | v2rayNG、ClashMetaForAndroid、FlClash、NekoBox |
| iOS | Surge、Shadowrocket、Stash、Loon、Quantumult X |
| macOS | FlClash、mihomo-party、Clash Verge Rev、Surge |
| 鸿蒙 | ClashBox |

---

## 十、踩坑清单（速查表）

| 坑 | 现象 | 根因 | 正确做法 |
| --- | --- | --- | --- |
| 1 | 首次部署就 522 | 自定义域未初始化 | 等 3–5 分钟，证书生效 |
| 2 | 小黄云灰着 + 522 | 流量没经过 CF 边缘 | DNS 记录开启 Proxy（小黄云） |
| 3 | 变量名用错（UUID vs ADMIN） | 后台进不去 | 用 `ADMIN` 配后台密码 |
| 4 | 漏绑 KV 命名空间 | 配置不持久/异常 | 绑定 KV，变量名 `KV` |
| 5 | 改了变量仍不生效 | 旧构建在跑 | **重新部署**（关键！） |
| 6 | 访问根域名是 Nginx 页 | 这是防探测伪装 | 后台入口在 `/admin` |
| 7 | 把 /UUID 当入口 | 仍显示 Nginx 页 | 正确入口是 `/admin` |
| 8 | CNAME 指错 | 行为异常 | 统一指向 `edgetunnel.pages.dev` |
| 9 | 改完 NS 仍无效 | 域名拼写错位 | 核对 zaddone vs addone |
| 10 | 改完 NS 等很久 | 全球 DNS 缓存 | 等 15–30 分钟，点"检查名称服务器" |
| 11 | 接管页有 8 条 A/AAAA | 注册商默认停放记录 | 全部删除后"继续前往激活" |
| 12 | 节点连不上 | ProxyIP 失效 | 订阅加 `?proxyip=新IP` |

---

## 关联笔记

- 校园网终极折腾指南 — 校园网环境下使用本节点的网关与代理策略

---

## 参考资料

- [cmliu/edgetunnel 仓库（权威）](https://github.com/cmliu/edgetunnel)
- [官方详细教程 cmliussss.com/p/edt2](https://cmliussss.com/p/edt2/)
- [LancelotRar/best-cf-ips — 优选 IP](https://github.com/LancelotRar/best-cf-ips)
- [DigitalPlatDev/FreeDomain — 免费域名注册](https://github.com/DigitalPlatDev/FreeDomain)
- [YouTube 主教程 CM 喂饭 27](https://www.youtube.com/watch?v=kuL4xR2Co9A)
- [YouTube 备选教程](https://www.youtube.com/watch?v=iYiH-PjfGYw&t=418s)
- [YouTube CF VLESS 教程](https://www.youtube.com/watch?v=tKe9xUuFODA&t=474s)
- [wandou.eu.org Edgetunnel 指南](https://wandou.eu.org/archives/410)
- [fastly.blog.cmliussss.com edt2 文档](https://fastly.blog.cmliussss.com/p/edt2/)
