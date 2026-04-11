# Java期末复习题

> 来源：Obsidian/10-学业与考试/期末复习资料/大二下/Java/Java期末复习题.md

### 第1章 Java开发入门

#### 一、填空题

1. Java是一种​**​面向对象​**​语言，它是由​**​SUN​**​公司（已被Oracle公司收购）开发的高级程序设计语言。
2. 针对不同的开发市场，SUN公司将Java划分为三个技术平台，它们分别是​**​JavaSE​**​、​**​JavaEE​**​和​**​JavaME​**​。
3. Java语言的特点有简单性、​**​面向对象​**​、​**​跨平台性​**​、安全性，支持​**​多线程​**​和分布式。
4. SUN公司提供了一套Java开发环境，简称​**​JDK​**​。
5. JDK中，存放可执行程序的目录是​**​bin​**​。

#### 二、判断题

1. Java是1995年5月正式发布的。
   **• 答案：对**

2. JRE中包含了Java基本类库、JVM和开发工具。
   **• 答案：错**
   **• 解析**：JRE包含基本类库和JVM，但不包含开发工具（开发工具在JDK中）。

3. 编译Java程序需要使用java命令。
   **• 答案：错**
   **• 解析**：编译Java程序需使用javac命令，java命令用于运行程序。

4. Java中的包是专门用来存放类的，通常功能相同的类存放在相同的包中。
   **• 答案：对**

5. IDEA开发工具Debug模式下不进入函数内部的单步调试快捷键是F7。
   **• 答案：错**
   **• 解析**：IDEA中F8是不进入函数内部的单步调试（Step Over），F7是进入函数内部的单步调试（Step Into）。

#### 三、选择题

1. Java属于那种语言？（C）
   • A、机器语言
   • B、汇编语言
   • C、高级语言
   • D、以上都不对

2. Java语言的特点有哪些？（多选）（ABCD）
   • A、简单性
   • B、面向对象
   • C、跨平台性
   • D、支持多线程

3. 在JDK的bin目录下有许多exe可执行文件，其中java.exe命令的作用是（D）
   • A、Java文档制作工具。
   • B、Java解释器。
   • C、Java编译器。
   • D、Java启动器。

4. IDEA开发工具Debug模式下进入函数内部的单步调试快捷键是（A）
   • A、F7
   • B、F8
   • C、Shift+F7
   • D、Shift+F8

5. 下面那种类型的文件可以在Java虚拟机中运行？（D）
   • A、.java
   • B、.jre
   • C、.exe
   • D、.class

#### 四、简答题

1. **简述Java的特点。**
   • Java的特点包括​*​简单性、面向对象、安全性、跨平台性、支持多线程、分布性​*​。

2. **简述Java的运行机制。**
   • Java程序的运行需经过编译和运行两个步骤。首先将后缀名为`.java`的源文件编译成后缀名为`.class`的字节码文件，然后由Java虚拟机（JVM）解释执行字节码文件并显示结果。

#### 五、编程题

编写一个简单的Java程序，输出“这是第一个Java程序!”。

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("这是第一个Java程序!");
    }
}
```

### 第2章 Java编程基础

#### 一、填空题（重复2）

1. Java 程序代码必须放在一个类中，类使用​**​class​**​关键词定义。
2. Java 中的注释有三类，分别是​**​单行注释​**​、​**​多行注释​**​和​**​文档注释​**​。
3. 在Java中，变量的数据类型分为两种，即基本​**​数据​**​和​**​引用数据​**​类型。
4. 在逻辑运算符中，运算符​**​&​**​、​**​&&​**​用于表示逻辑与，​**​|​**​、​**​||​**​表示逻辑或。
5. 数组是一个​**​容器​**​，存储到数组中的每个元素，都有自己的自动编号，最小值为​**​0​**​。

#### 二、判断题（重复2）

1. Java 语言不区分大小写。
   **• 答案：错**
   **• 解析**：Java 严格区分大小写，如"Hello"和"hello"被视为不同标识符。

2. continue 语句只用于循环语句中，它的作用是跳出循环。
   **• 答案：错**
   **• 解析**：continue 作用是终止本次循环进入下一次循环，break 才是跳出循环。

3. 三元运算符的语法格式为“判断条件？表达式1：表达式2”。
   **• 答案：对**

4. 循环嵌套是指在一个循环语句的循环体中再定义一个循环语句的语法结构。while、do…while、for 循环语句都可以进行嵌套，并且它们之间也可以互相嵌套。
   **• 答案：对**

5. 在switch 条件语句和循环语句中都可以使用break语句。
   **• 答案：对**

#### 三、选择题（重复2）

1. 下列选项中，关于类的定义格式正确的是（AC）（多选）
   • A、 修饰符 class 类名{
   程序代码
   }
   • B、修饰符 类名class {
   程序代码
   }
   • C、class 类名{
   程序代码
   }
   • D、类名 class {
   程序代码
   }

2. 下列选项中，那些属于合法的标识符？（A）
   • A、 username
   • B、 class
   • C、 123username
   • D、 Hello World
   • 解析：B是关键字，C以数字开头，D包含空格，均不合法。

3. 下列选项中，使用比较运算符正确的是（B）
   • A、 4！=3结果为false（应为4!=3）
   • B、 4 == 3 结果为false
   • C、 4<=3结果为true（实际为false）
   • D、 4>=3结果为true

4. 请阅读下面代码。

```java
int a=3；
int b=2；
switch (b){
	case 1:
		a--；
		break;
	case 2:
		a++；
		case 3:
		a=a+3；
	default:
		a++;
	break;
}
System.out.println("a="+a);
```

上述程序运行结束时，变量a的值为（D）
• A、4
• B、5
• C、7
• D、8
• 解析：case 2无break会继续执行case 3和default

5. 假设int x=2,三元表达式x>0？x+1：5（C）
   • A、0
   • B、2
   • C、3
   • D、5
   • 解析：x>0为true，取x+1=3

#### 四、简答题（重复2）

1. **简述Java语言中的8种基本数据类型，并说明每种数据类型所占用的空间大小。**
   • ​**​byte​**​：字节型，1字节
   • ​**​short​**​：短整型，2字节
   • ​**​int​**​：整型，4字节
   • ​**​long​**​：长整型，8字节
   • ​**​float​**​：单精度浮点型，4字节
   • ​**​double​**​：双精度浮点型，8字节
   • ​**​char​**​：字符型，2字节
   • ​**​boolean​**​：布尔型，1字节（存储true/false）

2. **简述跳转语句break与continue的作用和区别。**
   • 在switch条件语句和循环语句中都可以使用break语句。当它出现在switch条件语 句中时，作用是终止某个case并跳出switch结构。当它出现在循环语句中，作用是跳出循 环语句，执行循环后面的代码
   • continue语句用在循环语句中，它的作用是终止本次循环， 执行下一次循环。

#### 五、编程题（重复2）

1. 请编写程序，实现计算“1+3+5+7+…+99”的值，要求如下。
   （1）使用循环语句实现自然数1~99的遍历。
   （2）在遍历过程中，通过条件判断当前遍历的书是否为奇数，如果是就累加，否则不 加。

```java
public class getSum {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; i < 100; i++) {
            if (i % 2 != 0)
                sum += i;
        }
        System.out.println(sum);
    }
}
```

2. 请编写程序，实现获取数组{22，24，76，12，21，33}的最大数。

```java
public class Example28 {
    public static void main(String[] args) {
        int[] arr = {22, 24, 76, 12, 21, 33};
        int max = getMax(arr);
        System.out.println("max=" + max);
    }

