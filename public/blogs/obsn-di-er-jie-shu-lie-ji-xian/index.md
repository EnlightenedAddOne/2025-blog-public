> 来源：Obsidian/10-学业与考试/考研/高数/第二节数列极限.md

# 数列极限02

## 子数列

从数列 $\{a_n\}$: $a_1$, $a_2$, ..., $a_n$, ... 中选取 `无穷多项` ，并按原来的先后顺序组成新的数列，称新数列为原数列的子列，记为
$$\{a_{n_k}\}: a_{n_1}, a_{n_2}, ..., a_{n_k}, ...$$
其中下标 $n_1$, $n_2$, ..., $n_k$, ... 为正整数。

## 数列求和

### 等差数列

首项为 $a_1$，公差为 $d (d \neq 0)$ 的数列 $a_1, a_1 + d, a_1 + 2d, \dots, a_1 + (n-1)d, \dots$。

① 通项公式 $a_n = a_1 + (n-1)d$。

② 前 $n$ 项的和 $S_n = \frac{n}{2} [2a_1 + (n-1)d] = \frac{n}{2} (a_1 + a_n)$。

### 等比数列

首项为 $a_1$，公比为 $r (r \neq 0)$ 的数列 $a_1, a_1 r, a_1 r^2, \dots, a_1 r^{n-1}, \dots$。

① 通项公式 $a_n = a_1 r^{n-1}$。

② 前 $n$ 项的和 $S_n = \begin{cases} na_1, & r = 1, \\ \frac{a_1(1-r^n)}{1-r}, & r \neq 1. \end{cases}$

③ 常用 $1 + r + r^2 + \dots + r^{n-1} = \frac{1-r^n}{1-r} (r \neq 1)$。

