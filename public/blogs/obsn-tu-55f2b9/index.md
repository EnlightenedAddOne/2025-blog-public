> 来源：Obsidian/10-学业与考试/考研/数据结构/06.图.md

# 第六章：图 (Graph)

## 1. 图的基本概念

- 对应视频：`6.1_1_图的基本概念`

### 1.1 图的定义

**图 (Graph)** $G = (V, E)$：

- $V$：顶点 (Vertex) 的有穷非空集合。
- $E$：边 (Edge) 的有穷集合。

### 1.2 图的分类

- **无向图**：边没有方向，$(v_i, v_j) = (v_j, v_i)$。
- **有向图**：边有方向，$<v_i, v_j> \neq <v_j, v_i>$（弧）。
- **完全图**：
  - 无向完全图：$n$ 个顶点有 $\frac{n(n-1)}{2}$ 条边。
  - 有向完全图：$n$ 个顶点有 $n(n-1)$ 条弧。
- **稀疏图 vs 稠密图**：边数 $e < n \log n$ 为稀疏图。

### 1.3 度、路径与连通性

- **度 (Degree)**：
  - 无向图：与顶点相连的边数。
  - 有向图：入度 (ID) + 出度 (OD)。
  - **握手定理**：$\sum_{i=1}^{n} d_i = 2e$（度数和 = 2倍边数）。
- **路径**：顶点序列 $v_p, v_{i_1}, v_{i_2}, ..., v_q$。
  - **简单路径**：顶点不重复。
  - **回路/环**：第一个和最后一个顶点相同。
- **连通性**：
  - **连通图**（无向图）：任意两顶点都有路径。
  - **强连通图**（有向图）：任意两顶点双向都有路径。
  - **连通分量**：极大连通子图。

---

## 2. 图的存储结构

- 对应视频：`6.2_1_邻接矩阵`、`6.2_2_邻接表`

### 2.1 邻接矩阵 (Adjacency Matrix)

**存储方式**：二维数组 $A[i][j]$。

- 无向图：$A[i][j] = 1$ 表示存在边 $(v_i, v_j)$，对称矩阵。
- 有向图：$A[i][j] = 1$ 表示存在弧 $<v_i, v_j>$。
- 带权图：$A[i][j] = w_{ij}$（权值），无边则为 $\infty$ 或 0。

**C语言代码实现**：

```c
#define MaxVertexNum 100  // 最大顶点数
typedef char VertexType;  // 顶点类型
typedef int EdgeType;     // 边的权值类型

typedef struct {
    VertexType Vex[MaxVertexNum];          // 顶点表
    EdgeType Edge[MaxVertexNum][MaxVertexNum]; // 邻接矩阵，边表
    int vexnum, arcnum;                    // 图的当前顶点数和弧数
} MGraph;
```

**特点**：

- **优点**：
  - 容易判断两顶点间是否有边：$O(1)$。
  - 适合稠密图。
  - 方便计算顶点的度：第 $i$ 行非零元素个数。
- **缺点**：
  - 空间复杂度 $O(V^2)$，稀疏图浪费空间。
  - 遍历需要 $O(V^2)$ 时间。
- **唯一性**：邻接矩阵表示唯一。

### 2.2 邻接表 (Adjacency List)

**存储方式**：顶点表 + 边表（链表）。

- 顶点表：数组，存储顶点信息和指向第一条边的指针。
- 边表：链表，存储与该顶点相邻的所有顶点。

**C语言代码实现**：

```c
// 边表节点
typedef struct ArcNode {
    int adjvex;              // 该弧所指向的顶点位置
    struct ArcNode *next;    // 指向下一条弧的指针
    // int weight;           // 若为带权图，可加权值域
} ArcNode;

// 顶点表节点
typedef struct VNode {
    VertexType data;         // 顶点信息
    ArcNode *first;          // 指向第一条依附该顶点的弧
} VNode, AdjList[MaxVertexNum];

// 邻接表
typedef struct {
    AdjList vertices;        // 邻接表
    int vexnum, arcnum;      // 图的顶点数和弧数
} ALGraph;
```

**特点**：

- **优点**：
  - 节省空间：$O(V + E)$。
  - 适合稀疏图。
  - 方便找所有邻接点。
