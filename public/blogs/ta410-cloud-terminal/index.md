> 来源：Obsidian/20-技术知识库/硬件/TA410_云终端_完整修复手册.md

# 青葡萄 TA410 云终端 · 刷机与网卡修复完整手册

> **适用读者**：拿到这台设备 + 本文档的人，应能快速了解现状、复现已做过的操作、继续完成网卡修复与内核编译。
> **最后更新**：2026-09-02
> **维护说明**：本文档整合了《CS918 网卡修复报告》、Google Gemini 完整刷机对话、MobaXterm 完整启动日志，以及全部调试过程。其中网卡 PHY 型号以**最终拆机确认**为准（LAN8720A），早期报告中的"RTL8201F"结论已被推翻。

---

## 1. 设备硬件信息

| 项目 | 详情 |
|---|---|
| **设备型号** | 青葡萄科技 THINPUTER **TA410** 智能云终端（与 CS918 Q7V 同板型/同参考设计） |
| **主控 SoC** | Rockchip **RK3188**（Cortex-A9 四核，最高 1.6GHz，ARMv7 / armhf 32 位） |
| **实际芯片丝印** | F16B121PH（内核识别为 "RK3188T CS918"，RK3188 的低功耗降频版） |
| **内存** | 1 GB DDR3 |
| **板载存储** | 8 GB **NAND Flash**（非 eMMC，原厂启动介质） |
| **有线网卡 PHY** | **SMSC LAN8720A**（丝印：第一行 SMSC / 第二行 8720A / 第三行 925A72A / 第四行 BTW） |
| **PHY 参考时钟** | **板上无 25MHz 晶振**（已拆机确认，LAN8720A 周围只有电感 2R2 和电容） |
| **GPU** | ARM Mali-400 MP4（内核 `lima` 驱动，4 个 pp 核心，128K L2 cache） |
| **显示控制器** | Rockchip VOP + IT66121 HDMI 转码芯片 |
| **RTC** | NXP PCF8563（I2C 地址 0x51，内核识别为 rtc0；有"低电压"告警，时钟不可靠） |
| **USB 控制器** | 2× DWC2 OTG（`10180000.usb`、`101c0000.usb`） |
| **主板丝印** | H16_MAIN_V13 20160528 |
| **DDR 颗粒** | SEC（三星）K4B4G16 系列 |
| **电源** | 5V / 2A DC 圆口，**5.5×2.1mm，内正外负** |

### 1.1 供电稳压器清单（来自启动日志，可对照排查硬件）

| 稳压器名 | 电压用途 | 状态 |
|---|---|---|
| VCC_RMII | 网卡 PHY 3.3V | 已修复为 always-on |
| VCC_DDR / VDD_LOG / VDD_ARM | 核心供电 | enabled |
| VCC_IO / VDD_10 | IO 供电 | enabled |
| VDD_HDMI / VCC_18 / VCCA_33 | 外设供电 | enabled |
| VCCIO_WL | 无线（本板未用） | disabled |
| sdmmc-supply | SD 卡 | enabled |
| otg-vbus / host-pwr | USB 供电 | enabled |

---

## 2. 设备外观与接口

| 接口 | 数量/规格 | 说明 |
|---|---|---|
| **HDMI** | 1× | 最高 1080P@60Hz（经 IT66121 转码） |
| **VGA** | 1× | 直出，可接老式显示器 |
| **USB 2.0** | 4× | ⚠️ **全部经 USB Hub 芯片扩展，无 OTG 直连**，不支持 USB 线刷 |
| **TF 卡槽（MicroSD）** | 1× | **唯一的外部引导通道**（BootROM 支持） |
| **RJ45 网口** | 1× | 百兆，PHY 为 LAN8720A |
| **音频** | 3.5mm 麦克风输入 + 3.5mm 耳机输出 | 独立两孔 |
| **DC 电源** | 5V 2A | 5.5×2.1mm 圆口，内正外负 |
| **TTL 串口** | 4 针通孔 | 板载调试口，波特率 115200 |

> **拆机要点**：底面四个角的黑色橡胶防滑垫下藏有螺丝；外壳有塑料卡扣，用撬片沿缝隙划开。

---

## 3. 原厂系统与初始状态

- **原厂系统**：基于 Android 深度定制的 **Thinclient OS（瘦客户机系统）**。
- **锁定情况**：开机即进入"**某高校**"校园网的远程桌面连接器（Kiosk 全屏锁定界面），需账号密码登录，且写死了内网虚拟桌面服务器地址。离开校园网即"无法连接服务器"，普通用户无法进入任何本地系统。
- **本质定位**：一台"带网络的显示器+键鼠转接盒"（VDI 客户端），本地无开放操作系统可用。

