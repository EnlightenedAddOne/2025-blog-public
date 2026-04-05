> 来源：Obsidian/10-学业与考试/考研/数据结构/04.串.md

# 第四章：串 (String)

## 1. 串的基本概念

- 对应视频：`4.1_1_串的定义`

### 1.1 串的定义

**串 (String)**：由零个或多个字符组成的有限序列，记作 $S = "a_1a_2...a_n"$（$n \ge 0$）。

- $n$：串的长度。
- $n = 0$：空串。
- **子串**：串中任意个连续字符组成的子序列。
- **主串**：包含子串的串。
- **字符位置**：字符在序列中的序号（从1开始）。
- **子串位置**：子串第一个字符在主串中的位置。

### 1.2 串的基本操作

- `StrAssign(&T, chars)`：赋值操作。
- `StrCopy(&T, S)`：复制操作。
- `StrEmpty(S)`：判空操作。
- `StrLength(S)`：求串长。
- `StrCompare(S, T)`：比较操作（按字典序）。
- `Concat(&T, S1, S2)`：串联接。
- `SubString(&Sub, S, pos, len)`：求子串。
- `Index(S, T)`：定位操作（返回子串 $T$ 在主串 $S$ 中第一次出现的位置）。

---

## 2. 串的存储结构

- 对应视频：`4.2_1_串的存储结构`

### 2.1 定长顺序存储

**C语言代码实现**：

```c
#define MAXLEN 255  // 预定义最大串长

// 定长顺序存储
typedef struct {
    char ch[MAXLEN];  // 静态数组存储
    int length;       // 串的当前长度
} SString;
```

**特点**：

- 简单，但最大长度固定，可能浪费空间或溢出。
- `ch[0]` 可以闲置不用，也可以用来存放串长度。

### 2.2 堆分配存储

**C语言代码实现**：

```c
// 堆分配存储
typedef struct {
    char *ch;      // 动态分配存储区首地址
    int length;    // 串的当前长度
} HString;

// 初始化串
void InitString(HString &S) {
    S.ch = NULL;
    S.length = 0;
}

// 生成串
void StrAssign(HString &S, char *cstr) {
    if(S.ch) free(S.ch);  // 释放原空间
    int len = 0;
    char *c = cstr;
    while(*c) { len++; c++; }  // 求长度

    if(len == 0) {
        S.ch = NULL;
        S.length = 0;
    } else {
        S.ch = (char*)malloc(len * sizeof(char));
        for(int i = 0; i < len; i++)
            S.ch[i] = cstr[i];
        S.length = len;
    }
}
```

**特点**：

- 动态分配，节省空间。
- 需要手动管理内存（malloc/free）。

### 2.3 块链存储

**C语言代码实现**：

```c
#define CHUNKSIZE 4  // 每个节点存储的字符数

// 块链存储节点
typedef struct Chunk {
    char ch[CHUNKSIZE];
    struct Chunk *next;
} Chunk;

typedef struct {
    Chunk *head, *tail;  // 头指针和尾指针
    int length;          // 串的当前长度
} LString;
```

**特点**：

- 每个节点存储多个字符，减少指针开销。
- 适合频繁插入删除操作。
- 可能存在存储密度问题（最后一个节点未满）。

---

## 3. 模式匹配算法 (Pattern Matching)

### 3.1 朴素模式匹配算法 (Brute-Force)

- 对应视频：`4.3_1_朴素模式匹配`

**算法思想**：

- 主串 $S$，模式串 $T$（子串）。
- 从主串的第一个字符开始，逐个与模式串比较。
- 若匹配失败，主串指针 $i$ 回溯到下一个起始位置，模式串指针 $j$ 回到开头。

**C语言代码实现**：

```c
// 朴素模式匹配算法
int Index_BF(SString S, SString T) {
    int i = 1, j = 1;  // i为主串指针，j为模式串指针（从1开始）

    while(i <= S.length && j <= T.length) {
        if(S.ch[i] == T.ch[j]) {  // 字符匹配
            i++;
            j++;
        } else {                  // 字符不匹配
            i = i - j + 2;        // i回溯到下一个起始位置
            j = 1;                // j回到模式串开头
        }
    }

    if(j > T.length)  // 匹配成功
        return i - T.length;
    else
        return 0;     // 匹配失败
}
```

**复杂度分析**：