- **缺点**：
  - 判断两顶点是否有边需要遍历链表：$O(V)$。
  - 计算度（有向图的入度）不方便。
- **唯一性**：邻接表表示不唯一（链表顺序任意）。

### 2.3 十字链表（有向图）

**目的**：解决有向图的邻接表难以求入度的问题。

**C语言代码实现**：

```c
// 弧节点
typedef struct ArcBox {
    int tailvex, headvex;    // 弧尾、弧头顶点位置
    struct ArcBox *hlink, *tlink; // 弧头相同、弧尾相同的下一条弧
    // int weight;           // 权值
} ArcBox;

// 顶点节点
typedef struct VexNode {
    VertexType data;
    ArcBox *firstin, *firstout; // 第一条入弧和出弧
} VexNode;

typedef struct {
    VexNode xlist[MaxVertexNum];
    int vexnum, arcnum;
} OLGraph;
```

### 2.4 邻接多重表（无向图）

**目的**：便于操作无向图的边（如删除边）。

**C语言代码实现**：

```c
// 边节点
typedef struct EBox {
    int ivex, jvex;          // 边的两个顶点
    struct EBox *ilink, *jlink; // 分别指向依附这两个顶点的下一条边
} EBox;

// 顶点节点
typedef struct VexBox {
    VertexType data;
    EBox *firstedge;         // 指向第一条依附该顶点的边
} VexBox;

typedef struct {
    VexBox adjmulist[MaxVertexNum];
    int vexnum, edgenum;
} AMLGraph;
```

---

## 3. 图的遍历

- 对应视频：`6.3_1_图的广度优先遍历(BFS)`、`6.3_2_图的深度优先遍历(DFS)`

### 3.1 广度优先搜索 (BFS)

**算法思想**：类似树的层序遍历，使用**队列**。

1. 访问起始顶点 $v$，标记为已访问，入队。
2. 队列不空时，出队一个顶点，访问其所有未访问的邻接点，标记并入队。
3. 重复步骤2，直到队列为空。

**C语言代码实现**：

```c
bool visited[MaxVertexNum];  // 访问标记数组

// 广度优先遍历
void BFSTraverse(Graph G) {
    for(int i = 0; i < G.vexnum; ++i)
        visited[i] = false;  // 初始化未访问标记
    InitQueue(Q);            // 初始化辅助队列Q
    for(int i = 0; i < G.vexnum; ++i) {  // 对每个连通分量
        if(!visited[i])      // 若未访问，则从该顶点开始BFS
            BFS(G, i);
    }
}

// 从顶点v出发，广度优先遍历图G
void BFS(Graph G, int v) {
    visit(v);                // 访问初始顶点v
    visited[v] = true;       // 对v做已访问标记
    EnQueue(Q, v);           // 顶点v入队列Q
    while(!isEmpty(Q)) {
        DeQueue(Q, v);       // 顶点v出队列
        // 检测v的所有邻接点
        for(w = FirstNeighbor(G, v); w >= 0; w = NextNeighbor(G, v, w)) {
            if(!visited[w]) {     // w为v的尚未访问的邻接顶点
                visit(w);         // 访问顶点w
                visited[w] = true;// 对w做已访问标记
                EnQueue(Q, w);    // 顶点w入队列
            }
        }
    }
}
```

**BFS 求单源最短路径**（无权图）：

```c
// 求从顶点u到其他顶点的最短路径
void BFS_MIN_Distance(Graph G, int u) {
    int d[MaxVertexNum];     // d[i]表示从u到i的最短路径长度
    int path[MaxVertexNum];  // path[i]表示从u到i的路径上i的前驱

    for(int i = 0; i < G.vexnum; i++) {
        d[i] = -1;           // 初始化路径长度为-1（未访问）
        path[i] = -1;        // 初始化前驱为-1
    }

    d[u] = 0;
    visited[u] = true;
    EnQueue(Q, u);

    while(!isEmpty(Q)) {
        DeQueue(Q, u);
        for(w = FirstNeighbor(G, u); w >= 0; w = NextNeighbor(G, u, w)) {
            if(!visited[w]) {
                visited[w] = true;
                d[w] = d[u] + 1;    // 路径长度+1
                path[w] = u;        // 记录前驱
                EnQueue(Q, w);
            }
        }
    }
}
```

