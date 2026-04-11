> 来源：Obsidian/10-学业与考试/期末复习资料/大二下/Java/Java课本程序题.md

# 案例2-1 库房出入货物程序设计

## 案例介绍

### 任务描述

现要对华为和小米两种手机产品进行入库，本案例要求编写一个模拟商品入库的程序，可以在控制台输入入库商品的数量，最后打印出仓库中所有商品详细信息以及所有商品的总库存数和库存商品总金额。

### 商品信息

- 品牌型号
- 尺寸
- 价格
- 配置
- 库存
- 总价

## 案例目标

- 学会分析”库房出入货物”任务实现的逻辑思路。
- 能够独立完成”库房出入货物”程序的源代码编写、编译以及运行。
- 能够在程序中使用算术运算符进行运算操作。
- 能够在程序中使用赋值运算符进行赋值操作。
- 掌握Java中的变量和运算符的知识点。

## 案例思路

1. 查看运行结果后，可以将该程序分为3部分实现（商品入库、库存清单、总库存数与库存商品总金额）
2. 商品入库是变化的数据，需要记录商品信息后打印。通过运行结果，我们可以分析出如下属性：
   - 品牌型号：商品的名称，`String`类型。
   - 尺寸：手机的大小，`double`类型。
   - 价格：手机的单价，`double`类型。
   - 配置：手机的内存等配置，`String`类型。
   - 库存数：此项数据为用户输入的数据，用户输入需要使用`Scanner`类。
   - 总价：经过计算后打印，可以设置单独的变量，`double`类型。
3. 库存清单中又包含了3部分，顶部为固定的数据，直接打印；中部为变化的数据，与商品入库的数据一致，打印出所有商品的详情，底部也为固定样式，直接打印即可。
4. 总库存数与库存商品总金额是统计操作，需经过计算后打印，可以设置两个单独的变量：所有商品的库存总数：`int`类型；库存商品总金额：`double`类型。

## 案例实现

```java
package chapter0201;
import java.util.Scanner;

public class access {
    public static void main(String[] args) {
        /*
         * 现在有两款手机华为与小米需要做入库处理，我们需要编写一个程序来实现商品的入库，
         * 入库完成后，打印入库商品的详细信息并计算出入库商品的数量与入库商品总金额。
         */
        // 华为手机
        String huaweiBrand = "华为";
        double huaweiSize = 5.5;
        double huaweiPrice = 3688.88;
        String huaweiConfig = "8+128g 全面刘海屏";
        // 小米手机
        String xiaomiBrand = "小米";
        double xiaomiSize = 5.0;
        double xiaomiPrice = 2988.88;
        String xiaomiConfig = "4+64g 全面屏";

        // 华为手机入库
        System.out.println("品牌型号：" + huaweiBrand);
        System.out.println("尺寸：" + huaweiSize);
        System.out.println("价格：" + huaweiPrice);
        System.out.println("配置：" + huaweiConfig);
        Scanner sc1 = new Scanner(System.in);
        System.out.println("请输入" + huaweiBrand + "手机的库存");
        int huanweiCount = sc1.nextInt();
        double huaweiTotal = huanweiCount * huaweiPrice;
        System.out.println("库存" + huaweiBrand + "手机的总金额:" + huaweiTotal);

        // 小米手机入库
        System.out.println("品牌型号：" + xiaomiBrand);
        System.out.println("尺寸：" + xiaomiSize);
        System.out.println("价格：" + xiaomiPrice);
        System.out.println("配置：" + xiaomiConfig);
        System.out.println("请输入" + xiaomiBrand + "手机的库存");
        int xiaomiCount = sc1.nextInt();
        double xiaomiTotal = xiaomiCount * xiaomiPrice;
        System.out.println("库存" + xiaomiBrand + "手机的总金额：" + xiaomiTotal);

        // 库存清单
        System.out.println("------------库存清单------------");
        System.out.println("品牌型号 尺寸 价格 配置 库存数量 总价");
        System.out.println(huaweiBrand + "       " + huaweiSize + "   " + huaweiPrice + "  " + huaweiConfig + "      " + huanweiCount + "       " + huaweiTotal);
        System.out.println(xiaomiBrand + "       " + xiaomiSize + "    " + xiaomiPrice + "      " + xiaomiConfig + "       " + xiaomiCount + "       " + xiaomiTotal);
        System.out.println("---------------------------------");

        // 总库存数量与库存总价
        int total = huanweiCount + xiaomiCount;
        double totalMoney = huaweiTotal + xiaomiTotal;
        System.out.println("总库存：" + total);
        System.out.println("库存总价：" + totalMoney + "￥");
    }
}
```