- **最好情况**：$O(n)$（第一次就匹配成功）。
- **最坏情况**：$O(mn)$（每次都在最后一个字符失配）。
  - 例如：$S = "aaaab"$，$T = "aaab"$。

**缺点**：主串指针 $i$ 需要回溯，效率低。

---

### 3.2 KMP 算法 (Knuth-Morris-Pratt)

- 对应视频：`4.3_2_KMP算法`、`4.3_3_KMP算法的next数组`

**核心思想**：

- **主串指针 $i$ 不回溯**，仅模式串指针 $j$ 回退。
- 利用已经匹配过的信息，避免重复比较。
- 引入 **Next 数组**，记录失配时 $j$ 应回退的位置。

#### 3.2.1 Next 数组的定义

**定义**：`next[j]` 表示当模式串第 $j$ 个字符失配时，$j$ 应该回退到的位置。

**求解规则**（手算必考）：

- `next[1] = 0`（第一个字符失配，无需回退）。
- `next[j] = k`，其中 $k$ 是满足 $T[1...k-1] = T[j-k+1...j-1]$ 的最大值。
  - 即：模式串中以 $T[j-1]$ 结尾的**最长相等前后缀**的长度 + 1。

**特殊情况**：

- 若不存在相等前后缀，则 `next[j] = 1`。

#### 3.2.2 Next 数组的手工求解（重要）

**示例**：求模式串 $T = "ababaaababaa"$ 的 Next 数组。

| $j$       | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $T[j]$    | a   | b   | a   | b   | a   | a   | a   | b   | a   | b   | a   | a   |
| `next[j]` | 0   | 1   | 1   | 2   | 3   | 4   | 2   | 2   | 3   | 4   | 5   | 6   |

**手算步骤**：

1. `next[1] = 0`（固定）。
2. `next[2] = 1`（第一个字符前无前缀）。
3. `next[3]`：$T[1...1] = "a" \neq T[2...2] = "b"$ → `next[3] = 1`。
4. `next[4]`：$T[1...1] = "a" = T[3...3] = "a"$ → `next[4] = 2`。
5. `next[5]`：$T[1...2] = "ab" = T[3...4] = "ab"$ → `next[5] = 3`。
6. `next[6]`：$T[1...3] = "aba" = T[3...5] = "aba"$ → `next[6] = 4`。
7. `next[7]`：$T[1...1] = "a" = T[6...6] = "a"$ → `next[7] = 2`。
8. 以此类推...

#### 3.2.3 KMP 算法实现

**C语言代码实现**：

```c
// KMP 算法
int Index_KMP(SString S, SString T, int next[]) {
    int i = 1, j = 1;

    while(i <= S.length && j <= T.length) {
        if(j == 0 || S.ch[i] == T.ch[j]) {  // j==0 表示从头开始匹配
            i++;
            j++;
        } else {
            j = next[j];  // j回退，i不回溯
        }
    }

    if(j > T.length)
        return i - T.length;  // 匹配成功
    else
        return 0;             // 匹配失败
}
```

#### 3.2.4 Next 数组的代码求解

**C语言代码实现**：

```c
// 求 Next 数组
void get_next(SString T, int next[]) {
    int i = 1, j = 0;
    next[1] = 0;

    while(i < T.length) {
        if(j == 0 || T.ch[i] == T.ch[j]) {
            i++;
            j++;
            next[i] = j;
        } else {
            j = next[j];  // j回退
        }
    }
}
```

**复杂度**：

- 求 Next 数组：$O(m)$（$m$ 为模式串长度）。
- KMP 匹配：$O(n)$（$n$ 为主串长度）。
- **总复杂度**：$O(m + n)$。

---

### 3.3 KMP 算法的优化：Nextval 数组

- 对应视频：`4.3_4_KMP算法的优化`

#### 3.3.1 Next 数组的缺陷

**示例**：$S = "aaaab"$，$T = "aaab"$。

- 当 $j = 4$ 失配时，$j$ 回退到 `next[4] = 3`。
- 但 $T[3] = T[4] = 'a'$，仍然会失配，继续回退。

**问题**：若 $T[j] = T[next[j]]$，则回退到 `next[j]` 仍会失配。

#### 3.3.2 Nextval 数组的定义

**优化思想**：

