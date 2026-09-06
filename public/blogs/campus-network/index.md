> 来源：Obsidian/20-技术知识库/网络/校园网终极折腾指南.md

# 校园网终极折腾指南

> 核心目标
> 本指南旨在彻底解决校园网（如 giWiFi、锐捷、深信服等）的诸多痛点，实现以下四大终极目标：
> 1. **突破设备限制**：绕过 3 台设备限制，并防止深信服 DPI 检测封号。
> 2. **防 DNS 劫持**：防止网关透明劫持 53 端口，保护隐私。
> 3. **全局无感去广告**：在解析阶段直接屏蔽广告域名。
> 4. **全自动断线重连**：彻底告别每天手动点击认证弹窗的烦恼。

---

## 一、网络架构与检测原理

### 1. 整体架构

采用 **OpenWrt（主路由）+ AdGuard Home（旁路 DNS）** 的方案，常以 DietPi/树莓派等独立环境作为旁路设备：

- **NAT 伪装**：所有设备连接 OpenWrt，校园网计费系统仅可见路由器 WAN 口的单一 MAC/IP 地址。
- **DoH 加密**：拦截局域网 53 端口（UDP）请求，由 AdGuard Home 封装为 HTTPS 流量（443 端口）转发，绕过校园网网关的 DPI 检测与 DNS 劫持。
- **黑名单阻断**：利用本地规则在解析阶段直接屏蔽广告域名，实现全网无感去广告。
- **绿灯通道**：放行系统探测域名与认证域名走明文，保证认证页面正常弹出。

### 2. 多设备检测原理

校园网主要通过 **DPI（深度包检测）** 分析不同设备流量的特征来判断是否存在多台设备共享上网。常见检测特征包括：

- **不同的 TTL 值**（不同操作系统初始 TTL 不同，且每过一个路由器递减 1）
- **不同的 NTP 时间服务器请求**（Windows / macOS / Android 默认对时服务器不同）
- **不同的 HTTP User-Agent**（暴露浏览器与设备厂商信息）
- **IPID 递增规律**（不同设备 IP 标识符递增模式不同）

因此，需要在路由器层面将这些特征统一，把多台设备伪装成单一设备。

---

## 二、OpenWrt 预防多设备检测

> 版本说明
> 从 OpenWrt 22.03 开始，防火墙已升级为 `fw4`（nftables），旧版的 `iptables` 命令已失效。以下配置针对基于 `fw4` 的新版固件（如 Kwrt 24.10）。为兼容部分缺失特定内核模块的固件，建议使用自定义链。

### 1. 统一 TTL 值

通过 SSH 登录 OpenWrt 终端执行以下命令，写入规则并重启防火墙：

```bash
# 写入自定义的 nftables TTL 修改规则
cat << 'EOF' > /etc/nftables.d/12-mangle-ttl-128.nft
chain custom_ttl_set {
    type filter hook postrouting priority 300; policy accept;
    oifname "wan" ip ttl set 128
    oifname "wan" ip6 hoplimit set 128
    oifname "pppoe-wan" ip ttl set 128
    oifname "pppoe-wan" ip6 hoplimit set 128
}
EOF

# 重启防火墙使规则生效
service firewall restart
```

_验证命令（可选）：_ `nft list ruleset | grep -A 6 "custom_ttl_set"`

### 2. 劫持 NTP 请求

统一接管局域网内所有设备的对时请求，消除不同系统的时间服务器差异。

1. 导航至 `网络` -> `DHCP/DNS` -> `常规设置`。
2. 勾选 **截获 NTP 请求**（Intercept NTP）。
3. 点击 `保存并应用`。

### 3. 统一 User-Agent（UA2F）

明文 HTTP 流量会暴露不同设备的浏览器 UA。使用 UA2F（User-Agent to Firefox）插件统一修改未加密 HTTP 流量的特征。

1. 导航至 `服务` -> `UA2F`。
2. 勾选 `启用`、`自动设置防火墙规则`、`处理来自内网的 HTTP 流量`。
3. 点击 `保存并应用`。
4. 使用底部的 `检查 User-Agent` 测试服务器端 UA 是否已统一。

