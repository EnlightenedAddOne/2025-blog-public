# 🧠 深度学习全家桶 · 详解版

> 来源：Obsidian/10-学业与考试/期末复习资料/人工智能/🧠 深度学习全家桶 · 详解版.md

> [!abstract] 笔记说明
> 本文档基于《深度学习全家桶》知识图谱进行扩展，对核心概念、数学原理及应用场景进行了名词解释。
> **适用场景**：面试复习、概念速查、知识体系构建。

---

## 1. 🏗️ 深度学习基本结构

### 前馈网络 (Feedforward)

- **感知机 (Perceptron)**: 最简单的神经网络单元，模拟神经元，由输入、权重、偏置和激活函数组成。只能解决线性可分问题。
- **多层感知机 (MLP)**: 也称为全连接网络 (Dense Network)。通过堆叠多个感知机（隐藏层）并引入非线性激活函数，理论上可以拟合任何函数（万能近似定理）。
- **卷积神经网络 (CNN)**: 专门处理网格结构数据（如图像）。通过**局部感知**和**权值共享**大大减少了参数量。
- **残差网络 (ResNet)**: 解决了深层网络难以训练（梯度消失/退化）的问题。核心是引入**跳跃连接 (Skip Connection)**，学习 $H(x) = F(x) + x$。

### 序列模型 (Sequence Models)

- **RNN (循环神经网络)**: 具有记忆功能，隐藏层的输出会作为下一时刻的输入。
- **LSTM (长短期记忆网络)**: RNN 的升级版，通过“门控机制”解决长序列训练中的梯度消失问题。
- **GRU (门控循环单元)**: LSTM 的简化版，参数更少，训练速度通常更快，效果相近。

### 自注意力模型 (Attention Models)

- **Transformer**: 抛弃了循环结构，完全基于 Attention 机制。具有并行计算能力强、捕捉长距离依赖能力强的特点。是目前 LLM (大语言模型) 的基石。

---

## 2. ⚡ 常见激活函数

> [!tip] 核心作用
>
> 引入非线性因素，使神经网络能够拟合复杂的非线性函数。如果没有激活函数，多少层网络都等价于一层线性变换。

- **Sigmoid**: $\sigma(x) = \frac{1}{1+e^{-x}}$。将输出压缩到 (0, 1)。
  - _缺点_：易导致梯度消失；输出不是以 0 为中心；计算 exp 耗时。

- **Tanh**: 双曲正切。将输出压缩到 (-1, 1)。
  - _优点_：以 0 为中心，收敛比 Sigmoid 快。
  - _缺点_：依然存在梯度消失问题。

- **ReLU (修正线性单元)**: $max(0, x)$。目前最常用的激活函数。
  - _优点_：计算简单；正区间不饱和（解决梯度消失）。
  - _缺点_：Dead ReLU 问题（负区间梯度为 0，神经元可能“死亡”）。

- **Leaky ReLU**: 在负区间给一个很小的斜率（如 0.01），解决 Dead ReLU 问题。

- **GELU (高斯误差线性单元)**: 结合了 ReLU、Dropout 和 Zoneout 的思想。在 Transformer (BERT, GPT) 中被广泛使用。它是平滑的，且允许小的负值。

---

## 3. 🖼️ CNN 家族详解

![CNN architecture layers的图片](https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcT4_3eT_CK5L2YbBw-GWXqpAyNBlBbJmT2TnrFOpmDOwTBU5TWrYg7L-VCwNUhM5aRVudaIHvHVyTNNrfKkAFbrx4Gi1bSSUGIF_prl8Ko4LJbFWIM)

### 核心组件

- **卷积层 (Convolution)**: 提取特征。
  - **Kernel/Filter (卷积核)**: 提取特征的窗口（如边缘检测、纹理检测）。
  - **Padding (填充)**: 在图像边缘补 0，保持输出特征图的大小不变。
  - **Stride (步长)**: 卷积核滑动的步距。Stride > 1 会导致特征图尺寸减小（降采样）
  - **Feature Map (特征图)**: 卷积操作后的输出结果。

- **池化层 (Pooling)**: 降采样，减少参数，保持特征不变性（平移、旋转）。
  - **Max Pooling**: 取窗口内最大值（提取最显著特征，如纹理）。
  - **Average Pooling**: 取窗口内平均值（保留背景信息）。

### 经典架构演进

1. **LeNet**: CNN 的鼻祖，用于手写数字识别。
2. **AlexNet**: 深度学习爆发的起点。引入 ReLU、Dropout，使用 GPU 训练。
3. **VGG**: 探索了“深度”的重要性。使用连续的 $3\times3$ 小卷积核代替大卷积核。
4. **Inception (GoogLeNet)**: 增加网络的“宽度”。引入 Inception 模块，并行使用不同尺寸的卷积核。
5. **ResNet**: 引入残差结构，让网络可以做得非常深（152层甚至1000层）。

---

## 4. ⏳ 序列模型家族 (RNN → LSTM → GRU)

### RNN 的痛点

- **梯度消失/爆炸**: 在反向传播时，梯度连乘导致长距离的时间步无法获得有效的梯度更新。只能“记住”最近的信息。

### LSTM (Long Short-Term Memory)

通过 3 个门来控制信息流：

