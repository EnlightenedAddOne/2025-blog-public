> 来源：Obsidian/30-项目与实践/项目说明/嵌入式-智能家居/智能家居物联网系统 - 项目说明文档.md

## 📋 项目概述

本项目是一个基于**嵌入式Linux**和**MQTT协议**的智能家居物联网系统，实现了传感器数据采集、云端通信、设备控制以及智能联动等功能。系统通过多种传感器实时监测环境状态，并根据预设规则自动控制家居设备，同时支持远程云端控制。

---

## 🎯 核心功能

### 1. **传感器数据采集**

- 🌡️ 温湿度监测
- ☀️ 环境光照检测
- 🚶 人体红外感应
- ⚡ 电压监控

### 2. **设备智能控制**

- 💡 LED灯光控制
- 🌀 风扇调速控制
- 🔔 蜂鸣器报警

### 3. **MQTT云端通信**

- 📤 实时上报传感器数据
- 📥 接收云端控制指令
- 🔄 双向通信机制

### 4. **智能联动场景**

- 💡 自动照明：光线不足且有人时自动开灯
- 🌀 智能通风：温湿度过高自动启动风扇
- 🚨 安防模式：夜间检测到人体自动报警
- 💤 节能模式：无人超时自动关闭设备
- ⚠️ 环境报警：温度/电压异常持续报警

---

## 📁 项目结构

```
MQTT/
├── src/                      # 源代码目录
│   ├── main.c               # 主程序入口
│   ├── mqtt_client.c        # MQTT客户端实现
│   ├── linkage.c            # 智能联动逻辑
│   ├── tah.c                # 温湿度传感器
│   ├── light.c              # 光照/红外/人体检测传感器
│   ├── voltage.c            # 电压传感器
│   ├── led.c                # LED控制
│   ├── fan.c                # 风扇控制
│   ├── buzzer.c             # 蜂鸣器控制
│   ├── io.c                 # 通用IO读写接口
│   ├── cJSON.c              # JSON解析库
│   ├── gpio.c               # GPIO操作（暂未使用）
│   └── home.c               # （预留文件）
│
├── inc/                      # 头文件目录
│   ├── head.h               # 主头文件（函数声明）
│   ├── mqtt_client.h        # MQTT客户端头文件
│   ├── linkage.h            # 联动模块头文件
│   └── cJSON.h              # JSON库头文件
│
├── build/                    # 编译输出目录
│   └── app                  # 可执行文件
│
├── test/                     # 测试程序目录
│
├── Makefile                  # 编译配置文件
└── README.md                 # 本说明文档
```

---

## 🔧 技术架构

### **硬件平台**

- **开发板：** STM32MP157 / 类似嵌入式Linux平台
- **传感器接口：** IIO子系统 (`/sys/bus/iio/devices/`)
- **执行器接口：** Sysfs文件系统

### **软件技术栈**

| 技术         | 说明                    |
| ------------ | ----------------------- |
| **编程语言** | C语言                   |
| **通信协议** | MQTT (mosquitto库)      |
| **数据格式** | JSON (cJSON库)          |
| **操作系统** | Linux (Buildroot/Yocto) |
| **编译工具** | GCC + Makefile          |

### **第三方库**

- **libmosquitto：** MQTT客户端库
- **cJSON：** 轻量级JSON解析库
- **pthread：** 多线程支持
- **libm：** 数学库

---

## 📊 数据格式规范

### **上报数据（开发板 → 云端）**

#### 1. 温湿度数据

```json
{
	"tem": 20.5,
	"hum": 65.2,
	"id": 0
}
```

#### 2. 光照数据

```json
{
	"light": 150.3,
	"id": 0
}
```

#### 3. 人体检测数据

```json
{
	"infrared": 1,
	"id": 0
}
```

- `infrared`: `1` = 检测到人体，`0` = 无人

---

### **控制指令（云端 → 开发板）**

#### 1. LED控制

```json
{
	"lamp": true,
	"id": 0
}
```

- `lamp`: `true` = 开灯，`false` = 关灯
- `id`: LED编号（0-1，对应LED1-LED2）

#### 2. 风扇控制

```json
{
	"fan": true,
	"id": 0
}
```

- `fan`: `true` = 启动，`false` = 关闭

#### 3. 蜂鸣器控制

```json
{
	"alarm": true,
	"id": 0
}
```

- `alarm`: `true` = 鸣响，`false` = 静音

---

## 🎮 智能联动规则

| 场景                | 触发条件                                | 执行动作              | 优先级  |
| ------------------- | --------------------------------------- | --------------------- | ------- |
| ⚠️ **环境异常报警** | 温度 > 35°C 或<br>电压 < 3.0V 或 > 5.5V | 蜂鸣器持续报警        | 🔴 最高 |
| 🚨 **智能安防**     | 光照 < 10 lux（夜间）<br>且检测到人体   | 蜂鸣器报警<br>LED闪烁 | 🟠 高   |
| 💡 **自动照明**     | 光照 < 20 lux<br>且有人                 | 自动开灯              | 🟡 中   |
| 🌀 **智能通风**     | 温度 > 28°C 或<br>湿度 > 70%            | 启动风扇              | 🟡 中   |
| 💤 **节能模式**     | 无人超过 30 秒                          | 关闭灯光+风扇         | 🟢 低   |

