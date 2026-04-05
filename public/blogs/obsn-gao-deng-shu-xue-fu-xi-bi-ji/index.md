> 来源：Obsidian/10-学业与考试/考研/高等数学复习笔记.md

# 高等数学复习笔记

## 第0讲 基础公式与代数变形

### 1. 乘法公式与因式分解

- $(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
- $a^3 \pm b^3 = (a \pm b)(a^2 \mp ab + b^2)$

### 2. 常用不等式

- **均值不等式**：对于 $a, b > 0$，有调和平均 $\le$ 几何平均 $\le$ 算术平均 $\le$ 平方平均，即 $\frac{2}{\frac{1}{a}+\frac{1}{b}} \le \sqrt{ab} \le \frac{a+b}{2} \le \sqrt{\frac{a^2+b^2}{2}}$
- **绝对值/三角不等式**：$||a|-|b|| \le |a \pm b| \le |a|+|b|$
- **伯努利不等式**：$(1+x)^n \ge 1+nx$，当且仅当 $n=0$ 或 $x=0$ 时等号成立
- **柯西不等式**：$(a_1^2+a_2^2+\dots+a_n^2)(b_1^2+b_2^2+\dots+b_n^2) \ge (a_1b_1+a_2b_2+\dots+a_nb_n)^2$

### 3. 一元二次方程与数列

- **韦达定理**：设 $ax^2+bx+c=0$ ($a \neq 0$) 的两个根为 $x_1, x_2$，则 $x_1+x_2 = -\frac{b}{a}$，$x_1x_2 = \frac{c}{a}$
- **斯特林公式 (Stirling's approximation)**：$n! \sim \sqrt{2\pi n}(\frac{n}{e})^n$
- **等差数列**：通项公式 $a_n = a_1 + (n-1)d$；求和公式 $S_n = \frac{n}{2}(a_1+a_n)$
- **等比数列**：通项公式 $a_n = a_1q^{n-1}$；求和公式当 $q=1$ 时 $S_n = na_1$，当 $q \neq 1$ 时 $S_n = \frac{a_1(1-q^n)}{1-q}$

### 4. 坐标系及其变换

- **直角坐标系平移**：平面上一点 $M$，旧坐标为 $(x,y)$，新坐标为 $(X,Y)$。若旧坐标系原点为 $(0,0)$，新坐标系原点为 $(a,b)$，则 $\begin{cases}x=X+a\\ y=Y+b\end{cases} \Rightarrow \begin{cases}X=x-a\\ Y=y-b\end{cases}$
- **坐标轴旋转**：$Ox$ 轴绕原点逆时针旋转 $\theta$ 得到 $OX$ 轴，变换公式为 $\begin{cases}x = X\cos\theta - Y\sin\theta \\ y = X\sin\theta + Y\cos\theta\end{cases}$

---

## 第1讲 函数、极限与连续

### 1. 函数的性质与判定

- **单值函数判定**：作铅直线，若任一条铅直线与 $f(x)$ 至多有 1 个交点，则为单值函数。
- **反函数判定**：在满足单值函数的情况下，作水平直线，若任一条水平直线与 $f(x)$ 至多有 1 个交点，则该函数有反函数。
- **双曲正弦函数与反双曲正弦函数**：
  - **双曲正弦函数**：$y = \sinh x = \frac{e^x - e^{-x}}{2}$ \* **性质**：定义域为 $(-\infty, +\infty)$，值域为 $(-\infty, +\infty)$；是奇函数（关于原点对称）；在整个定义域内单调递增；且其导数为双曲余弦： $(\sinh x)' = \cosh x = \frac{e^x + e^{-x}}{2}$。
  - **反双曲正弦函数**：$y = \text{arsinh } x = \ln(x + \sqrt{x^2+1})$ \* **性质**：定义域为 $(-\infty, +\infty)$，值域为 $(-\infty, +\infty)$；是奇函数（关于原点对称）；在整个定义域内单调递增。
    - **导数**：$(\text{arsinh } x)' = [\ln(x + \sqrt{x^2+1})]' = \frac{1}{\sqrt{x^2+1}}$
- **奇偶性判定**：
  - 复合函数 $f(\varphi(x))$：内偶则全偶，内奇同外。
  - $f(x)$ 为奇函数 $\Rightarrow$ $f'(x)$ 为偶函数；求导一次，奇偶互换。
  - 奇 $\pm$ 奇 = 奇；偶 $\pm$ 偶 = 偶。
  - 奇 $\times$ 奇 = 偶；奇 $\times$ 偶 = 奇；偶 $\times$ 偶 = 偶。
- **周期性**：若 $f(x)$ 以 $T$ 为周期，则 $f(ax+b)$ 以 $\frac{T}{|a|}$ 为周期；若 $f(x)$ 以 $T$ 为周期，则其导数和积分也以 $T$ 为周期。

### 2. 反三角函数

- $y = \arcsin x$ 主值区间 $[-\frac{\pi}{2}, \frac{\pi}{2}]$ _ $y = \arccos x$ 主值区间 $[0, \pi]$ _ 恒等式：
  - $\sin(\arcsin x) = x, x \in [-1, 1]$
  - $\cos(\arccos x) = x, x \in [-1, 1]$
  - $\arcsin(\sin x) = x, x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$
  - $\arccos(\cos x) = x, x \in [0, \pi]$
  - $\sin(\arccos x) = \sqrt{1-x^2}$；$\cos(\arcsin x) = \sqrt{1-x^2}, x \in [-1, 1]$
- 互余关系：$\arcsin x + \arccos x = \frac{\pi}{2} \ (x \in [-1,1])$；$\arctan x + \text{arccot } x = \frac{\pi}{2} \ (x \in (-\infty, +\infty))$

### 3. 极限保号性与无穷小

- **局部保号性**：
  - 脱帽严格不等：$\lim f > 0 \Rightarrow f > 0$；$\lim f < 0 \Rightarrow f < 0$
  - 戴帽非严格不等：$f \ge 0 \Rightarrow \lim f \ge 0$；$f \le 0 \Rightarrow \lim f \le 0$
- **无穷小的性质**：有限个无穷小的和/积是无穷小；有界函数与无穷小的积为无穷小。

### 4. 等价无穷小

- 当 🐶 $\to 0$ 时：
  $$
  \begin{aligned}
  \sin 🐶 &\sim 🐶 & \qquad \tan 🐶 &\sim 🐶 \\
  \ln(1+🐶) &\sim 🐶 & \qquad e^{🐶} - 1 &\sim 🐶 \\
  \arcsin 🐶 &\sim 🐶 & \qquad \arctan 🐶 &\sim 🐶 \\
  \log_a(1+🐶) &\sim \frac{🐶}{\ln a} & \qquad a^{🐶} - 1 &\sim 🐶 \ln a \\
  1 - \cos 🐶 &\sim \frac{1}{2}🐶^2 & \qquad \sqrt[n]{1+🐶} - 1 &\sim \frac{🐶}{n} \\
  🐶 - \sin 🐶 &\sim \frac{1}{6}🐶^3 & \qquad \tan 🐶 - 🐶 &\sim \frac{1}{3}🐶^3 \\
  (1+🐶)^\alpha - 1 &\sim \alpha 🐶 & \qquad \arcsin 🐶 - 🐶 &\sim \frac{1}{6}🐶^3 \\
  🐶 - \arctan 🐶 &\sim \frac{1}{3}🐶^3 & \qquad \tan 🐶 - \sin 🐶 &\sim \frac{1}{2}🐶^3
  \end{aligned}
  $$

### 5. 常用泰勒公式

$\sin x = x - \frac{x^3}{3!} + o(x^3),$ $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + o(x^4),$

$\arcsin x = x + \frac{x^3}{3!} + o(x^3),$ $\tan x = x + \frac{x^3}{3} + o(x^3),$

$\arctan x = x - \frac{x^3}{3} + o(x^3),$ $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} + o(x^3),$

$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + o(x^3),$ $(1+x)^{\alpha} = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!} x^2 + o(x^2).$