### 3.1 刷机前遇到的"拦路虎"（逐一破解）

1. **散热片取不下来** → 用热固性导热硅胶粘死，加热不融化，**不可硬撬**（会连芯片焊盘一起拔起报废）。
2. **看不清芯片型号** → 改用 TTL 串口抓开机日志，破译 `52 4B 33 31 30 42` = ASCII "RK310B" = **RK3188**。
3. **USB 线刷失败** → 4 个 USB 口全经 Hub 芯片扩展，无 OTG 直连引脚，MaskROM 模式无法通过 USB 接收固件。
4. **U 盘不能启动** → BootROM 阶段只认 eMMC/NAND 和原生 SDMMC（TF 卡槽），不认 USB。

---

## 4. 当前系统信息

| 项目 | 详情 |
|---|---|
| **操作系统** | Armbian 21.05.0-trunk（Debian Buster） |
| **内核** | `5.10.27-rk3188 #trunk SMP`，构建时间 2021-04-05，armv7l |
| **U-Boot** | `U-Boot 2021.01-armbian`（含 SPL） |
| **当前使用的 DTB** | `/boot/dtb/rk3188-rbox-cs918.dtb` |
| **启动介质** | 29.1 GB SD 卡（`/dev/mmcblk0`，单分区 `mmcblk0p1` 挂载 `/`） |
| **启动方式** | TF 卡启动，U-Boot 读 `/boot/extlinux/extlinux.conf` |
| **SSH 登录** | `root` / 密码 `yourpass` |
| **板载 8G NAND** | DTB 中已定义（`nand-controller@10500000`），但内核**无 NAND 驱动**，未识别 |

关键内核配置（来自 `/boot/config-*`）：
- `CONFIG_ARC_EMAC_CORE=y`
- `CONFIG_EMAC_ROCKCHIP=y`（网卡驱动编译进内核，非模块）
- NAND / MTD 驱动**未编译**

启动参数（`/boot/extlinux/extlinux.conf` 的 APPEND 行）：
```
root=UUID=ff308d0e-e3fa-496e-9a11-ac07af45608b
console=uart8250,mmio32,0x20064000 console=ttyS2,115200
coherent_pool=2M video=HDMI-A-1:e rootflags=data=writeback rw
no_console_suspend consoleblank=0 fsck.fix=yes fsck.repair=yes
net.ifnames=0 bootsplash.bootfile=bootsplash.armbian cpufreq.off=1
```

> **注意 `cpufreq.off=1`**：这是刷机时人为追加的关键参数，用于禁用 CPU 调频（`cpufreq-dt` 驱动在该内核上注册失败 -19，不加会卡死）。

---

## 5. 当前操作方式（联网 + 远程控制）

这是用户当前的完整操作链，接手者需了解：

### 5.1 联网：手机 USB 网络共享

板载网卡未修好，当前通过**手机 USB 网络共享（RNDIS）**上网：

1. 手机用 USB 线连到板子的某个 USB 口。
2. 手机开启"USB 网络共享"。
3. 板子获得 `usb0` 接口，IP 网段 `192.168.70.x`（板子 `192.168.70.3`）。

### 5.2 查看 IP：通过显示器

板子接 HDMI 显示器，开机登录后执行 `ip addr`（或 `ip a`）查看 usb0 的 IP 地址。

### 5.3 远程操作：手机 SSH

用手机上的 SSH 客户端（如 Termux 或 JuiceSSH）连接板子：
```
ssh root@192.168.70.3   # 密码 yourpass
```

### 5.4 电脑操作：scrcpy 手机投屏

手机通过 **scrcpy** 投屏到电脑，实现用电脑键盘鼠标操作手机（进而操作板子），解决"板子无键盘/无法直接操作"的问题。

```
# 电脑上安装 scrcpy 后，USB 连手机
scrcpy
```

### 5.5 完整链路图

```
[电脑] --scrcpy投屏--> [手机] --USB网络共享--> [TA410板子]
                        ↑
                        └── SSH (root@192.168.70.3) 反向操作板子

[显示器] --HDMI--> [TA410板子]  ← 用来 ip addr 看 IP
```

> 补充：早期还用过 TTL 串口（USB-TTL 模块 + MobaXterm）直接操作板子，波特率 115200，console 在 `ttyS2`。

