> 来源：Obsidian/10-学业与考试/考研/数据结构/07.查找.md

# 第七章：查找 (Search)

## 1. 线性结构查找

### 1.1 顺序查找 (Sequential Search)

- 对应视频：`7.2_1_顺序查找和折半查找`
- **算法思想**：从表的一端开始，逐个比较关键字，直到找到或查找失败。
- **复杂度**：$O(n)$。$ASL_{成功} = (n+1)/2$，$ASL_{失败} = n$。
- **特点**：
  - 适用于**顺序表**和**链表**。
  - 表**无序**或**有序**均可。
  - 效率低，但对数据结构要求最低。

**C语言代码实现**：

```c
// 顺序查找（带哨兵）
int Search_Seq(SeqList L, ElemType key) {
    L.data[0] = key;                    // 哨兵，避免查找时每次都判断是否越界
    int i;
    for(i = L.length; L.data[i] != key; --i); // 从后往前查找
    return i;                           // 若返回0则查找失败
}
```

**考点提示**：

- 哨兵的作用是**减少循环内的判断次数**（不需要每次检查 `i >= 0`）。
- 顺序查找是**唯一适用于链表**的查找方法。

---

### 1.2 折半查找 (Binary Search)

- **算法思想**：在**有序顺序表**中，每次取中间元素比较，将查找区间缩小一半。
- **复杂度**：$O(\log n)$。$ASL_{成功} \approx \log_2(n+1) - 1$。
- **特点**：
  - **仅适用于有序顺序表**（需随机访问）。
  - 判定树为**平衡二叉树**。

**C语言代码实现**：

```c
// 折半查找（非递归）
int Binary_Search(SeqList L, ElemType key) {
    int low = 0, high = L.length - 1, mid;
    while(low <= high) {
        mid = (low + high) / 2;         // 取中间位置
        if(L.data[mid] == key)
            return mid;                 // 查找成功
        else if(L.data[mid] > key)
            high = mid - 1;             // 从前半部分继续查找
        else
            low = mid + 1;              // 从后半部分继续查找
    }
    return -1;                          // 查找失败
}

// 折半查找（递归）
int Binary_Search2(SeqList L, ElemType key, int low, int high) {
    if(low > high) return -1;           // 查找失败
    int mid = (low + high) / 2;
    if(L.data[mid] == key) return mid;
    else if(L.data[mid] > key)
        return Binary_Search2(L, key, low, mid-1);
    else
        return Binary_Search2(L, key, mid+1, high);
}
```

**考点提示**：

- 判定树中，**成功节点**在树中，**失败节点**在叶子的空指针处。
- 查找长度 = 判定树中节点所在层数（根节点层数为1）。

---

### 1.3 分块查找 (Block Search)

- 对应视频：`7.2_2_分块查找`
- **算法思想**：将表分为若干块，块间有序（前一块的最大值 < 后一块的最小值），块内无序。先在**索引表**中折半查找确定块，再在块内顺序查找。
- **复杂度**：$O(\sqrt{n})$（最优分块情况）。
- **特点**：性能介于顺序查找和折半查找之间，适合**动态插入**场景。

**C语言代码实现**：

```c
// 索引表结构
typedef struct {
    ElemType maxValue;  // 块的最大关键字
    int low, high;      // 块的起始和结束位置
} Index;

// 分块查找
int Block_Search(SeqList L, Index idx[], int b, ElemType key) {
    // b为块的个数
    int i = 0;
    // 在索引表中顺序查找（也可用折半查找）
    while(i < b && key > idx[i].maxValue) i++;
    if(i >= b) return -1;  // 大于所有块的最大值

    // 在块内顺序查找
    for(int j = idx[i].low; j <= idx[i].high; j++) {
        if(L.data[j] == key) return j;
    }
    return -1;  // 查找失败
}
```

## 2. 树形结构查找

