> 来源：Obsidian/10-学业与考试/考研/wangdao-data-structure-main/ch2/single-link/单链表.md

# 单链表

## 1. typedef 关键词

`typedef` 关键字：数据类型重命名。

```cpp
typedef <数据类型> <别名>
```

```cpp
int x = 1;
int *p;
```

```cpp
typedef int zhengshu;
typedef int *zhengshuzhizhen;
zhengshu x = 1;
zhengshuzhizhen p;
```

## 2. 定义单链表

结点：

- 数据域
- 指针域

```cpp
struct LNode
{
    ElemType data;
    struct LNode *next;
};
```

```cpp
struct LNode *p = (struct LNode*) malloc(sizeof(struct LNode))
```

```cpp
typedef struct LNode LNode;
LNode *p = (LNode *) malloc(sizeof LNode);
```

> [!tip] 高级写法
>
> ```cpp
> typedef struct LNode
> {
>     ElemType data;
>     struct LNode *next;
> } LNode, *LinkList;
> ```
>
> 等价于：
>
> ```cpp
> struct LNode
> {
>     ElemType data;
>     struct LNode *next;
> };
> typedef struct LNode LNode;
> typedef struct LNode *LinkList;
> ```

声明一个单链表时，只需要声明一个头指针 `L`，指向单链表的第一个结点。

```cpp
LNode *L; // 强调这是一个结点
```

```cpp
LinkList L; // 强调这是一个单链表
```

## 3. 不带头结点的单链表

```cpp
// 初始化一个空的单链表，不带头结点
bool InitList(LinkList &L)
{
    L = NULL;
    return true;
}
```

```cpp
// 判断单链表是否为空
bool Empty(LinkList L)
{
    return L == NULL;
}
```

> [!important] 写代码更麻烦
>
> - 对第一个数据结点和后续数据结点的处理需要用不同的代码逻辑
> - 对空表和非空表的处理需要用不同的代码逻辑