- 若 $T[j] = T[next[j]]$，则 `nextval[j] = nextval[next[j]]`。
- 否则，`nextval[j] = next[j]`。

**求解规则**：

```
nextval[1] = 0;
for j = 2 to m:
    if T[j] == T[next[j]]:
        nextval[j] = nextval[next[j]]
    else:
        nextval[j] = next[j]
```

#### 3.3.3 Nextval 数组的手工求解

**示例**：$T = "ababaaababaa"$。

| $j$          | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $T[j]$       | a   | b   | a   | b   | a   | a   | a   | b   | a   | b   | a   | a   |
| `next[j]`    | 0   | 1   | 1   | 2   | 3   | 4   | 2   | 2   | 3   | 4   | 5   | 6   |
| `nextval[j]` | 0   | 1   | 0   | 1   | 0   | 4   | 2   | 1   | 0   | 1   | 0   | 4   |

**手算步骤**：

1. `nextval[1] = 0`（固定）。
2. `nextval[2] = 1`（$T[2] = 'b' \neq T[next[2]] = T[1] = 'a'$）。
3. `nextval[3]`：$T[3] = 'a' = T[next[3]] = T[1] = 'a'$ → `nextval[3] = nextval[1] = 0`。
4. `nextval[4]`：$T[4] = 'b' = T[next[4]] = T[2] = 'b'$ → `nextval[4] = nextval[2] = 1`。
5. `nextval[5]`：$T[5] = 'a' = T[next[5]] = T[3] = 'a'$ → `nextval[5] = nextval[3] = 0`。
6. `nextval[6]`：$T[6] = 'a' \neq T[next[6]] = T[4] = 'b'$ → `nextval[6] = next[6] = 4`。
7. 以此类推...

#### 3.3.4 Nextval 数组的代码实现

**C语言代码实现**：

```c
// 求 Nextval 数组（改进的 Next 数组）
void get_nextval(SString T, int nextval[]) {
    int i = 1, j = 0;
    nextval[1] = 0;

    while(i < T.length) {
        if(j == 0 || T.ch[i] == T.ch[j]) {
            i++;
            j++;
            // 优化：若当前字符与前缀相同，则继承前缀的nextval值
            if(T.ch[i] != T.ch[j])
                nextval[i] = j;
            else
                nextval[i] = nextval[j];
        } else {
            j = nextval[j];
        }
    }
}
```

**使用 Nextval 的 KMP 算法**：

```c
// 使用 Nextval 的 KMP 算法
int Index_KMP_Nextval(SString S, SString T, int nextval[]) {
    int i = 1, j = 1;

    while(i <= S.length && j <= T.length) {
        if(j == 0 || S.ch[i] == T.ch[j]) {
            i++;
            j++;
        } else {
            j = nextval[j];  // 使用 nextval 回退
        }
    }

    if(j > T.length)
        return i - T.length;
    else
        return 0;
}
```

---

## 4. KMP 算法总结与考点

### 4.1 Next 数组与 Nextval 数组对比

| 项目       | Next 数组              | Nextval 数组                                    |
| ---------- | ---------------------- | ----------------------------------------------- |
| **定义**   | 失配时 $j$ 回退的位置  | 优化后的回退位置                                |
| **求解**   | 最长相等前后缀长度 + 1 | 若 $T[j] = T[next[j]]$，继承 `nextval[next[j]]` |
| **优点**   | 简单                   | 减少无效比较                                    |
| **缺点**   | 可能存在冗余比较       | 需额外判断                                      |
| **复杂度** | $O(m)$                 | $O(m)$                                          |

### 4.2 KMP 算法的核心要点

1. **主串指针不回溯**：这是 KMP 相对于朴素算法的最大优势。
2. **Next 数组的物理意义**：记录了模式串的"自匹配"信息。
3. **手算 Next/Nextval**：
   - Next：看 $j-1$ 位置之前的最长相等前后缀。
   - Nextval：在 Next 基础上，若字符相同则继承。
4. **时间复杂度**：$O(m + n)$，优于朴素算法的 $O(mn)$。

### 4.3 考试常见题型

1. **手算 Next/Nextval 数组**（必考）：
   - 给定模式串，求 Next 数组。
   - 给定模式串，求 Nextval 数组。
2. **KMP 匹配过程**：
   - 给定主串、模式串和 Next 数组，模拟匹配过程。
   - 统计匹配过程中的比较次数。
