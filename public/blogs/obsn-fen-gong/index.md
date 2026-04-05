# 分工

> 来源：Obsidian/30-项目与实践/项目说明/嵌入式-智能家居/分工.md

### 🟢 第一部分：硬件感知 (传感器读取)

涉及文件： tah.c, light.c, io.c

代码核心逻辑讲解：

1. **Linux IIO 子系统 (Industrial I/O)：**
   - **原理：** 你的代码（如 `tah.c` 和 `voltage.c`）并没有直接操作寄存器，而是利用了 Linux 的 IIO 子系统。系统将传感器映射为文件系统中的节点（例如 `/sys/bus/iio/devices/iio:device0/in_temp_raw`）。

   - 标准计算公式：

     在 temp_get() 和 voltage_get() 中，你都用到了这个公式：

     C

     ```
     value = (raw + offset) * scale / 1000;
     ```

     - `raw`: 传感器读到的原始数值。

     - `offset`: 偏移量（校准用）。

     - `scale`: 缩放比例（转换用）。

     - `/1000`: 通常 Linux 内核返回的单位是毫（如毫摄氏度、毫伏），除以 1000 转换为标准单位。

2. **通用文件读取 (`io.c` -> `read_data`)：**
   - 使用了标准 C 库的 `fopen("r")` 和 `fscanf`。

   - **面试/答辩应对：** 如果老师问“为什么不直接读数字？”，回答：“为了提高代码复用性，我封装了 `read_data` 函数，只要传入设备路径就能读出浮点数，这符合 Linux ‘一切皆文件’ 的设计思想。”

---

### 🔵 第二部分：硬件控制 (执行器)

涉及文件： led.c, fan.c, buzzer.c, io.c

代码核心逻辑讲解：

1. **Sysfs 控制 (LED 和 风扇)：**
   - **原理：** `led.c` 和 `fan.c` 通过向文件写入字符串来控制硬件。

   - **关键点：** `write_data` 函数使用了 `fopen("w")` 和 `fprintf`。

   - **风扇调速：** 在 `fan.c` 中，你写入的是 PWM (脉冲宽度调制) 的值（如 "200"），这个值决定了风扇的转速（占空比）。

2. **Input 子系统 (蜂鸣器 `buzzer.c`)：**
   - **原理：** 蜂鸣器不像 LED 那样简单写 1/0，它使用了 Linux 的 **Input Subsystem**。

   - **核心结构体：**

     C

     ```
     struct input_event event;
     event.type = EV_SND;    // 表示声音事件
     event.code = SND_TONE;  // 表示产生音调
     event.value = value;    // 频率值 (Hz)
     ```

   - **区别：** 这里用的是 `fwrite` 写入二进制结构体，而不是 `fprintf` 写入字符串。这是答辩时的一个技术亮点。

---

### 🟠 第三部分：智能算法 (联动逻辑)

涉及文件： linkage.c, linkage.h

代码核心逻辑讲解：

1. **阈值管理 (`linkage.h`)：**
   - 所有的判断标准（如 `TEMP_HIGH_THRESHOLD` 23.0度）都定义在头文件中。这样修改参数不需要重新编译整个逻辑代码，体现了**配置与代码分离**的思想。

2. **状态保持与去抖动：**
   - 在 `linkage.c` 的函数中（如 `linkage_auto_lighting`），你使用了 `static int light_status`。

   - **作用：** 记录上一次的状态（开还是关）。只有当“需要开灯”且“当前是关灯状态”时，才发送指令。避免了在循环中重复发送控制指令，浪费系统资源。

3. **超时机制 (`linkage_energy_saving`)：**
   - 使用了 `<time.h>` 库。

   - 逻辑：`current_time - last_human_time >= 30`。通过记录最后一次检测到人的时间戳，与当前时间做差，实现“人走灯灭”的延时功能。

---

### 🟣 第四部分：网络通信 (MQTT & JSON)