---

## 🚀 快速开始

### **1. 环境准备**

```bash
# 安装必要的库（开发板上）
opkg update
opkg install libmosquitto mosquitto-clients
```

### **2. 编译项目**

```bash
cd ~/code
make clean
make
```

**预期输出：**

```
正在编译...
源文件列表:
  - src/buzzer.c
  - src/cJSON.c
  - src/fan.c
  - src/io.c
  - src/led.c
  - src/light.c
  - src/linkage.c
  - src/main.c
  - src/mqtt_client.c
  - src/tah.c
  - src/voltage.c
✅ 编译完成: build/app
```

### **3. 配置MQTT**

修改 mqtt_client.c 中的连接参数：

```c
const char *host = "mqtt.yyzlab.com.cn";               // MQTT服务器地址
const char *topic_publish = "YOUR_ID/Device2AIOTSIM";  // 上报Topic
const char *topic_subscribe = "YOUR_ID/AIOTSIM2APP";   // 订阅Topic
```

### **4. 运行程序**

```bash
# 需要root权限（访问硬件设备）
sudo ./build/app
```

**正常输出示例：**

```
========== 智能家居系统启动 ==========
正在初始化MQTT连接...
✅ MQTT初始化成功
正在订阅Topic: 1767767988559/AIOTSIM2APP
✅ 订阅成功，等待云端消息...
====================================

========== 联动功能配置 ==========
  💡 自动照明: ✅ 启用
  🌀 自动通风: ✅ 启用
  🚨 安防模式: ✅ 启用
  💤 节能模式: ✅ 启用
  🔔 异常报警: ✅ 启用
====================================

[第 1 次采集] 20:30:00
  📊 温度: 20.50°C
  💧 湿度: 65.20%
  ☀️  光照: 150.30 lux
  ⚡ 电压: 3.30 V
  📏 距离: 10.50
  👤 人体: 无人

  🤖 [联动检测中...]

  📤 [温湿度] {"tem":20.50,"hum":65.20,"id":0}
  📤 [光照] {"light":150.30,"id":0}
  📤 [人体检测] {"infrared":0,"id":0}
  ⏳ 等待3秒...
```

---

## 🧪 功能测试

### **测试1：传感器读取**

```bash
# 温度
cat /sys/bus/iio/devices/iio:device0/in_temp_input

# 湿度
cat /sys/bus/iio/devices/iio:device0/in_humidityrelative_input

# 光照
cat /sys/bus/iio/devices/iio:device1/in_illuminance_input

# 距离/人体检测
cat /sys/bus/iio/devices/iio:device1/in_proximity_raw
```

### **测试2：设备控制**

```bash
# 打开LED1
echo 1 > /sys/class/leds/led-user1/brightness

# 启动风扇
echo 200 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle

# 测试蜂鸣器
./build/app  # 然后发送云端指令 {"alarm":true,"id":0}
```

### **测试3：云端控制**

使用 `mosquitto_pub` 命令测试：

```bash
# 打开灯
mosquitto_pub -h mqtt.yyzlab.com.cn -p 1883 \
  -t "YOUR_ID/AIOTSIM2APP" \
  -m '{"lamp":true,"id":0}'

# 启动风扇（重复2）
mosquitto_pub -h mqtt.yyzlab.com.cn -p 1883 \
  -t "YOUR_ID/AIOTSIM2APP" \
  -m '{"fan":true,"id":0}'

# 触发报警
mosquitto_pub -h mqtt.yyzlab.com.cn -p 1883 \
  -t "YOUR_ID/AIOTSIM2APP" \
  -m '{"alarm":true,"id":0}'
```

---

## 🔍 核心模块说明

### **1. MQTT客户端模块 (`mqtt_client.c`)**

**功能：**

- 连接MQTT服务器
- 订阅云端控制Topic
- 发布传感器数据
- 接收并解析云端指令

**关键函数：**

```c
struct mosquitto* mqtt_init();                    // 初始化连接
int mqtt_subscribe(struct mosquitto *);           // 订阅Topic
int mqtt_publish(struct mosquitto *, int, void*); // 发布数据
void receive_message(...);                        // 消息回调
```

---

### **2. 智能联动模块 (`linkage.c`)**

**功能：**

- 实现5大智能场景
- 传感器数据与设备控制联动
- 可配置的规则引擎

**关键函数：**

```c
void linkage_init(SystemConfig *);                      // 初始化配置
void linkage_execute(SystemConfig *, SensorData *);     // 执行联动
void linkage_auto_lighting(...);                        // 自动照明
void linkage_auto_ventilation(...);                     // 智能通风
void linkage_security_alarm(...);                       // 安防报警
void linkage_energy_saving(...);                        // 节能模式
void linkage_environment_alarm(...);                    // 环境报警
```

**配置结构体：**

