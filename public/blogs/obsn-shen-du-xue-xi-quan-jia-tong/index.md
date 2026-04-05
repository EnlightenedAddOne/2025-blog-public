> 来源：Obsidian/10-学业与考试/期末复习资料/人工智能/深度学习全家桶.md

# 🧠 深度学习全家桶 · 知识图谱

## 0. 全局总图（可以放在笔记首页）

```
深度学习全家桶
├── 模型结构：MLP / CNN / RNN / LSTM / GRU / Transformer / ResNet
├── 基础模块：卷积 / 池化 / 激活函数 / 注意力机制 / 残差结构 / 正则化
├── 损失函数：L1 / L2 / Huber / Cross-Entropy
├── 优化器：SGD / Momentum / RMSProp / Adam / AdamW
└── 训练技巧：Dropout / BN / LayerNorm / Data Augmentation
```

---

## 1. 深度学习基本结构

```
深度学习
├── 前馈网络（Feedforward）
│   ├── 感知机 Perceptron
│   ├── 多层感知机 MLP
│   ├── 卷积神经网络 CNN
│   └── 残差网络 ResNet
├── 序列模型（Sequence Models）
│   ├── RNN
│   ├── LSTM
│   └── GRU
└── 自注意力模型（Attention Models）
    ├── Multi-Head Attention
    └── Transformer
```

---

## 2. 常见激活函数

```
激活函数
├── Sigmoid
├── Tanh
├── ReLU
├── Leaky ReLU
└── GELU（Transformer 中使用）
```

---

## 3. CNN 家族

```
CNN（卷积神经网络）
├── 卷积层（Convolution）
│   ├── 卷积核 / Filter
│   ├── Padding
│   ├── Stride
│   └── Feature Map
├── 池化层（Pooling）
│   ├── Max Pooling
│   ├── Average Pooling
│   └── Global Pooling
└── 经典架构
    ├── LeNet
    ├── AlexNet
    ├── VGG
    ├── GoogLeNet（Inception）
    └── ResNet（残差结构）
```

---

## 4. 序列模型家族（RNN → LSTM → GRU）

```
序列模型
├── RNN（循环神经网络）
│   ├── 存在梯度消失 / 梯度爆炸问题
│   └── 适合短序列
├── LSTM
│   ├── 解决长依赖问题
│   ├── 输入门
│   ├── 遗忘门
│   └── 输出门
└── GRU
    ├── LSTM 的简化版
    ├── 更新门
    └── 重置门
```

---

## 5. 自注意力与 Transformer 家族

```
自注意力模型
└── Transformer
    ├── Encoder-Decoder 结构
    ├── 多头注意力（Multi-Head Attention）
    ├── 残差连接（Residual）
    ├── 层归一化（LayerNorm）
    ├── 前馈网络（FFN）
    └── 位置编码（Positional Encoding）
```

---

## 6. 损失函数（分类 vs 回归）

```
损失函数
├── 回归 Regression
│   ├── L1 损失（MAE）
│   ├── L2 损失（MSE）
│   └── Huber Loss
└── 分类 Classification
    ├── Cross Entropy（交叉熵）
    └── NLLLoss（负对数似然）
```

---

## 7. 优化算法

```
优化器
├── SGD（随机梯度下降）
│   └── Mini-Batch 版本最常用
├── Momentum（动量）
├── RMSProp
├── Adam（最常用）
└── AdamW（Transformer 默认）
```

---

## 8. 训练技巧

```
训练技巧
├── Dropout（防止过拟合）
├── Batch Normalization（BN）
├── Layer Normalization（Transformer 用）
├── 数据增强（Data Augmentation）
└── 早停 Early Stopping
```

---

## 9. 经典网络与术语汇总

```
经典模型与概念
├── AlexNet —— 让深度学习重新起飞（ReLU + Dropout）
├── VGG —— 深但结构简单
├── ResNet —— 引入残差结构，解决深度退化
├── LSTM/GRU —— 序列数据
└── Transformer —— 当前主流的 NLP / 多模态模型基础
```

---
