> 来源：Obsidian/30-项目与实践/项目说明/C语言课设/学生学籍管理系统.md

# 要求概述

- 系统以菜单的的方式工作
- 学生籍贯录入功能
- 学生籍贯信息浏览功能
- 查询和排序功能，如按学号查询，按籍贯查询
- 学生籍贯信息的修改和删除

---

# 开发环境

- 系统：Win 11 专业版
- 编译器：Visual Studio 2022
- 编程语言：C 语言

---

# 程序亮点及不足

## 亮点

    1. 本程序使用了 easyx 图形库，使得该管理系统的界面显示的信息更加的清晰。
    2. 由于调用了鼠标操作和键盘操作，使得在进行信息输入的时候也更加的便捷。
    3. 在程序开始运行后先开辟一个指定大小的空间，然后调用Void readStu (Class_t*Class)函数来读取文件信息，将其放在所开辟的空间中，结束运行时再执行IntsaveStu (Class_t* Class)将修改后的信息保存进文件。

## 不足

     1. 在本程序中定义的链表是一个静态的链表，无法根据需求进行空间的开辟。
     2. 在显示学生信息的界面中，有益没有设置换页的功能，导致只能显示一页的学生信息，当学生数据过多时当无法全部显示。
     3. 在主菜单界面，“保存退出” 鼠标点击时判定不准确。

---

# 🔯总流程图

###

---

# 核心代码详解

## void MENU()

此代码为主菜单的界面布局设置，调用了easyx 库中的函数来放置背景图片，同时将在Button. Cpp 函数中配置好的按钮放置在界面上。

## void readStu(Class_t\* Class)

此函数的作用为：读取文件内容，由于创建了存储学生信息的结构体，在主程序运行开始后先为其开辟一个用来存储数据的空间，之后将所开辟的空间地址的头指针传递给此函数，然后该函数开始从文件中读取信息将其读取到所开辟的空间中，在保存文件时，调用与之相对的 int saveStu (Class_t\* Class) 函数将修改之后的内容再次写入文件。

## void button(int x, int y, int w, int h, char\* text)

此函数的作用为：调用easyx 库函数绘制一个矩形，并为其设置颜色、大小、坐标，并通过函数计算文字坐标使其居中显示。设计此函数的目的是让其作为主界面的选择菜单，通过鼠标点击相应的按钮来跳转到各个界面来执行相应的功能，从而简化操作流程。

## int main(int argc, char const\* argv[])

由于在其他文件里设置好了各个函数，再在主函数里调用，使得主函数较为简短，其主要功能为：检测鼠标和键盘的消息，通过读取鼠标或键盘的操作来完成函数的调用，从而执行不同的操作。

# 数据结构设计

## 学生信息数据

定义了两个结构体，分别用来存储学生信息和学生人数

```C
typedef struct Student
{
    char num[20];//学生学号
    char name[20];//学生姓名
    char Ethnic_group[20]; // 民族
    char birth_Place[20];  // 出生地
    char Native_place[20]; // 籍贯
} Student_t;

typedef struct Class
{
    Student_t stu_arr[50]; // 这个班级最多有50个学生
    unsigned int index;    // 当前班级学生的个数
} Class_t;                 // 班级的类

```

### 按钮数据信息

```C
struct Button_Set
{
    int num = 7;      //按钮数量
    int bw = 150;    //按钮宽度
    int bh = 40;     //按钮高度
    int bx = (window_width() - bw) / 2-200;         //按钮x坐标
    int by1 = (window_height() - bh * num) / 2-200; //按钮y坐标
};

//学生信息界面按钮配置
struct Stu_Button_Set
{
    int Stunum = 4;      //按钮数量
    int Stubw = 130;    //按钮宽度
    int Stubh = 50;     //按钮高度
    int Stubx1 = 0;         //按钮x坐标
    int Stuby1 = 0; //按钮y坐标
};
```

# 系统模块功能

## 主函数

### main.cpp 文件

^b24793