```c
typedef struct {
    int auto_light;        // 自动照明开关
    int auto_fan;          // 自动通风开关
    int security_mode;     // 安防模式开关
    int energy_saving;     // 节能模式开关
    int alarm_enabled;     // 报警功能开关
    time_t last_human_time; // 上次检测到人的时间
} SystemConfig;
```

---

### **3. 传感器接口层**

#### **温湿度传感器 (`tah.c`)**

```c
float temp_get();  // 获取温度（°C）
float hum_get();   // 获取湿度（%）
```

#### **光照传感器 (`light.c`)**

```c
float illumi_get();        // 环境光照（lux）
float infrared_get();      // 红外光强度
float distance_get();      // 接近度原始值
int human_detect();        // 人体检测（1=有人，0=无人）
```

#### **电压传感器 (`voltage.c`)**

```c
float voltage_get();  // 系统电压（V）
```

---

### **4. 设备控制层**

#### **LED控制 (`led.c`)**

```c
int led_set(int led_index, const char *led_state);
// led_index: 1-2
// led_state: "1"=开，"0"=关
```

#### **风扇控制 (`fan.c`)**

```c
void fan_set(char *pwm);
// pwm: "0"=关闭，"200"=启动
```

#### **蜂鸣器控制 (`buzzer.c`)**

```c
int buzzer_set(unsigned int value);
// value: 0=关闭，1000-2000=频率（Hz）
```

---

## ⚙️ 配置参数

### **联动阈值配置 (`linkage.h`)**

```c
#define TEMP_HIGH_THRESHOLD 28.0      // 高温阈值（启动风扇）
#define TEMP_DANGER_THRESHOLD 35.0    // 危险高温（报警）
#define HUM_HIGH_THRESHOLD 70.0       // 高湿度阈值
#define LIGHT_DARK_THRESHOLD 20.0     // 暗光阈值（开灯）
#define LIGHT_NIGHT_THRESHOLD 10.0    // 夜间阈值（安防模式）
#define VOLTAGE_LOW_THRESHOLD 3.0     // 低电压报警
#define VOLTAGE_HIGH_THRESHOLD 5.5    // 高电压报警
#define NO_HUMAN_TIMEOUT 30           // 无人超时时间（秒）
```

### **人体检测阈值 (`light.c`)**

```c
#define INFRARED_THRESHOLD 50.0
// 距离值 > 50.0 判定为有人
// 根据实际传感器调整
```

---

## 📈 性能指标

| 指标             | 数值    |
| ---------------- | ------- |
| **数据采集周期** | 3秒     |
| **MQTT连接延迟** | < 1秒   |
| **联动响应时间** | < 100ms |
| **内存占用**     | < 10MB  |
| **CPU占用**      | < 5%    |

---

## 🐛 常见问题

### **Q1: 编译报错 "undefined reference to mosquitto_xxx"**

**A:** 缺少libmosquitto库

```bash
opkg install libmosquitto libmosquitto-dev
```

### **Q2: 运行提示 "Permission denied"**

**A:** 需要root权限访问硬件设备

```bash
sudo ./build/app
```

### **Q3: MQTT连接失败**

**A:** 检查网络连接和服务器地址

```bash
ping mqtt.yyzlab.com.cn
mosquitto_sub -h mqtt.yyzlab.com.cn -t test
```

### **Q4: 传感器读取值异常**

**A:** 检查硬件路径是否正确

```bash
ls /sys/bus/iio/devices/
cat /sys/bus/iio/devices/iio:device0/in_temp_input
```

### **Q5: 人体检测不准确**

**A:** 调整阈值 `INFRARED_THRESHOLD`

```c
// 先读取原始值
float distance = distance_get();
printf("距离值: %.2f\n", distance);

// 根据实际情况调整阈值
#define INFRARED_THRESHOLD 50.0  // 修改这个值
```

---

## 🔮 后续扩展方向

### **功能扩展**

- [ ] 添加语音控制接口
- [ ] 增加历史数据存储（SQLite）
- [ ] Web可视化界面
- [ ] 手机APP控制
- [ ] 机器学习预测模型

### **硬件扩展**

- [ ] 添加摄像头（视频监控）
- [ ] 门窗传感器
- [ ] 烟雾报警器
- [ ] 智能门锁

### **软件优化**

- [ ] 多线程异步处理
- [ ] 断线重连机制
- [ ] 数据缓存队列
- [ ] OTA远程升级

---

## 👥 开发团队

- **开发者：** [你的名字]
- **学校/单位：** [学校名称]
- **课程：** 嵌入式系统课程设计
- **时间：** 2026年1月

---

## 📄 许可证

本项目仅用于教学和学习目的。

---

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- **邮箱：** [your.email@example.com]
- **GitHub：** [github.com/yourusername]

---

## 🙏 致谢

感谢以下开源项目：

- [Eclipse Mosquitto](https://mosquitto.org/) - MQTT消息代理
- [cJSON](https://github.com/DaveGamble/cJSON) - JSON解析库
- [Buildroot](https://buildroot.org/) - 嵌入式Linux构建系统

---

**最后更新时间：** 2026年1月7日