    static int getMax(int[] arr) {
        int max = arr[0];
        for (int x = 1; x < arr.length; x++) {
            if (arr[x] > max) {
                max = arr[x];
            }
        }
        return max;
    }
}
```

### 第3章 面向对象（上）

#### 一、填空题（重复3）

1. 面向对象的三大特征是**封装**、**继承**、**多态**。
2. 定义类的关键字为**class**。
3. 针对类、成员方法和属性，Java提供了4种访问控制权限，分别是**private**、**protected**、**public**和 **default**。
4. 静态方法必须使用**static**关键字来修饰。
5. 类的封装是指在定义一个类时，将类中的属性私有化，即使用**private**关键字来修饰。

#### 二、判断题（重复3）

1. 在成员方法中出现的this关键字，代表的是调用这个方法的对象。
   答案：**对**
2. 静态变量只能在静态方法中使用。
   答案：**错**
3. 与普通方法一样，构造方法也可以重载。
   答案：**对**
4. 私有属性只能在它所在类中被访问，为了能让外界访问私有属性，需要提供一些使用public修饰的公有方法。
   答案：**对**
5. 封装就是隐藏对象的属性和实现细节，仅对外提供公有的方法。
   答案：**对**

#### 三、选择题（重复3）

1. 下列关于this的说法中，错误的是（D）
   A、只能在构造方法中使用this调用其它的构造方法，不能在成员方法中使用。
   B、在构造方法中，使用this调用构造方法的语句必须位于第一行，且只能出现一次。
   C、this 关键字可以用于区分成员变量与局部变量。
   D、this 可以出现在任何方法中。
   - **解析：** 在 **静态方法（static 方法）** 中，**不能使用 `this`**，因为 `this` 表示当前对象实例，而静态方法不依赖于对象实例。

2. 阅读下列程序：

   ```java
   class Test {
       private static String name;
       static {
           name = "World";
           System.out.print(name);
       }
       public static void main(String[] args) {
           System.out.print("Hello");
           Test test = new Test();
       }
   }
   ```

   下列选项中，程序运行结果是（B）
   A、HelloWorld
   B、WorldHello
   C、Hello
   D、World

3. 下列关于构造方法的描述中，错误的是（D）
   A、构造方法的方法名必须和类名一致。
   B、构造方法不能写返回值类型。
   C、构造方法可以重载。
   D、构造方法的访问权限必须和类的访问权限一致。

4. 被声明为private，protected 及 public 的类成员，在类外部可以被访问的成员是（A）
   A、只能访问到声明为public的成员
   B、只可能访问到声明为protected和public的成员
   C、都可以访问
   D、都不能访问

   **`public`**：公开访问级别，任何其他类都可以访问。
   **`protected`**：受保护访问级别，同一包内的类和所有子类可以访问。
   **`private`**：私有访问级别，仅在定义它的类内部可以访问。
   **无修饰符（包级私有）**：默认访问级别，同一包内的类可以访问，但其他包的类无法访问。

5. 阅读下列程序：
   ```java
   class A{
       int x;
       static int y;
       void fac(String s){
           System.out.println(“字符串：”+s);
       }
   }
   ```
   下列选项中描述正确的是（B）
   A、x,y和s都是成员变量
   B、x是实例变量，y是类变量，s是局部变量
   C、x和y是实例变量，s是参数
   D、x,y和s都是实例变量

#### 四、简答题（重复3）

1. **请简述你对面向对象的三大特征的理解。**
   面向对象的特点主要可以概括为封装性、继承性和多态性。
   其中封装是面向对象核心思想，将对象的属性和行为封装起来，不需要让外界知道具体实现细节，这就是封装思想。
   继承性主要描述的是类与类之间的关系，通过继承，可以在无需重新编写原有类的情况下，对原有类的功能进行扩展。
   多态性指的是在程序中允许出现重名现象，它指在一个类中定义的属性和方法被其它类继承后，它们可以具有不同的数据类型或表现出不同的行为，这使得同一个属性和方法在不同的类中具有不同的语义。

2. **请简述成员变量与局部变量的区别。**
   在 Java中，定义在类中的变量被称为成员变量。定义在方法中的变量被称为局部变量。如果在某一个方法中定义的局部变量与成员变量同名，这种情况是允许的。此时，在方法中通过变量名访问到的是局部变量，而并非成员变量。

#### 五、编程题（重复3）

定义一个表示学生信息的类Student，要求如下：
（1）类Student 的成员变量：
sNo 表示学号；sName表示姓名；sSex表示性别；sAge表示年龄；sJava：表示Java课程成绩。
（2）类Student 带参数的构造方法：
在构造方法中通过形参完成对成员变量的赋值操作。
（3）类Student 的方法成员：
 getNo（）：获得学号；
 getName（）：获得姓名；
 getSex（）：获得性别；
 getAge（）获得年龄；
 getJava（）：获得Java 课程成绩
根据类Student的定义，创建五个该类的对象，输出每个学生的信息，计算并输出这五个学生Java语言成绩的平均值，以及计算并输出他们Java语言成绩的最大值和最小值。
**Student.java**

```java
public class Student {
    private String sNo;
    private String sName;
    private String sSex;
    private int sAge;
    private int sJava;
    // getter & setter 方法
    public String getsNo() {
        return sNo;
    }
    public void setsNo(String sNo) {
        this.sNo = sNo;
    }
    public String getsName() {
        return sName;
    }
    public void setsName(String sName) {
        this.sName = sName;
    }
    public String getsSex() {
        return sSex;
    }
    public void setsSex(String sSex) {
        this.sSex = sSex;
    }
    public int getsAge() {
        return sAge;
    }
    public void setsAge(int sAge) {
        this.sAge = sAge;
    }
    public int getsJava() {
        return sJava;
    }
    public void setsJava(int sJava) {
        this.sJava = sJava;
    }
    public Student(String sNo, String sName, String sSex, int sAge, int sJava) {
        this.sNo = sNo;
        this.sName = sName;
        this.sSex = sSex;
        this.sAge = sAge;
        this.sJava = sJava;
    }
}
```

**Test.java**

```java
public class Test {
    public static void main(String[] args) {
        Student[] students = new Student[5];
        students[0] = new Student("220110", "Tom", "男", 18, 85);
        students[1] = new Student("220111", "Tohm", "男", 18, 82);
        students[2] = new Student("220112", "Tomf", "女", 18, 79);
        students[3] = new Student("220113", "WTom", "男", 18, 85);
        students[4] = new Student("220114", "seTom", "男", 18, 90);
        int sum = 0;
        int average = 0;
        int max = students[0].getsJava();
        int min = students[0].getsJava();
        for (Student student : students) {
            int java = student.getsJava();
            sum += java;
            if (max < java) {
                max = java;
            }
            if (min > java) {
                min = java;
            }
        }
        average = sum / (students.length);
        System.out.println("Java 语言的平均成绩是:" + average);
        System.out.println("Java 语言成绩的最大值是:" + max);
        System.out.println("Java 语言成绩的最小值是:" + min);
    }
}
```

### 第4章 面向对象（下）

#### 一、填空题（重复4）

1. Java中一个类最多可以继承`1`个类。
2. 在继承关系中，子类会自动继承父类中的方法，但有时在子类中需要对继承的方法进行一些修改，即对父类的方法进行`重写`。
3. `final`关键字可用于修饰类、变量和方法，它有“这是无法改变的”或者“最终”的含义。
4. Java提供了一个关键字`instanceof`，可以判断一个对象是否为某个类(或接口)的实例或者子类实例。
5. 一个类如果要实现一个接口，可以通过关键字`implements`来实现这个接口。

#### 二、判断题（重复4）

1. Exception类称为异常类，它表示程序本身可以处理的错误，在开发Java程序中进行的异常处理，都是针对Exception类及其子类。
   - **答案：对**

2. 在try…catch语句中，try语句块存放可能发生异常的语句。
   - **答案：对**

3. 当一个类实现接口时，没有必要实现接口中的所有方法。
   - **答案：错**

4. 父类的引用指向自己子类的对象是多态的一种体现形式。
   - **答案：对**

5. 方法重写时，子类抛出的异常类型大于等于父类抛出的异常类型。
   - **答案：错**

#### 三、选择题（重复4）

1. 下面程序运行的结果是（B）

```java
class Demo{
	public static void main(String[] args){
		int x= div(1,2);
		try{
		}catch(Exception e){
			System.out.println(e);
		}
		System.out.println(x);
	}
	public static int div(int a,int b){
		return a/b;
	}
}
```

- A、输出 1
- B、输出 0
- C、输出 0.5
- D、编译失败

2. 现有两个类A、B，以下描述中表示B继承自A的是（D）

- A、class A extends B.class
- B、class B implements A
- C、class A implements B
- D、class B extends A

3. 函数重写与函数重载的相同之处是（B）

- A、权限修饰符
- B、函数名
- C、返回值类型
- D、形参列表

4. 下列关于接口的说法中，错误的是（D）

- A、接口中定义的方法默认使用“public abstract”来修饰
- B、接口中的变量默认使用“public static final”来修饰
- C、接口中的所有方法都是抽象方法
- D、接口中定义的变量可以被修改

- **解析：**
  **A、`interface`**
  是接口的关键字，用于**声明接口**
  **B、`implements`**
  是接口的关键字，用于**类实现接口**。
  **D、`default`**
  是接口的关键字（Java 8+），用于定义接口的**默认方法**

5. 阅读下段代码：

```java
class Dog{
public String name;
Dog(String name){
this.name=name;
}
}
public class Demo1{
public static void main(String[] args){
Dog dog1= new Dog("xiaohuang");
Dog dog2= new Dog("xiaohuang");
String s1= dog1.toString();
String s2= dog2.toString();
String s3="xiaohuang";
String s4="xiaohuang";
}
}
```

返回值为true的是（C）

- A、dog1.equals(dog2)
- B、s1.equals(s2)
- C、s3.equals(s4)
- D、dog1 == dog2

#### 四、简答题（重复4）

1. **请简述Java中继承的概念以及使用继承的好处。**
   - 继承是指在一个现有类的基础上构建一个新的类，新类被称为子类，原有类被称为父类。子类会自动拥有父类的所有可继承属性和方法。通过继承可以在无需重新编写原有类的情况下扩展其功能，这提高了代码复用性和维护性。

2. **简要概述多态的作用。**
   - 多态允许应用程序不必为每一个子类编写功能调用，只需要对抽象父类进行处理即可，大大提高程序的可复用性。子类的功能可以被父类的方法或引用变量所调用，这叫向后兼容，可以提高可扩充性和可维护性。使用多态还可以解决项目中紧耦合的问题，提高程序的扩展性。

#### 五、编程题（重复4）

某公司的雇员分为以下若干类：
(1) Employee：这是所有员工总的父类。
① 属性：员工的姓名,员工的生日月份
② 方法：getSalary(int month) 根据参数月份来确定工资，如果该月员工过生日，则公 司会 额外奖励100 元。
(2) SalariedEmployee：Employee 的子类，拿固定工资的员工。
① 属性：月薪。 (3)HourlyEmployee：Employee 的子类，按小时拿工资的员工，每月工作超出160小时 的部分按照1.5 倍工资发放。
① 属性：每小时的工资、每月工作的小时数。
(4) SalesEmployee：Employee 的子类，销售，工资由月销售额和提成率决定。
① 属性：月销售额、提成率。
(5) BasePlusSalesEmployee：SalesEmployee 的子类，有固定底薪的销售人员，工资由底 薪加 上销售提成部分。
① 属性：底薪。 要求： 创建一个Employee 数组，分别创建若干不同的Employee对象，并打 印某个月的工资。
**注意：要求把每个类都做成完全封装，不允许非私有化属性。**

```java
abstract class Employee {
    private String name; // 定义姓名name并私有化属性
    private int month; // 定义生日月份month并私有化属性