# 案例2-2 小明都可以买什么

## 案例介绍（重复2）

### 任务描述（重复2）

编写一个智能购物计算小程序，在一家商店有书本、铅笔、橡皮、可乐、零食五种商品，商品价格如下表所示：

| 商品名称 | 价格 |
| -------- | ---- |
| 书本     | 12元 |
| 铅笔     | 1元  |
| 橡皮     | 2元  |
| 可乐     | 3元  |
| 零食     | 5元  |

假如你带了20元，且必须购买一本书，剩余的钱还可以购买哪种商品，可以购买几件，购买完后又能剩余多少钱？

## 运行结果

任务运行结果如图2-2所示。

## 案例目标（重复2）

- 学会分析"智能购物"程序的实现思路
- 根据思路独立完成”智能购物”的源代码编写、编译及运行。
- 掌握在程序中使用switch条件语句进行运算操作。

## 案例思路（重复2）

1. 从任务描述中可知，要实现此功能，我们需要先定义5种商品，定义五个`int`值作为这五种商品的价格。
2. 从运行结果可知，我们需要先打印各个商品的价格以及带了多少钱，并选择需要购买商品的序列号。
3. 选择到序列号后，我们需要使用switch条件语句进行判断用户要购买那件商品，并在switch条件语句中，计算可以购买多少其他商品和剩余多少钱。

## 案例实现（重复2）

```java
package chapter0202;
import java.util.Scanner;

public class shopping {
    public static void main (String[] args) {
        /*
         * 假如你有20元，至少需要购买1本书，剩余的钱还可以购买那些东西。
         */
        int pencil = 1;   //铅笔价格
        int rubber = 2;   //橡皮价格
        int cola = 3;     //可乐价格
        int book = 12;    //书本价格
        int snacks = 5;   //零食价格

        System.out.println("书本的价格为" + book + "元，您总共有20元");
        System.out.println("1.铅笔的价格为：" + pencil + "元");
        System.out.println("2.橡皮的价格为：" + rubber + "元");
        System.out.println("3.可乐的价格为：" + cola + "元");
        System.out.println("4.零食的价格为：" + snacks + "元");

        Scanner sc1 = new Scanner(System.in);
        System.out.println("请输入其他需要购买商品的序列号：");
        int id = sc1.nextInt();

        switch (id){
            case 1:
                int pencilmoney = 20 - book;
                int pencilsum = pencilmoney / pencil;
                int pencilsurplus = pencilmoney % pencil;
                System.out.println("购买完书本后还可以购买铅笔" + pencilsum + "个，还剩" + pencilsurplus + "元");
                break;
            case 2:
                int rubbermoney = 20 - book;
                int rubbersum = rubbermoney / rubber;
                int rubbersurplus = rubbermoney % rubber;
                System.out.println("购买完书本后还可以购买橡皮" + rubbersum + "个，还剩" + rubbersurplus + "元");
                break;
            case 3:
                int colamoney = 20 - book;
                int colasum = colamoney / cola;
                int colasurplus = colamoney % cola;
                System.out.println("购买完书本后还可以购买可乐" + colasum + "个，还剩" + colasurplus + "元");
                break;
            case 4:
                int snacksmoney = 20 - book;
                int snackssum = snacksmoney / snacks;
                int snackssurplus = snacksmoney % snacks;
                System.out.println("购买完书本后还可以购买零食" + snackssum + "个，还剩" + snackssurplus + "元");
                break;
            default:
                System.out.println("您的输入有误。");
                break;
        }
    }
}
```

# 【实验2-3】超市购物小程序

## 任务介绍

### 1.任务描述

编写一个超市购物程序，在一家超市有牙刷、毛巾、水杯、苹果和香蕉五种商品，商品价格如下表所示。

| 编号 | 商品名称 | 价格   |
| ---- | -------- | ------ |
| 1    | 牙刷     | 8.8元  |
| 2    | 毛巾     | 10.0元 |
| 3    | 水杯     | 18.8元 |
| 4    | 苹果     | 12.5元 |
| 5    | 香蕉     | 15.5元 |