> 前置条件与故障排查
> **必须关闭流量卸载**：在 `网络` -> `防火墙` -> `常规设置` 中将 **路由/NAT 卸载** 设为 **禁用**。流量卸载会绕过 CPU 与防火墙，导致 UA2F 无法抓包。
>
> **代理软件冲突**：OpenClash、PassWall 等代理工具可能劫持 80/443 端口流量，导致 UA2F 拿不到数据。配置与测试时建议先暂时关闭代理，或在代理规则中排除校园网检测流量。

### 4. 进阶防御（按需配置）

若完成上述步骤后仍被检测，可叠加以下方案：

- **修改 IPID 防检测**：编译固件时加入 `kmod-rkp-ipid` 模块，修改 IPID 递增规律。
- **开启 DNS 加密**：使用 `https-dns-proxy` 或 `SmartDNS` 等插件，将上游 DNS 设为 DoH/DoT 加密服务器，防止 DNS 请求暴露设备厂商特征（如苹果 mDNS 请求、小米服务器请求）。

---

## 三、部署 AdGuard Home 旁路 DNS

利用独立环境（如 DietPi/树莓派）部署旁路 DNS，把局域网 DNS 请求加密封装为 HTTPS（DoH）流量，绕过校园网对 53 端口的劫持。

### 1. 容器化部署

使用 `host` 网络模式确保无缝接管局域网端口，并建立数据持久化：

```bash
mkdir -p ~/docker-files/adguard-data/work
mkdir -p ~/docker-files/adguard-data/conf

docker run -d \
    --name adguardhome \
    --restart unless-stopped \
    --network host \
    -v ~/docker-files/adguard-data/work:/opt/adguardhome/work \
    -v ~/docker-files/adguard-data/conf:/opt/adguardhome/conf \
    adguard/adguardhome
```

### 2. DNS 上游与“绿灯通道”配置（关键）

进入面板（`http://192.168.1.133`）-> **设置** -> **DNS 设置**：

- **上游 DNS 服务器**（开启并行请求）：

  ```
  https://dns.alidns.com/dns-query
  https://doh.pub/dns-query
  [/wifiopenapiauth.com/msftconnecttest.com/msftncsi.com/captive.apple.com/connectivitycheck.gstatic.com/connect.rom.miui.com/]114.114.114.114
  ```

  > 绿灯通道解析
  > 最后一行极其重要！它能让系统网络探测域名和 giWiFi 认证域名走明文、主动被校园网劫持，从而**保证认证页面能正常弹出**，避免出现“安全死锁”（即 DoH 加密后认证弹窗无法跳出）。

- **Bootstrap DNS**（用于解析上游节点）：

  ```
  223.5.5.5
  119.29.29.29
  114.114.114.114
  ```

### 3. 拦截规则配置

进入 **过滤器** -> **DNS 黑名单**，启用精简规则以防误杀：

- `CHN: anti-AD`（国内去广告主力）
- `AdGuard DNS filter`（基础兜底）
- `OISD Blocklist Big`（大白名单无感过滤）

> 强屏蔽环境应对策略
> 若校园网强屏蔽导致 GitHub 规则无法拉取，可利用国内加速镜像替换规则 URL；或直接在宿主机新建规则文件（路径如 `~/docker-files/adguard-data/work/my_local_filter.txt`），并在面板“自定义列表”中填入容器内绝对路径：`/opt/adguardhome/work/my_local_filter.txt`。

---

## 四、OpenWrt 强制引流与防泄漏

必须切断操作系统的“并发查询”机制，确保解析请求 100% 经过 AdGuard Home：

1. **修改 DHCP 下发配置**：
   - 路径：`网络 -> 接口 -> LAN -> DHCP 服务器 -> 高级设置`。
   - 设置 **DHCP 选项** 为：`6,192.168.1.133`。

   > 致命禁忌
   > 绝对不能添加备用 DNS（如 `,192.168.1.1`），否则会导致操作系统并发查询，引发 DNS 泄露和广告漏网，使防劫持彻底失效。必须容忍单点故障风险以换取绝对安全。

2. **隔绝上级污染**：
   - 路径：`网络 -> DHCP/DNS -> 常规设置`。
   - 勾选 **忽略解析文件**（Ignore resolve file）。