    public Employee() {}

    public Employee(String name, int month) {
        this.name = name;
        this.month = month;
    }

    public String getName() {
        return name; // 返回name属性
    }

    public int getMonth() {
        return month; // 返回month属性
    }

    public void setName(String name) {
        this.name = name; // 本类中的属性name
    }

    public void setMonth(int month) {
        this.month = month; // 本类中的属性month
    }

    public double getSalary(int month) {
        double salary = 0; // 定义工资变量
        if (this.month == month) {
            salary += 100;
        }
        return salary;
    }
}

class SalariedEmployee extends Employee {
    private double monthSalary; // 封装monthSalary属性

    public SalariedEmployee() {}

    public SalariedEmployee(String name, int month, double monthSalary) {
        super(name, month);
        this.monthSalary = monthSalary;
    }

    public double getMonthSalary() {
        return monthSalary;
    }

    public void setMonthSalary(double monthSalary) {
        this.monthSalary = monthSalary;
    }

    @Override
    public double getSalary(int month) {
        double salary = monthSalary + super.getSalary(month);
        return salary;
    }
}

// 其他子类类似定义

public class Test {
    public static void main(String[] args) {
        Employee[] employees = new Employee[]{
            new SalariedEmployee("张三", 1, 6000),
            // 添加其他员工实例
        };

        for (Employee employee : employees) {
            System.out.println(Math.round(employee.getSalary(10)));
        }
    }
}
```

### 第5章 Java API

#### 一、填空题（重复5）

1. 在Java中定义了两个类来封装对字符串的操作，它们分别是`String`和`StringBuffer`。
2. 在程序中，获取字符串长度的方法是`length()`。
3. Math类中，用于获取一个数的绝对值的方法是`Math.abs()`。
4. java.util包中的Random类的作用是可以在指定的取值范围内随机产生数字。
5. Instant类代表的是某个时间。其内部是由两个`Long字段`组成，第一部分保存的是`标准Java计算时代（就是1970年1月1日开始）`到现在的秒数，第二部分保存的是`纳秒数`。

#### 二、判断题（重复5）

1. String对象和StringBuffer对象都是字符串变量，创建后都可以修改。
   - **答案：错**
   - **​解析​**​：String对象不可修改，StringBuffer对象可修改。

2. Math.round(double d)方法的作用是将一个数四舍五入，并返回一个double数。
   - **答案：错**

3. StringBuffer类和String类一样，都是不可变对象。
   - **答案：错**

4. Pattern类用于创建一个正则表达式，也可以说创建一个匹配模式，它的构造方法是私有的，不可以直接创建。
   - **答案：对**

5. 每次使用java命令启动虚拟机都对应一个Runtime实例，并且只有一个实例。
   - **答案：对**

#### 三、选择题（重复5）

1. 以下关于String类的常见操作中，哪个是方法会返回指定字符ch在字符串中最后一次出现位置的索引（B）
   - A、int indexOf(int ch)
   - B、int lastIndexOf(int ch)
   - C、int indexOf(String str)
   - D、int lastIndexOf(String str)

2. String s="itcast"; 则s.substring(3,4)返回的字符串是以下选项中的那个？（C）
   - A、ca
   - B、c
   - C、a
   - D、as

3. 下列选项中，可以正确实现String初始化的是（A）
   - A、String str="abc";
   - B、String str='abc';
   - C、String str= abc;
   - D、String str= 0;

4. 下面关于Math.random()方法生成的随机数，正确的是哪项（A）
   - A、0.8652963898062596
   - B、-0.2
   - C、3.0
   - D、1.2

5. 下列选项中，哪个是程序正确的输出结果？（A）

```java
class StringDemo{
public static void main(String[] args){
	String s1= “a”; String s2= “b”;
	show(s1,s2);
	System.out.println(s1+s2);
	}
	public static void show(String s1,String s2){
		s1= s1+”q”;
		s2= s2+ s1;
	}
}
```

- A、ab
- B、aqb
- C、aqbaq
- D、aqaqb

#### 四、简答题（重复5）

1. **简述StringBuffer和StringBuilder有什么区别。**
   - `StringBuffer`类和`StringBuilder`类的对象都可以被多次修改，并不产生新的未使用对象。`StringBuilder`类是JDK5中新加的类，它与`StringBuffer`之间最大不同在于`StringBuilder`的方法不是线程安全的，也就是说`StringBuffer`可以被同步访问，而`StringBuilder`不能。

2. **简述8种基本数据类型及其对应的包装类。**

| 基本数据类型 | 对应的包装类 |
| :----------: | :----------: |
|     byte     |     Byte     |
|     char     |  Character   |
|     int      |   Integer    |
|    short     |    Short     |
|     long     |     Long     |
|    float     |    Float     |
|    double    |    Double    |
|   boolean    |   Boolean    |

#### 五、编程题（重复5）

1. 编写一个每次随机生成10个0（包括）到100之间的随机正整数。

```java
public static void main(String args[]){
    for(int i=0;i<10;i++){
        System.out.println(new Random().nextInt(101));
    }
}
```

2. 编写一个程序，实现字符串大小写的转换并倒序输出。要求如下:
   - 使用for循环将字符串“ITcastHeiMa”从最后一个字符开始遍历。
   - 遍历的当前字符如果是大写字符，就使用toLowerCase()方法将其转换为小写字符，反之则使用toUpperCase()方法将其转换为大写字符。
   - 定义一个StringBuffer对象，调用append()方法依次添加遍历的字符，最后调用StringBuffer对象的toString()方法，并将得到的结果输出。

```java
public class Test01{
    public static void main(String[] args){
        String str="ITcastHeiMa";
        char[] ch= str.toCharArray();
        StringBuffer buffer= new StringBuffer();
        for(int i=str.length()-1; i>=0; i--){
            if(ch[i]>='A'&& ch[i]<='Z'){
                buffer.append(String.valueOf(ch[i]).toLowerCase());
            } else if(ch[i]>='a'&& ch[i]<='z'){
                buffer.append(String.valueOf(ch[i]).toUpperCase());
            }
        }
        System.out.println(buffer.toString());
    }
}
```

### 第6章 集合类

#### 一、填空题（重复6）

1. `Collection`是所有单列集合的父接口，它定义了单列集合（List和Set）通用的一些方法。
2. 使用Iterator遍历集合时，首先需要调用`hashNext()`方法判断是否存在下一个元素，若存在下一个元素，则调用`next()`方法取出该元素。
3. List集合的主要实现类有`ArrayList`、`LinkedList`，Set集合的主要实现类有`HashSet`、`TreeSet`，Map集合的主要实现类有`HashMap`、`TreeMap`。
4. Map接口是一种双列集合，它的每个元素都包含一个键对象`Key`和值对象`Value`，键和值对象之间存在一种对应关系，称为映射。
5. ArrayList内部封装了一个长度可变的`数组`。

#### 二、判断题（重复6）

1. Set集合通过键值对的方式来存储对象。
   - **答案：错**

2. ArrayList集合查询元素的速度很快，但是增删改查效率较低。
   - **答案：对**

3. Set接口主要有两个实现类，分别是HashSet和TreeSet。
   - **答案：对**

4. Map接口是一种双列集合，它的每个元素都包含一个键对象Key和值对象Value。
   - **答案：对**

5. Lambda表达式只能是一个语句块。
   - **答案：错**

#### 三、选择题（重复6）

1. 以下哪些集合可以保存具有映射关系的数据（BC）
   - A、ArrayList
   - B、TreeMap
   - C、HashMap
   - D、TreeSet

2. 下列关于LinkedList类的方法，不是从List接口中继承而来的是（B）
   - A、toArray()
   - B、pop()
   - C、remove()
   - D、isEmpty()

3. 以下属于Map接口集合常用方法的有（ABCD）
   - A、boolean containsKey(Object key)
   - B、Collection values()
   - C、void forEach(BiConsumer action)
   - D、boolean replace(Object key, Object value)

4. 使用Iterator时，判断是否存在下一个元素可以使用以下哪个方法（D）
   - A、next()
   - B、hash()
   - C、hasPrevious()
   - D、hasNext()

5. 阅读下面的代码：

```java
public class Example{
    public static void main(String[] args){
        String[] strs={"Tom","Jerry","Donald"};
        for(String str: strs){
            str="Tuffy";
        }
        System.out.println(strs[0]+","+ strs[1]+","+ strs[2]);
    }
}
```

程序的运行结果是（C）

- A、Tom,Jerry
- B、Tom,Jerry, Tuffy
- C、Tom,Jerry,Donald
- D、以上都不对

#### 四、简答题（重复6）

1. **简述集合List、Set和Map的区别。**
   - `List`的特点是元素有序、可重复。`List`接口的主要实现类有`ArrayList`和`LinkedList`。
   - `Set`的特点是元素无序、不可重复。`Set`接口的主要实现类有`HashSet`和`TreeSet`。
   - `Map`的特点是存储的元素是键(Key)、值(Value)映射关系，元素都是成对出现的。`Map`接口的主要实现类有`HashMap`和`TreeMap`。

2. **简述为什么ArrayList的增删操作比较慢，查找操作比较快。**
   - 由于`ArrayList`集合的底层是使用一个数组来保存元素，在增加或删除指定位置的元素时，会导致创建新的数组，效率比较低，因此不适合做大量的增删操作。但这种数组的结构允许程序通过索引来访问元素，因此使用`ArrayList`集合查找元素很便捷。

#### 五、编程题（重复6）

1. 请按照下列要求编写程序。
   （1） 编写一个Student类，包含name和age属性，提供有参构造方法。 （2） 在Student类中，重写toString()方法，输出age和name的值。
   （3） 在Student类中，重写hashCode()和equals()方法 a.hashCode()的 返回值是name 的hash值与age的和。b.equals()判断对象的name和age是否相同，相同则返回true不同返 回false。
   （4）最后编写一个测试类，创建一个HashSet对象hs，向 hs中添加多个Student 对象，假设有两个Student对象相等，输出HashSet，观察是否添加成功。

```java
class Student {
    private int age;
    private String name;

