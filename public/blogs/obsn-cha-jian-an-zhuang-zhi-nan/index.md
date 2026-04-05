> 来源：Obsidian/20-技术知识库/环境配置/OpenCode插件安装指南.md

# OpenCode 插件安装指南

## 简介

OpenCode 是一个 AI 助手插件，可以直接在 Obsidian 的侧边栏中嵌入使用，为你的笔记提供 AI 能力。

**功能特点**：

- 总结和提炼长篇内容
- 起草、编辑和润色写作
- 查询和探索知识库
- 生成大纲和结构化笔记

## 环境要求

- **Obsidian**（桌面版本）
- **Bun**：包管理器和构建工具
- **OpenCode CLI**：需要先安装 OpenCode 命令行工具

### 安装 Bun（如果未安装）

```bash
# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1|iex"

# macOS/Linux
curl -fsSL https://bun.sh/install | bash
```

### 安装 OpenCode CLI（如果未安装）

```bash
npm install -g @opencode/cli
```

## 安装步骤

### 1. 克隆插件仓库

在你的 Obsidian vault 根目录下执行：

```bash
# Windows (Git Bash)
git clone https://github.com/mtymek/opencode-obsidian.git .obsidian/plugins/obsidian-opencode

# PowerShell
git clone https://github.com/mtymek/opencode-obsidian.git .obsidian/plugins/obsidian-opencode
```

### 2. 安装依赖并构建

```bash
cd .obsidian/plugins/obsidian-opencode
bun install
bun run build
```

### 3. 在 Obsidian 中启用插件

1. 打开 Obsidian
2. 进入 `设置` → `社区插件`
3. 找到并启用 "OpenCode" 插件

### 4. 复制 AGENTS.md（可选）

将插件自带的 `AGENTS.md` 复制到工作区根目录，用于说明项目结构：

```bash
cp .obsidian/plugins/obsidian-opencode/AGENTS.md .
```

## 常见问题与解决方案

### 问题 1：Failed to start OpenCode - Executable not found at 'opencode'

**原因**：
在 Windows 系统上，插件默认的 opencode 路径无法找到可执行文件。

**解决方案**：

1. 找到 OpenCode CLI 的安装路径，通常是：
   ```
   C:\Users\你的用户名\AppData\Roaming\npm\opencode.cmd
   ```
2. 在插件设置中配置正确的路径：
   - 打开 Obsidian → `设置` → `社区插件` → `OpenCode`
   - 在 "OpenCode path" 中填入完整路径：
     ```
     C:\Users\21099\AppData\Roaming\npm\opencode.cmd
     ```
   - 在 "Project directory" 中填入你的 vault 根目录，例如：
     ```
     D:\PROJECT\Markdown\Obsidian
     ```

### 问题 2：启动时一直转圈等待

**原因**：
插件的健康检查端点路径错误，导致无法正确检测服务器状态。

**解决方案**：
这是插件的一个 bug，需要手动修改代码：

1. 打开 `.obsidian/plugins/obsidian-opencode/src/ProcessManager.ts`
2. 找到 `checkServerHealth()` 方法（约第 181 行）
3. 将：
   ```typescript
   const response = await fetch(`${this.getUrl()}/global/health`, {
   ```
   改为：
   ```typescript
   const response = await fetch(
     `http://${this.settings.hostname}:${this.settings.port}/global/health`,
   ```
4. 重新构建插件：
   ```bash
   cd .obsidian/plugins/obsidian-opencode
   bun run build
   ```
5. 重启 Obsidian

## 使用方法

### 打开 OpenCode 面板

- **快捷键**：`Ctrl + Shift + O`（Windows）或 `Cmd + Shift + O`（macOS）
- **工具栏**：点击左侧的终端图标
- **命令面板**：`Ctrl/Cmd + P`，搜索 "Toggle OpenCode panel"

### 可用命令

| 命令                  | 描述            |
| --------------------- | --------------- |
| Toggle OpenCode panel | 显示/隐藏侧边栏 |
| Start OpenCode server | 手动启动服务器  |
| Stop OpenCode server  | 手动停止服务器  |

### 插件设置说明

| 设置项                | 说明                                                    | 默认值    |
| --------------------- | ------------------------------------------------------- | --------- |
| Port                  | OpenCode Web 服务器端口号                               | 14096     |
| Hostname              | 绑定的主机名                                            | 127.0.0.1 |
| OpenCode path         | OpenCode 可执行文件路径                                 | opencode  |
| Project directory     | OpenCode 起始目录（留空使用 vault 根目录）              | 空        |
| Auto-start server     | Obsidian 启动时自动启动服务器（不推荐，会影响启动速度） | false     |
| Default view location | 面板打开位置（侧边栏或主窗口）                          | Sidebar   |

## 技术细节

### 插件架构

```
src/
├── main.ts           # 插件入口，继承 Plugin
├── types.ts          # 类型和常量定义
├── OpenCodeView.ts   # 侧边栏视图（ItemView）包含 iframe
├── ProcessManager.ts # 服务器进程生命周期管理
└── SettingsTab.ts    # 设置 UI（PluginSettingTab）
```

### 工作原理

1. **进程管理**：使用 Node.js `child_process.spawn()` 启动 OpenCode 服务器
2. **健康检查**：通过轮询 `/global/health` 端点确认服务器就绪
3. **嵌入显示**：通过 iframe 嵌入 OpenCode Web UI 到 Obsidian 侧边栏
4. **CORS 配置**：服务器启动时配置允许 `app://obsidian.md` 跨域访问

### 构建输出

- `main.js`：打包后的 CommonJS 模块
- `styles.css`：插件样式文件
- `manifest.json`：插件元数据

## 注意事项

- 仅支持桌面版本，移动端不支持（使用了 Node.js API）
- 确保 OpenCode CLI 已正确安装并可在命令行中访问
- 首次使用时建议手动启动服务器，确认配置无误后再启用自动启动
- 如果修改了配置，需要重启 Obsidian 使更改生效

## 参考资源

- [OpenCode 官网](https://opencode.ai)
- [插件 GitHub 仓库](https://github.com/mtymek/opencode-obsidian)
- [Obsidian 插件开发文档](https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin)

---

_本文档基于 Windows 11 环境编写，macOS 和 Linux 用户可参考类似步骤。_
