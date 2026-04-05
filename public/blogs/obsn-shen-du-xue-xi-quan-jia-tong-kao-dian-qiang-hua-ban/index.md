# 🧠 深度学习全家桶 · 考点强化版

> 来源：Obsidian/10-学业与考试/期末复习资料/人工智能/🧠 深度学习全家桶 · 考点强化版.md

## 0. 🗺️ 全局总图与基础

> [!example] 核心三要素 (选择题 Q1)
> 现代人工智能发展的**三大要素**：==算力==、==算法==、==数据==。

```
深度学习全家桶
├── 模型结构：MLP / CNN / RNN / LSTM / GRU / Transformer / ResNet
├── 基础模块：卷积 / 池化 / 激活函数 / 注意力机制 / 残差结构 / 正则化
├── 损失函数：L1 / L2 / Huber / Cross-Entropy
├── 优化器：SGD / Momentum / RMSProp / Adam / AdamW
└── 训练技巧：Dropout / BN / LayerNorm / Data Augmentation
```

---

## 1. 🏗️ 深度学习基本结构

> [!example] 考点笔记
>
> - **感知机限制**：单层感知机只能解决==线性可分==问题（如无法解决 XOR 异或问题）。(选择 Q21/25)
> - **MLP 核心**：多层感知机必须引入==隐藏层==和==非线性激活函数==，否则等效于单层网络。(选择 Q23/26)

```
深度学习
├── 前馈网络（Feedforward）
│ ├── 感知机 Perceptron
│ ├── 🔥 多层感知机 MLP (引入非线性)
│ ├── 🔥 卷积神经网络 CNN (处理图像/网格数据)
│ └── 🔥 残差网络 ResNet (解决深度退化)
├── 序列模型（Sequence Models）
│ ├── RNN (适合短序列，存在梯度问题)
│ ├── 🔥 LSTM (引入门控，解决长依赖)
│ └── 🔥 GRU (LSTM简化版)
└── 自注意力模型（Attention Models）
├── Multi-Head Attention
└── 🔥 Transformer (并行计算，长距离依赖)
```

---

## 2. ⚡ 常见激活函数

> [!example] 考点笔记
>
> - **Sigmoid**：输出区间 ==(0, 1)==。缺点：易导致==梯度消失==。(选择 Q4/27/46/53)
> - **ReLU**：🔥**首选**。正区间导数为 1，有效缓解梯度消失；计算简单（仅阈值操作）。(选择 Q36/45/简答4)
> - **Softmax**：用于**多分类**输出，将输出归一化为==概率分布==，和为 1。(选择 Q7/15/16)

```
激活函数
├── Sigmoid (映射到 0~1，用于二分类输出或门控)
├── Tanh (映射到 -1~1)
├── 🔥 ReLU (解决梯度消失，计算最快)
├── Leaky ReLU (解决 Dead ReLU)
└── GELU（Transformer 中使用）
```

---

## 3. 🖼️ CNN 家族 (计算机视觉)

> [!example] 考点笔记
>
> - **核心优势**：==局部感知== (Local features) 和 ==权值共享== (Parameter sharing)，大大减少参数量。(选择 Q31/34/40)
> - **计算公式**：$Output = (Input - Kernel + 2 \times Padding) / Stride + 1$ (应用题 Q1/Q35)
> - **感受野**：堆叠小卷积核 (3x3) 可替代大卷积核，参数更少但感受野相同。(判断 Q38/简答10)

```
CNN（卷积神经网络）
├── 🔥 卷积层（Convolution）
│ ├── 卷积核 / Filter (提取局部特征：边缘/纹理)
│ ├── Padding (填充：保持尺寸)
│ ├── Stride (步长：降维)
│ └── Feature Map
├── 🔥 池化层（Pooling）
│ ├── Max Pooling (取最大值，提取显著特征)
│ ├── Average Pooling
│ └── 作用：==降维==、减少参数、==平移不变性== (简答5/判断32)
└── 经典架构
├── AlexNet (ReLU + Dropout + GPU，深度学习起点)
├── 🔥 VGG (全用 3x3 小卷积核，深层结构)
├── GoogLeNet (Inception 模块：多尺度并行卷积)
└── 🔥 ResNet (残差结构：解决深层梯度消失)
```

---

## 4. ⏳ 序列模型家族（RNN → LSTM → GRU）

> [!example] 考点笔记
>
> - **RNN 问题**：时间反向传播链太长导致==梯度消失==，难以捕捉长距离依赖。(选择 Q53/64)
> - **LSTM 核心**：引入==细胞状态== (Cell State) 和==门控机制== (Input/Forget/Output)。
> - **遗忘门**：Sigmoid 激活，决定保留多少旧信息 ($F_t \to 1$ 保留，$F_t \to 0$ 遗忘)。(简答3)
> - **GRU**：只有==更新门==和==重置门==，参数更少，训练更快。(选择 Q54/22)