    public Student(int age, String name) {
        this.age = age;
        this.name = name;
    }

    @Override
    public String toString() {
        return age + ":" + name;
    }

    @Override
    public int hashCode() {
        return name.hashCode() + age;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (!(obj instanceof Student))
            return false;
        Student stu = (Student) obj;
        return this.name.equals(stu.name) && this.age == stu.age;
    }
}

public class Test {
    public static void main(String[] args) {
        HashSet<Student> hs = new HashSet<>();
        hs.add(new Student(18, "zhangsan"));
        hs.add(new Student(20, "lisa"));
        hs.add(new Student(20, "lisa"));
        System.out.println(hs);
    }
}
```

2. 请按照下列提示编写一个泛型接口以及其实现类。
   提示：
   （1）创建一个泛型接口Generic，并创建一个抽象方法get(Tt)；
   （2）创建一个实现类GenericImpl，空实现get(Tt)方法。

```java
interface Generic<T> {
    public abstract void get(T t);
}

class GenericImpl<T> implements Generic<T> {
    public void get(T t) {
    }
}
```

### 第7章 IO（输入输出）

#### 一、填空题（重复7）

1. Java中的I/O流，按照传输数据的不同，可分为`字节流`和`字符流`。
2. File类中`java.io`包中唯一代表磁盘文件本身的对象，它定义了一些与平台无关的方法用于操作文件。
3. 计算机中，无论是文本、图片、音频还是视频，所有文件都是以`二进制(字节)`形式存在的。
4. IO提供两个带缓冲的字节流，分别是`BufferedInputStream`和`BufferedOutputStream`。
5. 在JDK中提供了两个类可以将字节流转换为字符流，它们分别是`InputStreamReader`和`OutputStreamWriter`。

#### 二、判断题（重复7）

1. 如果一个File表示目录下有文件或者子目录，调用delete()方法也可以将其删除。
   - **答案：错**

2. File类提供了一系列方法，用于操作其内部封装的路径指向的文件或者目录，boolean exists()方法是判断文件或目录是否存在。
   - **答案：对**

3. JDK提供了两个抽象类InputStream和OutputStream，它们是字节流的顶级父类，所有的字节输入流都继承自InputStream，所有的字节输出流都继承自OutputStream。
   - **答案：错**

4. InputStreamReader是Reader的子类，它可以将一个字节输出流转换成字符输出流。
   - **答案：错**

#### 三、选择题（重复7）

1. 下列选项中，哪些是标准输入输出流？（AB）
   - A、System.In
   - B、System.Out
   - C、InputStream
   - D、OutputStream

2. File类中以字符串形式返回文件绝对路径的方法是哪一项？（C）
   - A、getParent()
   - B、getName()
   - C、getAbsolutePath()
   - D、getPath()

3. 下列选项中，哪个流使用到了缓冲技术？（A）
   - A、BufferedOutputStream
   - B、FileInputStream
   - C、DataOutputStream
   - D、FileReader

4. 在程序开发中，经常需要对文本文件的内容进行读取，如果想从文件中直接读取字符便可以使用字符输入流（C）
   - A、Reader
   - B、Writer
   - C、FileReader
   - D、FileWriter

5. File类提供了一系列方法，用于操作其内部封装的路径指向的文件或者目录，当File对象对应的文件不存在时，使用哪个方法将新建的一个File对象指定到新文件中。（C）
   - A、String getAbsolutePath()
   - B、boolean canRead()
   - C、boolean createNewFile()
   - D、boolean exists()

#### 四、简答题（重复7）

1. **简述字符流与字节流的区别。**
   - 字节流的两个基类是InputStream和OutputStream，字符流的两个基类是Reader和Writer，它们都是Object类的直接子类。字节流是处理以8位字节为基本单位的字节流类；Reader和Writer类是专门处理16位字节的字符流类。

2. **简述InputStreamReader类与OutputStreamWriter类的作用。**
   - InputStreamReader是Reader的子类，它可以将一个字节输入流转换成字符输入流，方便直接读取字符。OutputStreamWriter是Writer的子类，它可以将一个字节输出流转换成字符输出流，方便直接写入字符。

#### 五、编程题（重复7）

编写一个程序，分别使用字节流和字符流拷贝一个文本文件。要求如下:

- 使用FileInputStream、FileOutputStream和FileReader、FileWriter分别进行拷贝。
- 使用字节流拷贝时，定义一个1024长度的字节数组作为缓冲区，使用字符流拷贝。

```java
import java.io.*;

