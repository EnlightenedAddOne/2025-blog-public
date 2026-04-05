> 来源：Obsidian/10-学业与考试/考研/数据结构/05.树与二叉树.md

# 第五章：树与二叉树 (Tree & Binary Tree)

## 1. 树的基本概念

- 对应视频：`5.1.1_树的定义`、`5.1.2_树的性质`

### 1.1 基本术语

- **度 (Degree)**：节点拥有的子树数量。树的度是所有节点度的最大值。
- **深度 (Depth)**：从根节点到该节点的层数（根节点深度为1）。
- **高度 (Height)**：从该节点到叶子节点的最长路径长度。
- **叶子节点**：度为0的节点。
- **分支节点**：度不为0的节点。

### 1.2 树的性质

- **性质1**：节点数 = 所有节点的度数之和 + 1。
  - 即：$n = n_0 + n_1 + n_2 + ... = \sum_{i=0}^{m} n_i$
  - 边数 = 节点数 - 1 = $\sum_{i=1}^{m} i \cdot n_i$
- **性质2**：度为 $m$ 的树第 $i$ 层至多有 $m^{i-1}$ 个节点（$i \ge 1$）。
- **性质3**：高度为 $h$ 的 $m$ 叉树至多有 $(m^h - 1)/(m - 1)$ 个节点。

---

## 2. 二叉树 (Binary Tree)

### 2.1 二叉树的定义与特性

- 对应视频：`5.2.1_二叉树的定义`、`5.2.2_二叉树的性质`

**定义**：每个节点最多有两个子树的有序树。

**特殊二叉树**：

- **满二叉树**：除叶子节点外，每个节点度都为2，且叶子节点都在最底层。
  - 高度为 $h$ 的满二叉树有 $2^h - 1$ 个节点。
- **完全二叉树**：编号与满二叉树一一对应（从上到下，从左到右）。
  - 若有 $n$ 个节点，则高度 $h = \lceil \log_2(n+1) \rceil$。

### 2.2 二叉树的性质（必背）

- **性质1**：第 $i$ 层至多有 $2^{i-1}$ 个节点（$i \ge 1$）。
- **性质2**：高度为 $h$ 的二叉树至多有 $2^h - 1$ 个节点。
- **性质3（重要）**：$n_0 = n_2 + 1$（叶子数 = 度为2的节点数 + 1）。
  - **证明**：设总节点数为 $n$，则 $n = n_0 + n_1 + n_2$。
  - 边数 = $n - 1 = n_1 + 2n_2$（每个分支节点产生的边）。
  - 联立得：$n_0 = n_2 + 1$。
- **性质4（完全二叉树）**：
  - 若 $i > 1$，父节点编号为 $\lfloor i/2 \rfloor$。
  - 若 $2i \le n$，左孩子编号为 $2i$；若 $2i+1 \le n$，右孩子编号为 $2i+1$。
  - 若 $n$ 为偶数，则 $n_1 = 1$；若 $n$ 为奇数，则 $n_1 = 0$。

### 2.3 二叉树的存储结构

**C语言代码实现**：

```c
// 顺序存储（适合完全二叉树）
#define MaxSize 100
typedef struct {
    ElemType data[MaxSize];  // 存储节点值
    int length;              // 当前节点数
} SqBiTree;

// 链式存储（二叉链表）
typedef struct BiTNode {
    ElemType data;                  // 数据域
    struct BiTNode *lchild, *rchild; // 左右孩子指针
} BiTNode, *BiTree;

// 三叉链表（增加父节点指针）
typedef struct TriTNode {
    ElemType data;
    struct TriTNode *lchild, *rchild, *parent;
} TriTNode, *TriTree;
```

---

## 3. 二叉树的遍历 (必考重点)

- 对应视频：`5.3_1_二叉树的遍历`

### 3.1 递归遍历

**C语言代码实现**：