**复杂度**：

- 邻接矩阵：$O(V^2)$。
- 邻接表：$O(V + E)$。

### 3.2 深度优先搜索 (DFS)

**算法思想**：类似树的先序遍历，使用**递归**或**栈**。

1. 访问起始顶点 $v$，标记为已访问。
2. 递归访问 $v$ 的未访问的邻接点。

**C语言代码实现**：

```c
// 深度优先遍历
void DFSTraverse(Graph G) {
    for(int v = 0; v < G.vexnum; ++v)
        visited[v] = false;  // 初始化已访问标记数组
    for(int v = 0; v < G.vexnum; ++v)
        if(!visited[v])
            DFS(G, v);       // 对每个连通分量调用一次DFS
}

// 从顶点v出发，深度优先遍历图G
void DFS(Graph G, int v) {
    visit(v);                // 访问顶点v
    visited[v] = true;       // 设已访问标记
    for(w = FirstNeighbor(G, v); w >= 0; w = NextNeighbor(G, v, w)) {
        if(!visited[w]) {    // w为v的尚未访问的邻接顶点
            DFS(G, w);       // 递归访问
        }
    }
}
```

**非递归实现（栈）**：

```c
void DFS_Non_Recursive(Graph G, int v) {
    InitStack(S);
    Push(S, v);
    visited[v] = true;
    visit(v);

    while(!IsEmpty(S)) {
        int flag = 0;        // 标记是否有未访问的邻接点
        GetTop(S, v);        // 取栈顶元素（不出栈）

        for(w = FirstNeighbor(G, v); w >= 0; w = NextNeighbor(G, v, w)) {
            if(!visited[w]) {
                Push(S, w);
                visited[w] = true;
                visit(w);
                flag = 1;
                break;       // 找到一个未访问的邻接点即跳出
            }
        }

        if(flag == 0)        // 所有邻接点都已访问
            Pop(S, v);
    }
}
```

**复杂度**：

- 邻接矩阵：$O(V^2)$。
- 邻接表：$O(V + E)$。

**考点提示**：

- BFS 可求**单源最短路径**（无权图）。
- DFS 可判断图是否有环、求连通分量。
- 遍历序列**不唯一**（取决于邻接点顺序）。

---

## 4. 最小生成树 (Minimum Spanning Tree, MST)

- 对应视频：`6.4_1_最小生成树`

### 4.1 基本概念

**生成树**：包含图中全部顶点的一个极小连通子图（$n$ 个顶点，$n-1$ 条边）。

**最小生成树**：带权连通无向图中，边的权值之和最小的生成树。

**性质**：

- $n$ 个顶点的连通图的生成树有 $n-1$ 条边。
- 若砍去一条边，则会变成非连通图。
- 若加上一条边，则会形成回路。

### 4.2 Prim 算法（普里姆算法）

**算法思想**：从某一顶点开始，逐步扩展生成树。

1. 初始化：选择一个起始顶点 $v_0$，集合 $U = \{v_0\}$。
2. 重复：从 $U$ 到 $V-U$ 中选择权值**最小**的边 $(u, v)$，将 $v$ 加入 $U$。
3. 直到 $U$ 包含所有顶点。

**C语言代码实现**：

```c
// Prim算法：从顶点u开始构造最小生成树
void Prim(MGraph G, int u) {
    int lowcost[MaxVertexNum];  // 顶点集U到V-U的最短边的权值
    int closest[MaxVertexNum];  // 最短边在U中的顶点
    bool visited[MaxVertexNum]; // 标记顶点是否在U中

    // 初始化
    for(int i = 0; i < G.vexnum; i++) {
        lowcost[i] = G.Edge[u][i];  // 初始化为u到其他顶点的权值
        closest[i] = u;              // 初始化最短边的起点为u
        visited[i] = false;
    }
    visited[u] = true;

    // 找剩余n-1个顶点
    for(int i = 1; i < G.vexnum; i++) {
        int min = INF, k = -1;

        // 找到未访问顶点中lowcost最小的顶点k
        for(int j = 0; j < G.vexnum; j++) {
            if(!visited[j] && lowcost[j] < min) {
                min = lowcost[j];
                k = j;
            }
        }

        visited[k] = true;           // 将k加入集合U
        // 输出边：(closest[k], k)，权值为lowcost[k]

        // 更新lowcost和closest
        for(int j = 0; j < G.vexnum; j++) {
            if(!visited[j] && G.Edge[k][j] < lowcost[j]) {
                lowcost[j] = G.Edge[k][j];
                closest[j] = k;
            }
        }
    }
}
```