```C
#include"information.h"
#include "Interface.h"
int main(int argc, char const* argv[])
{
    draw_window();

    int choose = 0;
    int id = 0;
    int code = 0;
    int chose = 0;

    Class_t* Class = (Class_t*)malloc(sizeof(Class_t));//开辟空间，静态

    if (Class == NULL)
    {
        printf("开辟空间失败!\n");
        return -1;
    }

    Class->index = 0;

    MENU();//绘制主界面
    int jiemian = 1;
    readStu(Class);//读取文件
    ExMessage msg;
    struct Button_Set BS;//按钮配置
    while (true) {
        window_beginDraw;
        if (peekmessage(&msg, EM_MOUSE | EM_KEY)) {
            switch (msg.message)
            {

            case WM_LBUTTONDOWN:
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 0 && msg.y <= BS.by1 + BS.bh * 0 + BS.bw)
                {
                    //搜索信息
                    window_clear();
                    chose = 1;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 1 && msg.y <= BS.by1 + BS.bh * 1 + BS.bw)
                {
                    //显示信息
                    chose = 2;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 2 && msg.y <= BS.by1 + BS.bh * 2 + BS.bw)
                {
                    //添加信息
                    chose = 3;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 3 && msg.y <= BS.by1 + BS.bh * 3 + BS.bw)
                {
                    //删除信息
                    chose = 4;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 4 && msg.y <= BS.by1 + BS.bh * 4 + BS.bw)
                {
                    //5.排序
                    chose = 5;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 5 && msg.y <= BS.by1 + BS.bh * 5 + BS.bw)
                {
                    //6.修改
                    chose = 6;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 6 && msg.y <= BS.by1 + BS.bh * 6 + BS.bw)
                {
                    //7.保存退出
                    chose = 7;
                }
                if (msg.x >= BS.bx && msg.x <= BS.bx + BS.bw && msg.y >= BS.by1 + BS.bh * 7 && msg.y <= BS.by1 + BS.bh * 7 + BS.bw)
                {
                    //7.保存退出
                    chose = 8;
                }

                break;
            case  WM_KEYDOWN:
                if (msg.vkcode == VK_ESCAPE) {
                    chose = 8;

                }
                break;

            default:
                break;
            }

        }
        switch (chose)
        {
        case 1:
            search(Class);
            chose = 8;
            break;
        case 2:

            display(Class);
            chose = 8;
            break;
        case 3:

            add(Class);
            chose = 8;
            break;
        case 4:
            del(Class);
            display(Class);
            chose = 8;
            break;
        case 5:
            sort(Class);
            display(Class);
            chose = 8;
            break;
        case 6:
            modify(Class);
            chose = 8;
            break;
        case 7:
            Exit(Class);
            break;
        case 8:
            MENU();
            break;
        default:
            break;
        }

        window_flushDraw();
    }
    window_endDraw();
    return 0;
}

```

^ecb65d

## 文件读写操作

### 读取文件

#### Information. Cpp 文件

```C
#include"information.h"

//读取学生信息
void readStu(Class_t* Class) {
    int i = 0;
    FILE* fp;
    fp = fopen("students.txt", "a+");
    if (fp == NULL) {
        printf("文件打开失败!\n");
        exit(0);
    }

    fscanf(fp, "%d", &Class->index);  //读取文件首行的学生人数，并储存在index
    for (i = 0; i < Class->index; i++) {
        fscanf(fp, "%s %s %s %s %s", Class->stu_arr[i].num, Class->stu_arr[i].name, Class->stu_arr[i].Ethnic_group, Class->stu_arr[i].birth_Place, Class->stu_arr[i].Native_place);
    }
    fclose(fp);
    printf("导入学生信息成功!\n");
}

//保存学生信息
int saveStu(Class_t* Class) {
    int i = 0;
    if (Class->index == 0) {
        printf("还没有学生，请输入\n");
        return -1;
    }
    FILE* fp;
    fp = fopen("students.txt", "w");
    if (fp == NULL) {
        printf("文件打开失败!\n");
        exit(0);
    }

    fprintf(fp, "%d\n", Class->index);
    for (i = 0; i < Class->index; i++) {
        fprintf(fp, "%s %s %s %s %s\n", Class->stu_arr[i].num, Class->stu_arr[i].name, Class->stu_arr[i].Ethnic_group, Class->stu_arr[i].birth_Place, Class->stu_arr[i].Native_place);
    }
    fclose(fp);
    printf("写入成功!\n");
}
```

#### Information. H 文件

```C
#ifndef __INFORMATION_H__
#define __INFORMATION_H__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Student
{
    char num[20];//学生学号
    char name[20];//学生姓名
    char Ethnic_group[20]; // 民族
    char birth_Place[20];  // 出生地
    char Native_place[20]; // 籍贯
} Student_t;

typedef struct Class
{
    Student_t stu_arr[50]; // 这个班级最多有50个学生
    unsigned int index;    // 当前班级学生的个数
} Class_t;                 // 班级的类

void readStu(Class_t* Class);//读取学生信息
int saveStu(Class_t* Class);//保存学生信息

#endif
```

## 界面设计

### 主界面菜单及函数

#### Interface. Cpp 文件