```c
// 先序遍历（PreOrder）：根 -> 左 -> 右
void PreOrder(BiTree T) {
    if(T != NULL) {
        visit(T);               // 访问根节点
        PreOrder(T->lchild);    // 递归遍历左子树
        PreOrder(T->rchild);    // 递归遍历右子树
    }
}

// 中序遍历（InOrder）：左 -> 根 -> 右
void InOrder(BiTree T) {
    if(T != NULL) {
        InOrder(T->lchild);     // 递归遍历左子树
        visit(T);               // 访问根节点
        InOrder(T->rchild);     // 递归遍历右子树
    }
}

// 后序遍历（PostOrder）：左 -> 右 -> 根
void PostOrder(BiTree T) {
    if(T != NULL) {
        PostOrder(T->lchild);   // 递归遍历左子树
        PostOrder(T->rchild);   // 递归遍历右子树
        visit(T);               // 访问根节点
    }
}
```

### 3.2 非递归遍历（栈实现）

**先序遍历（非递归）**：

```c
void PreOrder_NonRecursive(BiTree T) {
    InitStack(S);
    BiTree p = T;
    while(p || !IsEmpty(S)) {
        if(p) {                     // 一路向左
            visit(p);               // 访问节点
            Push(S, p);             // 入栈
            p = p->lchild;          // 左孩子
        } else {                    // 出栈，转向右子树
            Pop(S, p);
            p = p->rchild;
        }
    }
}
```

**中序遍历（非递归）**：

```c
void InOrder_NonRecursive(BiTree T) {
    InitStack(S);
    BiTree p = T;
    while(p || !IsEmpty(S)) {
        if(p) {                     // 一路向左
            Push(S, p);             // 入栈
            p = p->lchild;
        } else {                    // 出栈并访问
            Pop(S, p);
            visit(p);               // 访问节点
            p = p->rchild;          // 转向右子树
        }
    }
}
```

**后序遍历（非递归）**：

```c
void PostOrder_NonRecursive(BiTree T) {
    InitStack(S);
    BiTree p = T, r = NULL;  // r记录最近访问过的节点
    while(p || !IsEmpty(S)) {
        if(p) {                         // 走到最左边
            Push(S, p);
            p = p->lchild;
        } else {                        // 向右
            GetTop(S, p);               // 读栈顶节点（不出栈）
            if(p->rchild && p->rchild != r) { // 右子树存在且未被访问
                p = p->rchild;          // 转向右子树
            } else {                    // 访问节点
                Pop(S, p);
                visit(p);
                r = p;                  // 记录最近访问的节点
                p = NULL;               // 节点访问完后，重置p指针
            }
        }
    }
}
```

### 3.3 层序遍历（队列实现）

**C语言代码实现**：

```c
// 层序遍历（LevelOrder）
void LevelOrder(BiTree T) {
    InitQueue(Q);
    BiTree p;
    EnQueue(Q, T);                  // 根节点入队
    while(!IsEmpty(Q)) {
        DeQueue(Q, p);              // 出队
        visit(p);                   // 访问节点
        if(p->lchild != NULL)       // 左孩子入队
            EnQueue(Q, p->lchild);
        if(p->rchild != NULL)       // 右孩子入队
            EnQueue(Q, p->rchild);
    }
}
```

### 3.4 由遍历序列构造二叉树（考点）

**考点提示**：

- **先序 + 中序** 可以唯一确定一棵二叉树。
- **后序 + 中序** 可以唯一确定一棵二叉树。
- **先序 + 后序** **不能**唯一确定（缺少中序无法确定左右子树分界）。
- **层序 + 中序** 可以唯一确定一棵二叉树。

**构造算法思想**（以先序+中序为例）：

1. 先序序列第一个元素是根节点。
2. 在中序序列中找到根节点，左边是左子树，右边是右子树。
3. 递归构造左右子树。

---

## 4. 线索二叉树 (Threaded Binary Tree)

- 对应视频：`5.3_2_线索二叉树`

### 4.1 基本思想

**目的**：利用二叉树中的空指针域，存放节点的前驱和后继信息，将非线性结构线性化。