用户输入商品序列号进行商品购买，用户输入购买数量后计算出所需要花费的钱，一次购买结束后，需要用户输入“Y”或“N”，“Y”代表继续购买，“N”代表购物结束。

### 2.运行结果

任务运行结果如图2-3所示。

![image.png](https://gitee.com/zhangjiayi1219/obsidian_picture/raw/master/img/202506052248948.png)

## 任务目标

- 学会分析“超市购物”程序的实现思路。
- 根据思路独立完成“超市购物”的源代码编写、编译及运行。
- 掌握在程序中使用while循环结构和switch循环结构语句进行运算操作。

## 实现思路

从运行结果可以看出，我们需要先定义5个商品的价格，double类型，再打印出5种商品的价格。

从运行结果可以看出，这里我们让用户填写购买商品的序列号以及购买的数量，需要使用到Scanner类。

从运行结果可以看出，我们循环了选择购买的条件语句，这里使用while嵌套switch语句可以达到我们的目的，我们需要使用while循环switch的选择结构，而switch是判断用户选择购买商品序列号的条件语句。

## 实现代码

超市购物程序的实现代码，如文件2-3所示。

```java
package chapter0203;

import java.util.Scanner;

public class supermarket {

	/*
	 * 模拟商城购物小系统：1.用户选择商品后，后台计算商品价格；
	 *                     2.使用while循环实现用户多次购买商品。
	 */

	  public static void  main (String[] args) {
		       double toothbrush=8.8;   //牙刷价格
		  double towel=10.0;        //毛巾价格
		  double cup=18.8; 		    //水杯价格
		  double apple=12.5;        //苹果价格
		  double banana=15.5;       //香蕉价格
		  int i=0;
		  String a="Y";
		  System.out.println("-------------黑马小商城-------------");
		  System.out.println("1.牙刷的价格为："+toothbrush+"元");
		  System.out.println("2.毛巾的价格为："+towel+"元");
		  System.out.println("3.水杯的价格为："+cup+"元");
		  System.out.println("4.苹果的价格为："+apple+"元");
		  System.out.println("5.香蕉的价格为："+banana+"元");
		  while(a.equals("Y")) {
			  Scanner sc1 = new Scanner(System.in);
			  System.out.println("请输入你需要购买商品的序列号：");
			  i=sc1.nextInt();
			  switch(i){
			  case 1:
				  System.out.println("请输入你需要购买牙刷的数量:");
				  int toothbrushnnumber=sc1.nextInt();
				  double toothbrushnnum=toothbrushnnumber*toothbrush;
				  System.out.println("你购买了牙刷"+toothbrushnnumber+"
                                          支，需要花费"+toothbrushnnum+"元");
				  System.out.println("需要继续购买请输入Y，否则输入N");
				  a=sc1.next();
				  break;
			  case 2:
				  System.out.println("请输入你需要购买毛巾的数量:");
				  int towelnumber=sc1.nextInt();
				  double towelnum=towelnumber*towel;
				  System.out.println("你购买了毛巾"+towelnumber+"个，需要
                                            花费"+towelnum+"元");
				  System.out.println("需要继续购买请输入Y，否则输入N");
				  a=sc1.next();
				  break;
			  case 3:
				  System.out.println("请输入你需要购买水杯的数量:");
				  int cupnumber=sc1.nextInt();
				  double cupnum=cupnumber*cup;
				  System.out.println("你购买了水杯"+cupnumber+"个，需要花
                                             费"+cupnum+"元");
				  System.out.println("需要继续购买请输入Y，否则输入N");
				  a=sc1.next();
				  break;
			  case 4:
				  System.out.println("请输入你需要购买苹果的数量:");
				  int applenumber=sc1.nextInt();
				  double applenum=applenumber*apple;
				  System.out.println("你购买了苹果"+applenumber+"斤，需要
                                            花费"+applenum+"元");
				  System.out.println("需要继续购买请输入Y，否则输入N");
				  a=sc1.next();
				  break;
			  case 5:
				  System.out.println("请输入你需要购买香蕉的数量:");
				  int banananumber=sc1.nextInt();
				  double banananum=banananumber*banana;
				 System.out.println("你购买了香蕉"+banananumber+"斤，需要
                                            花费"+banananum+"元");
				  System.out.println("需要继续购买请输入Y，否则输入N");
				  a=sc1.next();
				  break;
			  }
		  }
		  System.out.println("期待您的下次光临！");
	  }
}
```