```C
#include "Interface.h"

IMAGE  m_bk;

//切换后的界面颜色
void jiemian()
{
    setbkcolor(RGB(25, 34, 41));
}

//提示消息居中显示
void news_middle(char* text) {
    window_clear();
    outtextxy((window_width() - textwidth(text)) / 2, (window_height() - textheight(text)) / 2-100, text);
}

void  MENU()
{
    loadimage(&m_bk, "./m_bk.jpg", window_width(), window_height());
    putimage(0, 0, &m_bk);
    struct Button_Set BS;
    char s[8][50] = { "搜索信息","显示信息","添加信息", "删除信息","信息排序","修改信息" , "保存退出"};
    for (int i = 0; i < BS.num; i++) {
        button(BS.bx, BS.by1 + BS.bh * i, BS.bw, BS.bh, s[i]);
    }

}

//1.搜索
int search(Class_t* Class) {
    char name[20];
    int i;
    struct Stu_Button_Set stuBS;
    if (Class->index == 0)
    {
        news_middle((char *)"还没有学生，请输入");
        //printf("还没有学生，请输入：\n");
        return -1;
    }
    char chose[10];
    InputBox(chose, 10, "1.姓名查找 2.学号查找 3.出生地查找", "请输入要查询学生信息的方式", NULL, 0, 0);

    if (strcmp(chose, "1") == 0) {
        InputBox(name, 20, "姓名", "请输入要查询的学生姓名", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].name) == 0) {

                char s[5][25] = { "学号","姓名","民族","出生地","户籍", };
                for (int k = 0; k < 5; k++) {
                    button(stuBS.Stubx1 + stuBS.Stubw * k, stuBS.Stuby1, stuBS.Stubw, stuBS.Stubh, s[k]);
                }
                button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
                button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
                button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
                button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
                button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);
                break;
            }
        }
        if (i == Class->index) {
            news_middle((char*)"没有该学员");

            //printf("没有该学员！");
        }
    }
    if (strcmp(chose, "2") == 0) {
        InputBox(name, 20, "学号", "请输入要查询的学生学号", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].num) == 0) {

                char s[5][25] = { "学号","姓名","民族","出生地","户籍", };
                for (int k = 0; k < 5; k++) {
                    button(stuBS.Stubx1 + stuBS.Stubw * k, stuBS.Stuby1, stuBS.Stubw, stuBS.Stubh, s[k]);
                }
                button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
                button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
                button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
                button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
                button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);
                break;
            }
        }
        if (i == Class->index) {
            news_middle((char*)"没有该学员");

            //printf("没有该学员！");
        }
    }

    if (strcmp(chose, "3") == 0) {
        InputBox(name, 20, "出生地", "请输入要查询的学生出生地", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].birth_Place) == 0) {

                char s[5][25] = { "学号","姓名","民族","出生地","户籍", };
                for (int k = 0; k < 5; k++) {
                    button(stuBS.Stubx1 + stuBS.Stubw * k, stuBS.Stuby1, stuBS.Stubw, stuBS.Stubh, s[k]);
                }
                button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
                button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
                button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
                button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
                button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);
                break;
            }
        }
        if (i == Class->index) {
            news_middle((char*)"没有该学员");

            //printf("没有该学员！");
        }
    }

    system("pause");
    return 0;

}

//2.显示学生信息
int display(Class_t* Class) {

    struct Stu_Button_Set stuBS;

    // 表头
    char s[5][25] = { "学号","姓名","民族","出生地","户籍",};
    for (int i = 0; i < 5; i++) {
        button(stuBS.Stubx1 + stuBS.Stubw * i, stuBS.Stuby1 , stuBS.Stubw, stuBS.Stubh, s[i]);
    }

    int i;
    if (Class->index == 0) {
        news_middle((char*)"还没有学生，请输入");
        printf("还没有学生，请输入\n");
        return -1;
    }
    for (i = 0; i < Class->index; i++)
    {
        button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
        button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
        button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
        button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
        button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);

        printf("学号:%-10s 姓名：%-10s 民族：%-10s 出生地：%-10s 籍贯：%-10s\n", Class->stu_arr[i].num, Class->stu_arr[i].name, Class->stu_arr[i].Ethnic_group, Class->stu_arr[i].birth_Place, Class->stu_arr[i].Native_place);
    }
    system("pause");
    return 0;

}

//3.添加学生信息
int add(Class_t* Class) {
    Student_t stu;
BEGIN:

    InputBox(stu.num,20, "学号","请输入学生学号信息：",  NULL,0,0);
    InputBox(stu.name, 20, "姓名","请输入学生姓名信息：",  NULL, 0, 0);
    InputBox(stu.Ethnic_group, 20, "民族","请输入学生民族信息：",  NULL, 0, 0);
    InputBox(stu.birth_Place, 20,"出生地", "请输入学生出生地信息：",  NULL, 0, 0);
    InputBox(stu.Native_place, 20, "户籍","请输入学生户籍信息：",  NULL, 0, 0);
    printf("请输入学生的 学号、姓名、民族、出生地、籍贯：\n");

    for (int i = 0; i < Class->index; i++)
    {
        if (strcmp(Class->stu_arr[i].num, stu.num) == 0)
        {
            window_clear();
            printf("该学生已经存在，请重新输入：\n");
            news_middle((char*)"该学生已经存在，请重新输入");

            goto BEGIN;
        }
    }
    Class->stu_arr[Class->index] = stu;
    Class->index++;
    printf("插入成功！\n");
    news_middle((char*)"插入成功");
    system("pause");
    return 0;
}

//4.删除学生信息
int del(Class_t* Class) {

    int i = 0;
    int j = 0;
    char name[20];
    if (Class->index == 0)
    {
        news_middle((char*)"还没有学生，请输入");
        //outtextxy(200, 200, "还没有学生，请输入");
        //printf("还没有学生，请输入\n");
        return -1;      //代表函数非正常终止
    }
    char chose[10];
    InputBox(chose, 20, "1.姓名查找 2.学号查找", "请选择要查找所删除学生的方式", NULL, 0, 0);
    if (strcmp(chose, "1") == 0) {
        InputBox(name, 20, "姓名", "请输入要删除学生的姓名：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++)
        {
            if (strcmp(name, Class->stu_arr[i].name) == 0)
            {
                for (j = i; j < Class->index - 1; j++)
                {
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                }
                Class->index--;
                news_middle((char*)"删除成功!!!");
                //outtextxy(200, 200, "删除成功!!!");
                _getch();
                break;
            }
        }
        //当循环整个班级人数后，没有这个学生
        if (i == Class->index)
        {
            window_clear();
            news_middle((char*)"班级没有这个学员!");
            //outtextxy(200, 200, "班级没有这个学员!");

            return -1;
        }
    }
    if (strcmp(chose, "2") == 0) {
        InputBox(name, 20, "学号", "请输入要删除学生的学号：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++)
        {
            if (strcmp(name, Class->stu_arr[i].num) == 0)
            {
                for (j = i; j < Class->index - 1; j++)
                {
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                }
                Class->index--;
                news_middle((char*)"删除成功!!!");
                //outtextxy(200, 200, "删除成功!!!");
                _getch();
                break;
            }
        }
        //当循环整个班级人数后，没有这个学生
        if (i == Class->index)
        {
            window_clear();
            news_middle((char*)"班级没有这个学员!");
            //outtextxy(200, 200, "班级没有这个学员!");

            return -1;
        }
    }

}

//5.排序
int sort(Class_t* Class) {

    int i, j;
    Student_t temp;
    if (Class->index == 0)
    {
        news_middle((char*)"还没有学生，请输入");
        //outtextxy(200, 200, "还没有学生，请输入");
        return -1;
    }
//BEGIN:
    char chose[10];
    window_clear();
    InputBox(chose, 10, "1.学号 2.户籍 3.姓名", "请选择排序方式", NULL, 0, 0);
    if (strcmp(chose, "1") == 0) {
        for (i = 0; i < Class->index - 1; i++)
        {
            for (j = 0; j < Class->index - 1 - i; j++)
            {
                if (strcmp(Class->stu_arr[j].num, Class->stu_arr[j + 1].num) > 0)
                {
                    temp = Class->stu_arr[j];
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                    Class->stu_arr[j + 1] = temp;
                }

            }
        }
    news_middle((char*)"学号由低到高排序已完成");
    _getch();
    }
    if (strcmp(chose, "2") == 0) {
        for (i = 0; i < Class->index - 1; i++)
        {
            for (j = 0; j < Class->index - 1 - i; j++)
            {
                if (strcmp(Class->stu_arr[j].Native_place, Class->stu_arr[j + 1].Native_place) > 0)
                {
                    temp = Class->stu_arr[j];
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                    Class->stu_arr[j + 1] = temp;
                }

            }
        }
        news_middle((char*)"籍贯由低到高排序已完成");
        _getch();
    }
    if (strcmp(chose, "3") == 0) {
        for (i = 0; i < Class->index - 1; i++)
        {
            for (j = 0; j < Class->index - 1 - i; j++)
            {
                if (strcmp(Class->stu_arr[j].name, Class->stu_arr[j + 1].name) > 0)
                {
                    temp = Class->stu_arr[j];
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                    Class->stu_arr[j + 1] = temp;
                }

            }
        }
        news_middle((char*)"姓名由低到高排序已完成");
        _getch();
    }
    /*else {
        news_middle((char*)"输入错误");
        goto BEGIN;
    }*/

    return 0;

}

//6.修改
int modify(Class_t* Class) {
    char chose[10] ;
    char name[20];
    char Native_Place[20];// 籍贯
    char Ethnic_Group[20]; // 民族
    char Birth_Place[20];  // 出生地

    int i = 0;
    if (Class->index == 0) {
        window_clear();
        news_middle((char*)"还没有学生信息");
        return -1;
    }
    window_clear();
    char chose1[10];
    InputBox(chose1, 10, "1.姓名查找 2.学号查找", "请选择要查找所删除学生信息的方式", NULL, 0, 0);
    if (strcmp(chose1, "1") == 0) {
        InputBox(name, 20, "姓名", "请输入要修改学生的姓名：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].name) == 0) {
                InputBox(chose, 10, "1.民族 2.出生地 3.籍贯", "请选择要修改信息", NULL, 0, 0);
                if (strcmp(chose, "1") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Ethnic_group, Ethnic_Group);
                    window_clear();
                    news_middle((char*)"修改成功");

                }
                if (strcmp(chose, "2") == 0) {
                    InputBox(Birth_Place, 20, "出生地", "请输入要修改的出生地", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].birth_Place, Birth_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                if (strcmp(chose, "3") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Native_place, Native_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                break;
            }
        }
        if (i == Class->index) {
            window_clear();
            news_middle((char*)"没有该学员");

        }

    }

    if (strcmp(chose1, "2") == 0) {
        InputBox(name, 20, "学号", "请输入要修改学生的学号：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].num) == 0) {
                InputBox(chose, 10, "1.民族 2.出生地 3.籍贯", "请选择要修改信息", NULL, 0, 0);
                if (strcmp(chose, "1") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Ethnic_group, Ethnic_Group);
                    window_clear();
                    news_middle((char*)"修改成功");

                }
                if (strcmp(chose, "2") == 0) {
                    InputBox(Birth_Place, 20, "出生地", "请输入要修改的出生地", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].birth_Place, Birth_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                if (strcmp(chose, "3") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Native_place, Native_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                break;
            }
        }
        if (i == Class->index) {
            window_clear();
            news_middle((char*)"没有该学员");

        }

    }

    system("pause");
    return 0;

}

//7.保存退出
void Exit(Class_t* Class) {
    saveStu(Class);//保存
    closegraph();//退出
}

void draw_window()
{
    Window(640, 720, 1);    // 创建绘图窗口，大小为 640x480 像素
    set_window_title("管理系统");//窗口名称
    jiemian();
}

```