涉及文件： mqtt_client.c, cJSON.c

代码核心逻辑讲解：

1. **MQTT 协议流程 (`mqtt_client.c`)：**
   - **初始化：** `mosquitto_new` 创建实例 -> `mosquitto_connect` 连接服务器。

   - **订阅：** `mosquitto_subscribe` 监听云端发来的指令。

   - **回调函数 (重中之重)：** `receive_message` 函数。
     - 当云端下发控制指令时，这个函数会被自动调用。

     - **逻辑：** 收到 payload -> 调用 `cJSON_Parse` 解析 -> 根据解析结果控制 LED/风扇。

2. **JSON 序列化与反序列化：**
   - **发送数据 (`home.c`)：** 使用 `cJSON_CreateObject` 创建对象，`cJSON_AddNumberToObject` 添加数据，最后 `cJSON_Print` 转成字符串发送。

   - **接收指令 (`mqtt_client.c`)：** 使用 `cJSON_GetObjectItem(msg, "lamp")` 查找特定字段，判断是开还是关。

---

### 🔴 第五部分：系统构建与集成 (主控)

涉及文件： home.c, Makefile, tasks.json

代码核心逻辑讲解：

1. **工程构建 (`Makefile`)：**
   - **自动化编译：** 定义了 `SRCS` (源文件) 和 `INCS` (头文件)，使用了 `wildcard` 自动寻找 `src` 目录下所有的 `.c` 文件。

   - **链接库：** `-lmosquitto -lpthread -lm -lgpiod`。
     - 老师如果问：“为什么要加 `-lm`？”，回答：“因为使用了 `cJSON` 库或数学计算，涉及数学函数库。”

     - `-lpthread`：MQTT 库在后台使用了多线程进行消息监听。

2. **主循环模型 (`home.c`)：**
   - **结构：** 这是一个典型的 **无限循环 (While Loop)** 结构。

   - **流程：**
     1. **采集** (调用 `temp_get` 等)。

     2. **联动** (调用 `linkage_execute` 进行本地判断)。

     3. **上报** (调用 `mqtt_publish` 发送数据给云端)。

     4. **休眠** (`sleep(3)` 或 `usleep`)，防止 CPU 占用率 100%。

3. **开发工具配置 (`tasks.json` / `sftp.json`)：**
   - 这部分不是 C 代码，而是 VSCode 的配置。

   - `sftp.json`：保存时自动把代码上传到开发板。

   - `tasks.json`：配置了 SSH 远程执行 `make` 命令，让你点一下就能在板子上编译运行。

---

### ⚠️ 答辩常见追问 (预测 & 速答)

1. **问：你的温湿度数据如果不准怎么校准？**
   - **答：** 在读取逻辑中（`tah.c`），使用了 `offset`（偏移量）和 `scale`（缩放）文件。我可以通过修改系统底层的 `offset` 文件来进行硬件校准，或者在代码中对 `value` 进行软件加减补偿。

2. **问：如果网络断了，你的系统还能工作吗？**
   - **答：** 可以。我的“智能联动”逻辑（`linkage.c`）是在本地运行的，不依赖网络。即使断网，自动开关灯、高温报警等功能依然有效，只是手机端看不到数据了。

3. **问：为什么蜂鸣器要用 `fwrite` 而不是 `fprintf`？**
   - **答：** 因为蜂鸣器使用的是 Linux 的 Input 子系统，它需要接收一个标准的 `struct input_event` 二进制结构体数据，包含时间、类型、代码和值。这比简单的字符流控制更底层、更精确。

4. **问：MQTT 相比 HTTP 有什么优势？**
   - **答：** MQTT 是长连接，轻量级，开销小，非常适合嵌入式设备。而且它支持“发布/订阅”模式，设备不需要一直轮询服务器，服务器有指令可以直接推送到设备（通过回调函数），实时性更好。
