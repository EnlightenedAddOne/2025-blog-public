> 来源：Obsidian/10-学业与考试/期末复习资料/python/Python 期末考试复习笔记.md

# Python 期末考试复习笔记

> [!abstract] 考试概况
> **考试范围**：第 1 - 8 章
> **核心重点**：**第 3、4、6、8 章**（重点复习简答题和编程题）
> **基础覆盖**：第 1、2、5、7 章（主要涉及填空、判断、选择）

---

## 🎯 第一部分：核心重点突破 (第3、4、6、8章)

> [!attention] 重点复习建议
> 这部分内容出现在**大题**（简答、编程）中的概率极高。
>
> 1. **简答题**：背诵关键词（已加粗）。
> 2. **编程题**：建议手写两遍代码，注意缩进。

### 📘 第三章：流程控制

#### 1. 简答题重点

- **break 与 continue 的区别**
  - **break**：用于**结束整个循环**，跳出循环体，不再执行循环内的后续代码。
  - **continue**：用于**结束本次循环**，跳过本次循环体中剩余的代码，直接进入下一次循环的判断。
- **while 与 for 的区别**
  - **while**：基于**条件**的循环。适用于循环次数**未知**，但知道终止条件的情况。
  - **for**：遍历序列（如列表、字符串）或可迭代对象。适用于**已知**遍历范围或需要对序列中每个元素进行操作的情况。

#### 2. 编程题精选

> [!example] 输出 100 以内偶数 (while循环)
>
> ```python
> num = 0
> while num <= 100:
>     if num % 2 == 0:
>         print(num)
>     num += 1
> ```

> [!example] 判断正负数
>
> ```python
> num = int(input("请输入一个数："))
> if num > 0:
>     print("输入的数是正数")
> elif num < 0:
>     print("输入的数是负数")
> else:
>     print("输入的数是零")
> ```

> [!example] 输出 100 以内质数 (素数)
>
> ```python
> for i in range(2, 100):
>     for j in range(2, i):
>         if i % j == 0:
>             break
>     else: # 注意 else 与 for 对齐
>         print(i)
> ```

---

### 📘 第四章：字符串

#### 1. 简答题重点

- **什么是字符串？**
  - 由字母、符号或数字组成的字符序列。
  - 定义：单引号/双引号（单行），三引号（多行）。
- **格式化字符串的 3 种方式**
  1.  **% 格式化**：`"%s" % value`
  2.  **format() 方法**：`"{ }".format(value)`
  3.  **f-string**：`f"{value}"` (最推荐)
- **字符串对齐方法**
  - `center()`：居中
  - `ljust()`：左对齐
  - `rjust()`：右对齐

#### 2. 编程题精选

> [!example] 统计小写字母数量
>
> ```python
> s = 'AbcDeFGhIJ'
> count = 0
> for i in s:
>     # 方法一：比较字符范围
>     if 'a' <= i <= 'z':
>         count += 1
>     # 方法二：使用 islower()
>     # if i.islower():
>     #     count += 1
> print(count)
> ```

> [!example] 查找并替换字符串
>
> ```python
> string = " Life is short. I use python"
> # find找不到返回-1，这里判断是否不等于-1
> if string.find('python') != -1:
>     new_string = string.replace('python', 'Python')
>     print(new_string)
> else:
>     print(string)
> ```

---

### 📘 第六章：函数

#### 1. 简答题重点

- **参数传递的区别**
  - **位置参数**：按顺序传递，位置严格对应。
  - **关键字参数**：通过参数名指定值，顺序可打乱。
  - **默认参数**：定义时指定默认值，调用时可省略。
- **局部变量 vs 全局变量**
  - **局部变量**：函数**内部**定义，作用域仅限函数内，函数结束即销毁。
  - **全局变量**：函数**外部**定义，整个程序通用。
- **混合参数传递规则**
  - 顺序：位置参数 -> 关键字参数 -> 默认参数 -> 打包传递 (`*args`, `**kwargs`)。

#### 2. 编程题精选