**复杂度**：$O(V^2)$（适合稠密图）。

### 4.3 Kruskal 算法（克鲁斯卡尔算法）

**算法思想**：按边的权值从小到大选择，不形成回路。

1. 初始化：每个顶点自成一个连通分量。
2. 按权值递增顺序选择边 $(u, v)$：
   - 若 $u$ 和 $v$ 属于不同连通分量，则加入生成树，合并连通分量。
   - 否则舍弃该边。
3. 直到选出 $n-1$ 条边。

**C语言代码实现**：

```c
// 边的定义
typedef struct {
    int u, v;      // 边的两个顶点
    int weight;    // 边的权值
} Edge;

// Kruskal算法
void Kruskal(Graph G) {
    Edge edges[MaxEdgeNum];  // 存储所有边
    int parent[MaxVertexNum];// 并查集

    // 初始化并查集
    for(int i = 0; i < G.vexnum; i++)
        parent[i] = -1;

    // 将所有边按权值排序（省略排序代码）
    Sort(edges, G.arcnum);

    int count = 0;  // 已选边数
    for(int i = 0; i < G.arcnum && count < G.vexnum - 1; i++) {
        int u = edges[i].u, v = edges[i].v;
        int root1 = Find(parent, u);  // 找u所在集合的根
        int root2 = Find(parent, v);  // 找v所在集合的根

        if(root1 != root2) {          // 不在同一连通分量
            // 输出边：(u, v)，权值为edges[i].weight
            Union(parent, root1, root2); // 合并两个集合
            count++;
        }
    }
}

// 并查集的Find操作
int Find(int parent[], int x) {
    if(parent[x] < 0) return x;
    return parent[x] = Find(parent, parent[x]);  // 路径压缩
}

// 并查集的Union操作
void Union(int parent[], int root1, int root2) {
    parent[root1] = root2;  // 简单合并
}
```

**复杂度**：$O(E \log E)$（适合稀疏图）。

**考点提示**：

- **Prim**：归并顶点，从顶点出发，适合稠密图。
- **Kruskal**：归并边，从边出发，适合稀疏图。
- 两种算法都使用**贪心策略**。

---

## 5. 最短路径

- 对应视频：`6.4_2_最短路径问题_BFS算法`、`6.4_3_最短路径问题_Dijkstra算法`、`6.4_4_最短路径问题_Floyd算法`

### 5.1 Dijkstra 算法（迪杰斯特拉算法）

**问题**：求带权有向图中某个源点到其余各顶点的最短路径（**单源最短路径**）。

**限制**：不能有**负权边**。

**算法思想**：贪心策略，类似 Prim 算法。

1. 初始化：源点 $v_0$ 到自己的距离为0，到其他顶点的距离为边权（无边则为 $\infty$）。
2. 选择未确定最短路径的顶点中，距离源点最近的顶点 $u$，确定其最短路径。
3. 更新：通过 $u$ 更新其他顶点的最短距离。
4. 重复步骤2、3，直到所有顶点的最短路径都确定。

**C语言代码实现**：

```c
// Dijkstra算法：求顶点u到其他顶点的最短路径
void Dijkstra(MGraph G, int u) {
    int dist[MaxVertexNum];   // 源点u到各顶点的最短路径长度
    int path[MaxVertexNum];   // 路径上的前驱
    bool visited[MaxVertexNum]; // 标记是否已找到最短路径

    // 初始化
    for(int i = 0; i < G.vexnum; i++) {
        dist[i] = G.Edge[u][i];   // 初始化为u到i的边权
        visited[i] = false;
        if(dist[i] < INF)
            path[i] = u;          // 若u和i相邻，前驱为u
        else
            path[i] = -1;         // 否则无前驱
    }
    dist[u] = 0;
    visited[u] = true;

    // 找剩余n-1个顶点的最短路径
    for(int i = 1; i < G.vexnum; i++) {
        int min = INF, k = -1;

        // 找到未访问顶点中dist最小的顶点k
        for(int j = 0; j < G.vexnum; j++) {
            if(!visited[j] && dist[j] < min) {
                min = dist[j];
                k = j;
            }
        }

        visited[k] = true;        // 将k的最短路径确定

        // 更新dist和path
        for(int j = 0; j < G.vexnum; j++) {
            if(!visited[j] && dist[k] + G.Edge[k][j] < dist[j]) {
                dist[j] = dist[k] + G.Edge[k][j];  // 更新最短路径长度
                path[j] = k;                       // 更新前驱
            }
        }
    }
}
```

