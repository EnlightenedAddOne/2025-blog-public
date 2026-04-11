> 来源：Obsidian/10-学业与考试/期末复习资料/python/Python重点习题集.md

# Python快速编程入门(第三版) - 重点习题集

#Python #编程/Python #习题

---

## 第3章 流程控制

### 一、简答题

**1. 简述 break 和 continue 语句的区别。**

- **break**：用于完全结束（终止）所在的循环结构。一旦执行 break，循环体中剩余的代码不再执行，且不再判断循环条件，直接跳出循环，执行循环之后的代码。
- **continue**：用于跳过本次循环中剩余的代码，直接进入下一次循环的条件判断。它不会终止整个循环，只是提前结束当前的这一轮循环。

**2. 简述 while 和 for 语句的区别。**

- **while 语句**：属于条件循环。它根据一个条件表达式的真假来决定是否执行循环。适用于**循环次数不确定**，只知道循环结束条件的场景（例如：直到用户输入"exit"为止）。
- **for 语句**：属于遍历循环。它通常用于遍历序列（如字符串、列表、元组、range()序列等）。适用于**循环次数已知**或需要对集合中每个元素进行操作的场景。

### 二、编程题

**1. 编写程序，实现利用 while 语句输出 100 以内偶数的功能。**

```python
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

# 或者步长法：
# i = 0
# while i <= 100:
#     print(i, end=" ")
#     i += 2
```

**2. 编写程序，实现判断用户输入的数是正数还是负数的功能。**

```Python
# 获取用户输入并转为浮点数
num = float(input("请输入一个数字: "))

if num > 0:
    print("这是一个正数")
elif num < 0:
    print("这是一个负数")
else:
    print("这是0")
```

**3. 编写程序，实现输出 100 以内质数的功能。**

```Python
print("100以内的质数有：")
for i in range(2, 101):
    is_prime = True  # 假设是质数
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
```

---

## 第4章 字符串

### 一、简答题（重复2）

**1. 请简述什么是字符串。**

字符串是由一系列字符组成的不可变序列。这些字符可以包括字母、数字、符号以及中文汉字等。在 Python 中，字符串可以使用单引号 `' '`、双引号 `" "` 或三引号 `''' '''` / `""" """` 来定义。

**2. 请简述 Python 中格式化字符串的几种方式。**

主要有三种方式：

1. **% 格式化**：使用 `%` 占位符（如 `%s`, `%d`）配合元组进行格式化。
2. **format() 方法**：使用 `{}` 作为占位符，调用字符串的 `.format()` 方法传入参数。
3. **f-string (格式化字符串字面值)**：在字符串引号前加 `f`，直接在 `{}` 中写入变量名或表达式，是 Python 3.6+ 引入的最简洁方式。

**3. 请简述 Python 中用于实现字符串对齐的内置方法。**

- `center(width, fillchar)`: 居中对齐，使用指定字符填充至指定宽度。
- `ljust(width, fillchar)`: 左对齐，使用指定字符填充至指定宽度。
- `rjust(width, fillchar)`: 右对齐，使用指定字符填充至指定宽度。

### 二、编程题（重复2）

**1. 编写程序，已知字符串 s='AbcDeFGhIJ'，请计算该字符串中小写字母的数量。**

```Python
s = 'AbcDeFGhIJ'
count = 0
for char in s:
    if char.islower(): # 或者使用 'a' <= char <= 'z'
        count += 1
print(f"小写字母的数量是: {count}")
```

**2. 编写程序，检查字符串 "Life is short. I use python" 中是否包含字符串 "python"，若包含则将其替换为 "Python" 后输出新字符串，否则输出原字符串。**

```Python
s = "Life is short. I use python"
target = "python"

if target in s:
    new_s = s.replace(target, "Python")
    print(new_s)
else:
    print(s)
```

---

## 第6章 函数

### 一、简答题（重复3）

**1. 简述位置参数的传递、关键字参数的传递、默认参数的传递的区别。**

- **位置参数**：按照实参和形参定义的先后顺序依次传递，数量和位置必须一一对应。
- **关键字参数**：调用函数时通过“形参名=值”的形式传递，不需要遵守位置顺序，明确了哪个值传给哪个参数。
- **默认参数**：在定义函数时为形参指定一个默认值。调用时如果未传递该参数，则使用默认值；如果传递了，则覆盖默认值。

**2. 简述函数参数混合传递的规则。**

在定义和调用函数时，如果混合使用多种参数传递方式，必须遵循优先级规则（从高到低）：