#### Interface. H 文件

```C
#ifndef __INFORMATION_H__
#define __INFORMATION_H__
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Student
{
    char num[20];//学生学号
    char name[20];//学生姓名
    char Ethnic_group[20]; // 民族
    char birth_Place[20];  // 出生地
    char Native_place[20]; // 籍贯
} Student_t;

typedef struct Class
{
    Student_t stu_arr[50]; // 这个班级最多有50个学生
    unsigned int index;    // 当前班级学生的个数
} Class_t;                 // 班级的类

void readStu(Class_t* Class);//读取学生信息
int saveStu(Class_t* Class);//保存学生信息

#endif

```

### 界面按钮设置

#### Button. Cpp文件

```C
#include "Button.h"
#include<easyx.h>

void button(int x, int y, int w, int h, char* text)
{
    setbkmode(TRANSPARENT);//文字背景透明
    setfillcolor(RGB(25, 34, 41));
    //setfillcolor(GREEN);
    fillroundrect(x, y, x + w, y + h, 10, 10);

    char s1[] = "宋体";
    settextstyle(30, 0, s1);
    settextcolor(RGB(127, 227, 225));//设置文字颜色

    int tx = x + (w - textwidth(text)) / 2;
    int ty = y + (h - textheight(text)) / 2;

    outtextxy(tx, ty, text);

}
```