```
序列模型
├── RNN（循环神经网络）
│ ├── 存在梯度消失 / 梯度爆炸问题
│ └── 适合短序列
├── 🔥 LSTM
│ ├── 解决长依赖问题
│ ├── 输入门
│ ├── 遗忘门 (关键：控制历史信息保留)
│ └── 输出门
└── 🔥 GRU
├── LSTM 的简化版
├── 更新门
└── 重置门
```

---

## 5. 🤖 自注意力与 Transformer 家族

> [!example] 考点笔记
>
> - **并行计算**：Transformer 抛弃了 RNN 的循环结构，可以==并行训练==。(选择 Q57)
> - **位置编码**：因为 Attention 无序，需引入 Positional Encoding 记录==序列顺序==。(选择 Q60/68)
> - **多头注意力**：在不同子空间并行提取特征，增强表达能力。(选择 Q56)
> - **Masked Attention**：Decoder 中使用，防止看到“未来”的信息。(选择 Q58)

```
自注意力模型
└── 🔥 Transformer
├── Encoder-Decoder 结构
├── 🔥 多头注意力（Multi-Head Attention）
├── 残差连接（Residual）
├── 层归一化（LayerNorm，平衡特征分布）
├── 前馈网络（FFN）
└── 🔥 位置编码（Positional Encoding）
```

---

## 6. 📉 损失函数 (Loss Functions)

> [!example] 考点笔记
>
> - **分类任务**：使用 ==交叉熵 (Cross Entropy)==。预测越准，交叉熵越==小==。(选择 Q5/7/18)
> - **回归任务**：使用 ==均方误差 (MSE / L2 Loss)==。(选择 Q6/填空3)

```
损失函数
├── 回归 Regression (预测数值)
│ ├── L1 损失（MAE）
│ ├── 🔥 L2 损失（MSE，最常用）
│ └── Huber Loss
└── 分类 Classification (预测类别)
├── 🔥 Cross Entropy（交叉熵，配合 Softmax）
└── NLLLoss（负对数似然）
```

---

## 7. 🚀 优化算法

> [!example] 考点笔记
>
> - **梯度下降方向**：沿着==负梯度==方向更新。(选择 Q11)
> - **学习率 (Learning Rate)**：
>   - 过大 $\to$ ==震荡/发散==。
>   - 过小 $\to$ ==收敛过慢==。(选择 Q8/9)
> - **SGD vs Batch**：SGD 每次用==1个样本==，Mini-Batch 用==一批样本==。(选择 Q12)

```
优化器
├── SGD（随机梯度下降）
│ └── Mini-Batch 版本最常用
├── Momentum（动量）
├── RMSProp
├── 🔥 Adam（结合 Momentum + RMSProp，最常用）
└── AdamW（Transformer 默认）
```

---

## 8. 🛠️ 训练技巧 (Tricks)

> [!example] 考点笔记
>
> - **过拟合 (Overfitting)**：训练误差低，测试误差高。
>   - _解决方法_：==Dropout==、==权重衰减 (L2)==、==数据增强==、==早停==。(选择 Q37/50/简答3)
> - **Dropout**：随机让神经元失活，类似集成学习，训练时开，推理时关。(选择 Q30/51)
> - **Batch Norm (BN)**：加速收敛，缓解梯度消失。(选择 Q32)
> - **数据集划分**：训练集(学参数)、==验证集==(调超参)、测试集(评测)。(填空35)

```
训练技巧
├── 🔥 Dropout（防止过拟合，随机失活）
├── 🔥 Batch Normalization（BN，加速收敛，防梯度消失）
├── Layer Normalization（Transformer 用）
├── 🔥 数据增强（Data Augmentation，提升泛化能力）
└── 早停 Early Stopping
```

---

## 9. 🏆 经典网络与术语汇总

| 模型/术语       | 核心一句话 (考点)                                               |
| :-------------- | :-------------------------------------------------------------- |
| **AlexNet**     | 引入 ReLU + Dropout，GPU 训练，深度学习爆发点。                 |
| **VGG**         | 堆叠 $3 \times 3$ 小卷积核，结构规整深邃。                      |
| **ResNet**      | **残差连接 (Shortcut)**，$H(x) = F(x) + x$，解决深度梯度退化。  |
| **Inception**   | 多尺度卷积并行，增加网络宽度。                                  |
| **LSTM**        | 门控机制 + 细胞状态，解决 RNN 梯度消失。                        |
| **Transformer** | **Attention is all you need**，并行计算，长距离依赖，LLM 基石。 |
| **One-hot**     | 分类标签的常用编码方式。                                        |

---

### 💡 复习建议 (基于题库)

1. **公式必背**：
   - 卷积输出尺寸计算（应用题常考）。
   - 交叉熵 Loss 计算（应用题 Q6）。

2. **对比必会**：
   - Sigmoid vs ReLU (为什么选 ReLU?)。
   - LSTM vs GRU (GRU 少个门，快)。
   - VGG vs ResNet (ResNet 解决了什么?)。

3. **概念必清**：
   - 过拟合的表现和解决方法。
   - 梯度消失的原因和解决方法。