---

## 6. 核心问题清单与状态

| # | 问题 | 状态 | 说明 |
|---|---|---|---|
| 1 | 原厂系统锁定（某高校） | ✅ 已解决 | TF 卡刷入 Armbian 绕过 |
| 2 | 散热片无法拆除 | ✅ 已绕过 | 改走 TTL 串口抓日志 |
| 3 | USB 线刷不可用 | ✅ 已绕过 | 改用 TF 卡启动 |
| 4 | 内核启动崩溃（3.1s 处） | ✅ 已解决 | 换 CS918 DTB + `cpufreq.off=1` |
| 5 | 显示器黑屏 / 键盘输入 | ✅ 已解决 | 用户自行解决 |
| 6 | 无网络、命令需手敲 | ✅ 已解决 | 手机 USB 网络共享 |
| 7 | 无法远程操作 | ✅ 已解决 | SSH + scrcpy |
| 8 | **有线网卡 probe 失败** | ⏳ **核心未解决** | eth0 不出现，见第 8 节 |
| 9 | 8G NAND 识别不到 | ⏳ 未解决 | 需自编译内核加 NAND 驱动 |

---

## 7. 刷机全流程（从选系统到点亮）

### 7.1 选系统的关键结论

- **RK3188 没有官方/现成的 Armbian 完美适配包**，只能"考古"。
- 关键资料源：Armbian 论坛 RK3188 帖子、俄罗斯开发者 balbes150 的镜像库（Yandex 网盘）。
- 最终采用：Armbian 21.05.0-trunk（Debian Buster，内核 5.10.27），DTB 用 **rk3188-rbox-cs918.dtb**（CS918 是当年最泛滥的公版 RK3188 盒子，硬件定义最"丐"，最不易踩高级电源管理芯片的坑）。

### 7.2 硬件开荒（拆机 + 识别芯片）

1. 拆机：撕四角橡胶垫 → 拧螺丝 → 撬卡扣。
2. 散热片取不下（热固性胶）→ 放弃拆芯片。
3. TTL 串口抓日志：USB-TTL 模块接板子 4 针通孔（GND/TX/RX，**VCC 不接**），波特率 115200。
4. 破译 `52 4B 33 31 30 42` = "RK310B" = RK3188（末尾 0B 是 PLL 未初始化时的波特率漂移，实为 88）。

### 7.3 刷机路径探索（走过的弯路）

| 尝试 | 结果 |
|---|---|
| USB 双头线刷（MaskROM） | ❌ 4 个 USB 全经 Hub，无 OTG |
| U 盘启动 | ❌ BootROM 不认 USB |
| **TF 卡启动** | ✅ **最终方案** |

### 7.4 TF 卡刷机 + 启动（最终成功路径）

1. 用 balenaEtcher 把 Armbian 镜像烧到 TF 卡（镜像用 balbes150 的 RK3188 版）。
2. **关键一步**：用树莓派 3B（或其他 Linux 机器）挂载 TF 卡，修改 `/boot/extlinux/extlinux.conf`：
   ```bash
   # 换成 CS918 的 DTB
   sudo sed -i 's/rk3188-ugoos-ut2.dtb/rk3188-rbox-cs918.dtb/g' /mnt/tf/boot/extlinux/extlinux.conf
   # 追加禁用 CPU 调频（否则内核 3.1s 处崩溃）
   sudo sed -i 's/bootsplash.armbian/bootsplash.armbian cpufreq.off=1/g' /mnt/tf/boot/extlinux/extlinux.conf
   ```
3. 卸载 TF 卡，插回 TA410，上电启动。
4. 首次启动进入 `armbian login:`，设置 root 密码 + 创建普通用户（可狂按回车跳过）。
5. 登录后即 `root@rk3188:~#`，系统点亮成功。

### 7.5 启动日志关键硬件识别（来自 MobaXterm 日志）

- `Model: RK3188 rbox`，`DRAM: 1 GiB`
- `mmc0: new high speed SDHC card ... SDABC 29.1 GiB`
- `rtc-pcf8563 1-0051: registered as rtc0`（低电压告警）
- `[drm] HDMITX it66121 ... indentified`
- `lima 10090000.gpu: mali400 ... pp0~pp3`
- `dwc2 10180000.usb / 101c0000.usb: DWC OTG Controller`（两个 USB 控制器）
- USB 设备：YICHIP 无线键鼠（`3151:3020`）、CX 2.4G 无线接收器（`3554:fa09`）、USB2.0 Hub（`05e3:0608`）
- `rockchip_emac 10204000.ethernet: ARC EMAC detected ... MAC address d2:2d:3e:50:f9:25`