3. **算法填空题**：
   - 补全 KMP 算法或 get_next 函数的关键代码。
4. **复杂度分析**：
   - 比较朴素算法和 KMP 算法的复杂度。

---

## 5. 重要考点与易错点总结

### 5.1 必背要点

- **Next 数组的求解**：
  - `next[1] = 0`，`next[2] = 1`（固定）。
  - `next[j]` = 模式串中以 $T[j-1]$ 结尾的最长相等前后缀长度 + 1。
- **Nextval 数组的优化**：
  - 若 $T[j] = T[next[j]]$，则 `nextval[j] = nextval[next[j]]`。
  - 否则 `nextval[j] = next[j]`。
- **复杂度**：
  - 朴素算法：$O(mn)$。
  - KMP 算法：$O(m + n)$。

### 5.2 易错点

1. **Next 数组下标**：
   - 部分教材从 0 开始，部分从 1 开始，注意区分。
   - 本笔记采用从 1 开始的下标。
2. **Next 与 Nextval 的混淆**：
   - Next 是基础，Nextval 是优化。
   - 考试时注意题目要求。
3. **手算 Next 时的常见错误**：
   - 忘记 `next[1] = 0`。
   - 混淆前缀和后缀的定义（前缀不包含最后一个字符，后缀不包含第一个字符）。
4. **KMP 匹配过程**：
   - 主串指针 $i$ **不回溯**，只有 $j$ 回退。
   - `j = 0` 时表示从头开始，此时 $i$ 和 $j$ 同时前进。

### 5.3 记忆口诀

- **Next 数组**：最长前后缀，加一不加零。
- **Nextval 优化**：字符相同找祖宗，不同直接用 Next。
- **KMP 核心**：主串不回头，模式跳着走。

---

## 6. 串的应用

### 6.1 字符串匹配的实际应用

- **文本编辑器**：查找、替换功能。
- **搜索引擎**：关键词匹配。
- **DNA 序列分析**：基因片段匹配。
- **病毒检测**：特征码匹配。

### 6.2 其他模式匹配算法（了解）

- **BM 算法 (Boyer-Moore)**：从右向左匹配，实际应用中效率更高。
- **Sunday 算法**：BM 算法的简化版。
- **AC 自动机**：多模式串匹配（基于 KMP 和字典树）。

**考试重点**：408 考研主要考 **KMP 算法**，其他算法了解即可。

---

## 7. 补充：字符串常见操作的实现

### 7.1 串比较

**C语言代码实现**：

```c
// 串比较（字典序）
int StrCompare(SString S, SString T) {
    for(int i = 1; i <= S.length && i <= T.length; i++) {
        if(S.ch[i] != T.ch[i])
            return S.ch[i] - T.ch[i];  // 返回差值
    }
    return S.length - T.length;  // 长度不同
}
```

### 7.2 求子串

**C语言代码实现**：

```c
// 求子串：从 S 的第 pos 个字符起，长度为 len 的子串赋给 Sub
bool SubString(SString &Sub, SString S, int pos, int len) {
    if(pos < 1 || pos > S.length || len < 0 || len > S.length - pos + 1)
        return false;  // 参数不合法

    for(int i = 1; i <= len; i++)
        Sub.ch[i] = S.ch[pos + i - 1];
    Sub.length = len;
    return true;
}
```

### 7.3 串连接

**C语言代码实现**：

```c
// 串连接：用 T 返回 S1 和 S2 连接而成的新串
bool Concat(SString &T, SString S1, SString S2) {
    if(S1.length + S2.length > MAXLEN)
        return false;  // 超出最大长度

    for(int i = 1; i <= S1.length; i++)
        T.ch[i] = S1.ch[i];
    for(int i = 1; i <= S2.length; i++)
        T.ch[S1.length + i] = S2.ch[i];
    T.length = S1.length + S2.length;
    return true;
}
```

---

## 8. 总结

**串的核心**：

- **存储**：定长、堆分配、块链。
- **模式匹配**：朴素算法（$O(mn)$）、KMP 算法（$O(m+n)$）。
- **KMP 关键**：Next/Nextval 数组的求解，主串指针不回溯。

**408 考研重点**：

1. 手算 Next/Nextval 数组（必考）。
2. KMP 匹配过程模拟。
3. 算法代码填空。
4. 复杂度分析。