---

## 第2讲 数列极限

### 1. 极限计算法则

- 若 $\lim_{x\to x_0} f(x) = A$，则 $\lim_{x\to x_0} |f(x)| = |A|$（反之不成立）。
- 极限四则运算简记：存在 $\pm$ 存在 = 存在；存在 $\pm$ 不存在 = 不存在；不存在 $\pm$ 不存在 = 不确定。
- 注意：$\lim_{n\to\infty} (a_n+b_n)$ 存在，并不意味着 $\lim_{n\to\infty} a_n$ 和 $\lim_{n\to\infty} b_n$ 均存在。

### 2. 常用缩放不等式

- $\sin x < x < \tan x \ (0 < x < \frac{\pi}{2})$
- $\sin x < x \ (x > 0)$
- $x < \tan x < \frac{4}{\pi}x \ (0 < x < \frac{\pi}{4})$
- $\arctan x \le x \le \arcsin x \ (0 \le x \le 1)$
- $e^x > x+1$
- $x-1 \ge \ln x \ (x > 0)$
- $\frac{1}{x+1} < \ln(1+\frac{1}{x}) < \frac{1}{x} \ (x > 0)$ 或 $\frac{x}{1+x} < \ln(1+x) < x \ (x > 0)$

### 3. n次根号极限

