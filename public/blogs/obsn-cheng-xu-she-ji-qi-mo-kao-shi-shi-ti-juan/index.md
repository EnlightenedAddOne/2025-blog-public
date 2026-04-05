# 《Java程序设计》期末考试试题卷（A）

> 来源：Obsidian/10-学业与考试/期末复习资料/大二下/Java/《Java程序设计》期末考试试题卷（A）.md

## 一、单项选择题（每小题2分，共10题共计20分）

1. 在JDK的bin目录下有许多可执行文件，其中`java.exe`命令的作用是（ ）
   - A. Java文件编译器
   - B. Java源文件
   - C. Java虚拟机
   - **D. Java启动器**

2. 语句`int x=2`, 三元表达式 `x>0?x+1:5`（ ）
   - A. 0
   - B. 2
   - **C. 3**
   - D. 5

3. 下列关于对象的类型转换的描述，说法错误的是（ ）
   - A.对象的类型转换可通过自动转换或强制转换进行
   - B.无继承关系的两个类的对象之间试图转换会出现编译错误
   - **C.由 new 语句创建的父类对象可以强制转换为子类的对象**
   - D.子类的对象转换为父类类型后，父类对象不能调用子类的特有方法

4. 下列哪个类是所有异常类的父类。（ ）
   - **A. Throwable**
   - B. Error
   - C. Exception
   - D. RuntimeException

5. 下列（ ）叙述是正确的?
   - A.Java 应用程序由若干个类所构成，这些类必须在一个源文件
   - **B.Java 应用程序由若干个类所构成，这些类可以在一个源文件中，也可以在若干个源文件中，其中必须有源文件含有主类。**
   - C.Java 源文件必须含有主类。
   - D. Java 源文件如果含有主类，主类必须是 public 类。

6. 以下关于 String 类的常见操作中,哪个是方法会返回指定字符 ch 在字符串中最后一次出现位置的索引（ ）
   - A. indexOf(String str)
   - B. lastIndexOf(String str)
   - C. indexOf(int ch)
   - **D. lastIndexOf(int ch)**

7. 下列关于 ArrayList 的描述中，错误的是（ ）
   - A.ArrayList 集合可以看作一个长度可变的数组
   - B.ArrayList 集合不适合做大量的增删操作
   - C.ArrayList 集合查找元素非常便捷
   - **D.ArrayList 集合中的元素索引从1开始**

8. 下列选项中，能够实现预编译的是（ ）
   - A. Statement
   - B. Connection
   - **C. PreparedStatement**
   - D. DriverManager

9. 以下哪种原因不会导致线程暂停运行（ ）
   - A.等待
   - B.阻塞
   - C. 休眠
   - **D.挂起及由于 I/0 操作而阻塞**

10. 面向对象编程语言的三大特性不包括（ ）
    - A. 封装性
    - **B.抽象性**
    - C. 继承性
    - D.多态性

## 二、程序阅读与改错（每小题5分，共4题20分）

1. **该程序段演示了 ArrayList 的用法，但( )处代码可能有误，正确的请答√，错误的请答X并改正，改正时要求完整重写本行代码，否则不得分。**

```java
public class Demo {
    public static void main(String[] args) {
	    // 创建Araylis 集合
        ArrayList list = new ArrayList<Integer>(); // (1)❌
		//更正: ArrayList<Integer> list = new ArrayList<Integer>();

        // 向该集合中添加整数元素1,2和3
	    list.add(1);
        list.add(new Integer(2)); // (2)
        list.add(3);

        // 创建 Iterator 对象
        Iterator iterator = list.iterator(); // (3)❌
        //更正: Iterator iterator = list.iterator();

        // 判断是否还有下一个元素
        while (iterator.hasNext()) { // (4)
            Integer i = (Integer) iterator.next(); // (5)
            System.out.println(i);
        }
    }
}

```

2. **下边的程序演示了数据连接与断开数据库连接的操作，并把这两个功能封装到了Dbutil中，用到的数据库Mysql5.0版本，数据库名称是db_book**

```java
import java.sql.Connection;
import java.sql.DriverManager;

public class DBUtil {
    private String dbUrl = "jdbc:mysql://localhost:3306/db_book";
    private String dbUserName = "root"; // 用户名
    private String dbPassword = "123456"; // 密码
    private String jdbcName = "com.mysql.jdbc.Driver"; // (1)

    public Connection getCon() throw Exception {     // (2)❌
    //更正: throws

        Class.forName(jdbcName); // (3)
        Connection con = DriverManager.getConnection(dbUrl);    // (4)❌ 缺少用户名密码
        return con;
    }

    public void closeCon(Connection con) throws Exception {
        if (con != null) {
            con.close();// (5)
        }
    }

    public static void main(String[] args) {
        DBUtil dbUtil = new DBUtil();
        try {
            dbUtil.getCon();
            System.out.println("数据库连接成功！");
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("数据库连接失败！");
        }
    }
}

```

## 三、程序设计题（2小题，第1小题20分，第2小题40分，共60分）

1. 首先定义一个基本几何图形的基类（Shape）`Shape`类定义为普通类，包括String类型的`name`属性，定义方法：

- `double getArea()`计算面积
- `double getLength()`计算周长

然后定义其子类`Circle`实现以上方法。要求通过主函数输出各图形的面积和周长。（正方形、圆），测试代码要体现代码的多态性

```java
abstract class Shape {
    String name;

    public Shape(String name) {
        this.name = name;
    }

    abstract double getArea();
    abstract double getLength();
}

class Circle extends Shape {
    double radius;

    public Circle(String name, double radius) {
        super(name);
        this.radius = radius;
    }

    double getArea() {
        return Math.PI * radius * radius;
    }

    double getLength() {
        return 2 * Math.PI * radius;
    }
}

class Square extends Shape {
    double side;

    public Square(String name, double side) {
        super(name);
        this.side = side;
    }

    double getArea() {
        return side * side;
    }

    double getLength() {
        return 4 * side;
    }
}

public class TestShape {
    public static void main(String[] args) {
        Shape[] shapes = {
            new Circle("圆形", 5),
            new Square("正方形", 4)
        };

        for (Shape s : shapes) {
            System.out.println(s.name + " 面积: " + s.getArea() + "，周长: " + s.getLength());
        }
    }
}

```

2. 体操比赛（`Gymnastics`类）和学校考察（`School`类）分别实现`getAverage()`方法，体操比赛需要先去掉一个最高分和最低分再计算，而学校不需要，他们都继承接口`ComputerAverage`，使用多态特性调用实现类方法。

```java
interface ComputerAverage {
    double getAverage(double[] scores);
}

class Gymnastics implements ComputerAverage {
    public double getAverage(double[] scores) {
        if (scores.length <= 2) return 0;
        double max = scores[0], min = scores[0], sum = 0;
        for (double s : scores) {
            sum += s;
            if (s > max) max = s;
            if (s < min) min = s;
        }
        return (sum - max - min) / (scores.length - 2);
    }
}

class School implements ComputerAverage {
    public double getAverage(double[] scores) {
        double sum = 0;
        for (double s : scores) sum += s;
        return sum / scores.length;
    }
}

public class TestAverage {
    public static void main(String[] args) {
        double[] scores = {9.5, 8.0, 7.5, 9.0, 6.0};

        ComputerAverage ca1 = new Gymnastics();
        ComputerAverage ca2 = new School();

        System.out.println("体操比赛平均分: " + ca1.getAverage(scores));
        System.out.println("学校考察平均分: " + ca2.getAverage(scores));
    }
}

```