---

## 8. 网卡问题：完整技术分析

### 8.1 现象

开机 `dmesg` 报错（当前最终状态，已修完设备树后）：

```
[ 3.408976] rockchip_emac 10204000.ethernet: ARC EMAC detected with id: 0x7fd02
[ 3.417265] rockchip_emac 10204000.ethernet: IRQ is 36
[ 3.423669] rockchip_emac 10204000.ethernet: MAC address is now d2:2d:3e:50:f9:25
[ 3.432974] libphy: Synopsys MII Bus: probed
[ 3.437815] mdio_bus Synopsys MII Bus: mdio has invalid PHY address
[ 3.444922] mdio_bus Synopsys MII Bus: scan phy mdio at address 0
[ 4.787693] rockchip_emac 10204000.ethernet: cannot register MDIO bus Synopsys MII Bus
[ 4.796642] rockchip_emac 10204000.ethernet: failed to probe MII bus
[ 4.803822] rockchip_emac 10204000.ethernet: failed to probe arc emac (-5)
```

- `ip link` 只有 `lo`、`sit0`、`usb0`，**没有 eth0**。
- 最终错误码 **-5 = -EIO**。
- 关键：`scan phy mdio at address 0` 之后卡约 1.3 秒才报错，是 **MDIO 事务完成标志轮询超时**（40 × 25ms ≈ 1s）。

### 8.2 错误码演进史（排查轨迹）

| 阶段 | 错误码 | 根因 | 修复动作 |
|---|---|---|---|
| 最初 | `-5`（MDIO 注册失败） | pinctrl 冲突（4 个引脚组互相重叠）+ PHY compatible 缺失 | 精简 pinctrl、补 compatible |
| 补 pinctrl 后 | `-22`（EINVAL） | pinctrl-0 引用了冲突的引脚组 | 精简为 `<0x1234 0x0d>` |
| 补 compatible 后 | `-19`（ENODEV，of_phy_connect failed） | PHY 节点结构是旧式（直接子节点），驱动是新式（要求 mdio 子节点） | 加 `mdio {}` 子节点 |
| 加 mdio 后（当前） | `-5`（EIO，MDIO 扫描超时） | MDIO 地址 0 读不到 PHY ID | **卡在硬件层，见 8.4** |

### 8.3 已确认的软件层事实（都已修对）

经过多轮调试，设备树的以下配置**已与官方内核定义完全对齐**，无需再改：

1. ✅ **pinctrl**：`pinctrl-0 = <0x1234 0x0d>`（emac-xfer + emac-mdio），与官方 `rk3188.dtsi` 一致
2. ✅ **emac-xfer 引脚组**（8 根，全 func 2）：`gpio3-16~23`，其中第 6 根 `gpio3-21` 就是 `mac_clk`（官方确认 func 2 正确）
3. ✅ **compatible**：`ethernet-phy@0` 加了 `compatible = "smsc,lan8720a"`
4. ✅ **phy 属性**：`phy = <0x0f>`（属性名就是 `phy`，不是 `phy-handle`）
5. ✅ **phy-supply**：REG9 "VCC_RMII" 加了 `regulator-always-on`，供电已上电（`VCC_RMII: enabled`，`supplied by vsys`）
6. ✅ **mdio 子节点**：PHY 已包进 `mdio {}`，驱动能正确扫描（出现了 `scan phy mdio at address 0`）
7. ✅ **时钟树**：`ext_rmii`（50MHz）→ `sclk_macref`（50MHz，enabled）

### 8.4 当前卡点：硬件层（软件已到极限）

软件层（设备树）已做到理论上完美，但 **MDIO 地址 0 读不到 PHY ID**（读回无效值，扫描超时）。这排除了供电问题（供电已上电），只剩硬件层三个可能，按概率排序：

1. **LAN8720A 的 25MHz 参考时钟没起振**（最可能）
   - LAN8720A 必须有参考时钟才能工作，板上**无晶振**。
   - DTB 里的 `ext-rmii` 是 50MHz（给 MAC 的 macref），但**是否物理地送到了 PHY 的 CLKIN（第 2 脚）是未知的**。
   - 整个 DTS 里**没有任何 mac_clk 时钟输出引脚的特殊配置**（因为 CS918 的 RTL8201F 自带晶振，不需要）。