- $\lim_{n\to\infty} \sqrt[n]{a_1^n+a_2^n+\dots+a_n^n} = \max\{a_1, a_2, \dots, a_n\}$

---

## 第3讲 一元函数微分学的概念

### 1. 导数定义与连续可导性

- $f'(x_0) = \lim_{\Delta x\to 0} \frac{f(x_0+\Delta x)-f(x_0)}{\Delta x} = \lim_{x\to x_0} \frac{f(x)-f(x_0)}{x-x_0}$
- 设 $f(x)$ 在 $x=a$ 处连续，$F(x) = f(x)|x-a|$，则只有当 $f(a)=0$ 时，$F(x)$ 在 $x=a$ 处才可导。

### 2. 导数计算法则

- **反函数求导**：反函数 $x = \varphi(y)$，一阶导数 $\varphi'(y) = \frac{1}{f'(x)}$；二阶导数 $\varphi''(y) = -\frac{f''(x)}{[f'(x)]^3}$
- **参数方程求导**：一阶导数 $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$；二阶导数 $\frac{d^2y}{dx^2} = \frac{(dy/dx)'_t}{dx/dt}$

### 3. 高阶导数公式

- **归纳法常用公式**：
  - $(e^{ax+b})^{(n)} = a^n e^{ax+b}$
  - $[\sin(ax+b)]^{(n)} = a^n \sin(ax+b+\frac{n\pi}{2})$
  - $[\cos(ax+b)]^{(n)} = a^n \cos(ax+b+\frac{n\pi}{2})$
  - $[\ln(ax+b)]^{(n)} = (-1)^{n-1} a^n \frac{(n-1)!}{(ax+b)^n}$
  - $(\frac{1}{ax+b})^{(n)} = (-1)^n a^n \frac{n!}{(ax+b)^{n+1}}$
- **莱布尼茨公式 (Leibniz)**：
  - $(u \pm v)^{(n)} = u^{(n)} \pm v^{(n)}$
  - $(uv)^{(n)} = \sum_{k=0}^n C_n^k u^{(n-k)}v^{(k)} = u^{(n)}v + C_n^1 u^{(n-1)}v' + \dots + u v^{(n)}$
- **泰勒展开式**：（原笔记 P179，内容留待补充）

---

## 第5讲 一元函数微分学的应用（一：几何应用）

### 1. 极值判别

- **第一充分条件**：$f(x)$ 在 $x=x_0$ 处连续，且 $f'(x_0)=0$。若 $f'(x_0^-) > 0$ 且 $f'(x_0^+) < 0$，则有极大值；反之极小值。
- **第二充分条件**：设 $f(x)$ 在 $x_0$ 处二阶可导，且 $f'(x_0)=0, f''(x_0) \neq 0$。若 $f''(x_0) < 0$ 取极大值；若 $f''(x_0) > 0$ 取极小值。

### 2. 凹凸性与拐点判别

- **凹凸性**：设函数 $f(x)$ 在区间 $I$ 上二阶可导。若在 $I$ 上 $f''(x) > 0$，则 $f(x)$ 在 $I$ 上的图形是凹的。
- **拐点第一充分条件**：$f(x)$ 在 $x_0$ 处连续，二阶导数存在，且该点左右邻域内 $f''(x)$ 变号，则点 $(x_0, f(x_0))$ 为曲线拐点。
- **拐点第二充分条件**：在 $x_0$ 邻域内三阶可导，且 $f''(x_0)=0, f'''(x_0) \neq 0$，则点 $(x_0, f(x_0))$ 是曲线拐点。

### 3. 多项式根与极值/拐点结论

- 设多项式 $f(x) = (x-a)^n g(x) \ (n \ge 1)$ 且 $g(a) \neq 0$。当 $n$ 为偶数时，$x=a$ 是极值点；当 $n$ 为奇数时，点 $(a, 0)$ 是拐点。
- 设 $f(x) = (x-a_1)^{n_1}(x-a_2)^{n_2}\dots(x-a_k)^{n_k}$。设 $k_1$ 为 $n_i=1$ 的个数，$k_2$ 为 $n_i \ge 2$ 的偶数个数，$k_3$ 为 $n_i \ge 3$ 的奇数个数。则：
  - 极值点个数为：$k_1 + 2k_2 + k_3 - 1$
  - 拐点个数为：$k_1 + 2k_2 + 3k_3 - 2$
- **【例题补充】**：设 $f(x) = (x-1)(x-2)(x-3)^3(x-4)^4(x-5)^5$
  - 这里 $k_1=2$（对应一次项 $x-1, x-2$），$k_2=1$（对应偶次项 $x-4$），$k_3=2$（对应奇数次项 $x-3, x-5$）。
  - 极值点个数为：$2 + 2\times1 + 2 - 1 = 5$ 个
  - 拐点个数为：$2 + 2\times1 + 3\times2 - 2 = 8$ 个

### 4. 渐近线与曲率

- **寻找顺序**：铅直渐近线 $\rightarrow$ 水平渐近线 $\rightarrow$ 斜渐近线。
- **斜渐近线**：若 $\lim_{x\to+\infty} \frac{f(x)}{x} = a_1 \ (a_1 \neq 0)$，且 $\lim_{x\to+\infty} [f(x)-a_1x] = b_1$，则 $y = a_1x+b_1$ 是一条斜渐近线（$x \to -\infty$ 同理；只有当 $a, b$ 都存在时才存在斜渐近线）。
- **曲率**：$K = \frac{|y''|}{[1+(y')^2]^{3/2}}$；曲率半径 $R = \frac{1}{K}$

---

## 第6讲 一元微分应用（二：中值定理）

### 1. 闭区间连续函数定理

- **有界与最值定理**：设 $f(x)$ 在 $[a,b]$ 上连续，则 $m \le f(x) \le M$（$m, M$ 分别为最小值与最大值）。
- **介值定理**：当 $m \le \mu \le M$ 时，存在 $\xi \in [a,b]$ 使得 $f(\xi) = \mu$。
- **平均值定理**：当 $a < x_1 < x_2 < \dots < x_n < b$，在 $[x_1, x_n]$ 内至少存在一点 $\xi$ 使得 $f(\xi) = \frac{f(x_1)+f(x_2)+\dots+f(x_n)}{n}$。
- **零点定理**：当 $f(a)f(b) < 0$ 时，存在 $\xi \in (a,b)$ 使得 $f(\xi) = 0$。

### 2. 微分中值定理与导数性质

- **导数零点定理（达布定理）**：可导函数的导函数若在区间端点异号，则区间内必有导数为零的点。
- **费马定理**：设 $f(x)$ 在 $x_0$ 处可导且取极值，则 $f'(x_0) = 0$。
- **罗尔 (Rolle) 定理**：若 $f(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导，且 $f(a)=f(b)$，则存在 $\xi \in (a,b)$ 使得 $f'(\xi)=0$。
- **拉格朗日 (Lagrange) 中值定理**：若 $f(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导，则存在 $\xi \in (a,b)$ 使得 $\frac{f(b)-f(a)}{b-a} = f'(\xi)$。
- **柯西 (Cauchy) 中值定理**：若 $f(x), g(x)$ 在 $[a,b]$ 连续、$(a,b)$ 可导，且 $g'(x) \neq 0$，则存在 $\xi \in (a,b)$ 使得 $\frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(\xi)}{g'(\xi)}$。

### 3. 方程实根应用

- **辅助函数构造**：（原笔记 P215 提及，方法留待补充）
- **罗尔定理推论（判断根个数）**：若 $f^{(n)}(x) = 0$ 至多有 $k$ 个根，则 $f(x)$ 至多有 $k+n$ 个根。例如，$f''(x)=0$ 至多一个根，则 $f(x)=0$ 至多三个根。
- 任何实系数奇次方程至少有一个实根。

## 第8讲 一元函数积分学的概念与性质

### 1. 原函数（不定积分）存在定理

- 连续函数必有原函数。
- 含有第一类间断点的函数在包含间断点的区间内必没有原函数。
- 含有振荡间断点的函数无法确定是否有原函数。

### 2. 积分中值定理

- $\int_a^b f(x) dx = f(\xi)(b-a)$。

### 3. 定积分存在定理（黎曼积分）

- **充分条件**：
  - 若 $f(x)$ 在 $[a,b]$ 上连续，则 $\int_a^b f(x) dx$ 存在。
  - 若 $f(x)$ 在 $[a,b]$ 上单调，则 $\int_a^b f(x) dx$ 存在。
  - 若 $f(x)$ 在 $[a,b]$ 上有界，且只有有限个间断点，则 $\int_a^b f(x) dx$ 存在。
  - 若 $f(x)$ 在 $[a,b]$ 上有有限个第一类间断点，则 $\int_a^b f(x) dx$ 存在。
- **必要条件**：
  - 可积函数必有界，即若 $\int_a^b f(x) dx$ 存在，则 $f(x)$ 在 $[a,b]$ 上必有界。

### 4. 积分的保号性

- 若在区间 $[a,b]$ 上 $f(x) \le g(x)$，则有 $\int_a^b f(x) dx \le \int_a^b g(x) dx$，特殊的，有 $|\int_a^b f(x) dx| \le \int_a^b |f(x)| dx$。

### 5. 估值定理

- 设 $M, m$ 分别是 $f(x)$ 在 $[a,b]$ 上的最大值和最小值，$L$ 为区间 $[a,b]$ 的长度，则有 $mL \le \int_a^b f(x) dx \le ML$。

### 6. 定积分定义

- $\int_0^1 f(x) dx = \lim_{n \to \infty} \sum_{i=1}^n f(\frac{i}{n}) \frac{1}{n}$。

### 7. 变限积分性质

- 若 $f(x)$ 在 $I$ 上可积，则 $F(x) = \int_a^x f(t) dt$ 在 $I$ 上连续。
- 若 $f(x)$ 在 $I$ 上连续，则 $F(x) = \int_a^x f(t) dt$ 在 $I$ 上可导，且 $F'(x) = f(x)$。

### 7. 变限积分性质

- (1) 函数 $f(x)$ 在 $I$ 上可积，则函数 $F(x) = \int_a^x f(t) dt$ 在 $I$ 上连续。
  $F(x)$ 若存在，则一定连续，但 $f(x)$ 存在并不一定连续。
- (2) 函数 $f(x)$ 在 $I$ 上连续，则函数 $F(x) = \int_a^x f(t) dt$ 在 $I$ 上可导，且 $F'(x) = f(x)$。
- (3) 若 $x = x_0 \in I$ 是 $f(x)$ 唯一一跳跃间断点，则 $F(x) = \int_a^x f(t) dt$ 在 $x_0$ 处不可导，且 $\begin{cases} F'_-(x_0) = \lim_{x \to x_0^-} f(x) \\ F'_+(x_0) = \lim_{x \to x_0^+} f(x) \end{cases}$。
- 若 $x = x_0 \in I$ 是 $f(x)$ 唯一一可去间断点，则 $F(x) = \int_a^x f(t) dt$ 在 $x_0$ 处可导，且 $F'(x_0) = \lim_{x \to x_0} f(x) \neq f(x_0)$。

### 8. 反常积分敛散性判别

- **比较判别法**：设函数 $f(x), g(x)$ 在区间 $[a, +\infty)$ 上连续，并且 $0 \le f(x) \le g(x)$。
  - 若 $\int_a^{+\infty} g(x) dx$ 收敛，则 $\int_a^{+\infty} f(x) dx$ 收敛。
  - 若 $\int_a^{+\infty} f(x) dx$ 发散，则 $\int_a^{+\infty} g(x) dx$ 发散。
- **比较判别法的极限形式**：设函数 $f(x), g(x)$ 在区间 $[a, +\infty)$ 上连续，且 $f(x) \ge 0, g(x) \ge 0$，$\lim_{x \to +\infty} \frac{f(x)}{g(x)} = \lambda$。
  - 当 $0 < \lambda < +\infty$ 时，两者有相同的敛散性。
  - 当 $\lambda = 0$ 时，若 $\int_a^{+\infty} g(x) dx$ 收敛，则 $\int_a^{+\infty} f(x) dx$ 也收敛。
  - 当 $\lambda = \infty$ 时，若 $\int_a^{+\infty} g(x) dx$ 发散，则 $\int_a^{+\infty} f(x) dx$ 也发散。
- **四个敛散性判别结论（p积分）**：
  - ① $\int_0^1 \frac{1}{x^p} dx$：当 $0 < p < 1$ 时收敛；当 $p \ge 1$ 时发散。
  - ② $\int_1^{+\infty} \frac{1}{x^p} dx$：当 $p > 1$ 时收敛；当 $p \le 1$ 时发散。
  - ③ $\int_0^1 \frac{\ln x}{x^p} dx$ 与 ① 的敛散性一致（$\ln x$ 不影响敛散性）。
  - ④ $\int_1^{+\infty} \frac{\ln x}{x^p} dx$ 与 ② 的敛散性一致（$\ln x$ 不影响敛散性）。

---

## 第9讲 一元函数积分学的计算

### 1. 基本积分公式

- （课本 P278 的基本积分公式）
  **① 幂函数积分**
- $\int x^k dx = \frac{1}{k+1}x^{k+1} + C \quad (k \neq -1)$
- $\int \frac{1}{x^2} dx = -\frac{1}{x} + C$
- $\int \frac{1}{\sqrt{x}} dx = 2\sqrt{x} + C$

**② 对数函数积分**

- $\int \frac{1}{x} dx = \ln|x| + C \quad \rightarrow (\ln x)' = \frac{1}{x}$

**③ 指数函数积分**

- $\int e^x dx = e^x + C$
- $\int a^x dx = \frac{a^x}{\ln a} + C \quad (a>0 \text{ 且 } a \neq 1) \quad \rightarrow (a^x)' = a^x \ln a$

**④ 三角函数积分 (一次)**

- $\int \sin x dx = -\cos x + C \qquad \qquad  \qquad \qquad \int \cos x dx = \sin x + C$
- $\int \tan x dx = -\ln|\cos x| + C \qquad \qquad  \qquad \qquad \int \cot x dx = \ln|\sin x| + C$
  > 推导：$\int \tan x dx = \int \frac{\sin x}{\cos x} dx = -\int \frac{1}{\cos x} d(\cos x) = -\ln|\cos x| + C$
- $\int \frac{dx}{\cos x} = \int \sec x dx = \ln|\sec x + \tan x| + C$
- $\int \frac{dx}{\sin x} = \int \csc x dx = \ln|\csc x - \cot x| + C$
- $\int \sec^2 x dx = \tan x + C \qquad \qquad  \qquad \qquad \int \csc^2 x dx = -\cot x + C$
- $\int \sec x \tan x dx = \sec x + C \qquad \qquad  \qquad \qquad \int \csc x \cot x dx = -\csc x + C$

**⑤ 反正切型积分**

- $\int \frac{1}{1+x^2} dx = \arctan x + C$
- $\int \frac{1}{a^2+x^2} dx = \frac{1}{a}\arctan\frac{x}{a} + C \quad (a > 0)$

**⑥ 反正弦型积分**

- $\int \frac{1}{\sqrt{1-x^2}} dx = \arcsin x + C$
- $\int \frac{1}{\sqrt{a^2-x^2}} dx = \arcsin\frac{x}{a} + C \quad (a > 0)$

**⑦ 根号加减对数型积分**

- $\int \frac{1}{\sqrt{x^2+a^2}} dx = \ln(x + \sqrt{x^2+a^2}) + C \quad (\text{常见 } a=1)$
- $\int \frac{1}{\sqrt{x^2-a^2}} dx = \ln|x + \sqrt{x^2-a^2}| + C \quad (|x| > |a|)$

**⑧ 有理分式对数型积分**

- $\int \frac{1}{x^2-a^2} dx = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right| + C$
- $\int \frac{1}{a^2-x^2} dx = \frac{1}{2a}\ln\left|\frac{x+a}{x-a}\right| + C$

**⑨ 圆面积型积分**

- $\int \sqrt{a^2-x^2} dx = \frac{a^2}{2}\arcsin\frac{x}{a} + \frac{x}{2}\sqrt{a^2-x^2} + C \quad (a > |x| \ge 0)$

**⑩ 三角函数积分 (二次)**

- $\int \sin^2 x dx = \frac{x}{2} - \frac{\sin 2x}{4} + C \quad \leftarrow \left(\text{降幂: } \sin^2 x = \frac{1-\cos 2x}{2}\right)$
- $\int \cos^2 x dx = \frac{x}{2} + \frac{\sin 2x}{4} + C \quad \leftarrow \left(\text{降幂: } \cos^2 x = \frac{1+\cos 2x}{2}\right)$
- $\int \tan^2 x dx = \tan x - x + C \quad \leftarrow \left(\tan^2 x = \sec^2 x - 1\right)$
- $\int \cot^2 x dx = -\cot x - x + C \quad \leftarrow \left(\cot^2 x = \csc^2 x - 1\right)$

![IMG_20260331_224919](/blogs/obsn-gao-deng-shu-xue-fu-xi-bi-ji/IMG_20260331_224919.jpg)

### 2. 分部积分法的推广（表格法）

- $\int u v^{(n)} dx = u v^{(n-1)} - u' v^{(n-2)} + u'' v^{(n-3)} - u^{(3)} v^{(n-4)} + \dots + (-1)^n \int u^{(n)} v dx$。
  ![Pasted image 20260331225919](/blogs/obsn-gao-deng-shu-xue-fu-xi-bi-ji/Pasted image 20260331225919.png)

### 3. 指数与三角函数乘积公式

① $\int e^{ax} \sin bx dx = \frac{\begin{vmatrix} (e^{ax})' & (\sin bx)' \\ e^{ax} & \sin bx \end{vmatrix}}{a^2+b^2} + C = \frac{ae^{ax} \sin bx - be^{ax} \cos bx}{a^2+b^2} + C$；

② $\int e^{ax} \cos bx dx = \frac{\begin{vmatrix} (e^{ax})' & (\cos bx)' \\ e^{ax} & \cos bx \end{vmatrix}}{a^2+b^2} + C = \frac{ae^{ax} \cos bx + be^{ax} \sin bx}{a^2+b^2} + C$。

再如， $\int e^{-x} \sin nx dx = \frac{-e^{-x} \sin nx - ne^{-x} \cos nx}{(-1)^2+n^2} + C$。

### 4. 有理函数积分的拆分法则

- 形如 $\int \frac{P_n(x)}{Q_m(x)} dx \ (n < m)$：
  - 若分母含有因式 $(ax+b)$，则拆出 $\frac{A}{ax+b}$。
  - 若分母含有因式 $(ax+b)^k$，则拆出 $\frac{A_1}{ax+b} + \frac{A_2}{(ax+b)^2} + \dots + \frac{A_k}{(ax+b)^k}$。
  - 若分母含有因式 $(px^2+qx+r)$，则拆出 $\frac{Ax+B}{px^2+qx+r}$。
  - 若分母含有因式 $(px^2+qx+r)^k$，则拆出 $\frac{A_1x+B_1}{px^2+qx+r} + \frac{A_2x+B_2}{(px^2+qx+r)^2} + \dots + \frac{A_kx+B_k}{(px^2+qx+r)^k}$。

### 5. 万能公式变换

- 设 $t = \tan\frac{x}{2}$，则有：
  - $\sin x = \frac{2t}{1+t^2}$
  - $\cos x = \frac{1-t^2}{1+t^2}$
  - $dx = \frac{2}{1+t^2} dt$ （注意不要漏掉微分项的替换）

### 6. 点火公式（华里士公式 / Wallis）

- **基础区间 $[0, \frac{\pi}{2}]$**：
  $$
  \int_0^{\frac{\pi}{2}} \sin^n x dx = \int_0^{\frac{\pi}{2}} \cos^n x dx =
  \begin{cases}
  \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot \dots \cdot \frac{2}{3} \cdot 1, & n \text{ 为大于 } 1 \text{ 的奇数}, \\
  \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot \dots \cdot \frac{1}{2} \cdot \frac{\pi}{2}, & n \text{ 为正偶数}.
  \end{cases}
  $$
- **推广区间 $[0, \pi]$**：
  $$
  \int_0^\pi \sin^n x dx =
  \begin{cases}
  2 \cdot \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot \dots \cdot \frac{2}{3} \cdot 1, & n \text{ 为大于 } 1 \text{ 的奇数}, \\
  2 \cdot \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot \dots \cdot \frac{1}{2} \cdot \frac{\pi}{2}, & n \text{ 为正偶数},
  \end{cases}
  $$

$$
\int_0^\pi \cos^n x dx =
\begin{cases}
0, & n \text{ 为正奇数}, \\
2 \cdot \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot \dots \cdot \frac{1}{2} \cdot \frac{\pi}{2}, & n \text{ 为正偶数}.
\end{cases}
$$

- **推广区间 $[0, 2\pi]$**：
  $$
  \int_0^{2\pi} \cos^n x dx = \int_0^{2\pi} \sin^n x dx =
  \begin{cases}
  0, & n \text{ 为正奇数}, \\
  4 \cdot \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdot \dots \cdot \frac{1}{2} \cdot \frac{\pi}{2}, & n \text{ 为正偶数}.
  \end{cases}
  $$

### 7. 变限积分求导

- $F(x) = \int_{\varphi_1(x)}^{\varphi_2(x)} f(t) dt \Rightarrow F'(x) = f(\varphi_2(x))\varphi_2'(x) - f(\varphi_1(x))\varphi_1'(x)$。

### 8. 伽马函数（反常积分计算）

- **定义**：$\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1} e^{-x} dx \stackrel{x=t^2}{=\!=\!=} 2\int_0^{+\infty} t^{2\alpha-1} e^{-t^2} dt \quad (x, t > 0) .$
- **性质**：
  - 递推式：$$\Gamma(\alpha+1) = \int_0^{+\infty} x^\alpha e^{-x} dx = -\int_0^{+\infty} x^\alpha d(e^{-x}) = -x^\alpha e^{-x} \Big|_0^{+\infty} + \int_0^{+\infty} e^{-x} \alpha x^{\alpha-1} dx = \alpha\Gamma(\alpha) ,$$
  - 若 $\alpha = n$（正整数），则 $\Gamma(n+1) = n!$。
  - 特殊值：$\Gamma(1) = 1$，$\Gamma(\frac{1}{2}) = \sqrt{\pi}$。
- **计算示例**：$\Gamma(\frac{5}{2}) = \Gamma(1 + \frac{3}{2}) = \frac{3}{2}\Gamma(\frac{3}{2}) = \frac{3}{2}\Gamma(1 + \frac{1}{2}) = \frac{3}{2} \times \frac{1}{2}\Gamma(\frac{1}{2}) = \frac{3}{4}\sqrt{\pi}$。

---

## 第10讲 一元函数积分学的几何应用

### 1. 平面图形面积

- **直角坐标方程**：$S = \int_a^b |y_1(x) - y_2(x)| dx$。
- **极坐标方程**：$S = \frac{1}{2} \int_\alpha^\beta |r_1^2(\theta) - r_2^2(\theta)| d\theta$。
- **参数方程**：$\begin{cases} x = x(t) \\ y = y(t) \end{cases} \Rightarrow S = \int_\alpha^\beta y(t) x'(t) dt$ （本质是套用直角坐标系下的面积公式 $\int y dx$，进行换元计算）。

### 2. 旋转体体积

- 曲线 $y = f(x)$ 与 $x=a, x=b$ 及 $x$ 轴围成的曲边梯形绕 $x$ 轴旋转：$V_x = \pi \int_a^b f^2(x) dx$。
- 绕 $y$ 轴旋转：$V_y = 2\pi \int_a^b x|f(x)| dx$。
- 平面曲线 $L: y=f(x)$ 绕定直线 $Ax+By+C=0$ 旋转：
  $$V = \frac{\pi}{(A^2+B^2)^{3/2}} \int_a^b (Ax+Bf(x)+C)^2 |Af'(x)-B| dx$$

### 3. 形心坐标公式

- $\bar{x} = \frac{\int_a^b x f(x) dx}{\int_a^b f(x) dx}$。
- $\bar{y} = \frac{\frac{1}{2}\int_a^b f^2(x) dx}{\int_a^b f(x) dx}$。

### 4. 平面曲线的弧长

- **直角坐标方程**：$S = \int_a^b \sqrt{1+[y'(x)]^2} dx$。
- **参数方程**：$S = \int_\alpha^\beta \sqrt{[x'(t)]^2 + [y'(t)]^2} dt$。
- **极坐标方程**：$S = \int_\alpha^\beta \sqrt{[r(\theta)]^2 + [r'(\theta)]^2} d\theta$。

### 5. 旋转曲面的面积

- **直角坐标方程**（绕 $x$ 轴）：$S = 2\pi \int_a^b |f(x)| \sqrt{1+[f'(x)]^2} dx$。
- **参数方程**（绕 $x$ 轴）：$S = 2\pi \int_\alpha^\beta |y(t)| \sqrt{[x'(t)]^2+[y'(t)]^2} dt$。
- **极坐标方程**（绕极轴）：$S = 2\pi \int_\alpha^\beta |r(\theta)\sin\theta| \sqrt{[r(\theta)]^2+[r'(\theta)]^2} d\theta$。

---

## 第11讲 一元函数积分学的应用（三：等式与不等式）

### 1. 积分中值定理推论

- 若 $f(x), g(x)$ 在 $[a,b]$ 上连续，且 $g(x)$ 在 $[a,b]$ 上不变号，则存在 $\xi \in (a,b)$ 使得 $$\int_a^b f(x)g(x) dx = f(\xi)\int_a^b g(x) dx$$