#### Button. H 文件

```c
#ifndef __BUTTOM_H__
#define __BUTTOM_H__
#include"Window.h"
//主界面按钮配置
struct Button_Set
{
    int num = 7;      //按钮数量
    int bw = 150;    //按钮宽度
    int bh = 40;     //按钮高度
    int bx = (window_width() - bw) / 2-200;         //按钮x坐标
    int by1 = (window_height() - bh * num) / 2-200; //按钮y坐标
};

//学生信息界面按钮配置
struct Stu_Button_Set
{
    int Stunum = 4;      //按钮数量
    int Stubw = 130;    //按钮宽度
    int Stubh = 50;     //按钮高度
    int Stubx1 = 0;         //按钮x坐标
    int Stuby1 = 0; //按钮y坐标
};
void button(int x, int y, int w, int h, char* text);

#endif
```

### Easyx 库函数封装

#### Window. Cpp 文件

```C
#include "Window.h"
#include <iostream>

ExMessage m_msg;
HWND m_Handle;

void Window(int w, int h, int flag)
{
m_Handle=initgraph(w, h, flag);
setbkmode(TRANSPARENT);//文字背景透明
}

void set_window_title(const char *title)
{
SetWindowText(m_Handle, title);//设置窗口名称
}

int exec()
{
return getchar();//防止闪退
}

int window_width()//获取窗口宽度
{
return getwidth();
}

int window_height() //获取窗口高度
{
return getheight();
}

void window_clear()
{
cleardevice();//刷新
}

void window_beginDraw()
{
BeginBatchDraw();
}

void window_flushDraw()
{
FlushBatchDraw();
}

void window_endDraw()
{
EndBatchDraw();
}
```

#### Window. H 文件

```C
#ifndef __WINDOW_H__
#define __WINDOW_H__
#include<easyx.h>
#include<string.h>

void Window(int w, int h, int flag);
void set_window_title(const char*title );
int exec();

int window_width();
int window_height();
void window_clear();
void window_beginDraw();
void window_flushDraw();
void window_endDraw();

#endif
```

---

# 各文件函数功能

## Information. Cpp

### Void readStu (Class_t\* Class)

==读取 student. Txt 文件内的数据，并将其放在主函数所开辟的空间里

```C
//读取学生信息
void readStu(Class_t* Class) {
    int i = 0;
    FILE* fp;
    fp = fopen("students.txt", "a+");
    if (fp == NULL) {
        printf("文件打开失败!\n");
        exit(0);
    }

    fscanf(fp, "%d", &Class->index);  //读取文件首行的学生人数，并储存在index
    for (i = 0; i < Class->index; i++) {
        fscanf(fp, "%s %s %s %s %s", Class->stu_arr[i].num, Class->stu_arr[i].name, Class->stu_arr[i].Ethnic_group, Class->stu_arr[i].birth_Place, Class->stu_arr[i].Native_place);
    }
    fclose(fp);
    printf("导入学生信息成功!\n");
}
```

^e9cbc0

### Int saveStu (Class_t\* Class)

^15fe33

==将修改过后的数据保存在 student.txt 内

```C
int saveStu(Class_t* Class) {
    int i = 0;
    if (Class->index == 0) {
        printf("还没有学生，请输入\n");
        return -1;
    }
    FILE* fp;
    fp = fopen("students.txt", "w");
    if (fp == NULL) {
        printf("文件打开失败!\n");
        exit(0);
    }

    fprintf(fp, "%d\n", Class->index);
    for (i = 0; i < Class->index; i++) {
        fprintf(fp, "%s %s %s %s %s\n", Class->stu_arr[i].num, Class->stu_arr[i].name, Class->stu_arr[i].Ethnic_group, Class->stu_arr[i].birth_Place, Class->stu_arr[i].Native_place);
    }
    fclose(fp);
    printf("写入成功!\n");
}
```

## Button. Cpp

### Void button (int x, int y, int w, int h, char\* text)

==设置界面中的按钮或文本框，通过计算文字坐标，将文字放在矩形的中央。

