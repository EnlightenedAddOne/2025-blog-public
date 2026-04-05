# Vue前端

> 来源：Obsidian/30-项目与实践/项目说明/图书管理系统说明/Vue前端.md

    开发工具建议使用VsCode

## 项目简介

本项目为图书管理系统的前端部分，基于 Vue 3 + Vite 构建，配合后端 Spring Boot 实现完整的图书管理功能。前端实现了用户登录、图书借阅、归还、统计分析等模块，界面美观，交互友好。

## 目录结构说明

```
src/
├── App.vue                 # 应用入口组件
├── api/                    # API请求模块
│   ├── articleApi.ts       # 文章相关API
│   ├── bookApi.ts          # 图书相关API
│   ├── borrowApi.ts        # 借阅相关API
│   ├── menuApi.ts          # 菜单相关API
│   ├── modules/            # API模块
│   └── usersApi.ts         # 用户相关API
├── assets/                 # 静态资源
├── components/             # 组件目录
├── composables/            # 组合式API
├── config/                 # 配置文件
├── directives/             # 自定义指令
├── enums/                  # 枚举类型
├── router/                 # 路由配置
├── store/                  # 状态管理
├── types/                  # 类型定义
├── utils/                  # 工具函数
│   ├── constants/          # 常量定义
│   │   └── iconfont.ts     # 图标提取工具
│   └── ...
└── views/                  # 页面视图
    ├── books/              # 图书相关页面
    ├── borrow/             # 借阅相关页面
    ├── auth                # 认证相关页面（如登录、注册、忘记密码）
    ├── exception           # 异常页面（如 404、500 错误页面）
	└── system              # 系统管理页面（如用户管理、角色管理）
```

## 环境配置

### 环境状态检测

打`cmd`命令窗口，分别输入`node -v`和`pnpm -v`
![](/blogs/obsn-qian-duan/Pasted image 20250708112045.png)
如果都出现了对应的版本号（如上图），则说明环境已配置，可跳过此步骤。

### 安装Node.js

下载地址：[下载 | Node.js 中文网](https://nodejs.cn/download/)

![](/blogs/obsn-qian-duan/Pasted image 20250708112421.png)
根据自己的电脑选择版本下载，_为了适配接下来的`pnpm`请选择 v18.12 以上的版本_

安装过程可参考：[Node.js 安装配置 | 菜鸟教程](https://www.runoob.com/nodejs/nodejs-install-setup.html)

### 安装pnpm

**1. 打开`cmd`，输入以下命令：**

```bash
npm install -g pnpm
```

**2. 检查是否安装成功：**

```bash
pnpm -v
```

**3. 配置PNPM镜像源（可选，提高下载速度）**
若要切换至国内镜像源，如cnpm或其它国内快速源：

```bash
pnpm config set registry https://registry.npmmirror.com
```

安装过程可参考：[安装 | pnpm中文文档 | pnpm中文网](https://www.pnpm.cn/installation)，[安装pnpm - 且行且思 - 博客园](https://www.cnblogs.com/Fooo/p/18612748)，[pnpm的安装与配置-腾讯云开发者社区](https://cloud.tencent.com/developer/article/2427836)

## 启动前端

1. 项目初始化

   使用`VsCode`打开前端项目（其他的编译器也行，但建议使用VsCode）
   打开后，在终端的项目根目录里输入

   ```bash
   pnpm i
   ```

   ![](/blogs/obsn-qian-duan/Pasted image 20250708115529.png)

2. 项目启动
   ```bash
   pnpm dev
   ```