1. 位置参数
2. 关键字参数 / 默认参数
3. 可变位置参数 (`*args`)
4. 可变关键字参数 (\*\*kwargs)
   注意： 在调用时，位置参数必须在关键字参数之前。

**3. 简述局部变量和全局变量的区别。**

- **定义位置**：全局变量定义在函数外部；局部变量定义在函数内部。
- **作用域**：全局变量在整个程序运行期间都有效（除非被遮蔽）；局部变量只在定义它的函数内部有效，函数执行结束即销毁。
- **修改权限**：函数内部可以直接访问全局变量，但若要修改全局变量（不可变类型），需使用 `global` 关键字声明。

### 二、编程题（重复3）

**1. 编写函数，输出 1~100 中偶数之和。**

```Python
def sum_even():
    total = 0
    for i in range(1, 101):
        if i % 2 == 0:
            total += i
    print(f"1-100偶数之和为: {total}")

sum_even()
```

**2. 编写函数，计算 20×19×18×…×3 的结果。**

```Python
def calculate_product():
    result = 1
    # range左闭右开，步长为-1，所以是从20到3
    for i in range(20, 2, -1):
        result *= i
    return result

print(f"结果是: {calculate_product()}")
```

**3. 编写函数，判断用户输入的整数是否为回文数。（回文数：正向逆向相同，如12321）**

```Python
def is_palindrome(num):
    s_num = str(num)
    # 使用切片反转字符串进行比较
    if s_num == s_num[::-1]:
        return True
    else:
        return False

user_input = int(input("请输入一个整数: "))
if is_palindrome(user_input):
    print("是回文数")
else:
    print("不是回文数")
```

**4. 编写函数，判断用户输入的 3 个数字是否能作为边长构成三角形。**

```Python
def is_triangle(a, b, c):
    # 三角形判定规则：任意两边之和大于第三边
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("这三条边可以构成三角形")
    else:
        print("不能构成三角形")

a = float(input("边长1: "))
b = float(input("边长2: "))
c = float(input("边长3: "))
is_triangle(a, b, c)
```

**5. 编写函数，计算两个正整数的最小公倍数。**

```Python
def lcm(x, y):
    # 获取两个数中的较大值
    greater = x if x > y else y

    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm_val = greater
            break
        greater += 1
    return lcm_val

# 调用示例
print(lcm(12, 18)) # 输出 36
```

---

## 第8章 面向对象

### 一、简答题（重复4）

**1. 简述实例方法、类方法、静态方法的区别。**

- **实例方法**：第一个参数默认是 `self`（代表对象本身），只能通过对象调用（类调用需传参），可以访问实例属性和实例方法。
- **类方法**：使用 `@classmethod` 装饰，第一个参数默认是 `cls`（代表类本身），可以通过类或对象调用，可以访问类属性。
- **静态方法**：使用 `@staticmethod` 装饰，没有默认的必须参数（如 self 或 cls），可以通过类或对象调用，通常用于与类相关但不需要访问实例/类属性的独立功能。

**2. 简述什么是封装、继承和多态。**

- **封装**：将对象的属性和方法结合在一起，并隐藏对象的内部实现细节，仅对外提供公共的访问方式（接口），提高安全性。
- **继承**：子类自动拥有父类的属性和方法（公有成员），实现了代码的重用和扩展。
- **多态**：指不同的对象调用同一个方法时表现出不同的行为。在Python中通常表现为子类重写父类方法后，调用该方法时根据对象的实际类型执行对应的方法。

### 二、编程题（重复4）

**1. 定义一个 Circle (圆形) 类，包含属性 radius (半径)，以及 `get_perimeter()` 和 `get_area()` 方法。**

```Python
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        # 周长 = 2 * π * r
        return 2 * math.pi * self.radius

    def get_area(self):
        # 面积 = π * r^2
        return math.pi * (self.radius ** 2)

# 创建对象，半径为 5
c = Circle(5)
print(f"半径为5的圆周长: {c.get_perimeter():.2f}")
print(f"半径为5的圆面积: {c.get_area():.2f}")
```

**2. 定义一个 Course (课程) 类，包含属性 number, name, teacher, location (私有)，以及 `show_info()` 方法。**

```Python
class Course:
    def __init__(self, number, name, teacher, location):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.__location = location  # 私有属性，前加两个下划线

    def show_info(self):
        print("=== 课程信息 ===")
        print(f"编号: {self.number}")
        print(f"名称: {self.name}")
        print(f"教师: {self.teacher}")
        # 在类内部可以访问私有属性
        print(f"地点: {self.__location}")

# 创建对象
python_course = Course("CS101", "Python编程", "王老师", "一教302")

# 显示信息
python_course.show_info()
```