2. **MDIO 引脚接错**
   - 设备树 emac-mdio 用的是 GPIO3_C0/C1（gpio3-24/25），但 TA410 板上 LAN8720A 的 MDC/MDIO 可能接别的引脚。

3. **PHY 的 MDIO 地址不是 0**
   - LAN8720A 的 PHYAD0 引脚若拉高，地址是 1 而非 0（但驱动扫地址 0 失败，可尝试地址 1）。

> **关键矛盾点（历史报告 vs 最终结论）**：
> - 早期《CS918 网卡修复报告》假设"PHY 是 RTL8201F + 25MHz 晶振，板子走外部时钟，需注册 ext_rmii 时钟"。
> - 实际拆机确认 PHY 是 **LAN8720A + 无晶振**。
> - 因此早期"注册 ext_rmii 时钟"的修复方向**前提已不成立**，真正要解决的是"LAN8720A 的参考时钟从哪来"。

---

## 9. 已完成的全部操作（时间线）

### 阶段 A：硬件开荒与刷机
1. 拆机（撕胶垫、拧螺丝、撬卡扣），散热片取不下。
2. TTL 串口抓日志，识别芯片为 RK3188（`52 4B 33 31 30 42`）。
3. USB 线刷、U 盘启动均失败，确定 **TF 卡启动**方案。
4. balenaEtcher 烧 Armbian 镜像到 TF 卡。
5. 树莓派 3B 上改 `extlinux.conf`：换 CS918 DTB + 加 `cpufreq.off=1`。
6. TF 卡插回上电，成功启动，设置密码登录。

### 阶段 B：初始联网
7. 解决黑屏、键盘输入问题。
8. 手机 USB 网络共享 → 板子获得 `usb0`（192.168.70.3）。
9. 手机 SSH 连板子（`root@192.168.70.3`，密码 `yourpass`）。
10. 电脑用 scrcpy 投屏手机，实现远程操作。

### 阶段 C：网卡诊断（早期，有误判）
11. 下载内核 5.10 源码，梳理 emac probe 流程，定位 `-5` 是 MDIO 超时。
12. 补 `phy-mode`（无效，dtsi 本就有）。
13. 补 pinctrl（v1 失败、v2 追加 emac-xfer），发现板子用的是 vendor 自定义 `emac-xfer-ext` 组，**撤销**。

### 阶段 D：拆机 + 修正认知（关键转折）
14. **拆机确认 PHY 丝印是 SMSC 8720A（LAN8720A），且板上无 25MHz 晶振**。
15. 推翻早期"RTL8201F"假设。

### 阶段 E：设备树修复（逐步推进）
16. **精简 pinctrl**：`pinctrl-0` 从 `<0x0c 0x0d 0x0e 0x1234>` 精简为 `<0x1234 0x0d>`，消除 `-22`。
17. **补 compatible**：给 `ethernet-phy@0` 加 `compatible = "smsc,lan8720a"`，MDIO 注册成功，错误变 `-19`。
18. **确认 phy 属性名**：确认是 `phy`（非 `phy-handle`），无需改。
19. **加 regulator-always-on**：给 REG9 "VCC_RMII" 加 `regulator-always-on`，供电上电（`VCC_RMII: enabled`）。
20. **加 mdio 子节点**：把 `ethernet-phy@0` 包进 `mdio {}`，驱动开始正确扫描（出现 `scan phy mdio at address 0`）。
21. **确认引脚定义正确**：对比官方 `rk3188.dtsi`，emac-xfer 8 根引脚（含 mac_clk）完全一致，无遗漏。

### 阶段 F：时钟与硬件层分析
22. 查时钟树，确认 `ext_rmii`/`sclk_macref` 均 50MHz enabled。
23. 查 DTS 无 mac_clk 输出引脚配置 → 判断 CS918 DTB 本身就不含时钟输出（因 RTL8201F 不需要）。
24. 结论收敛到硬件层：LAN8720A 的参考时钟来源存疑。

---

## 10. 当前 DTB 的最终状态

当前 `/boot/dtb/rk3188-rbox-cs918.dtb` 已包含以下**所有已生效的修复**：