### 2.1 二叉排序树 (BST, Binary Search Tree)

- 对应视频：`7.3_1_二叉排序树`
- **定义**：左子树所有节点 < 根节点 < 右子树所有节点。
- **性质**：中序遍历得到**递增有序序列**。
- **复杂度**：平均 $O(\log n)$，最坏 $O(n)$（退化为单支树）。

**C语言代码实现**：

```c
// 二叉排序树节点定义
typedef struct BSTNode {
    ElemType data;
    struct BSTNode *lchild, *rchild;
} BSTNode, *BSTree;

// BST 查找（递归）
BSTNode* BST_Search(BSTree T, ElemType key) {
    if(T == NULL) return NULL;              // 查找失败
    if(key == T->data) return T;            // 查找成功
    else if(key < T->data)
        return BST_Search(T->lchild, key);  // 在左子树查找
    else
        return BST_Search(T->rchild, key);  // 在右子树查找
}

// BST 插入
int BST_Insert(BSTree &T, ElemType key) {
    if(T == NULL) {                         // 找到插入位置，插入新节点
        T = (BSTree)malloc(sizeof(BSTNode));
        T->data = key;
        T->lchild = T->rchild = NULL;
        return 1;                           // 插入成功
    }
    else if(key == T->data) return 0;       // 关键字已存在，插入失败
    else if(key < T->data)
        return BST_Insert(T->lchild, key);  // 插入到左子树
    else
        return BST_Insert(T->rchild, key);  // 插入到右子树
}

// BST 删除（重点、难点）
int BST_Delete(BSTree &T, ElemType key) {
    if(T == NULL) return 0;                 // 未找到，删除失败
    if(key < T->data)
        return BST_Delete(T->lchild, key);  // 在左子树删除
    else if(key > T->data)
        return BST_Delete(T->rchild, key);  // 在右子树删除
    else {  // 找到待删除节点
        if(T->lchild == NULL) {             // 左子树为空，右子树顶替
            BSTNode *temp = T;
            T = T->rchild;
            free(temp);
        }
        else if(T->rchild == NULL) {        // 右子树为空，左子树顶替
            BSTNode *temp = T;
            T = T->lchild;
            free(temp);
        }
        else {  // 左右子树都存在
            // 找到右子树的最小节点（中序后继）
            BSTNode *s = T->rchild;
            while(s->lchild != NULL) s = s->lchild;
            T->data = s->data;              // 用后继值替换当前节点
            BST_Delete(T->rchild, s->data); // 删除后继节点
        }
        return 1;
    }
}
```

**考点提示**：

- **删除操作**有三种情况：
  1. 叶子节点：直接删除。
  2. 只有一个孩子：孩子顶替该节点。
  3. 有两个孩子：用**中序前驱**（左子树最大）或**中序后继**（右子树最小）替换。

---

### 2.2 平衡二叉树 (AVL Tree)

- 对应视频：`7.3_2_平衡二叉树`
- **定义**：任意节点的左右子树高度差（平衡因子）的绝对值 $\le 1$。
- **调整**：通过**旋转**恢复平衡。四种情况：**LL**、**RR**、**LR**、**RL**。
- **复杂度**：$O(\log n)$。

**C语言代码实现（旋转操作）**：

