> 来源：Obsidian/10-学业与考试/考研/wangdao-data-structure-main/ch6/applications/图的应用.md

# 图的应用

## 1. 最小生成树

### 1.1. 概念

![最小生成树1](/blogs/obsn-tu-de-ying-yong/mst1.jpg)

![最小生成树2](/blogs/obsn-tu-de-ying-yong/mst2.jpg)

![最小生成树3](/blogs/obsn-tu-de-ying-yong/mst3.jpg)

### 1.2. 性质

![最小生成树4](/blogs/obsn-tu-de-ying-yong/mst4.jpg)

- 所有边的情况皆不相同。

![最小生成树5](/blogs/obsn-tu-de-ying-yong/mst5.jpg)

- $n$ 个顶点只有 $n-1$ 条边。

![最小生成树6](/blogs/obsn-tu-de-ying-yong/mst6.jpg)

![最小生成树7](/blogs/obsn-tu-de-ying-yong/mst7.jpg)

### 1.3. 算法

![最小生成树8](/blogs/obsn-tu-de-ying-yong/mst8.jpg)

- 不会产生回路
- 权值最小

都使用贪心算法策略。

> 考研中多考查算法步骤；代码编写考查较少。

#### 1.3.1. Prim

![最小生成树9](/blogs/obsn-tu-de-ying-yong/mst9.jpg)

![最小生成树10](/blogs/obsn-tu-de-ying-yong/mst10.jpg)

![最小生成树11](/blogs/obsn-tu-de-ying-yong/mst11.jpg)

![最小生成树12](/blogs/obsn-tu-de-ying-yong/mst12.jpg)

#### 1.3.2. Kruskal

![最小生成树13](/blogs/obsn-tu-de-ying-yong/mst13.jpg)

![最小生成树14](/blogs/obsn-tu-de-ying-yong/mst14.jpg)

![最小生成树15](/blogs/obsn-tu-de-ying-yong/mst15.jpg)

![最小生成树16](/blogs/obsn-tu-de-ying-yong/mst16.jpg)

## 2. 最短路径

![最短路径1](/blogs/obsn-tu-de-ying-yong/sp1.jpg)

![最短路径2](/blogs/obsn-tu-de-ying-yong/sp2.jpg)

> 考研中多考查算法步骤；代码编写考查较少。

### 2.1. Dijkstra

![最短路径3](/blogs/obsn-tu-de-ying-yong/sp3.jpg)

![最短路径4](/blogs/obsn-tu-de-ying-yong/sp4.jpg)

![最短路径5](/blogs/obsn-tu-de-ying-yong/sp5.jpg)

![最短路径6](/blogs/obsn-tu-de-ying-yong/sp6.jpg)

![最短路径7](/blogs/obsn-tu-de-ying-yong/sp7.jpg)

![最短路径8](/blogs/obsn-tu-de-ying-yong/sp8.jpg)

![最短路径9](/blogs/obsn-tu-de-ying-yong/sp9.jpg)

### 2.2. Floyd

![最短路径10](/blogs/obsn-tu-de-ying-yong/sp10.jpg)

![最短路径11](/blogs/obsn-tu-de-ying-yong/sp11.jpg)

![最短路径12](/blogs/obsn-tu-de-ying-yong/sp12.jpg)

## 3. 拓扑排序

### 3.1. 概念

![拓扑排序1](/blogs/obsn-tu-de-ying-yong/ts1.jpg)

![拓扑排序2](/blogs/obsn-tu-de-ying-yong/ts2.jpg)

### 3.2. 算法思想

![拓扑排序3](/blogs/obsn-tu-de-ying-yong/ts3.jpg)

![拓扑排序4](/blogs/obsn-tu-de-ying-yong/ts4.jpg)

![拓扑排序5](/blogs/obsn-tu-de-ying-yong/ts5.jpg)

![拓扑排序6](/blogs/obsn-tu-de-ying-yong/ts6.jpg)

![拓扑排序7](/blogs/obsn-tu-de-ying-yong/ts7.jpg)

![拓扑排序8](/blogs/obsn-tu-de-ying-yong/ts8.jpg)

## 4. 关键路径

![关键路径1](/blogs/obsn-tu-de-ying-yong/cp1.jpg)

- 事件最早发生时间：等待所有前置事件都完成。

![关键路径2](/blogs/obsn-tu-de-ying-yong/cp2.jpg)

- 事件最迟发生时间：不延期后置事件的发生。

![关键路径3](/blogs/obsn-tu-de-ying-yong/cp3.jpg)

- 活动最早开始时间。

![关键路径4](/blogs/obsn-tu-de-ying-yong/cp4.jpg)

- 活动最迟开始时间。

![关键路径5](/blogs/obsn-tu-de-ying-yong/cp5.jpg)

- 差额。

![关键路径6](/blogs/obsn-tu-de-ying-yong/cp6.jpg)

![关键路径7](/blogs/obsn-tu-de-ying-yong/cp7.jpg)

![关键路径8](/blogs/obsn-tu-de-ying-yong/cp8.jpg)