public class Test01 {
    public static void main(String[] args) throws Exception {
        // 字节流拷贝
        FileInputStream in = new FileInputStream("E:/src.txt");
        FileOutputStream out = new FileOutputStream("E:/des1.txt");
        byte[] buf = new byte[1024];
        int len;
        while ((len = in.read(buf)) != -1) {
            out.write(buf, 0, len);
        }
        in.close();
        out.close();

        // 字符流拷贝
        BufferedReader bf = new BufferedReader(new FileReader("E:/src.txt"));
        BufferedWriter bw = new BufferedWriter(new FileWriter("E:/des2.txt"));
        String str;
        while ((str = bf.readLine()) != null) {
            bw.write(str);
            bw.newLine();
        }
        bf.close();
        bw.close();
    }
}
```

### 第8章 多线程

#### 一、填空题（重复8）

1. 实现多线程的两种方式是继承`Thread`类和实现`Runnable`接口。
2. 线程的整个生命周期分为5个阶段，分别是新建状态（New）、就绪状态（Runnable）、运行状态（Running）、阻塞状态和死亡状态。
3. Thread类中的`start()`方法用于开户一个新线程，当新线程启动后，系统会自动调用`run()`方法。
4. 执行`sleep()`方法，可以让线程在规定的时间内休眠。
5. 同步代码块使用`synchronized`关键字来修饰。

#### 二、判断题（重复8）

1. 当我们创建一个线程对象时，该对象表示的线程就立即开始运行。
   - **答案：错**

2. 静态方法不能使用synchronized关键字来修饰。
   - **答案：错**

3. 对Java程序来说，只要还有一个前台线程在运行，这个进程就不会结束。
   - **答案：对**

4. 实现Runnable接口比继承Thread类创建线程的方式扩展性更好。
   - **答案：对**

5. 使用synchronized关键字修饰的代码块，被称作同步代码块。
   - **答案：对**

#### 三、选择题（重复8）

1. 下列有关线程的创建方式说法错误的是（C）
   - A、通过继承Thread类与实现Runnable接口都可以创建多线程程序
   - B、实现Runnable接口相对于继承Thread类来说，可以避免由于Java的单继承带来的局限性
   - C、通过继承Thread类与实现Runnable接口创建多线程这两种方式没有区别
   - D、大部分的多线程应用都会采用实现Runnable接口方式创建

2. 下列关于线程优先级的描述，错误的是（C）
   - A、NORM_PRIORITY代表普通优先级，默认值是5
   - B、一般情况下，主函数具有普通优先级
   - C、新建线程的优先级默认为最低
   - D、优先级高的线程获得先执行权的几率越大

3. 下面关于join()方法描述正确的是（D）
   - A、join()方法是用于线程休眠
   - B、join()方法是用于线程启动
   - C、join()方法是用于线程插队
   - D、join()方法是用于线程同步

4. Java多线程中，关于解决死锁的方法说法错误的是（D）
   - A、避免存在一个进程等待序列{P1，P2，…，Pn}，其中P1等待P2所占有的某一资源，P2等待P3所占有的某一源，…...，而Pn等待P1所占有的的某一资源，可以避免死锁
   - B、打破互斥条件，即允许进程同时访问某些资源，可以预防死锁，但是，有的资源是不允许被同时访问的，所以这种办法并无实用价值
   - C、打破不可抢占条件。即允许进程强行从占有者那里夺取某些资源。就是说，当一个进程已占有了某些资源，它又申请新的资源，但不能立即被满足时，它必须释放所占有的全部资源，以后再重新申请。它所释放的资源可以分配给其它进程。这样可以避免死锁
   - D、使用打破循环等待条件（避免第一个线程等待其它线程，后者又在等待第一个线程）的方法不能避免线程死锁

5. 对于线程的生命周期，下面四种说法正确的有哪些?(多选)(BC)
   - A、调用了线程的start()方法，该线程就进入运行状态
   - B、线程的run()方法运行结束或被未catch的InterruptedException等异常终结，那么该线程进入死亡状态
   - C、线程进入死亡状态,但是该线程对象仍然是一个Thread对象,在没有被垃圾回收器回收之前仍可以像引用其他对象一样引用它
   - D、线程进入死亡状态后，调用它的start()方法仍然可以重新启动

#### 四、简答题（重复8）

1. **简述创建多线程的两种方式。**
   - 一种是继承`java.lang`包下的`Thread`类，覆写`Thread`类的`run()`方法，在`run()`方法中实现运行在线程上的代码。
   - 另一种就是实现`java.lang.Runnable`接口，同样是在`run()`方法中实现运行在线程上的代码。

2. **简述同步代码块的作用。**
   - 同步代码块的作用是控制线程，保证同步代码块中只能有一个线程在运行，保证了多线程操作数据的安全性。

#### 五、编程题（重复8）

模拟三个老师同时给50个小朋友发苹果，每个老师相当于一个线程。

```java
public class Test01 {
    public static void main(String[] args) {
        Teacher t = new Teacher();
        new Thread(t, "陈老师").start();
        new Thread(t, "高老师").start();
        new Thread(t, "李老师").start();
    }
}