```c
// AVL 树节点定义
typedef struct AVLNode {
    ElemType data;
    int height;                     // 节点高度
    struct AVLNode *lchild, *rchild;
} AVLNode, *AVLTree;

// 获取节点高度
int getHeight(AVLNode *T) {
    return T == NULL ? 0 : T->height;
}

// LL 型调整（右旋）
void R_Rotate(AVLTree &T) {
    AVLNode *L = T->lchild;
    T->lchild = L->rchild;
    L->rchild = T;
    T->height = max(getHeight(T->lchild), getHeight(T->rchild)) + 1;
    L->height = max(getHeight(L->lchild), getHeight(L->rchild)) + 1;
    T = L;  // 更新根节点
}

// RR 型调整（左旋）
void L_Rotate(AVLTree &T) {
    AVLNode *R = T->rchild;
    T->rchild = R->lchild;
    R->lchild = T;
    T->height = max(getHeight(T->lchild), getHeight(T->rchild)) + 1;
    R->height = max(getHeight(R->lchild), getHeight(R->rchild)) + 1;
    T = R;  // 更新根节点
}

// LR 型调整（先左旋后右旋）
void LR_Rotate(AVLTree &T) {
    L_Rotate(T->lchild);  // 先对左孩子左旋
    R_Rotate(T);          // 再对根右旋
}

// RL 型调整（先右旋后左旋）
void RL_Rotate(AVLTree &T) {
    R_Rotate(T->rchild);  // 先对右孩子右旋
    L_Rotate(T);          // 再对根左旋
}
```

**考点提示**：

- **旋转判断口诀**：
  - **LL**（左孩子的左子树太高）：右旋。
  - **RR**（右孩子的右子树太高）：左旋。
  - **LR**（左孩子的右子树太高）：先左旋左孩子，再右旋根。
  - **RL**（右孩子的左子树太高）：先右旋右孩子，再左旋根。

---

### 2.3 B 树与 B+ 树

- 对应视频：`7.3_3_B树和B+树`
- **B 树**：$m$ 阶 B 树，每个节点最多 $m$ 个孩子，关键字数 $\lceil m/2 \rceil - 1 \le n \le m-1$。
- **B+ 树**：所有数据在叶子节点，叶子节点链成链表，适合**范围查询**。
- **应用**：数据库索引（MySQL 的 InnoDB 引擎使用 B+ 树）。

## 3. 散列结构 (Hash Table)

- 对应视频：`7.4_1_散列查找`、`7.4_2_散列查找(下)`
- **基本思想**：通过散列函数 $H(key)$ 直接计算出元素的存储地址，实现 $O(1)$ 查找。
- **散列函数**：
  - **除留余数法**（最常用）：$H(key) = key \% p$（$p$ 为不大于 $m$ 的最大质数）。
  - 直接定址法、平方取中法、数字分析法。
- **冲突处理**：不同关键字映射到同一地址。

### 3.1 开放定址法

**思想**：发生冲突时，按某种探测序列寻找下一个空位置。

#### (1) 线性探测法

- **探测序列**：$d_i = 0, 1, 2, 3, ..., m-1$。
- **优点**：实现简单。
- **缺点**：容易产生**堆积**（连续占用的位置越来越长）。

**C语言代码实现**：

```c
#define m 13  // 散列表长度（质数）

// 线性探测法插入
int Hash_Insert_Linear(int HT[], ElemType key) {
    int addr = key % m;  // 散列函数
    // 线性探测找空位
    while(HT[addr] != EMPTY) {  // EMPTY表示空位标记
        addr = (addr + 1) % m;  // 线性探测下一位置
    }
    HT[addr] = key;
    return addr;
}

// 线性探测法查找
int Hash_Search_Linear(int HT[], ElemType key) {
    int addr = key % m;
    while(HT[addr] != EMPTY && HT[addr] != key) {
        addr = (addr + 1) % m;
        if(addr == key % m) return -1;  // 循环一圈仍未找到
    }
    if(HT[addr] == key) return addr;    // 查找成功
    return -1;                          // 查找失败
}
```

#### (2) 平方探测法

- **探测序列**：$d_i = 0, 1^2, -1^2, 2^2, -2^2, ..., k^2, -k^2$（$k \le m/2$）。
- **优点**：避免堆积。
- **缺点**：不能探测到所有位置（散列表长度 $m$ 必须是质数）。

**C语言代码实现**：