**复杂度**：$O(V^2)$（使用堆优化可达 $O((V+E) \log V)$）。

### 5.2 Floyd 算法（弗洛伊德算法）

**问题**：求所有顶点对之间的最短路径（**多源最短路径**）。

**限制**：允许**负权边**，但不允许**负权环**。

**算法思想**：动态规划。

- $A^{(k)}[i][j]$：从 $v_i$ 到 $v_j$，只经过编号 $\le k$ 的顶点的最短路径长度。
- 状态转移：$A^{(k)}[i][j] = \min\{A^{(k-1)}[i][j], A^{(k-1)}[i][k] + A^{(k-1)}[k][j]\}$。

**C语言代码实现**：

```c
// Floyd算法：求所有顶点对的最短路径
void Floyd(MGraph G) {
    int A[MaxVertexNum][MaxVertexNum];  // 最短路径长度
    int path[MaxVertexNum][MaxVertexNum]; // 路径上的中转点

    // 初始化
    for(int i = 0; i < G.vexnum; i++) {
        for(int j = 0; j < G.vexnum; j++) {
            A[i][j] = G.Edge[i][j];
            path[i][j] = -1;  // 初始无中转点
        }
    }

    // 逐步考虑以k为中转点
    for(int k = 0; k < G.vexnum; k++) {
        for(int i = 0; i < G.vexnum; i++) {
            for(int j = 0; j < G.vexnum; j++) {
                if(A[i][k] + A[k][j] < A[i][j]) {
                    A[i][j] = A[i][k] + A[k][j];  // 更新最短路径
                    path[i][j] = k;               // 记录中转点
                }
            }
        }
    }
}
```

**复杂度**：$O(V^3)$。

**考点提示**：

- **Dijkstra**：单源，不能有负权边，$O(V^2)$。
- **Floyd**：多源，允许负权边，$O(V^3)$。
- **BFS**：无权图的单源最短路径，$O(V+E)$。

---

## 6. 拓扑排序与关键路径

- 对应视频：`6.4_6_拓扑排序`、`6.4_7_关键路径`

### 6.1 AOV 网与拓扑排序

**AOV 网 (Activity On Vertex)**：用顶点表示活动，有向边表示活动间的优先关系。

**拓扑排序**：将 AOV 网中的顶点排成一个线性序列，使得对于任意一条边 $<v_i, v_j>$，$v_i$ 都在 $v_j$ 之前。

**算法思想**：

1. 选择一个入度为 0 的顶点并输出。
2. 删除该顶点及其所有出边。
3. 重复步骤1、2，直到所有顶点输出或不存在入度为 0 的顶点（有环）。

**C语言代码实现**：

```c
// 拓扑排序
bool TopologicalSort(Graph G) {
    InitStack(S);
    int indegree[MaxVertexNum];  // 入度数组

    // 统计各顶点入度
    for(int i = 0; i < G.vexnum; i++)
        indegree[i] = 0;
    for(int i = 0; i < G.vexnum; i++) {
        for(ArcNode *p = G.vertices[i].first; p; p = p->next)
            indegree[p->adjvex]++;
    }

    // 将入度为0的顶点入栈
    for(int i = 0; i < G.vexnum; i++)
        if(indegree[i] == 0)
            Push(S, i);

    int count = 0;  // 记录输出顶点数
    while(!IsEmpty(S)) {
        Pop(S, i);
        print[count++] = i;  // 输出顶点i

        // 将i的所有邻接点的入度减1
        for(ArcNode *p = G.vertices[i].first; p; p = p->next) {
            int v = p->adjvex;
            if(--indegree[v] == 0)  // 入度减为0，入栈
                Push(S, v);
        }
    }

    if(count < G.vexnum)
        return false;  // 排序失败，有回路
    else
        return true;
}
```