- 若左子树为空，则 `lchild` 指向**前驱**节点。
- 若右子树为空，则 `rchild` 指向**后继**节点。
- 引入标志域 `ltag` 和 `rtag`：
  - `ltag = 0`：`lchild` 指向左孩子。
  - `ltag = 1`：`lchild` 指向前驱。
  - `rtag = 0`：`rchild` 指向右孩子。
  - `rtag = 1`：`rchild` 指向后继。

### 4.2 线索二叉树节点结构

**C语言代码实现**：

```c
// 线索二叉树节点定义
typedef struct ThreadNode {
    ElemType data;
    struct ThreadNode *lchild, *rchild;
    int ltag, rtag;  // 左右线索标志：0表示孩子，1表示线索
} ThreadNode, *ThreadTree;
```

### 4.3 中序线索化（递归）

**C语言代码实现**：

```c
// 中序线索化
void InThread(ThreadTree &p, ThreadNode *&pre) {
    if(p != NULL) {
        InThread(p->lchild, pre);       // 递归，线索化左子树

        // 处理当前节点
        if(p->lchild == NULL) {         // 左子树为空，建立前驱线索
            p->lchild = pre;
            p->ltag = 1;
        }
        if(pre != NULL && pre->rchild == NULL) { // 建立前驱的后继线索
            pre->rchild = p;
            pre->rtag = 1;
        }
        pre = p;                        // pre指向当前访问的节点

        InThread(p->rchild, pre);       // 递归，线索化右子树
    }
}

// 主过程
void CreateInThread(ThreadTree T) {
    ThreadNode *pre = NULL;
    if(T != NULL) {                     // 非空二叉树，线索化
        InThread(T, pre);               // 线索化二叉树
        pre->rchild = NULL;             // 处理遍历的最后一个节点
        pre->rtag = 1;
    }
}
```

### 4.4 在中序线索二叉树中找前驱和后继

**C语言代码实现**：

```c
// 中序线索二叉树中找中序后继
ThreadNode* Firstnode(ThreadNode *p) {  // 找以p为根的子树中第一个被中序遍历的节点
    while(p->ltag == 0) p = p->lchild;  // 最左下节点（不一定是叶子）
    return p;
}

ThreadNode* Nextnode(ThreadNode *p) {   // 找节点p在中序线索二叉树中的后继
    if(p->rtag == 0) return Firstnode(p->rchild); // 右子树最左下节点
    else return p->rchild;              // rtag==1 直接返回后继线索
}

// 不含头节点的中序线索二叉树的中序遍历算法
void InOrder(ThreadNode *T) {
    for(ThreadNode *p = Firstnode(T); p != NULL; p = Nextnode(p))
        visit(p);
}
```

**考点提示**：

- 先序、中序、后序线索二叉树的构造方法类似。
- 中序线索二叉树最常考，需掌握找前驱、后继的方法。

---

## 5. 树与森林的存储

- 对应视频：`5.4_1_树的存储结构`、`5.4_2_树和森林的遍历`

### 5.1 树的存储结构

**1. 双亲表示法**：

```c
#define MAX_TREE_SIZE 100
typedef struct {
    ElemType data;   // 数据元素
    int parent;      // 双亲位置域
} PTNode;

typedef struct {
    PTNode nodes[MAX_TREE_SIZE];
    int n;           // 节点数
} PTree;
```

- **优点**：找双亲容易。
- **缺点**：找孩子需要遍历整个数组。

**2. 孩子表示法**：

```c
typedef struct CTNode {  // 孩子节点
    int child;           // 孩子节点在数组中的位置
    struct CTNode *next; // 下一个孩子
} *ChildPtr;

typedef struct {
    ElemType data;
    ChildPtr firstchild; // 第一个孩子
} CTBox;

typedef struct {
    CTBox nodes[MAX_TREE_SIZE];
    int n, r;            // 节点数和根的位置
} CTree;
```

**3. 孩子兄弟表示法（最重要）**：