```c
// 平方探测法插入
int Hash_Insert_Quad(int HT[], ElemType key) {
    int addr = key % m;
    int i = 0;
    while(HT[addr] != EMPTY) {
        i++;
        addr = (key % m + i * i) % m;  // 平方探测
        if(i > m/2) return -1;         // 探测失败
    }
    HT[addr] = key;
    return addr;
}
```

### 3.2 拉链法 (Separate Chaining)

**思想**：将所有同义词（散列到同一地址的关键字）存储在一个**链表**中。

**C语言代码实现**：

```c
// 拉链法节点定义
typedef struct Node {
    ElemType data;
    struct Node *next;
} Node, *LinkList;

LinkList HT[m];  // 散列表（m个链表头指针）

// 拉链法插入
void Hash_Insert_Chain(ElemType key) {
    int addr = key % m;  // 散列函数
    // 头插法插入链表
    Node *s = (Node*)malloc(sizeof(Node));
    s->data = key;
    s->next = HT[addr];
    HT[addr] = s;
}

// 拉链法查找
Node* Hash_Search_Chain(ElemType key) {
    int addr = key % m;
    Node *p = HT[addr];
    while(p != NULL && p->data != key) {
        p = p->next;
    }
    return p;  // 返回节点指针，NULL表示未找到
}
```

### 3.3 性能分析

- **装填因子**：$\alpha = n/m$（$n$ 为元素个数，$m$ 为表长）。
- **查找效率**：与 $\alpha$ 有关，与 $n$ 无关。
- **经验值**：$\alpha \le 0.75$ 时性能较好。

**考点提示**：

- **开放定址法**要求 $\alpha < 1$（必须有空位）。
- **拉链法** $\alpha$ 可以 $\ge 1$（链表可以无限延长）。
- 删除操作：开放定址法不能直接删除（需要**伪删除标记**），拉链法可直接删除。

## 5. 重要考点与总结

### 5.1 查找算法对比表

| 查找方法     | 平均时间复杂度 | 空间复杂度 | 适用条件                   | 特点           |
| :----------- | :------------- | :--------- | :------------------------- | :------------- |
| **顺序查找** | $O(n)$         | $O(1)$     | 无序/有序均可，链表/顺序表 | 通用性强       |
| **折半查找** | $O(\log n)$    | $O(1)$     | **有序顺序表**             | 不适用链表     |
| **分块查找** | $O(\sqrt{n})$  | $O(b)$     | 块间有序，块内无序         | 适合动态       |
| **BST**      | $O(\log n)$    | $O(n)$     | 动态集合                   | 最坏 $O(n)$    |
| **AVL**      | $O(\log n)$    | $O(n)$     | 动态集合                   | 严格平衡       |
| **B 树**     | $O(\log n)$    | $O(n)$     | 大规模外存                 | 多路平衡       |
| **散列表**   | $O(1)$         | $O(m)$     | 无序集合                   | 不支持范围查询 |

### 5.2 易错点与陷阱

1. **折半查找**：
   - 只能用于**有序顺序表**，不能用于链表（无随机访问）。
   - 判定树中，查找失败在**叶子节点的空指针**处。
2. **BST 删除**：
   - 有两个孩子时，用**中序前驱**或**中序后继**替换（考试常考手画过程）。
3. **AVL 旋转**：
   - **LR** 和 **RL** 需要**两次旋转**，顺序不能错。
4. **散列表**：
   - **线性探测**易堆积，**平方探测**要求表长为质数。
   - **开放定址法**删除需要**伪删除**标记（不能直接删除）。
   - **拉链法** $\alpha$ 可 $> 1$，开放定址法 $\alpha < 1$。

### 5.3 记忆口诀

- **查找效率排序**：散列 > 平衡树 > 折半 > 分块 > 顺序。
- **BST vs AVL**：BST 最坏退化为链（$O(n)$），AVL 严格平衡（$O(\log n)$）。
- **B+ 树特点**：数据全在叶，叶子连成链，适合范围查（数据库）。