```C
void button(int x, int y, int w, int h, char* text)
{
    setbkmode(TRANSPARENT);//文字背景透明
    setfillcolor(RGB(25, 34, 41));
    //setfillcolor(GREEN);
    fillroundrect(x, y, x + w, y + h, 10, 10);

    char s1[] = "宋体";
    settextstyle(30, 0, s1);
    settextcolor(RGB(127, 227, 225));//设置文字颜色

    int tx = x + (w - textwidth(text)) / 2;
    int ty = y + (h - textheight(text)) / 2;

    outtextxy(tx, ty, text);
}
```

^abb4b7

## Interface. Cpp

### Void jiemian ()

==切换界面之后的界面背景颜色

```C
//切换后的界面颜色
void jiemian()
{
    setbkcolor(RGB(25, 34, 41));
}
```

### Void news_middle (char\* text)

```C
//提示消息居中显示
void news_middle(char* text) {
    window_clear();
    outtextxy((window_width() - textwidth(text)) / 2, (window_height() - textheight(text)) / 2-100, text);
}
```

将界面中出现的文本提示，在窗口的中央位置显示

### Void MENU ()

==主界面布局设置

```C
void  MENU()
{
    loadimage(&m_bk, "./m_bk.jpg", window_width(), window_height());
    putimage(0, 0, &m_bk);
    struct Button_Set BS;
    char s[8][50] = { "搜索信息","显示信息","添加信息", "删除信息","信息排序","修改信息" , "保存退出"};
    for (int i = 0; i < BS.num; i++) {
        button(BS.bx, BS.by1 + BS.bh * i, BS.bw, BS.bh, s[i]);
    }

}
```

^19edf3

### Int search (Class_t\* Class)

==搜索某个学生的信息，可选择搜索方式 1. 姓名查找 2. 学号查找 3. 出生地查找

```C
//1.搜索
int search(Class_t* Class) {
    char name[20];
    int i;
    struct Stu_Button_Set stuBS;
    if (Class->index == 0)
    {
        news_middle((char *)"还没有学生，请输入");
        //printf("还没有学生，请输入：\n");
        return -1;
    }
    char chose[10];
    InputBox(chose, 10, "1.姓名查找 2.学号查找 3.出生地查找", "请输入要查询学生信息的方式", NULL, 0, 0);

    if (strcmp(chose, "1") == 0) {
        InputBox(name, 20, "姓名", "请输入要查询的学生姓名", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].name) == 0) {

                char s[5][25] = { "学号","姓名","民族","出生地","户籍", };
                for (int k = 0; k < 5; k++) {
                    button(stuBS.Stubx1 + stuBS.Stubw * k, stuBS.Stuby1, stuBS.Stubw, stuBS.Stubh, s[k]);
                }
                button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
                button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
                button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
                button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
                button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1  + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);
                break;
            }
        }
        if (i == Class->index) {
            news_middle((char*)"没有该学员");

            //printf("没有该学员！");
        }
    }
    if (strcmp(chose, "2") == 0) {
        InputBox(name, 20, "学号", "请输入要查询的学生学号", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].num) == 0) {

                char s[5][25] = { "学号","姓名","民族","出生地","户籍", };
                for (int k = 0; k < 5; k++) {
                    button(stuBS.Stubx1 + stuBS.Stubw * k, stuBS.Stuby1, stuBS.Stubw, stuBS.Stubh, s[k]);
                }
                button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
                button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
                button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
                button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
                button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);
                break;
            }
        }
        if (i == Class->index) {
            news_middle((char*)"没有该学员");

            //printf("没有该学员！");
        }
    }

    if (strcmp(chose, "3") == 0) {
        InputBox(name, 20, "出生地", "请输入要查询的学生出生地", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].birth_Place) == 0) {

                char s[5][25] = { "学号","姓名","民族","出生地","户籍", };
                for (int k = 0; k < 5; k++) {
                    button(stuBS.Stubx1 + stuBS.Stubw * k, stuBS.Stuby1, stuBS.Stubw, stuBS.Stubh, s[k]);
                }
                button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1 + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
                button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
                button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
                button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
                button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1 + stuBS.Stubh , stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);
                break;
            }
        }
        if (i == Class->index) {
            news_middle((char*)"没有该学员");

            //printf("没有该学员！");
        }
    }

    system("pause");
    return 0;

}
```

### Int display (Class_t\* Class)

==显示学生信息

```C
/2.显示学生信息
int display(Class_t* Class) {

    struct Stu_Button_Set stuBS;

    // 表头
    char s[5][25] = { "学号","姓名","民族","出生地","户籍",};
    for (int i = 0; i < 5; i++) {
        button(stuBS.Stubx1 + stuBS.Stubw * i, stuBS.Stuby1 , stuBS.Stubw, stuBS.Stubh, s[i]);
    }

    int i;
    if (Class->index == 0) {
        news_middle((char*)"还没有学生，请输入");
        printf("还没有学生，请输入\n");
        return -1;
    }
    for (i = 0; i < Class->index; i++)
    {
        button(stuBS.Stubx1 + stuBS.Stubw * 0, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].num);
        button(stuBS.Stubx1 + stuBS.Stubw * 1, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].name);
        button(stuBS.Stubx1 + stuBS.Stubw * 2, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Ethnic_group);
        button(stuBS.Stubx1 + stuBS.Stubw * 3, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].birth_Place);
        button(stuBS.Stubx1 + stuBS.Stubw * 4, stuBS.Stuby1 + stuBS.Stubh * i + stuBS.Stubh, stuBS.Stubw, stuBS.Stubh, Class->stu_arr[i].Native_place);

        printf("学号:%-10s 姓名：%-10s 民族：%-10s 出生地：%-10s 籍贯：%-10s\n", Class->stu_arr[i].num, Class->stu_arr[i].name, Class->stu_arr[i].Ethnic_group, Class->stu_arr[i].birth_Place, Class->stu_arr[i].Native_place);
    }
    system("pause");
    return 0;

}

```