_配置完成后，局域网设备需断开 WiFi 重新连接，以获取新的 DNS 参数。_

---

## 五、全自动断线无感重连

利用 OpenWrt 的计划任务（Crontab）每分钟检测网络，一旦发现被校园网踢下线，自动发送 POST 认证请求完成无感重连。**由于每所学校的认证地址、Cookie 名、加密 `data` 都不一样**，本节不再贴出可直接复制的脚本，而是介绍一种通用流程——你自己抓一次登录请求，再交给 AI 生成适配你环境的脚本。

### 1. 抓取属于你自己的登录请求

这一步的目标是：在浏览器里手动登录一次校园网，同时让开发者工具把登录时浏览器"发出去的那条请求"完整记录下来。这条请求里包含了**网关地址、Cookie、加密后的账号密码**，正是后续脚本要照搬的全部内容。

> 何时打开 F12？
> 一定要**先打开开发者工具，再点击登录按钮**。登录成功的瞬间页面通常会发生跳转，如果不提前开，请求记录会被浏览器瞬间清空，导致抓不到任何东西。

**操作步骤：**

1. **打开认证页面**：在电脑浏览器中打开校园网认证页，输入账号密码，但**先不要点登录**。
2. **启动开发者工具**：按 `F12`（或右键页面空白处选择"检查"），在弹出的面板中切换到 **网络（Network）** 标签页。
3. **开启"保留日志"**：在网络面板的工具栏中勾选 **保留日志（Preserve log）**，并点一下"清除"按钮清空旧记录。这一步非常关键，否则登录跳转后请求记录会被清空。
![file-20260906163753190](/blogs/campus-network/file-20260906163753190.png)
   
4. **触发登录**：回到页面，点击"登录"按钮完成认证。
5. **定位 POST 请求**：网络面板里会出现若干条新记录。寻找那条 **方法（Method）显示为 `POST`**、名称（Name）通常包含 `login`、`auth`、`portal` 或 `user` 的请求（giWiFi 通常是 `authLogin?...`，锐捷通常是 `eportal/...`）。点击它，右侧"载荷（Payload）"或"表单数据"里就能看到你刚才提交的账号密码——通常是加密后的乱码，这很正常。

   ![抓包得到的 POST 请求列表](/blogs/campus-network/devtools-network-post-row.png)

6. **复制为 cURL**：右键点击这条 POST 请求，依次选择 **复制 → 复制为 cURL (bash)**。浏览器会把整条请求（含 URL、所有请求头、Cookie、表单数据）打包成一段可执行的 cURL 命令。

> 为什么要"复制为 cURL"而不是手抄参数？
> 手抄几乎一定会漏掉 Cookie、Referer、UA、`data` 加密字段等关键参数，而 cURL 是浏览器**一字不差**导出的完整请求，能保证脚本获得和真实登录一样的服务端响应。

### 2. 把抓到的请求交给 AI 生成脚本

把上一步复制的那一大段 cURL 命令直接发给 AI（推荐连同"我想把它改成 OpenWrt 自动重连脚本"的需求一并说明）。AI 会基于这段命令帮你做两件事：

- **剥离环境噪音**：去掉 `Accept-Language`、`User-Agent` 等与服务端鉴权无关的请求头，只保留 `Cookie`、`Content-Type`、`Referer` 等必需项，减少后续 Cookie 失效带来的影响。
- **生成可直接粘贴的脚本**：套用下面的标准模板，把 cURL 的 URL/请求头/数据原样填进去，并把检测断网的方式改成更稳健的 HTTP 特征匹配（`curl http://www.msftconnecttest.com/connecttest.txt` 抓取 `Microsoft Connect Test` 字符串），而不是容易被网关劫持的 `ping`。

> 给 AI 的"标准提问模板"
> 可以直接复制下面这段，把 cURL 命令粘到尾部发出去：
>
> ```
> 这是我抓到的校园网登录请求，请把它转成 Shell 脚本并满足：
> 1) 检测断网时请求 http://www.msftconnecttest.com/connecttest.txt，
>    判断返回内容是否包含 "Microsoft Connect Test"，超时 3 秒；
> 2) 仅在检测失败时才执行 POST 登录请求；
> 3) 输出到 /dev/null，不打印任何日志；
> 4) 在脚本开头加 export PATH=/usr/sbin:/usr/bin:/sbin:/bin。
>
> [cURL 命令粘贴在这里]
> ```