当 $n \to \infty$ 前 $n$ 项的公式：[[第一节函数与极限#无穷等比级数求和公式​​]]

### 一些常见数列前 n 项的和公式

① $\sum_{k=1}^{n} k = 1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$.

② $\sum_{k=1}^{n} k^2 = 1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}$.

③ $\sum_{k=1}^{n} \frac{1}{k(k+1)} = \frac{1}{1 \times 2} + \frac{1}{2 \times 3} + \frac{1}{3 \times 4} + \cdots + \frac{1}{n(n+1)} = \boxed{\frac{n}{n+1}}$.

怎么算出来的？裂项相消

$\begin{aligned}&= 1 - \frac{1}{2} + \frac{1}{2} - \frac{1}{3} + \frac{1}{3} - \frac{1}{4} + \cdots + \frac{1}{n} - \frac{1}{n+1} \\&= 1 - \frac{1}{n+1}\end{aligned}$

## 例题&结论

### 例题

**证明：若 $\lim_{n \to \infty} a_n = A$，则 $\lim_{n \to \infty} |a_n| = |A|$。**

证明：

$\forall \varepsilon > 0, \exists N > 0, n > N \Rightarrow |a_n - A| < \varepsilon.$
$\because |(|a| - |b|)| \leq |a - b|$
$\therefore ||a_n| - |A|| \leq |a_n - A|$
$\Rightarrow \forall \varepsilon > 0, \exists N > 0, n > N \Rightarrow ||a_n| - |A|| < \varepsilon.$
得 $\lim_{n \to \infty} |a_n| = |A|$

### **结论**

#### (1) 反例说明

此命题反过来不对，如取 $a_n = (-1)^n$，则 $\lim_{n \to \infty} |(-1)^n| = 1$．但 $\lim_{n \to \infty} (-1)^n$ 不存在。

#### **_(2) 特殊情况分析_**

在本题中若 $A = 0$，则 $||a_n| - |A|| = ||a_n| - 0| = |a_n - 0| = |a_n|$，即有

$\lim_{n \to \infty} a_n = 0 \Leftrightarrow \lim_{n \to \infty} |a_n| = 0,$

这结论常用，即若要证 $\lim_{n \to \infty} a_n = 0$，可转化为证 $\lim_{n \to \infty} |a_n| = 0$，由于 $|a_n| \geq 0$，若使用夹逼准则，便省了一半的力气，只需证 $|a_n| \leq 0$ 即可。

#### (3) 函数极限推广

此结论对函数亦成立，即若 $\lim_{x \to x_0} f(x) = A$，则 $\lim_{x \to x_0} |f(x)| = |A|$。

## 收敛数列的性质

### 有界性

若数列 $\{a_n\}$ 收敛，则其任何子列 $\{a_{n_k}\}$ 也收敛，且 $\lim_{k \to \infty} a_{n_k} = \lim_{n \to \infty} a_n$。

推论: $\lim_{n \to \infty} a_n = a \Leftrightarrow \lim_{k \to \infty} a_{2k} = a$ 且 $\lim_{k \to \infty} a_{2k-1} = a$。

**此定理为我们提供了一个判断数列发散的方法：**

1. 对于一个数列 $\{a_n\}$，如果能找到一个发散的子列，则原数列一定发散；
2. 如果能找到至少两个收敛的子列 $\{a_{n_k}\}$ 和 $\{a_{n'_k}\}$，但它们收敛到不同极限，则原数列也一定发散。

如 $\{n^{(-1)^n}\}$。

再例如，对于数列 $\{(-1)^n\}$：-1, 1, -1, 1, …, $(-1)^n$, …，我们找到其收敛的子列：

$\{(-1)^{2k}\}$：1, 1, …, 1, …；$\{(-1)^{2k-1}\}$：-1, -1, …, -1, …，

它们的极限分别为 1 和 -1，所以原数列发散。

### 唯一性

给出数列 $\{x_n\}$，若 $\lim_{n \to \infty} x_n = a$（存在），则 $a$ 是唯一的。

### 保号性

设 $\lim_{n \to \infty} x_n = a > b$，则存在 $N > 0$，当 $n > N$ 时，有 $x_n > b$。

若数列 $\{x_n\}$ 从某项起有 $x_n \geq b$，且 $\lim_{n \to \infty} x_n = a$，则 $a \geq b$，其中 $b$ 为任意实数。常考 $b=0$ 的情形。

## 海涅定理（归结原则）

设 $f(x)$ 在 $\dot{U}(x_0, \delta)$ 内有定义，则 $\lim_{x \to x_0} f(x) = A$ 存在 $\Leftrightarrow$ 对任何 $\dot{U}(x_0, \delta)$ 内以 $x_0$ 为极限的数列 $\{x_n\}$ ($x_n \neq x_0$)，极限 $\lim_{n \to \infty} f(x_n) = A$ 存在。

即：求 $n \to \infty$ 数列 $a_n$ 的极限时可以转换为求 $x \to \infty$ 函数 $f(x)$ 的极限。

![Pasted image 20250718180321](/blogs/obsn-di-er-jie-shu-lie-ji-xian/Pasted image 20250718180321.png)

## 极限的保号性

### 脱帽法

若 $\lim_{x \to a} f(x) > 0$，则 $f(x) > 0$

极限 > 0，则函数 > 0，是严格不等。

因此，极限若存在则函数一定存在，并强烈地推导过来。

### 戴帽法

若 $f(x) \geq 0$ 在某个区间内存在时，则 $\lim_{x \to a} f(x) \geq 0$

戴帽法有一个前提就是该点极限存在（因为是从函数值推断极限值的符号，如果这个极限不存在给它带一个帽子也没用）

# 数列极限03

## 夹逼准则（不等思想）

如果数列 $\{x_n\}$, $\{y_n\}$ 及 $\{z_n\}$ 满足下列条件：

① 从某项起，即存在 $n_0 \in \mathbb{N}_+$，当 $n > n_0$ 时，

$$ y_n \leq x_n \leq z_n \quad (n = 1, 2, \ldots) $$

② $\lim_{n \to \infty} y_n = a$, $\lim_{n \to \infty} z_n = a$.

则 $\{x_n\}$ 的极限存在，且 $\lim_{n \to \infty} x_n = a$.

## 放缩的常用方法

### (1) 利用简单的放大与缩小

$$
\begin{cases}
n \cdot u_{\min} \leq u_1 + u_2 + \cdots + u_n \leq n \cdot u_{\max}, \\
当 u_i \geq 0 时, 1 \cdot u_{\max} \leq u_1 + u_2 + \cdots + u_n \leq n \cdot u_{\max}.
\end{cases}
$$

例题：[[#例2.10：]]

### (2) 利用重要不等式

#### ① 绝对值不等式

设 $a, b$ 为实数，则

- $|a \pm b| \leq |a| + |b|$;
- $||a| - |b|| \leq |a - b|$.

可以将上述不等式 a. 推广为 $n$ 个实数的情形，即

$$
 |a_1 \pm a_2 \pm \cdots \pm a_n| \leq |a_1| + |a_2| + \cdots + |a_n|.
$$

#### ② 不等式链

$\sqrt{ab} \leq \frac{a+b}{2} \leq \sqrt{\frac{a^2 + b^2}{2}}$ ($a, b \geq 0$);

还有 $|ab| \leq \frac{a^2 + b^2}{2}$，例如，若 $u_n > 0$，则 $\frac{u_n}{n} = u_n \cdot \frac{1}{n} \leq \frac{u_n^2 + \frac{1}{n^2}}{2}$.

$\sqrt[3]{abc} \leq \frac{a+b+c}{3} \leq \sqrt{\frac{a^2 + b^2 + c^2}{3}}$ ($a, b, c \geq 0$).

#### ③ 幂函数的单调性

设 $a \geq b \geq 0$，则：

$$
\begin{cases}
当 m > 0 时, a^m \geq b^m, \\
当 m < 0 时, a^m \leq b^m.
\end{cases}
$$

#### ④ 分数不等式

若 $0 < a < x < b$，$0 < c < y < d$，则

$$
\frac{c}{b} < \frac{y}{x} < \frac{d}{a}.
$$

考研中考过：三角函数与 $S(x)$ 的关系

当 $n\pi < x < (n+1)\pi$，$2n < S(x) < 2(n+1)$ 时，

$$
\frac{2n}{(n+1)\pi} < \frac{S(x)}{x} < \frac{2(n+1)}{n\pi}.
$$

#### ⑤ 正弦与正切函数的比较

$$
\sin x < x < \tan x \quad (0 < x < \frac{\pi}{2}).
$$

#### ⑥ 正弦函数的性质

$$
\sin x < x \quad (x > 0).
$$

考研中考过：当 $x_n > 0$ 时，$x_{n+1} = \sin x_n < x_n$，故 $\{x_n\}$ 单调减少。

#### ⑦ 正切函数的上界

当 $0 < x < \frac{\pi}{4}$ 时，

$$
x < \tan x < \frac{4}{\pi} x.
$$

#### ⑧ 正弦函数的下界

当 $0 < x < \frac{\pi}{2}$ 时，

$$
\sin x > \frac{2}{\pi} x.
$$

#### ⑨ 反三角函数的比较

$$
\arctan x \leq x \leq \arcsin x \quad (0 \leq x \leq 1).
$$

可考：当 $x_n > 0$ 时，$x_{n+1} = \arctan x_n < x_n$，故 $\{x_n\}$ 单调减少。

#### ⑩ 指数函数的下界

$$
e^x \geq x + 1 \quad (\forall x).
$$

可考：当 $x_{n+1} = e^{x_n} - 1$ 时，由 $e^{x_n} - 1 \geq x_n$，得 $x_{n+1} \geq x_n$，即 $\{x_n\}$ 单调不减。

#### ⑪ 对数函数的上界

$$
x - 1 \geq \ln x \quad (x > 0).
$$

可考：当 $x_n > 0$ 时，若 $x_{n+1} = \ln x_n + 1$，由 $\ln x_n + 1 \leq x_n$，得 $x_{n+1} \leq x_n$，即 $\{x_n\}$ 单调不增。

#### ⑫ 对数函数的夹逼定理

$$
\frac{1}{1+x} < \ln(1+\frac{1}{x}) < \frac{1}{x} \quad (x > 0)
$$

或

$$
\frac{x}{1+x} < \ln(1+x) < x \quad (x > 0).
$$

其它不等式：[[第一节函数与极限#不等式]]

### 压缩映射原理.

#### 原理一

对数列 $\{x_n\}$，若存在常数 $k$（$0 < k < 1$），使得 $|x_{n+1} - a| \leq k|x_n - a|$，$n = 1, 2, \cdots$，则 $\{x_n\}$ 收敛于 $a$。

**证明**

$$
0 \leq |x_{n+1} - a| \leq k|x_n - a| \leq k^2|x_{n-1} - a| \leq \cdots \leq k^n|x_1 - a|,
$$

由于 $\lim_{n \to \infty} k^n = 0$，根据夹逼准则，有 $\lim_{n \to \infty} |x_{n+1} - a| = 0$，即 $\{x_n\}$ 收敛于 $a$。

例题：[[#例 2.8 (简化版压缩映射定理)]]

#### 原理二

对数列 $\{x_n\}$，若 $x_{n+1} = f(x_n)$，$n = 1, 2, \cdots$，$f(x)$ 可导，$a$ 是 $f(x) = x$ 的唯一解，且 $\forall x \in \mathbb{R}$，有 $|f'(x)| \leq k < 1$，则 $\{x_n\}$ 收敛于 $a$。

**证明**

$$
|x_{n+1} - a| = |f(x_n) - f(a)| \overset{\text{拉格朗日中值定理}}{=} |f'(\xi)||x_n - a| \leq k|x_n - a|
$$

其中 $\xi$ 介于 $a$ 与 $x_n$ 之间，由原理一，有 $\{x_n\}$ 收敛于 $a$。

例题：[[#例 2.8 (拉格朗-压缩映射定理)]]

## 例题

### 例2.10 (利用简单的放大与缩小)

求极限 $\lim_{n \to \infty} \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n}$，其中 $a_i (i=1, 2, \cdots, m)$ 都是非负数。

_解析_

$$
\sqrt[n]{1 \cdot a^n} \leq \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n} \leq \sqrt[n]{n \cdot a^n}
$$

其中，$a = \max \{a_1, a_2, \cdots, a_m\}$

$$
\begin{aligned}
& \Rightarrow a \leq \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n} \leq n^{\frac{1}{n}} \cdot a
\end{aligned}
$$

由于 $\lim_{n \to \infty} n^{\frac{1}{n}} = e^{\lim_{n \to \infty} \frac{1}{n} \ln n} = e^0 = 1$

$$
\begin{aligned}\Rightarrow a \leq \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n} \leq a \\\end{aligned}
$$

因此，

$$
\lim_{n \to \infty} \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n} = a
$$

### 例 2.11

设 $0 < a_n < \frac{\pi}{2}$，$0 < b_n < \frac{\pi}{2}$，$\cos a_n - a_n = \cos b_n$，且 $\lim_{n \to \infty} b_n = 0$，求 $\lim_{n \to \infty} a_n$ 和 $\lim_{n \to \infty} \frac{a_n}{b^2}$。

_解析_

**（1）** 求 $\lim_{n \to \infty} a_n$

① 近似式

考虑当 $x \to 0$ 时，$\cos x \approx 1 - \frac{x^2}{2}$。

② 做差分析

$$
\cos a_n - \cos b_n = a_n \geq 0
$$

由于 $\cos x$ 在 $(0, \frac{\pi}{2})$ 上是单调递减的，

$$
\Rightarrow \cos a_n > \cos b_n \Rightarrow a_n < b_n
$$

结合已知条件 $\lim_{n \to \infty} b_n = 0$，

$$
\Rightarrow \lim_{n \to \infty} a_n = 0
$$

**（2）** 求极限 $\lim_{n \to \infty} \frac{a_n}{b_n^2}$

由 $\cos a_n - a_n = \cos b_n$ 可得：

$$
1 - \frac{a_n^2}{2} - a_n \approx 1 - \frac{b_n^2}{2}
$$

整理得：

$$
-\frac{a_n^2}{2} - a_n \approx -\frac{b_n^2}{2}
$$

当 $n \to \infty$ 时，两边同时除以 $b_n^2$ 并取极限：

$$
\lim_{n \to \infty} \frac{-\frac{a_n^2}{2} - a_n}{b_n^2} = \lim_{n \to \infty} \left( -\frac{1}{2} \cdot \frac{a_n^2}{b_n^2} - \frac{a_n}{b_n^2} \right) = -\frac{1}{2}
$$

因此，

$$
\lim_{n \to \infty} \frac{a_n}{b_n^2} = \frac{1}{2}
$$

### 例 2.8 (简化版压缩映射定理)

若对于数列 $\{x_n\}$，存在常数 $k$（$0 < k < 1$），使得：

$$
|x_{n+1} - a| \leq k |x_n - a|, \quad n = 1, 2, \cdots
$$

证明 $\{x_n\}$ 收敛于 $a$。

_证明_

由于 $0 \leq |x_{n+1} - a| \leq k |x_n - a|$，可以进一步推导出：

$$
\begin{aligned}
0 &\leq |x_{n+1} - a| \leq k |x_n - a| \\
&\leq k^2 |x_{n-1} - a| \\
&\leq k^3 |x_{n-2} - a| \\
&\leq \cdots \\
&\leq k^n |x_1 - a|
\end{aligned}
$$

当 $n \to \infty$ 时，由于 $0 < k < 1$，则 $k^n \to 0$。因此，

$$
\lim_{n \to \infty} k^n |x_1 - a| = 0
$$

从而，

$$
\lim_{n \to \infty} |x_{n+1} - a| = 0
$$

由夹逼准则可得 $\{x_n\}$ 收敛于 $a$。

### 例 2.8 (拉格朗-压缩映射定理)

若对于数列 $\{x_n\}$，$x_{n+1} = f(x_n)$，$n = 1, 2, \cdots$，$f(x)$ 可导，$a$ 是 $f(x) = x$ 的唯一解，且 $\forall x \in \mathbb{R}$，有 $|f'(x)| \leq k < 1$。证明 $\{x_n\}$ 收敛于 $a$。

_证明_

$$
|x_{n+1} - a| = |f(x_n) - f(a)|
$$

根据拉格朗日中值定理，

$$
|f(x_n) - f(a)|= |f'(\xi)||x_n - a|
$$

其中 $\xi$ 介于 $x_n$ 和 $a$ 之间。

由于 $|f'(x)| \leq k < 1$，

$$
|f'(\xi)||x_n - a| \leq k|x_n - a|
$$

由 [[#例 2.8 (简化版压缩映射定理)]] 知，它是特殊的压缩映射过程，因此 $\{x_n\}$ 收敛于 $a$ 。

# 数列极限04

## 单调有界准则

单调有界数列必有极限，即若数列 $\{x_n\}$ 单调增加（减少）且有上界（下界），则 $\lim_{n \to \infty} x_n$ 存在。

1. 单调增加且有上界

$$
x_n \leq x_{n+1} \leq a \Rightarrow \lim_{n \to \infty} x_n = a
$$

2. 单调减少且有下界

$$
a \leq x_{n+1} \leq x_n \Rightarrow \lim_{n \to \infty} x_n = a
$$

## 证明数列 ${x_n}$ 单调性的常用方法

### a. 差值或比值法

$$
x_{n+1} - x_n > 0 \quad \text{或} \quad \frac{x_{n+1}}{x_n} > 1 \quad (\text{同号})
$$

$$
x_{n+1} - x_n < 0 \quad \text{或} \quad \frac{x_{n+1}}{x_n} < 1 \quad (\text{同号})
$$

### b. 数学归纳法

利用数学归纳法证明数列的单调性。

### c. 利用重要不等式

利用重要不等式来证明数列的单调性。[[#(2) 利用重要不等式]]

### d. 同号差值法

若 $x_n - x_{n-1}$ 与 $x_{n-1} - x_{n-2}$ 同号，则 $\{x_n\}$ 单调。

### e. 利用函数导数的结论

对于 $x_{n+1} = f(x_n)$ （$n = 1, 2, \cdots$），$x_n \in$ 区间 $I$：

- 若 $f'(x) > 0$，$x \in$ 区间 $I$，则数列 $\{x_n\}$ 单调：
  - 当 $x_2 > x_1$ 时，数列 $\{x_n\}$ 单调增加。
  - 当 $x_2 < x_1$ 时，数列 $\{x_n\}$ 单调减少。

- 若 $f'(x) < 0$，$x \in$ 区间 $I$，则数列 $\{x_n\}$ 不单调。

## 超越方程

![2](/blogs/obsn-di-er-jie-shu-lie-ji-xian/2.png)
![2.1](/blogs/obsn-di-er-jie-shu-lie-ji-xian/2.1.png)![2.2](/blogs/obsn-di-er-jie-shu-lie-ji-xian/2.2.png)