**复杂度**：$O(V + E)$。

### 6.2 AOE 网与关键路径

**AOE 网 (Activity On Edge)**：用边表示活动，权值表示活动持续时间，顶点表示事件。

**关键路径**：从源点到汇点的**最长路径**（决定整个工程的最短完成时间）。

**关键活动**：关键路径上的活动，其延误会导致整个工程延误。

**相关概念**：

- **事件 $v_k$ 的最早发生时间** $ve(k)$：从源点到 $v_k$ 的最长路径长度。
- **事件 $v_k$ 的最迟发生时间** $vl(k)$：不影响工程完成的最迟时间。
- **活动 $a_i$ 的最早开始时间** $e(i)$：$e(i) = ve(k)$（$a_i$ 的起点为 $v_k$）。
- **活动 $a_i$ 的最迟开始时间** $l(i)$：$l(i) = vl(j) - w_{ki}$（$a_i$ 的终点为 $v_j$，权值为 $w_{ki}$）。
- **活动 $a_i$ 的时间余量** $d(i) = l(i) - e(i)$。

**关键活动**：$d(i) = 0$ 的活动。

**算法步骤**：

1. 拓扑排序，求 $ve(k)$。
2. 逆拓扑排序，求 $vl(k)$。
3. 计算 $e(i)$ 和 $l(i)$，找出 $d(i) = 0$ 的活动。

**考点提示**：

- **拓扑排序**：判断有向图是否有环。
- **关键路径**：最长路径，决定工程最短工期。
- 缩短关键活动时间可缩短工期，但可能产生新的关键路径。

---

## 7. 核心算法复杂度对比（必考总结）

| 算法             | 邻接矩阵 | 邻接表             | 备注                   |
| :--------------- | :------- | :----------------- | :--------------------- |
| **BFS / DFS**    | $O(V^2)$ | $O(V+E)$           | 矩阵遍历需扫描整行     |
| **Prim 算法**    | $O(V^2)$ | $O(E \log V)$ (堆) | 矩阵适合稠密图         |
| **Kruskal 算法** | -        | $O(E \log E)$      | 适合稀疏图             |
| **Dijkstra**     | $O(V^2)$ | $O(E \log V)$ (堆) | 类似 Prim，无负权边    |
| **Floyd**        | $O(V^3)$ | -                  | 只能用矩阵，允许负权边 |
| **拓扑排序**     | $O(V^2)$ | $O(V+E)$           | 需维护入度表           |

> **注**：$V$ 为顶点数，$E$ 为边数。

---

## 8. 重要考点与易错点总结

### 8.1 必背公式

- **握手定理**：$\sum d_i = 2e$（无向图）；$\sum ID = \sum OD = e$（有向图）。
- **完全图边数**：无向 $\frac{n(n-1)}{2}$，有向 $n(n-1)$。
- **生成树**：$n$ 个顶点，$n-1$ 条边。
- **连通分量数**：DFS/BFS 调用次数。

### 8.2 易错点

1. **邻接矩阵 vs 邻接表**：
   - 矩阵唯一，表不唯一。
   - 矩阵适合稠密图，表适合稀疏图。
2. **BFS vs DFS**：
   - BFS 用队列，DFS 用栈/递归。
   - BFS 求无权图最短路径。
3. **Prim vs Kruskal**：
   - Prim 归并点，Kruskal 归并边。
   - Prim 适合稠密图，Kruskal 适合稀疏图。
4. **Dijkstra vs Floyd**：
   - Dijkstra 单源，Floyd 多源。
   - Dijkstra 不能有负权边，Floyd 允许负权边（无负权环）。
5. **拓扑排序**：
   - 判断有环：输出顶点数 < 总顶点数。
   - 拓扑序列不唯一。
6. **关键路径**：
   - 最长路径，不是最短路径。
   - 关键活动：$e(i) = l(i)$。

### 8.3 记忆口诀

- **图的遍历**：BFS 队列层层访，DFS 递归深探险。
- **最小生成树**：Prim 加点选最小，Kruskal 加边不成环。
- **最短路径**：Dijkstra 单源贪心选，Floyd 多源动态算。
- **拓扑关键**：拓扑入度删顶点，关键最长定工期。