```dts
ethernet@10204000 {
    compatible = "rockchip,rk3188-emac";
    reg = < 0x10204000 0x3c >;
    interrupts = < 0x00 0x13 0x04 >;
    #address-cells = < 0x01 >;
    #size-cells = < 0x00 >;
    rockchip,grf = < 0x0a >;
    clocks = < 0x02 0x1c4 0x02 0x44 >;
    clock-names = "hclk\0macref";
    max-speed = < 0x64 >;
    phy-mode = "rmii";
    status = "okay";
    assigned-clocks = < 0x02 0x44 >;
    assigned-clock-parents = < 0x0b >;
    pinctrl-0 = < 0x1234 0x0d >;          /* 精简后：emac-xfer + emac-mdio */
    pinctrl-names = "default";
    phy = < 0x0f >;
    phy-supply = < 0x10 >;

    mdio {                                 /* 新增：mdio 子节点 */
        #address-cells = < 0x01 >;
        #size-cells = < 0x00 >;
        ethernet-phy@0 {
            reg = < 0x00 >;
            compatible = "smsc,lan8720a";  /* 新增：PHY 型号 */
            phandle = < 0x0f >;
        };
    };
};
```

REG9 节点（VCC_RMII 供电）也已加 `regulator-always-on;`。

### 10.1 DTB 备份文件

| 文件 | 内容 |
|---|---|
| `rk3188-rbox-cs918.dtb.orig` | 最原始版本 |
| `rk3188-rbox-cs918.dtb.pinctrl-fixed` | pinctrl 修复后 |
| `rk3188-rbox-cs918.dtb.pre-phy-fix` | 加 regulator-always-on 前 |
| `rk3188-rbox-cs918.dtb.pre-mdio` | 加 mdio 子节点前 |

### 10.2 修改 DTB 的标准流程（复现用）

```bash
# 1. 反编译
dtc -I dtb -O dts /boot/dtb/rk3188-rbox-cs918.dtb > /tmp/current.dts 2>/dev/null

# 2. 编辑（用 perl/sed，见各阶段的具体命令）

# 3. 编译回 DTB
dtc -I dts -O dtb -o /tmp/test.dtb /tmp/current.dts 2>/tmp/dtc-warn.log

# 4. 检查（无 "error"/"fatal" 即成功，clocks 警告可忽略）
grep -iE "error|fatal" /tmp/dtc-warn.log && echo "有错误" || echo "编译成功"

# 5. 备份 + 写回 + 重启
cp /boot/dtb/rk3188-rbox-cs918.dtb /boot/dtb/rk3188-rbox-cs918.dtb.bak
cp /tmp/test.dtb /boot/dtb/rk3188-rbox-cs918.dtb
sync && reboot
```

> 注意：`/tmp` 每次重启被清空，重启后需重新反编译。

---

## 11. 网卡修复：剩余可行方向

软件层已到极限，剩余方向需硬件配合。按成本从低到高排列：

### 方向 1：尝试 PHY MDIO 地址 1（零成本，先试这个）

LAN8720A 的 PHYAD0 引脚若拉高，MDIO 地址是 1。改设备树把 `ethernet-phy@0`/`reg` 改成 `@1`/`<0x01>` 试一次。

### 方向 2：硬件测量时钟（有万用表/示波器）

量 LAN8720A 第 2 脚（CLKIN/XTAL1）对地电压/波形：
- 正常应有 50MHz 方波（约 1.6V 直流偏置）
- 若悬空（0V/浮动）→ 硬件没接时钟，软件无解

同时量第 9 脚（VDDCR，1.8V）和第 24 脚（VDDA/VDDIO，3.3V）确认供电。

### 方向 3：看走线（无仪器）

拍高清正对 LAN8720A 芯片照片，看第 2 脚（芯片第 1 脚有圆点标记，第 2 脚在旁边）有没有走线连回主控。

### 方向 4：确认时钟输出引脚配置

理论上 RK3188 的 `mac_clk` 在 GPIO3_C5（gpio3-21），func 2。但若 TA410 板上 PHY 的 CLKIN 连的是别的 GPIO，需要对照实际走线补 pinctrl 时钟输出配置。

### 方向 5：务实的退路 —— USB 网卡（强烈推荐）

花几块钱买 **USB 转 RJ45 网卡**（RTL8152/8153 芯片，内核原生支持），插上即是稳定有线网。**这是最省事、最确定的方案**，且完全绕开板载网卡的硬件时钟问题。

> **结论**：板载网卡能否救回，取决于 PHY 的参考时钟到底有没有从主控输出。若硬件层面时钟确实没接，软件无解，建议直接上 USB 网卡。

---

## 12. 系统迁移到 8G NAND 的方案

### 12.1 现状确认