1. **遗忘门 (Forget Gate)**: 决定丢弃上一个时刻细胞状态 ($C_{t-1}$) 中的哪些信息。
2. **输入门 (Input Gate)**: 决定当前输入 ($X_t$) 中有哪些信息需要存入细胞状态。
3. **输出门 (Output Gate)**: 决定基于当前状态，输出什么信息给隐藏层 ($h_t$)。

### GRU (Gated Recurrent Unit)

- 将 LSTM 的遗忘门和输入门合并为 **更新门 (Update Gate)**。
- 新增 **重置门 (Reset Gate)**。
- _总结_：GRU 是 LSTM 的高效变体，在小数据集上表现往往更好。

---

## 5. 🤖 Transformer 家族

![Transformer architecture diagram的图片](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcT9DhpD8wtyjJ8RwgOLhgMkTCzQMNIz9so7tauaFUvHFdRpOMOqLXFBnFRpelcz7s2Ypo3TC0Gdfmch-Kw9JT9n_W2YT1_KE_mAAQXRcoMUBxekuKI)

> [!NOTE] 核心公式：Scaled Dot-Product Attention
>
> $$ Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V $$
>
> Q: Query (查询), K: Key (键), V: Value (值)

- **Encoder-Decoder**: 原始 Transformer 的架构。
  - _Encoder_: 负责理解输入（如机器翻译中的源语言）。
  - _Decoder_: 负责生成输出（如目标语言）。

- **多头注意力 (Multi-Head Attention)**: 让模型关注不同位置的子空间信息（比如一个头关注语法，一个头关注语义）。
- **位置编码 (Positional Encoding)**: 因为 Attention 是并行计算的，本身不包含序列顺序信息，必须手动注入位置信号（正弦/余弦函数或可学习向量）。
- **LayerNorm**: 对每一个样本的特征向量进行归一化，独立于 Batch Size，更适合 NLP 任务。

---

## 6. 📉 损失函数 (Loss Functions)

### 回归 (Regression) - 预测数值

- **L1 Loss (MAE)**: $|y - \hat{y}|$。对异常值不敏感（鲁棒性强），但在 0 处不可导。
- **L2 Loss (MSE)**: $(y - \hat{y})^2$。对异常值敏感（平方放大了误差），收敛更平滑。
- **Huber Loss**: 结合了 L1 和 L2。误差小时用 L2（平滑收敛），误差大时用 L1（抗干扰）。

### 分类 (Classification) - 预测类别

- **Cross Entropy (交叉熵)**: 衡量两个概率分布之间的距离。
  - 公式：$Loss = -\sum y \cdot \log(\hat{y})$。
  - 通常配合 Softmax 使用。

- **NLLLoss**: 负对数似然损失。实际上 PyTorch 中 `CrossEntropyLoss = LogSoftmax + NLLLoss`。

---

## 7. 🚀 优化算法 (Optimizers)

- **SGD (随机梯度下降)**: 每次只用一个样本更新。震荡大，收敛慢。
  - **Mini-Batch SGD**: 每次用一批样本（Batch）。最常用，兼顾速度和稳定性。
- **Momentum (动量)**: 模拟物理动量，积累之前的梯度方向。冲过局部极小值，加速收敛。
- **RMSProp**: 自适应学习率。对频繁更新的参数给小学习率，不频繁的给大学习率。
- **Adam (Adaptive Moment Estimation)**: **Momentum + RMSProp** 的结合体。目前的默认首选优化器。
- **AdamW**: Adam + Weight Decay Decoupling。修复了 Adam 在权重衰减上的实现错误，是训练 Transformer/BERT 的标准配置。

---

## 8. 🛠️ 训练技巧 (Tricks)

- **Dropout**: 训练时随机让一部分神经元“失活”（输出为 0）。相当于训练了多个子网络的集成，有效防止**过拟合**。
- **Batch Normalization (BN)**: 对一个 Batch 的数据进行标准化（均值为 0，方差为 1）。
  - _作用_：加速收敛，允许更大的学习率，防止梯度消失。
  - _场景_：主要用于 CNN / 图像任务。
- **Layer Normalization (LN)**: 对单个样本的所有特征进行归一化。
  - _场景_：主要用于 RNN / Transformer / NLP 任务（因为 NLP 输入长度不一，BN 效果不好）。
- **Data Augmentation (数据增强)**: 翻转、旋转、裁剪、调色。增加数据多样性，提高模型泛化能力。
- **Early Stopping (早停)**: 当验证集 Loss 不再下降时，提前停止训练，防止过拟合。

---

## 9. 🏆 经典网络一句话总结

| **模型**        | **核心贡献 / 特点**                                                           | **适用领域**      |
| --------------- | ----------------------------------------------------------------------------- | ----------------- |
| **AlexNet**     | GPU训练 + ReLU + Dropout，深度学习元年                                        | 图像分类          |
| **VGG**         | 结构整洁，全部使用 $3\times3$ 卷积，深层网络                                  | 特征提取 Backbone |
| **ResNet**      | **残差连接**，解决了深层网络的梯度退化，甚至可达千层                          | CV 通用 Backbone  |
| **LSTM**        | 门控机制，解决了 RNN 长距离依赖问题                                           | 序列/时间序列     |
| **Transformer** | **Attention Is All You Need**，并行计算，不仅是 NLP 霸主，也正在攻占 CV (ViT) | NLP, CV, 多模态   |