最终你会得到一个可以直接覆盖到 `/root/giwifi_login.sh` 的脚本。把脚本写好后**一定要先手动测试一次**：

1. 在 OpenWrt 终端执行 `chmod +x /root/giwifi_login.sh` 赋予权限。
2. 在电脑浏览器里手动"下线"（或等待真正的 24 小时强制踢人）。
3. 终端里直接执行 `/root/giwifi_login.sh`，几秒后网络恢复即视为脚本可用。

### 3. 设置计划任务

进入 OpenWrt 面板 -> **系统** -> **计划任务**，添加：

```
* * * * * /root/giwifi_login.sh
```

点击保存并应用。路由器此后将每 1 分钟检测一次，断网后几十秒内即可自动发送凭证完成无感重连。

> Cookie 与加密参数会过期
> 大部分校园网（包括 giWiFi、锐捷）会在长时间未登录后刷新 `PHPSESSID` 或加密密钥（`iv`）。如果某天发现脚本突然失灵，**不需要改脚本结构**，只需按本节第 1 步重新抓一次请求、把新的 cURL 再次交给 AI 重写脚本即可。整套流程可以反复复用。

---

## 六、验证与排障指南

### 1. 验证防劫持

在电脑终端执行：

```powershell
nslookup baidu.com 192.168.1.133
```

- **穿透成功**：Server 返回 `DietPi.lan` 或正确节点 IP。
- **遭遇劫持**：Server 显示 `wifiopenapiauth.com` 等认证页特征，需重新检查上述配置。

### 2. 10 秒宕机自救法

若 AdGuard Home 意外崩溃导致全网无法解析（表现为微信正常、网页打不开）：

- 登录 OpenWrt 后台，删除 DHCP 选项中的 `6,192.168.1.133`，保存并应用。
- 手机等设备重连 WiFi 即可恢复基础网络；待修复容器后，再恢复该 DHCP 设置。

### 3. 常见故障排查汇总

| 现象 | 可能原因 | 处理建议 |
| --- | --- | --- |
| UA2F 抓不到包、UA 未统一 | 路由/NAT 卸载未关闭 | `网络 -> 防火墙 -> 常规设置` 禁用卸载 |
| UA2F 无数据 | 代理软件劫持 80/443 | 临时关闭 OpenClash/PassWall 再测试 |
| 仍被多设备检测 | 缺少 IPID / DNS 加密防御 | 叠加“进阶防御”方案 |
| 规则无法拉取 | 校园网屏蔽 GitHub | 用国内镜像或本地 `.txt` 规则文件 |
| 认证弹窗无法弹出 | DoH 导致“安全死锁” | 确认已配置绿灯通道域名分流 |
| 网页打不开但微信正常 | AdGuard Home 宕机 | 删除 DHCP 选项 `6,...` 临时恢复 |

---

## 参考资料

- [Openwrt 编译与防校园网多设备检测配置全流程](https://www.hetong-re4per.com/posts/multi-device-detection/)
- [OpenWrt 绕过校园网多设备检测](https://blog.blueke.top/posts/407208/)

---

> 整理说明
> 本文由《校园网终极折腾指南》《OpenWrt 预防校园网多设备检测配置指南》《校园网 (giWiFi) 突破限制与全网络防劫持去广告实战记录》三篇笔记合并整理而成，保留了各篇的关键技术内容并去重，统一了术语与标题层级。

---

## 相关笔记

- [OpenWrt 预防校园网多设备检测配置指南](/blog/obsn-yu-fang-xiao-yuan-wang-duo-she-bei-jian-ce-pei-zhi) — OpenWrt 侧防多设备检测的原始配置（TTL/NTP/UA2F/IPID）
- 校园网 (giWiFi) 突破限制与全网络防劫持去广告 — 树莓派/DietPi 旁路部署的实战记录
- [Edgetunnel CF Pages 全流程部署与 522 排查实战](/blog/edgetunnel-cf) — 用于科学上网的 CF Pages 代理节点部署