- 板载 8G 是 **NAND Flash**（不是 eMMC）。
- DTB 已定义 `nand-controller@10500000`（含 `nand-is-boot-medium`，说明原厂就是从 NAND 启动）。
- 但当前内核**无 NAND 驱动**（`dmesg` 无 nand 日志，`/dev/mtd*` 为空）。
- 当前系统装在 29G SD 卡上，只有一个 mmc host（mmc0）。

### 12.2 迁移可行性

**能做，但需要两步大工程：**

1. **重新编译内核**，加入 NAND 驱动：
   ```
   CONFIG_MTD=y
   CONFIG_MTD_NAND=y
   CONFIG_MTD_NAND_ROCKCHIP=y
   ```
   - `rockchip-nand-controller` 驱动明确支持 rk3188，5.15+ 内核已进主线。

2. **改 U-Boot 从 NAND 启动**：
   - 确认 U-Boot 支持 `nand read`
   - 把 boot（kernel + initramfs + dtb）和 rootfs 写入 NAND
   - 改 U-Boot 环境变量（`bootcmd`、`root=` 指向 NAND 分区）

### 12.3 务实建议

8G NAND 容量小、寿命短、速度慢，迁移后体验未必优于当前 29G SD 卡。**建议先修好网络（USB 网卡即可），再评估是否值得折腾 NAND。**

---

## 13. 自编译 Armbian 完整流程

> 目标：编译一个带 NAND 驱动 + 正确 TA410 设备树的内核。**在 x86 Linux 机器上编译，不要在 RK3188 云终端上编译。**

### 13.1 搭建环境

```bash
# 以 Ubuntu/Debian 为例
sudo apt update
sudo apt install -y git build-essential flex bison libssl-dev \
  libncurses-dev device-tree-compiler u-boot-tools \
  gcc-arm-linux-gnueabihf   # ARM 32 位交叉编译器（RK3188 是 armhf，不是 aarch64）

# 拉取 Armbian 构建框架
git clone --depth=1 https://github.com/armbian/build.git
cd build
```

### 13.2 定义板子

Armbian 官方对 RK3188 支持已边缘化，**没有现成 TA410 配置**，需基于最接近的 rk3188 板子（cs918 或 radxa rock）改一份 `.csc`/`.conf`，指定：
- 内核版本（建议 5.15+，NAND 驱动更稳定）
- u-boot 配置
- 输出镜像格式

### 13.3 写正确的 DTS

写一份干净的 `.dts` 源文件（非反编译紧凑格式）：

```
rk3188-ta410.dts
├─ nand-controller@10500000     ← 8G NAND（保留 nand-is-boot-medium）
├─ ethernet@10204000            ← 网卡
│   ├─ phy-mode = "rmii"
│   ├─ phy-supply = VCC_RMII（always-on）
│   └─ mdio { ethernet-phy@0 { smsc,lan8720a } }
├─ 时钟：ext-rmii 50MHz 的正确来源
└─ pinctrl：emac-mdio 引脚按 TA410 实际走线
```

> **必须先解决硬件疑点**：板上无晶振，LAN8720A 的 50MHz 参考时钟从哪来。这是写 DTS 前必须搞清的（见第 11 节方向 2/3）。

### 13.4 启用 NAND 驱动

在 `config/kernel/linux-rockchip64-*.config` 确认/添加：
```
CONFIG_MTD=y
CONFIG_MTD_NAND=y
CONFIG_MTD_NAND_ROCKCHIP=y
```

### 13.5 编译与刷写

```bash
./compile.sh BOARD=rk3188-ta410 BRANCH=current RELEASE=bullseye BUILD_MINIMAL=yes
```

编译 1~3 小时，产出 `.img`，用 balenaEtcher 刷入 SD 卡。

---

## 14. 快速上手指南
### 14.1 连接设备

1. 接上电源，插入 SD 卡（系统盘）。
2. 接 HDMI 显示器，插上 USB 键盘。
3. 或通过 TTL 串口（USB-TTL 模块 + MobaXterm，波特率 115200，console 在 `ttyS2`）。
4. 或通过 USB 网络共享 SSH：`root@192.168.70.3`，密码 `yourpass`。

### 14.2 判断当前状态

```bash
uname -a                    # 内核版本
lsblk                       # 存储（应只有 mmcblk0 = SD 卡）
ip link show                # 网卡（应只有 lo/sit0/usb0，无 eth0）
dmesg | grep -iE "emac|eth|mdio|phy|smsc"   # 网卡日志
cat /sys/class/regulator/*/name 2>/dev/null | grep -i rmii   # 查 PHY 供电
```

