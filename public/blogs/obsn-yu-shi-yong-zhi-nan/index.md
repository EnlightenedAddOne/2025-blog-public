> 来源：Obsidian/20-技术知识库/环境配置/OpenCode与OhMyOpenCode使用指南.md

# OpenCode 与 Oh My OpenCode 使用指南

> OpenCode 是一个开源的 AI 编程助手，Oh My OpenCode 是其增强插件，提供了多智能体协作系统。

---

## 一、OpenCode 简介

OpenCode 是一个**开源的 AI 编程代理工具**，可以：

- 分析代码
- 生成新功能
- 修改和优化项目
- 支持多种 AI 模型（Claude、ChatGPT、Gemini、GLM 等）
- 运行在终端中，操作方便

**官方网址**：https://opencode.ai/

---

## 二、Oh My OpenCode 简介

Oh My OpenCode 是 OpenCode 的**增强插件**（类似 Oh My Zsh 之 于 Zsh），将单个 AI 助手变成多模型协同的智能开发团队。

### 核心特性

| 特性         | 说明                           |
| ------------ | ------------------------------ |
| 多模型协作   | 可同时调用多个 AI 模型协同工作 |
| 智能体系统   | 内置多个专业 Agent             |
| 提示词优化   | 自动优化给 AI 的指令           |
| 后台任务管理 | 支持并行执行多个任务           |

---

## 三、四大核心智能体

Oh My OpenCode 内置了四个核心智能体：

| Agent          | 名称来源            | 职责                                                   |
| -------------- | ------------------- | ------------------------------------------------------ |
| **Sisyphus**   | 希腊神话 西西弗斯   | 主编排器：任务拆解、委托分配、TODO管理、后台并行执行   |
| **Atlas**      | 希腊神话 阿特拉斯   | 工作流支撑：与 Prometheus 协作，执行详细工作计划       |
| **Prometheus** | 希腊神话 普罗米修斯 | 计划者：创建详细的工作计划，配合 Atlas 执行            |
| **Hephaestus** | 希腊神话 赫菲斯托斯 | 深度工作者：自主探索、决策、执行跨文件跨领域的复杂任务 |

### 各 Agent 职责详解

- **Sisyphus**：技术主管，负责把需求拆解成具体步骤，指挥子 Agent 干活
- **Prometheus**：规划师，创建详细工作计划
- **Atlas**：执行者，启动后按照 Prometheus 的计划执行
- **Hephaestus**：手艺人，适合需要深度探索、自主决策的复杂任务

---

## 四、安装方法

```bash
# 方法一：使用 bun（推荐）
bunx oh-my-opencode install

# 方法二：使用 npm
npm install -g oh-my-opencode

# 方法三：通过 OpenCode 安装
# 在 OpenCode 中输入：
/init
```

**前提条件**：

- Node.js 18+ 或 Bun 1.0+
- OpenCode 已安装

---

## 五、快捷键

### Leader Key（领袖键）

OpenCode 使用 **Leader Key** 来避免与终端快捷键冲突。

**默认 Leader Key**: `Ctrl+X`

**用法**: 按下 `Ctrl+X`，松开，然后按第二个键。

### 基础操作

| 快捷键        | 操作       | 说明                                       |
| ------------- | ---------- | ------------------------------------------ |
| `Enter`       | 发送消息   | 发送当前输入                               |
| `Shift+Enter` | 换行       | 在输入框中添加新行（Windows 上可能不工作） |
| `Ctrl+J`      | 换行       | 替代 Shift+Enter 的方案                    |
| `Tab`         | 切换 Agent | 循环切换主要 Agent                         |
| `Shift+Tab`   | 反向切换   | 反向循环切换 Agent                         |
| `Escape`      | 中断       | 停止当前 AI 响应                           |
| `Ctrl+C`      | 清除输入   | 清空输入框内容                             |
| `Ctrl+D`      | 退出       | 关闭 OpenCode                              |
| `Ctrl+P`      | 命令面板   | 打开命令列表                               |

### Leader Key 操作

| 快捷键         | 操作       | 说明             |
| -------------- | ---------- | ---------------- |
| `Ctrl+X` → `n` | 新建会话   | 相当于 /new      |
| `Ctrl+X` → `l` | 会话列表   | 相当于 /sessions |
| `Ctrl+X` → `m` | 模型列表   | 相当于 /models   |
| `Ctrl+X` → `e` | 打开编辑器 | 打开文件编辑器   |
| `Ctrl+X` → `t` | 主题列表   | 切换主题         |
| `Ctrl+X` → `b` | 侧边栏     | 切换侧边栏显示   |
| `Ctrl+X` → `s` | 状态视图   | 查看状态信息     |
| `Ctrl+X` → `x` | 导出会话   | 导出当前会话     |
| `Ctrl+X` → `c` | 压缩视图   | 切换紧凑模式     |
| `Ctrl+X` → `g` | 时间线     | 查看会话时间线   |

### 消息浏览

| 快捷键       | 操作     |
| ------------ | -------- |
| `PageUp`     | 上一页   |
| `PageDown`   | 下一页   |
| `Ctrl+Alt+Y` | 上移一行 |
| `Ctrl+Alt+E` | 下移一行 |

---

## 六、常用命令

| 命令          | 说明                              |
| ------------- | --------------------------------- |
| `/init`       | 初始化项目，生成 AGENTS.md        |
| `/sessions`   | 查看会话列表                      |
| `/models`     | 切换模型                          |
| `/agents`     | 查看可用 Agent                    |
| `/start-work` | 从 Prometheus 计划启动 Atlas 执行 |

---

## 七、配置文件

### 文件位置

配置文件位于 `~/.config/opencode/opencode.json`：

```jsonc
{
	"$schema": "https://opencode.ai/config.json",
	"theme": "opencode",
	"model": "anthropic/claude-sonnet-4-5",
	"autoupdate": true,

	// Agent 配置
	"agents": {
		"sisyphus": {
			"model": "anthropic/claude-sonnet-4-5",
			"enabled": true
		}
	}
}
```

### 优先级顺序

1. 内联配置（`OPENCODE_CONFIG_CONTENT` 环境变量）
2. `.opencode` 目录
3. 项目配置（项目中的 `opencode.json`）
4. 自定义配置（`OPENCODE_CONFIG` 环境变量）
5. 全局配置（`~/.config/opencode/opencode.json`）
6. 远程配置（来自 `.well-known/opencode`）

---

## 八、已知问题

### Windows 上 Shift+Enter 问题

在 Windows 上，Shift+Enter 会直接发送消息而不是换行。

**临时解决方案**：使用 `Ctrl+J` 代替 Shift+Enter 来插入换行符。

**相关 Issue**：

- #8038: https://github.com/anomalyco/opencode/issues/8038
- #11983: https://github.com/anomalyco/opencode/issues/11983

---

## 九、更多资源

- 官方文档：https://opencode.ai/docs/
- Oh My OpenCode GitHub：https://github.com/code-yeongyu/oh-my-opencode
- 中文配置教程：https://didee.cn/opencode-config/

---

_最后更新：2026-03-02_