```c
typedef struct CSNode {
    ElemType data;
    struct CSNode *firstchild, *nextsibling; // 第一个孩子和右兄弟
} CSNode, *CSTree;
```

- **特点**：左孩子右兄弟，将树转换为二叉树。
- **应用**：树与二叉树的转换、森林与二叉树的转换。

### 5.2 树与森林的遍历

**树的遍历**：

- **先根遍历**：根 → 子树（从左到右）。对应二叉树的**先序遍历**。
- **后根遍历**：子树（从左到右）→ 根。对应二叉树的**中序遍历**。

**森林的遍历**：

- **先序遍历森林** = 依次先序遍历每棵树 = 对应二叉树的**先序遍历**。
- **中序遍历森林** = 依次后序遍历每棵树 = 对应二叉树的**中序遍历**。

**考点提示**：

- 树转二叉树：左孩子右兄弟。
- 树的先根 ↔ 二叉树的先序；树的后根 ↔ 二叉树的中序。

---

## 6. 哈夫曼树与哈夫曼编码

- 对应视频：`5.5_1_哈夫曼树`

### 6.1 基本概念

- **路径长度**：从树根到节点的路径上的分支数。
- **带权路径长度 (WPL)**：$WPL = \sum_{i=1}^{n} w_i \cdot l_i$（叶子权值 × 路径长度）。
- **哈夫曼树**：WPL 最小的二叉树（也称最优二叉树）。

### 6.2 哈夫曼树的构造（重点）

**算法思想**：

1. 将 $n$ 个节点作为 $n$ 棵只有根节点的二叉树，构成森林 $F$。
2. 选取森林中根节点权值**最小**的两棵树作为新树的左右子树，新树根节点权值为两个孩子权值之和。
3. 从森林中删除被选中的两棵树，并将新树加入森林。
4. 重复步骤2、3，直到森林中只剩一棵树，即为哈夫曼树。

**C语言代码实现**：

```c
// 哈夫曼树节点定义
typedef struct {
    int weight;              // 权值
    int parent, lchild, rchild; // 双亲、左右孩子下标
} HTNode, *HuffmanTree;

// 构造哈夫曼树
void CreateHuffmanTree(HuffmanTree &HT, int n) {
    if(n <= 1) return;
    int m = 2 * n - 1;       // 哈夫曼树共有 2n-1 个节点
    HT = new HTNode[m + 1];  // 0号单元不用，HT[1...m]

    // 初始化
    for(int i = 1; i <= m; i++) {
        HT[i].parent = HT[i].lchild = HT[i].rchild = 0;
    }

    // 输入前n个节点的权值（1~n号位置存放叶子节点）
    for(int i = 1; i <= n; i++)
        cin >> HT[i].weight;

    // 创建哈夫曼树
    for(int i = n + 1; i <= m; i++) {  // 合并产生n-1个节点
        int s1, s2;
        Select(HT, i - 1, s1, s2);     // 在HT[1...i-1]中选权值最小的两个，下标为s1、s2
        HT[s1].parent = HT[s2].parent = i;
        HT[i].lchild = s1;
        HT[i].rchild = s2;
        HT[i].weight = HT[s1].weight + HT[s2].weight;
    }
}
```

### 6.3 哈夫曼编码

**C语言代码实现**：

```c
// 从叶子到根逆向求编码
void CreateHuffmanCode(HuffmanTree HT, HuffmanCode &HC, int n) {
    HC = new char*[n + 1];          // 分配n个字符编码的头指针
    char *cd = new char[n];         // 分配临时存放编码的动态数组
    cd[n - 1] = '\0';               // 编码结束符

    for(int i = 1; i <= n; i++) {   // 逐个求字符的哈夫曼编码
        int start = n - 1;          // start指向最后，从后向前逐位存放编码
        int c = i, f = HT[i].parent;

        while(f != 0) {             // 从叶子节点向上回溯，直到根节点
            --start;
            if(HT[f].lchild == c) cd[start] = '0'; // 左孩子编码0
            else cd[start] = '1';   // 右孩子编码1
            c = f;
            f = HT[f].parent;
        }

        HC[i] = new char[n - start];
        strcpy(HC[i], &cd[start]);  // 从start开始的编码串复制到HC
    }
    delete[] cd;
}
```