class Teacher implements Runnable {
    private int notes = 50;

    public void run() {
        while (true) {
            dispatchNotes();
            if (notes <= 0) {
                break;
            }
        }
    }

    private synchronized void dispatchNotes() {
        if (notes > 0) {
            try {
                Thread.sleep(10); // 经过的线程休眠10毫秒
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println(Thread.currentThread().getName() + "---发出的苹果" + notes--);
        }
    }
}
```

### 第9章 网络编程

#### 一、填空题（重复9）

1. 传输层主要使网络程序进行通信，在进行网络通信时，可以采用TCP协议，也可以采用`UDP`协议。
2. 在下载文件时必须采用`TCP`协议。
3. JDK提供了一个`DatagramSocket`类，该类可以发送和接收DatagramPacket数据包。
4. 在JDK中提供了两个用于实现TCP程序的类，一个是`ServerSocket`类，用于表示服务器端；一个是Socket类，用于表示客户端。
5. 当客户端和服务端建立连接后，数据是以`IO流`的形式进行交互的，从而实现通信。

#### 二、判断题（重复9）

1. Socket类用于创建客户端程序，当两个Socket建立了专线连接后，连接的一端既能向另一端连续写入字节，也能从另一端读取字节。
   - **答案：对**

2. 在TCP程序中，ServerSocket类的实例对象可以实现一个服务器端的程序。
   - **答案：对**

3. DatagramSocket类中提供了accept()方法用于接收数据报包。
   - **答案：错**

4. byte[] buf= new byte \[ 1024 ]\;用于定义1024个字节数组的缓冲区。
   - **答案：对**

5. Socket类的getInputStream()返回一个InputStream类型的输入流对象，如果该对象是由服务器端的Socket返回，就用于读取服务端发送的数据。
   - **答案：对**

#### 三、选择题（重复9）

1. 下列有关网络通信的说法错误的是（D）
   - A、可以通过TCP协议进行可靠的网络通信
   - B、UDP协议适用于需要快速传输且不要求可靠性的场合
   - C、ServerSocket类用于服务器端监听客户端连接请求
   - D、DatagramSocket类中提供了accept()方法用于接收数据报包

2. 下列选项中，哪个不是接口的关键字？（C）
   - A、interface
   - B、implements
   - C、extends
   - D、default

3．下列关于UDP协议特点的描述中，错误的是（ D ）

- A、在UDP协议中，数据的发送端和接收端不建立逻辑连接。
- B、UDP协议消耗资源小，通信效率高，通常都会用于音频、视频和普通数据的传输。
- C、UDP协议在传输数据时不能保证数据的完整性，因此在传输重要数据时不建议使用 UDP协议。
- D、在UDP协议连接中，必须要明确客户端与服务器端。

4．下列说法中，错误的是（ B ）

- A、UDP在数据传输时，数据的发送端和接收端不建立逻辑连接。
- B、使用UDP协议传送数据保证了数据的完整性。
- C、TCP协议是面向连接的通信协议。
- D、TCP连接中必须要明确客户端与服务器端，由客户端向服务端发出连接请求。

5．在TCP/IP 网络中，为各种公共服务和系统保留的端口号范围是（ C ）

- A、0~65525
- B、0~1024
- C、0~1023
- D、0~80

#### 四、简答题（重复9）

1. **请简述UDP通信与TCP通信的区别。**
   - UDP通信与TCP通信的区别在于，UDP中只有发送端和接收端，不区分客户端与 服务器端，计算机之间可以任意地发送数据；而TCP通信是严格区分客户端与服务器端的， 在通信时，必须先由客户端去连接服务器端才能实现通信，服务器端不可以主动连接客户端， 并且服务器端程序需要事先启动，等待客户端的连接。

2. **请简述TCP连接的“三次握手”。**
   - 在TCP连接中必须要明确客户端与服务器端，由客户端向服务器端发出连接请求， 每次连接的创建都需要经过“三次握手”。
     - 第一次握手，客户端向服务器端发出连接请求， 等待服务器确认；
     - 第二次握手，服务器端向客户端回送一个响应，通知客户端收到了连接请 求；
     - 第三次握手，客户端再次向服务器端发送确认信息，确认连接。

#### 五、编程题（重复9）

使用基于UDP的Java Socket编程，完成在线咨询功能：
（1）客户向咨询人员咨询。
（2）咨询人员给出回答。
（3）客户和咨询人员可以一直沟通，直到客户发送bye给咨询人员。

```java
// AskServer.java
//在线客服咨询人员
public class AskServer {
    public static void main(String[] args) {
    //创建DatagramSocket，发送接收数据都依赖他
        DatagramSocket socket = null;
        try {
            socket = new DatagramSocket(8888);
            Scanner input = new Scanner(System.in);
            while (true) {
            //准备一个空的数据包，用来接收数据
                byte[] buf = new byte[1024];
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                //接收数据使用空的数据包
                socket.receive(packet);
                String info = new String(packet.getData(), 0, packet.getLength());
                System.out.println("客户端请求：" + info);
                //判断是否退出
                if ("bye".equals(info)) {
                    break;
                }
                //发送数据
                String result = input.nextLine();
                byte[] buf2 = result.getBytes();
                DatagramPacket packet2 = new DatagramPacket(buf2, buf2.length, packet.getAddress(), packet.getPort());
                socket.send(packet2);
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
        //关闭socket
            socket.close();
        }
    }
}

// AskClient.java
//在线客服客户
public class AskClient {
    public static void main(String[] args) {
    //创建DatagramSocket，发送接收数据都依赖他
        DatagramSocket socket = null;
        try {
            socket = new DatagramSocket(9999);
            Scanner input = new Scanner(System.in);
            while (true) {
                String str = input.nextLine();
                byte[] buf = str.getBytes();
                DatagramPacket packet = new DatagramPacket(buf, buf.length, InetAddress.getByName("192.168.1.252"), 8888);
                socket.send(packet);
                if ("bye".equals(str)) {
                    break;
                }
                byte[] buf2 = new byte[1024];
                DatagramPacket packet2 = new DatagramPacket(buf2, buf2.length);
                socket.receive(packet2);
                System.out.println("服务器端反馈：" + new String(packet2.getData(), 0, packet2.getLength()));
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            socket.close();
        }
    }
}
```

### 第10章 JDBC

#### 一、填空题（重复10）

1. JDBC驱动管理器专门负责注册特定的JDBC驱动器，主要通过`java.sql.DriverManager`类实现。
2. 在编写JDBC应用程序时，必须要把指定数据库驱动程序或类库加载到`classpath`中。
3. Statement接口的executeUpdate(String sql)方法用于执行SQL中的insert、`update`和delete语句。
4. PreparedStatement是Statement的子接口，用于执行`预编译`的SQL语句。
5. ResultSet接口中定义了大量的getXXX()方法，如果使用字段的索引来获取指定的数据，字段的索引是从`1`开始编号的。

#### 二、判断题（重复10）

1. 应用程序可以直接与不同的数据库进行连接，而不需要依赖于底层数据库驱动。
   - **答案：错**

2. Statement接口的execute(String sql)返回值是boolean，它代表sql语句的执行是否成功。
   - **答案：错**

3. PreparedStatement是Statement的子接口，用于执行预编译的SQL语句。
   - **答案：对**

4. 使用DriverManager.registerDriver进行驱动注册时，将导致数据库驱动被注册1次。
   - **答案：错**

5. PreparedStatement接口中的setDate()方法可以设置日期内容，但参数Date的类型必须是java.util.Date。
   - **答案：错**

#### 三、选择题（重复10）

1. 下面关于JDBC驱动器API与JDBC驱动器关系的描述，正确的是（A）
   - A、JDBC驱动器API是接口，而JDBC驱动器是实现类
   - B、JDBC驱动器API内部包含了JDBC驱动器
   - C、JDBC驱动器内部包含了JDBC驱动器API
   - D、JDBC驱动器是接口，而JDBC驱动器API是实现类

2. JDBC API主要位于下列选项的那个包中（A）
   - A、java.sql.\*
   - B、java.util.\*
   - C、javax.lang.\*
   - D、java.text.\*

3. 下面选项中，用于将参数化的SQL语句发送到数据库的方法是（B）
   - A、prepareCall(String sql)
   - B、prepareStatement(String sql)
   - C、registerDriver(Driver driver)
   - D、createStatement()

4. 下面选项，关于ResultSet中游标指向的描述正确的是（B）
   - A、ResultSet对象初始化时，游标在表格的第一行
   - B、ResultSet对象初始化时，游标在表格的第一行之前
   - C、ResultSet对象初始化时，游标在表格的最后一行之前
   - D、ResultSet对象初始化时，游标在表格的最后一行

5. 下列选项中，能够实现预编译的是（C）
   - A、Statement
   - B、Connection
   - C、PreparedStatement
   - D、DriverManager

#### 四、简答题（重复10）

1. **简述JDBC编程的6个开发步骤。**
   - 加载并注册数据库驱动；
   - 通过DriverManager获取数据库连接；
   - 通过Connection对象获取Statement对象；
   - 使用Statement执行SQL语句；
   - 操作ResultSet结果集；
   - 回收数据库资源。

2. **简述什么是预编译。**
   所谓预编译,就是说当相同的SQL语句再次执行时,数据库只需使用缓冲区中的数据,而不需要对SQL语句再次编译,从而有效提高数据的访问效率。

### 第11章 GUI

#### 一、填空题（重复11）

1. 向BorderLayout的布局管理器添加组件时，如果不指定添加到哪个区域，则默认添加到`CENTER`区域。
2. FlowLayout的构造方法FlowLayout(int align)中，参数align决定组件在每行中相对于`容器边界`的对齐方式。
3. 在程序中可以通过调用容器对象的`setLayout()`方法设置布局管理器。
4. 使用GridBagLayout布局管理器的关键在于`GridBagConstraints`对象，它才是控制容器中每个组件布局的核心类。
5. 如果多个JRadioButton按钮都要添加到面板和按钮组中，当为它们添加事件监听时，会有很多重复代码，因此可以把这些重复的代码抽取到`一个公共的方法`中。

#### 二、判断题（重复11）

1. 在应用程序中，当对窗体事件进行处理时，首先需要定义一个类实现WindowEvent接口作为窗体监听器。
   - **答案：错**

2. BorderLayout边界布局管理器可以将容器划分为四个区域。
   - **答案：错**

3. GridLayout布局管理器会将容器分成n行m列大小相等的网格，每个网格中可以放置多个组件。
   - **答案：错**

4. JRadioButton是一个对于JRadioButton按钮来说，当一个按钮被选中时，先前被选中的按钮就会自动取消选中。
   - **答案：对**

5. JTextField称为文本框，它只能接收单行文本的输入。
   - **答案：对**

#### 三、选择题（重复11）

1. JTextField的构造方法中，方法JTextField(String text, int column)的作用是（D）。
   - A、创建一个空的文本框，初始字符串为null
   - B、创建一个具有指定列数的文本框，初始字符串为null
   - C、创建一个显示指定初始字符串的文本框
   - D、创建一个具有指定列数，并显示指定初始字符串的文本框

2. 若想实现JRadioButton按钮之间的互斥，需要使用（A）类。
   - A、ButtonGroup
   - B、JComboBox
   - C、AbstractButton
   - D、以上都不行

3. 下列选项中，关于GridLayout（网格布局管理器）的说法错误的是（C）。
   - A、GridLayout布局管理器可以设置组件的大小
   - B、放置在GridLayout布局管理器中的组件将自动占据网格的整个区域
   - C、GridLayout布局管理器中，组件的相对位置不随区域的缩放而改变，但组件的大小会随之改变，组件始终占据网格的整个区域
   - D、GridLayout布局管理器缺点是总是忽略组件的最佳大小，所有组件的宽高都相同

4. FlowLayout的三个构造方法中，FlowLayout(int align, int hgap, int vgap)的作用是（C）。
   - A、组件默认居中对齐，水平、垂直间距默认为5个单位
   - B、指定组件相对于容器的对齐方式，水平、垂直间距默认为5个单位
   - C、指定组件的对齐方式和水平、垂直间距
   - D、与容器的开始端对齐方式一样

5. 下列选项中，关于BorderLayout边界布局管理器的说法错误的是（C）。
   - A、向BorderLayout布局管理器的容器中添加组件时需要使用add(Component comp, Object constraints)方法
   - B、add(Component comp, Object constraints)方法参数constraints是Object类型的
   - C、向BorderLayout的布局管理器添加组件时默认添加到SOUTH区域
   - D、BorderLayout的布局管理器的每个区域只能放置一个组件

#### 四、简答题（重复11）

1. **请简述使用GridBagLayout布局管理器的主要步骤。**
   - 创建GridbagLayout布局管理器，并使容器采用该布局管理器。
   - 创建GridBagConstraints对象（布局约束条件），并设置该对象的相关属性。
   - 调用GridBagLayout对象的setConstraints()方法建立GridBagConstraints对象和受控组件之间的关联。
   - 向容器中添加组件。

2. **请简述创建和添加下拉式菜单的主要步骤。**
   - 创建一个JMenuBar菜单栏对象，将其放置在JFrame窗口的顶部。
   - 创建JMenu菜单对象，将其添加到JMenuBar菜单栏中。
   - 创建JMenuItem菜单项，将其添加到JMenu菜单中。

#### 五、编程题（重复10）

要求使用GUI技术编写一个运算器，能实现两数加、减、乘、除，有运算、清除、退 出功能。运算器界面如图11-1所示。

![image.png](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202506010115958.png)

CalTest.java

```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CalTest extends JFrame {
    private TextField firText, secText, reText;
    private JLabel eqLabel;
    private JComboBox jbox;
    private String[] str;
    private Button calb, clearb, exitb;
    private Panel p, p2;

    public static void main(String[] args) {
        new CalTest("运算器");
    }

    public CalTest() {}

    public CalTest(String title) {
        setTitle(title);
        setLocation(500, 200);
        setDefaultCloseOperation(3);
        setResizable(false);
        setLayout(new FlowLayout());
        init();
        pack();
        setVisible(true);
    }

    public void init() {
        p = new Panel();
        p.setSize(300, 300);

        firText = new TextField(5);
        secText = new TextField(5);
        reText = new TextField(5);
        reText.setEditable(false);
        eqLabel = new JLabel("=");

        str = new String[]{"+", "-", "*", "/"};
        jbox = new JComboBox(str);

        p.add(firText);
        p.add(jbox);
        p.add(secText);
        p.add(eqLabel);
        p.add(reText);
        add(p);

        p2 = new Panel();

        calb = new Button("cal");
        calb.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                String sign = (String) jbox.getSelectedItem();
                if (sign.equals("+")) {
                    int num = Integer.parseInt(firText.getText());
                    int num2 = Integer.parseInt(secText.getText());
                    int add = num + num2;
                    reText.setText(add + "");
                } else if (sign.equals("-")) {
                    int num = Integer.parseInt(firText.getText());
                    int num2 = Integer.parseInt(secText.getText());
                    int sup = num - num2;
                    reText.setText(sup + "");
                } else if (sign.equals("*")) {
                    int num = Integer.parseInt(firText.getText());
                    int num2 = Integer.parseInt(secText.getText());
                    int sel = num * num2;
                    reText.setText(sel + "");
                } else {
                    int num = Integer.parseInt(firText.getText());
                    int num2 = Integer.parseInt(secText.getText());
                    int sele = num / num2;
                    reText.setText(sele + "");
                }
            }
        });