> [!example] 计算 1~100 偶数之和 (函数版)
>
> ```python
> def event_num_sum():
>     result = 0
>     counter = 1
>     while counter <= 100:
>         counter += 1
>         if counter % 2 == 1:
>             continue
>         result += counter
>     return result
> print(event_num_sum())
> ```

> [!example] 递归计算乘积 (20\*19\*...\*3)
>
> ```python
> def func(num):
>     if num == 3: # 题目若要求乘到3截止
>         return 3
>     else:
>         return num * func(num - 1)
> result = func(20)
> print(result)
> ```

> [!example] 判断回文数 (如 12321)
>
> ```python
> def is_palindrome():
>     num = input('请输入整数：')
>     # 字符串切片反转
>     if num == num[::-1]:
>         return True
>     else:
>         return False
> ```

> [!example] 判断三角形构成
>
> ```python
> def triangle():
>     a = int(input("边长1："))
>     b = int(input("边长2："))
>     c = int(input("边长3："))
>     # 任意两边之和大于第三边
>     if (a + b > c) and (a + c > b) and (b + c > a):
>         return "能构成三角形"
>     else:
>         return "不能构成三角形"
> ```

---

### 📘 第八章：面向对象

#### 1. 简答题重点

- **三种方法的区别**
  - **实例方法**：`def method(self)`，由对象调用，访问实例属性。
  - **类方法**：`@classmethod`，第一个参数 `cls`，访问类属性。
  - **静态方法**：`@staticmethod`，无默认参数，类似普通函数。
- **面向对象三大特性**
  1.  **封装**：隐藏细节，提供接口。
  2.  **继承**：代码复用，构建新类。
  3.  **多态**：接口通用，不考虑对象具体类型。

#### 2. 编程题精选

> [!example] 定义圆类 (Circle)
>
> ```python
> class Circle:
>     def __init__(self, tup, radius, color):
>         self.center = tup
>         self.radius = radius
>         self.color = color
>
>     def perimeter(self): # 周长
>         return 3.14 * 2 * self.radius
>
>     def area(self): # 面积
>         return 3.14 * self.radius * self.radius
>
> circle = Circle((0,0), 5, "蓝色")
> print(circle.perimeter())
> print(circle.area())
> ```

> [!example] 定义课程类 (Course) 含私有属性
>
> ```python
> class Course:
>     def __init__(self):
>         self.number = 1001
>         self.name = "语文"
>         self.teacher = "张老师"
>         self.__location = "305室" # 私有属性
>
>     def show_info(self):
>         # 类内部可以访问私有属性
>         return "课程：%s, 地点：%s" % (self.name, self.__location)
>
> course = Course()
> print(course.show_info())
> ```

---

## 📝 第二部分：基础知识串讲 (第1、2、5、7章)

> [!info] 说明
> 这部分主要针对**填空、选择、判断题**。

- **第 1 章**：Python 特点（简洁、开源、可移植）、后缀 `.py`、导入 `import`。
- **第 2 章**：缩进（4空格）、布尔值 (`True`/`False`)、`type()` 查看类型、变量名不能以数字开头。
- **第 5 章 (组合数据)**：
  - **列表** `[]`：有序，可变。
  - **元组** `()`：有序，**不可变**。
  - **字典** `{k:v}`：键唯一，无索引。删除方法：`pop()`, `clear()`。
  - **集合** `{v}`：无序，**唯一**（去重）。
- **第 7 章 (文件)**：
  - 文本 vs 二进制。
  - `read()` / `readline()` / `readlines()` (返回列表)。
  - 操作完必须 `close()`。

---

## ⚠️ 第三部分：考前速记 (易错点)

> [!failure] 考前必看：易错判断与选择
>
> 1. Python 程序比 C++ 代码量少，但运行速度通常**慢**。
> 2. 列表的索引是从 **0** 开始的，不是 1。
> 3. 字典的**键 (Key)** 必须是**唯一**的。
> 4. 构造方法的方法名是 `__init__` (前后各两个下划线)。
> 5. 子类调用父类方法使用 `super()`。
> 6. 除以 0 会引发 `ZeroDivisionError`。
> 7. **语法提醒**：`if`, `for`, `def`, `class` 等语句末尾千万别忘了加**冒号** `:`。