### 14.3 常见坑

- **`/tmp` 重启清空**：重启后需重新 `dtc` 反编译。
- **emac 驱动是编译进内核的**（无 `.ko`），所以 `lsmod | grep emac` 无结果。
- **属性名是 `phy`**，不是 `phy-handle`（RK3188 旧驱动）。
- **反编译 DTS 是紧凑格式**，多个属性挤在一行，改时用 perl 上下文锚点比 sed 行号更可靠。
- **dtc 编译的 clocks 警告可忽略**，只关注 `error`/`fatal`。
- **`cpufreq.off=1` 不能删**：删了会导致内核在电源管理模块崩溃。
- **原厂散热片不可硬撬**：热固性胶，硬撬会报废主板。

### 14.4 下一步建议（接手者优先做）

1. **先试 USB 网卡**（最省事，立即可稳定联网）。
2. 若要坚持板载网卡，按第 11 节方向 1→2→3→4 顺序排查硬件时钟。
3. 网络稳定后，再按第 13 节自编译内核救回 NAND。

---

## 15. 附录：关键命令速查

```bash
# ===== DTB 反编译/编译 =====
dtc -I dtb -O dts /boot/dtb/rk3188-rbox-cs918.dtb > /tmp/current.dts 2>/dev/null
dtc -I dts -O dtb -o /tmp/test.dtb /tmp/current.dts 2>/tmp/dtc.log

# ===== 网卡诊断 =====
dmesg | grep -iE "emac|eth|mdio|phy|smsc|scan"
ip link show
ls /sys/class/mdio_bus/          # 应只有 fixed-0（说明 emac MDIO 没扫到 PHY）
ls /sys/bus/mdio_bus/devices/    # 空 = 无 PHY 设备

# ===== PHY 供电 =====
for r in /sys/class/regulator/*; do echo "$(cat $r/name 2>/dev/null): $(cat $r/state 2>/dev/null)"; done

# ===== 时钟树 =====
cat /sys/kernel/debug/clk/clk_summary 2>/dev/null | grep -iE "macref|rmii|emac|mac"

# ===== 存储 / NAND =====
lsblk
cat /proc/partitions
ls -la /dev/mtd* 2>/dev/null && cat /proc/mtd 2>/dev/null
dtc -I dtb -O dts /boot/dtb/rk3188-rbox-cs918.dtb 2>/dev/null | grep -iE "nand|sfc|spi.*flash"

# ===== 内核配置 =====
grep -iE "ROCKCHIP_EMAC|ARC_EMAC|EMAC" /boot/config* 2>/dev/null
zcat /proc/config.gz 2>/dev/null | grep -iE "MTD|NAND"

# ===== 启动配置 =====
cat /boot/extlinux/extlinux.conf   # 看 DTB 路径 + APPEND 参数（含 cpufreq.off=1）

# ===== 回滚 DTB =====
cp /boot/dtb/rk3188-rbox-cs918.dtb.bak /boot/dtb/rk3188-rbox-cs918.dtb
sync && reboot
```

---

## 总结（一页看懂）

- **设备**：青葡萄 TA410 云终端 = RK3188（Cortex-A9 四核）+ 1GB RAM + 8G NAND + LAN8720A 网卡 PHY + Mali400 GPU，5V 2A 供电。
- **原厂系统**：某高校定制的 Thinclient OS，锁定在校园网，无法本地使用。
- **刷机**：TF 卡启动方案，Armbian 21.05（内核 5.10.27），换 CS918 DTB + 加 `cpufreq.off=1` 绕过电源管理崩溃。
- **当前操作**：手机 USB 共享网络（usb0, 192.168.70.3）+ SSH + scrcpy 投屏。
- **核心问题**：板载网卡起不来（MDIO 读不到 PHY），根因是 **LAN8720A 无参考时钟**（板上无晶振，CS918 DTB 未配置时钟输出）；软件层设备树已修到完美，卡在硬件。
- **最务实方案**：**USB 转 RJ45 网卡**，立即解决联网。
- **若要坚持板载网卡**：需硬件确认 LAN8720A 的 CLKIN 是否有 50MHz（量第 2 脚或看走线）。
- **8G NAND**：需自编译内核（加 `CONFIG_MTD_NAND_ROCKCHIP`）+ 改 U-Boot，工程量大，建议网络稳定后再做。
