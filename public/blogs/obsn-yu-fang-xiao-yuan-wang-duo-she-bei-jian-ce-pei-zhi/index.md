> 来源：Obsidian/20-技术知识库/OpenWrt 预防校园网多设备检测配置.md

# OpenWrt 预防校园网多设备检测配置指南

> [!info] 原理概述
> 校园网（如锐捷、深信服等）主要通过 DPI（深度包检测）技术分析网络流量特征来判断是否有多台设备共享网络。主要的检测特征包括：**不同的 TTL 值**、**不同的 NTP 时间服务器请求**、**不同的 HTTP User-Agent** 以及 **IPID 递增规律**。我们需要在路由器层面将这些特征统一，伪装成单一设备。

## 1. 统一 TTL 值（基础且核心）

不同操作系统发出的数据包初始 TTL 不同，且每经过一个路由器 TTL 会减 1。统一 WAN 口发出的数据包 TTL 可以有效防范基于跳数的检测。

> [!warning] 注意事项
> 从 OpenWrt 22.03 开始，防火墙已升级为 `fw4` (nftables)，旧版的 `iptables` 命令已失效。以下配置针对基于 `fw4` 的新版固件（如 Kwrt 24.10）。为了兼容部分缺失特定内核模块的固件，建议使用自定义链。

**操作步骤（通过 SSH 连接路由器终端执行）：**

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

## 2. 劫持 NTP 请求

不同设备（Windows/Mac/Android）默认的 NTP 时间服务器不同。路由器必须统一接管局域网内的所有对时请求。

**操作步骤（网页后台）：**

1. 导航至 `网络` -> `DHCP/DNS`。
2. 在 `常规设置` 选项卡中，向下滚动。
3. 勾选 **截获 NTP 请求** (Intercept NTP)。
4. 点击 `保存并应用`。

## 3. 统一 User-Agent (使用 UA2F)

明文 HTTP 流量会暴露不同设备的浏览器 UA。使用 UA2F (User-Agent to Firefox) 插件可以统一修改未加密 HTTP 流量的特征。

> [!bug] UA2F 未工作/失效排查
>
> 1. **必须关闭流量卸载：** 在 `网络` -> `防火墙` -> `常规设置` 中，将 **“路由/NAT 卸载”** 设为 **禁用**（关闭硬件/软件流量卸载）。流量卸载会绕过 CPU 和防火墙，导致 UA2F 无法抓取数据包。
> 2. **代理软件冲突：** OpenClash、PassWall 等网络代理工具可能会劫持 80/443 端口流量，导致 UA2F 拿不到数据。配置和测试时建议先暂时关闭代理软件，或在代理规则中排除校园网检测流量。

**操作步骤（网页后台）：**

1. 关闭流量卸载后，进入 `服务` -> `UA2F`。
2. 勾选 `启用`、`自动设置防火墙规则`、`处理来自内网的 HTTP 流量`。
3. 点击 `保存并应用`。
4. 使用底部的 `检查 User-Agent` 测试服务器端 UA 是否已统一。

## 4. 进阶防御（按需配置）

如果上述步骤后仍被检测，可叠加以下方案：

- **修改 IPID 防检测：** 在编译固件时加入 `kmod-rkp-ipid` 模块，修改 IPID 递增规律。
- **开启 DNS 加密：** 使用 `https-dns-proxy` 或 `SmartDNS` 等插件，将上游 DNS 设置为 DoH/DoT 加密服务器，防止 DNS 请求暴露设备厂商特征（如苹果 mDNS 请求、小米服务器请求）。

---

## 参考资料

- [Openwrt 编译与防校园网多设备检测配置全流程](https://www.hetong-re4per.com/posts/multi-device-detection/)
- [OpenWrt 绕过校园网多设备检测](https://blog.blueke.top/posts/407208/)