        clearb = new Button("clear");
        clearb.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                firText.setText(null);
                secText.setText(null);
                reText.setText(null);
            }
        });

        exitb = new Button("exit");
        exitb.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent arg0) {
                System.exit(0);
            }
        });

        p2.add(calb);
        p2.add(clearb);
        p2.add(exitb);
        add(p2, BorderLayout.SOUTH);
    }
}
```

### 第12章 反射

#### 一、填空题（重复12）

1. 反射机制的优点是可以实现`动态`创建对象和编译。
2. 如果想通过Class类实例化其他类的对象，则可以使用`newInstance()`方法，但是必须要保证被实例化的类中存在一个无参构造方法。
3. 通过反射可以得到一个类的完整结构，包括类的构造方法、类的属性、类的方法，这就需要用到java.lang.reflect包中的以下几个类，分别是`Constructor`、`Field`和`Method`。
4. 要取得一个类所实现的全部接口，必须使用Class中的`getInterfaces()`方法。
5. JVM在加载.class文件时，会产生一个`Class`对象代表该.class字节码文件，从该Class对象中可以获得类的信息。

#### 二、判断题（重复12）

1. 将Class对象实例化为本类对象时，可以通过无参构造完成，也可以通过有参构造完成。
   - **答案：对**

2. 要取得一个类中的全部方法，可以使用Class类中的getMethods()方法。
   - **答案：对**

3. 在反射机制中，把类中的成员（构造方法、成员方法、成员变量）都封装成了对应的类进行表示。
   - **答案：对**

4. Class类的对象用于表示当前运行的Java应用程序中的类和接口，Class类是一个未继承Object类的特殊类。
   - **答案：错**

5. JAVA反射机制是在运行状态中，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意一个方法；这种动态获取的信息以及动态调用对象的方法的功能称为java语言的反射机制。
   - **答案：对**

#### 三、选择题（重复12）

1. 如何获取一个类的字节码文件对象。（D）
   - A、对象名.class
   - B、类名.getClass()
   - C、Object类中的forName()方法
   - D、以上说法都不正确

2. 关于反射机制下列说法错误的是（C）
   - A、反射可以获取类中所有的属性和方法
   - B、反射可以构造类的对象，并获取其私有属性的值
   - C、反射机制指的是在程序编译期间，通过.class文件加载并使用一个类的过程
   - D、暴力反射可以获取类中私有的属性和方法

3. 下列关于通过反射方式获取方法并执行的过程说法正确的是 （B）
   - A、通过对象名.方法名(参数列表)的方式调用该方法
   - B、通过Class.getMethod(方法名，参数类型列表)的方式获取该方法
   - C、通过Class.getDeclaredMethod(方法名，参数类型列表)获取私有方法
   - D、通过invoke(对象名, 参数列表)方法来执行一个方法

4. 以下哪些方法在Class类中定义？（多选）（AC）
   - A．getConstructors()
   - B．getPrivateMethods()
   - C．getDeclaredFields()
   - D．getImports()
   - E．setField()

5. 假定Tester类有如下test()方法：public int test(int p1, Integer p2)，以下哪段代码能正确地动态调用一个Tester对象的test方法？（C）
   - A、
     Class classType=Tester.class; Object tester=classType.newInstance(); Method addMethod=classType.getMethod("test",new Class[]{int.class,int.class}); Object result=addMethod.invoke(tester,new Object[]{new Integer(100),new Integer(200)});
   - B、
     Class classType=Tester.class; Object tester=classType.newInstance(); Method addMethod=classType.getMethod("test",new Class[]{int.class,int.class}); int result=addMethod.invoke(tester,new Object[]{new Integer(100),new Integer(200)});
   - C、
     Class classType = Tester.class; Object tester = classType.newInstance(); Method addMethod = classType.getMethod("test", new Class[]{int.class, Integer.class}); Object result = addMethod.invoke(tester, new Object[]{new Integer(100), new Integer(200)});
   - D、
     Class classType=Tester.class;
     Object tester=classType.newInstance();
     Method addMethod=classType.getMethod("test",new Class[]{int.class,Integer.class});
     Integer result=addMethod.invoke(tester,new Object[]{new Integer(100),new Integer(200)});

#### 四、简答题（重复12）

1. **简述一下反射机制。**

   Java的反射（reflection）机制是指在程序的运行状态中，可以构造任意一个类的对象，可以得到任意一个对象所属的类的信息，可以调用任意一个类的成员变量和方法，可以获取任意一个对象的属性和方法。这种动态获取程序信息以及动态调用对象的功能称为Java语言的反射机制。

2. **简述实例化Class对象的三种方式。**

   实例化Class对象共有以下三种方式：
   - 根据类名获取：类名.class；
   - 根据对象获取：对象.getClass()；
   - 根据全限定类名获取：Class.forName("全限定类名")。
