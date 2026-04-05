> 来源：Obsidian/20-技术知识库/环境配置/GitHub连接问题解决.md

# GitHub 连接问题汇总

本文档记录 GitHub Push/Pull 失败时的常见错误及解决方案。

## 常见错误信息

### 错误 1：RPC failed - Connection reset

```
error: RPC failed; curl 28 Recv failure: Connection was reset
fatal: expected flush after ref listing
```

### 错误 2：连接超时

```
fatal: unable to access 'https://github.com/username/repo.git/':
Failed to connect to github.com port 443 after 21081 ms: Could not connect to server
```

## 解决方案

### 方案 1：使用代理（推荐）

#### Clash Verge 设置

1. 打开 Clash Verge
2. 开启系统代理
3. 确保代理端口已启用（默认 7890）
4. 设置 Git 代理：

```bash
# 设置 HTTP 代理
git config --global http.proxy http://127.0.0.1:7897
git config --global https.proxy http://127.0.0.1:7897

# 或者使用 SOCKS5 代理
git config --global http.proxy socks5://127.0.0.1:7897
git config --global https.proxy socks5://127.0.0.1:7897
```

#### 验证代理是否生效

```bash
git config --global --get http.proxy
git config --global --get https.proxy
```

#### 取消代理（如需要）

```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### 方案 2：配置 Hosts 文件

通过配置 hosts 文件绕过 DNS 污染，直接指定 GitHub 的 IP 地址。

#### 获取 GitHub IP 地址

访问以下网站获取最新的 GitHub IP：

- https://www.ipaddress.com/website/github.com/
- 或使用 hellogithub 提供的 hosts：https://raw.hellogithub.com/hosts

#### 各系统 hosts 文件位置

| 操作系统 | 路径                                    |
| -------- | --------------------------------------- |
| Windows  | `C:\Windows\System32\drivers\etc\hosts` |
| Linux    | `/etc/hosts`                            |
| macOS    | `/etc/hosts`                            |

#### 添加内容到 hosts

将以下内容添加到 hosts 文件末尾（IP 地址可能变化，请以实际查询结果为准）：

```
# GitHub
140.82.112.3 github.com
140.82.112.4 github.com
140.82.113.3 www.github.com
185.199.108.153 github.io
185.199.109.153 github.io
185.199.110.153 github.io
185.199.111.153 github.io
```

#### 刷新 DNS 缓存

修改 hosts 后，需要刷新 DNS 缓存使配置生效：

| 操作系统 | 命令                                                                                             |
| -------- | ------------------------------------------------------------------------------------------------ |
| Windows  | `ipconfig /flushdns`                                                                             |
| Linux    | `sudo nscd restart` 或 `sudo /etc/init.d/nscd restart`（如未安装 nscd：`sudo apt install nscd`） |
| macOS    | `sudo killall -HUP mDNSResponder`                                                                |

#### 验证

```bash
ping github.com
```

如果显示的 IP 是之前配置的 IP（如 140.82.x.x），说明配置生效。

### 方案 3：切换为 SSH 协议推送

HTTPS 协议推送失败通常是由于网络问题、防火墙限制或 SSL 证书问题导致的。SSH 协议通常具有更好的穿透性，不容易受到这些问题影响。

#### 前提条件

检查本地是否已配置 SSH 密钥：

```bash
# Windows
Get-ChildItem -Path $env:USERPROFILE\.ssh -ErrorAction SilentlyContinue

# Linux/macOS
ls -la ~/.ssh
```

如果没有 SSH 密钥，需要先生成：

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

然后将公钥添加到 GitHub 账户：GitHub → Settings → SSH and GPG keys → New SSH key

#### 修改远程仓库为 SSH 格式

```bash
# 查看当前远程仓库
git remote -v

# 将 HTTPS 格式转换为 SSH 格式
git remote set-url origin git@github.com:username/repo.git
```

SSH 格式为 `git@github.com:username/repo.git`，而不是 `https://github.com/`

#### 验证并推送

```bash
# 验证远程仓库已更改
git remote -v

# 尝试推送
git push
```

#### 常见错误

- **SSH 密钥未添加到 GitHub**：将 `~/.ssh/id_ed25519.pub` 内容添加到 GitHub
- **权限拒绝**：检查 GitHub 账户是否添加了正确的公钥

### 方案 4：更换网络/热点

有时是本地网络问题，尝试：

- 切换 WiFi
- 使用手机热点
- 等待网络恢复

## 诊断步骤

1. **检查网络连通性**

   ```bash
   ping github.com
   ```

2. **检查 GitHub 是否可访问**

   ```bash
   curl -I https://github.com
   ```

3. **检查当前代理配置**

   ```bash
   git config --global --list
   ```

4. **查看具体错误**
   ```bash
   GIT_CURL_VERBOSE=1 git push -v
   ```

## 参考链接

- [知乎：完美解决 GitHub push/pull 失败](https://www.zhihu.com/question/1927165637588919600)
- [mogiihu：彻底了解 GitHub Push 失败](https://mogiihu.github.io/posts/2025-09-05-%E5%AE%8C%E7%BE%8E%E8%A7%A3%E5%86%B3-github-push-%E5%A4%B1%E8%B4%A5/)
- [博客园：GitHub 连接超时解决](https://www.cnblogs.com/guchen33/p/19304547)
- [GitHub IP 地址查询](https://www.ipaddress.com/website/github.com/)
- [HelloGithub Hosts](https://raw.hellogithub.com/hosts)