**哈夫曼编码的性质**：

- **前缀编码**：任一字符的编码都不是另一字符编码的前缀。
- **唯一可译**：可以无二义地解码。
- **最优性**：对于给定的权值集合，哈夫曼编码的平均码长最短。

**考点提示**：

- 手工构造哈夫曼树（选最小两个合并）。
- $n$ 个叶子节点的哈夫曼树有 $2n-1$ 个节点。
- 没有度为1的节点（$n_1 = 0$）。

---

## 7. 并查集 (Union-Find Set)

- 对应视频：`5.5_2_并查集`

### 7.1 基本概念

**并查集**用于处理不相交集合的**合并**和**查询**问题。

**基本操作**：

- `Find(x)`：查找元素 $x$ 所属集合的代表元（根节点）。
- `Union(x, y)`：合并 $x$ 和 $y$ 所在的集合。

### 7.2 并查集的存储结构

**双亲表示法**：

```c
#define SIZE 100
int parent[SIZE];  // parent[x] = x的双亲节点，根节点parent[x] = -1或x

// 初始化
void Initial(int S[], int n) {
    for(int i = 0; i < n; i++)
        S[i] = -1;  // 每个元素独立成一个集合
}
```

### 7.3 Find 操作（查找根节点）

**简单实现**：

```c
int Find(int S[], int x) {
    while(S[x] >= 0) x = S[x];  // 循环找根
    return x;
}
```

**路径压缩优化**（重要）：

```c
int Find(int S[], int x) {
    if(S[x] < 0) return x;      // 根节点
    else return S[x] = Find(S, S[x]); // 路径压缩：直接指向根节点
}
```

### 7.4 Union 操作（合并集合）

**简单实现**：

```c
void Union(int S[], int Root1, int Root2) {
    S[Root2] = Root1;  // 将Root2并入Root1
}
```

**按秩合并优化**（树高优化）：

```c
void Union(int S[], int Root1, int Root2) {
    if(S[Root2] > S[Root1]) {   // Root2的节点数更少（S[x]存负的节点数）
        S[Root1] += S[Root2];   // 累加节点总数
        S[Root2] = Root1;       // 小树并入大树
    } else {
        S[Root2] += S[Root1];
        S[Root1] = Root2;
    }
}
```

**考点提示**：

- 路径压缩可以将树高降低到接近常数。
- 时间复杂度：单次操作接近 $O(1)$，$m$ 次操作 $O(m \alpha(n))$，其中 $\alpha(n)$ 是 Ackermann 函数的反函数，增长极慢。

---

## 8. 重要考点与易错点总结

### 8.1 必背公式

- **二叉树**：$n_0 = n_2 + 1$。
- **完全二叉树**：
  - 节点 $i$ 的父节点：$\lfloor i/2 \rfloor$。
  - 左孩子：$2i$，右孩子：$2i+1$。
  - 高度：$h = \lceil \log_2(n+1) \rceil$。
- **哈夫曼树**：$n$ 个叶子 → $2n-1$ 个节点，$n_1 = 0$。

### 8.2 易错点

1. **遍历构造**：先序+后序无法唯一确定二叉树。
2. **线索二叉树**：中序线索化时，前驱后继的建立顺序。
3. **树的存储**：孩子兄弟表示法（左孩子右兄弟）是重点。
4. **哈夫曼树**：每次选权值**最小**的两个，不是度最小。

### 8.3 记忆口诀

- **遍历顺序**：先（根）左右，左中（根）右，左右后（根）。
- **树转二叉树**：左孩子右兄弟。
- **线索标志**：0 是孩子，1 是线索。
- **并查集优化**：路径压缩 + 按秩合并。