### Int add (Class_t\* Class)

==添加学生信息。

```C
//3.添加学生信息
int add(Class_t* Class) {
    Student_t stu;
BEGIN:

    InputBox(stu.num,20, "学号","请输入学生学号信息：",  NULL,0,0);
    InputBox(stu.name, 20, "姓名","请输入学生姓名信息：",  NULL, 0, 0);
    InputBox(stu.Ethnic_group, 20, "民族","请输入学生民族信息：",  NULL, 0, 0);
    InputBox(stu.birth_Place, 20,"出生地", "请输入学生出生地信息：",  NULL, 0, 0);
    InputBox(stu.Native_place, 20, "户籍","请输入学生户籍信息：",  NULL, 0, 0);
    printf("请输入学生的 学号、姓名、民族、出生地、籍贯：\n");

    for (int i = 0; i < Class->index; i++)
    {
        if (strcmp(Class->stu_arr[i].num, stu.num) == 0)
        {
            window_clear();
            printf("该学生已经存在，请重新输入：\n");
            news_middle((char*)"该学生已经存在，请重新输入");

            goto BEGIN;
        }
    }
    Class->stu_arr[Class->index] = stu;
    Class->index++;
    printf("插入成功！\n");
    news_middle((char*)"插入成功");
    system("pause");
    return 0;
}

```

### Int del (Class_t\* Class)

==删除学生信息。

```C
//4.删除学生信息
int del(Class_t* Class) {

    int i = 0;
    int j = 0;
    char name[20];
    if (Class->index == 0)
    {
        news_middle((char*)"还没有学生，请输入");
        //outtextxy(200, 200, "还没有学生，请输入");
        //printf("还没有学生，请输入\n");
        return -1;      //代表函数非正常终止
    }
    char chose[10];
    InputBox(chose, 20, "1.姓名查找 2.学号查找", "请选择要查找所删除学生的方式", NULL, 0, 0);
    if (strcmp(chose, "1") == 0) {
        InputBox(name, 20, "姓名", "请输入要删除学生的姓名：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++)
        {
            if (strcmp(name, Class->stu_arr[i].name) == 0)
            {
                for (j = i; j < Class->index - 1; j++)
                {
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                }
                Class->index--;
                news_middle((char*)"删除成功!!!");
                //outtextxy(200, 200, "删除成功!!!");
                _getch();
                break;
            }
        }
        //当循环整个班级人数后，没有这个学生
        if (i == Class->index)
        {
            window_clear();
            news_middle((char*)"班级没有这个学员!");
            //outtextxy(200, 200, "班级没有这个学员!");

            return -1;
        }
    }
    if (strcmp(chose, "2") == 0) {
        InputBox(name, 20, "学号", "请输入要删除学生的学号：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++)
        {
            if (strcmp(name, Class->stu_arr[i].num) == 0)
            {
                for (j = i; j < Class->index - 1; j++)
                {
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                }
                Class->index--;
                news_middle((char*)"删除成功!!!");
                //outtextxy(200, 200, "删除成功!!!");
                _getch();
                break;
            }
        }
        //当循环整个班级人数后，没有这个学生
        if (i == Class->index)
        {
            window_clear();
            news_middle((char*)"班级没有这个学员!");
            //outtextxy(200, 200, "班级没有这个学员!");

            return -1;
        }
    }

}
```

### Int sort (Class_t\* Class)

==排序

```C
//5.排序
int sort(Class_t* Class) {

    int i, j;
    Student_t temp;
    if (Class->index == 0)
    {
        news_middle((char*)"还没有学生，请输入");
        //outtextxy(200, 200, "还没有学生，请输入");
        return -1;
    }
//BEGIN:
    char chose[10];
    window_clear();
    InputBox(chose, 10, "1.学号 2.户籍 3.姓名", "请选择排序方式", NULL, 0, 0);
    if (strcmp(chose, "1") == 0) {
        for (i = 0; i < Class->index - 1; i++)
        {
            for (j = 0; j < Class->index - 1 - i; j++)
            {
                if (strcmp(Class->stu_arr[j].num, Class->stu_arr[j + 1].num) > 0)
                {
                    temp = Class->stu_arr[j];
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                    Class->stu_arr[j + 1] = temp;
                }

            }
        }
    news_middle((char*)"学号由低到高排序已完成");
    _getch();
    }
    if (strcmp(chose, "2") == 0) {
        for (i = 0; i < Class->index - 1; i++)
        {
            for (j = 0; j < Class->index - 1 - i; j++)
            {
                if (strcmp(Class->stu_arr[j].Native_place, Class->stu_arr[j + 1].Native_place) > 0)
                {
                    temp = Class->stu_arr[j];
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                    Class->stu_arr[j + 1] = temp;
                }

            }
        }
        news_middle((char*)"籍贯由低到高排序已完成");
        _getch();
    }
    if (strcmp(chose, "3") == 0) {
        for (i = 0; i < Class->index - 1; i++)
        {
            for (j = 0; j < Class->index - 1 - i; j++)
            {
                if (strcmp(Class->stu_arr[j].name, Class->stu_arr[j + 1].name) > 0)
                {
                    temp = Class->stu_arr[j];
                    Class->stu_arr[j] = Class->stu_arr[j + 1];
                    Class->stu_arr[j + 1] = temp;
                }

            }
        }
        news_middle((char*)"姓名由低到高排序已完成");
        _getch();
    }
    /*else {
        news_middle((char*)"输入错误");
        goto BEGIN;
    }*/

    return 0;

}
```

### Int modify (Class_t\* Class)

==修改，可选择搜索要修改学生的方式 1. 姓名查找 2. 学号查找
查找到之后可选择要修改的学生信息 1. 民族 2. 出生地 3. 籍贯

```C
//6.修改
int modify(Class_t* Class) {
    char chose[10] ;
    char name[20];
    char Native_Place[20];// 籍贯
    char Ethnic_Group[20]; // 民族
    char Birth_Place[20];  // 出生地

    int i = 0;
    if (Class->index == 0) {
        window_clear();
        news_middle((char*)"还没有学生信息");
        return -1;
    }
    window_clear();
    char chose1[10];
    InputBox(chose1, 10, "1.姓名查找 2.学号查找", "请选择要查找所删除学生信息的方式", NULL, 0, 0);
    if (strcmp(chose1, "1") == 0) {
        InputBox(name, 20, "姓名", "请输入要修改学生的姓名：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].name) == 0) {
                InputBox(chose, 10, "1.民族 2.出生地 3.籍贯", "请选择要修改信息", NULL, 0, 0);
                if (strcmp(chose, "1") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Ethnic_group, Ethnic_Group);
                    window_clear();
                    news_middle((char*)"修改成功");

                }
                if (strcmp(chose, "2") == 0) {
                    InputBox(Birth_Place, 20, "出生地", "请输入要修改的出生地", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].birth_Place, Birth_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                if (strcmp(chose, "3") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Native_place, Native_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                break;
            }
        }
        if (i == Class->index) {
            window_clear();
            news_middle((char*)"没有该学员");

        }

    }

    if (strcmp(chose1, "2") == 0) {
        InputBox(name, 20, "学号", "请输入要修改学生的学号：", NULL, 0, 0);
        for (i = 0; i < Class->index; i++) {
            if (strcmp(name, Class->stu_arr[i].num) == 0) {
                InputBox(chose, 10, "1.民族 2.出生地 3.籍贯", "请选择要修改信息", NULL, 0, 0);
                if (strcmp(chose, "1") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Ethnic_group, Ethnic_Group);
                    window_clear();
                    news_middle((char*)"修改成功");

                }
                if (strcmp(chose, "2") == 0) {
                    InputBox(Birth_Place, 20, "出生地", "请输入要修改的出生地", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].birth_Place, Birth_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                if (strcmp(chose, "3") == 0) {
                    InputBox(Ethnic_Group, 20, "民族", "请输入要修改的民族", NULL, 0, 0);
                    strcpy(Class->stu_arr[i].Native_place, Native_Place);
                    window_clear();
                    news_middle((char*)"修改成功");
                }
                break;
            }
        }
        if (i == Class->index) {
            window_clear();
            news_middle((char*)"没有该学员");

        }

    }

    system("pause");
    return 0;

}

```

### Void Exit (Class_t\* Class)

==保存退出，调用 information .cpp 中的 int saveStu (Class_t\* Class) 函数 [[#^15fe33]]

```C
//7.保存退出
void Exit(Class_t* Class) {
    saveStu(Class);//保存
    closegraph();//退出
}
```

### Void draw_window ()

==绘制窗口

```C
void draw_window()
{
    Window(640, 720, 1);    // 创建绘图窗口，大小为 640x480 像素
    set_window_title("管理系统");//窗口名称
    jiemian();
}
```

## Window. Cpp

### Void Window (int w, int h, int flag)

==设置窗口大小

```C
void Window(int w, int h, int flag)
{
    m_Handle=initgraph(w, h, flag);
    setbkmode(TRANSPARENT);//文字背景透明
}
```

### Void set_window_title (const char \* title)

==设置窗口名称

```C
void set_window_title(const char *title)
{
    SetWindowText(m_Handle, title);//设置窗口名称
}
```

### Int exec ()

==防止闪退

```C
int exec()
{
    return getchar();//防止闪退
}
```

### Int window_width ()

==获取窗口宽度

```C
Int window_width ()
{
    Return getwidth ();
}
```

### int window_height ()

==获取窗口高度

```C
int window_height() //获取窗口高度
{
    return getheight();
}
```

### Void window_clear ()

==刷新

```C
void window_clear()
{
    cleardevice();//刷新
}
```

### Void window_beginDraw ()

==开始批量绘制

```C
void window_beginDraw()
{
    BeginBatchDraw();
}
```

### Void window_flushDraw ()

==执行未完成的绘制任务。

```C
void window_flushDraw()
{
    FlushBatchDraw();
}
```

### Void window_endDraw ()

==结束批量绘制

```C
void window_endDraw()
{
    EndBatchDraw();
}
```
