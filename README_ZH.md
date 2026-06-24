<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>你用 Claude、GPT、Gemini、DeepSeek 和本地模型。<br>
  RelayOS 让它们自动协作。</strong><br>
  <br>
  一个终端原生的 AI 运行时，将任务路由到最合适的模型，<br>
  跨会话记住项目上下文，并为你节省费用。
</p>

<p align="center">
  <a href="#-快速开始"><img src="https://img.shields.io/badge/快速开始-10B981?style=for-the-badge&logo=python" alt="快速开始"></a>
  <a href="#%EF%B8%8F-功能特性"><img src="https://img.shields.io/badge/功能特性-3B82F6?style=for-the-badge" alt="功能特性"></a>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-安装"><img src="https://img.shields.io/badge/pip_install_relayos-FF6F00?style=for-the-badge&logo=pypi" alt="安装"></a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/English-607D8B?style=flat-square" alt="English"></a>
  <a href="README_ZH.md"><img src="https://img.shields.io/badge/中文-EA4335?style=flat-square" alt="中文"></a>
  <a href="README_DE.md"><img src="https://img.shields.io/badge/Deutsch-FFD700?style=flat-square" alt="Deutsch"></a>
  <a href="README_ES.md"><img src="https://img.shields.io/badge/Espa%C3%B1ol-00C853?style=flat-square" alt="Español"></a>
  <a href="README_FR.md"><img src="https://img.shields.io/badge/Fran%C3%A7ais-1E90FF?style=flat-square" alt="Français"></a>
  <a href="README_JP.md"><img src="https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-FF4081?style=flat-square" alt="日本語"></a>
  <a href="README_KR.md"><img src="https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-03C75A?style=flat-square" alt="한국어"></a>
</p>

---

## 👋 问题

你打开 5 个浏览器标签页。ChatGPT 做推理，Claude 做架构，Gemini 做研究，DeepSeek 做编码。你把一个的输出拷贝粘贴到另一个。你把高级 token 浪费在免费模型就能完成的任务上。

**你浪费 30% 的时间管理工具，而不是构建产品。**

## 🎯 解决方案

RelayOS 是一个协调层，让你的 AI 工具像真正的团队一样工作：

```
┌─ 你 ─────────────────────────────────────────┐
│                                                │
│   relay session ask "Build a payment sys"      │
│                                                │
└─────────────────────┬──────────────────────────┘
                      │
┌─────────────────────▼──────────────────────────┐
│              RelayOS                            │
│                                                 │
│  1. 研究竞品       → Gemini (免费)              │
│  2. 设计架构       → Claude                    │
│  3. 实现代码       → GPT                       │
│  4. 安全审查       → DeepSeek (廉价)            │
│  5. 编写 API 文档  → Gemini (免费)              │
│                                                 │
│  总成本：$0.01    时间：45 秒                    │
└─────────────────────────────────────────────────┘
```

**零基础设施。** `pip install relayos && relay`。无需 Docker，无需服务器，无需浏览器。

---

## ✨ RelayOS 的独特之处

| 功能 | 作用 | 价值 |
|---------|-------------|---------|
| 🧠 **智能路由** | 为每个任务自动选择最佳模型 | 优先使用免费模型，高级模型仅在必要时启用 |
| 🔄 **多步骤计划** | 将任务分解为执行图 | 一条命令，多个 AI 模型协同工作 |
| 💾 **项目记忆** | 知识在会话间持久保留 | 工作者不会忘记学到的内容 |
| 💰 **成本控制** | 按模型追踪 + 预算限制 | 无意外账单 |
| 🔌 **21 种终端类型** | Claude、GPT、Gemini、DeepSeek、本地及 16+ 更多 | 使用你自己的工具 |
| ⌨️ **终端原生** | htop 风格的 TUI，无需浏览器 | 始终在你的工作流中 |

---

## ⚡ 快速开始

### 安装

```bash
pip install relayos
```

试试看——真的一条命令：

```bash
relay
```

打开控制面板。就像 `htop`，但用于你的 AI 团队。

### 与任意模型对话

```bash
# 自动路由到最佳模型
relay session chat "Explain Kubernetes architecture"

# 或指定特定工作者
relay session chat "Design this API" -w architect
```

### 执行多步骤任务

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS 会自动分解、路由并在最佳模型上执行每一步。

### 花钱前先规划

```bash
relay session plan "Build a payment system"
# 执行前显示成本估算
```

### 小组讨论（多个 AI 工作者）

```bash
relay session group "Review this architecture"
# 每个工作者贡献：研究员 → 架构师 → 审查员
```

### 即时切换模型

```bash
relay use opencode     # 所有任务 → OpenCode (免费)
relay use mimo         # 所有任务 → Mimo (免费)
relay use claude       # 所有任务 → Claude (高级)
relay use free         # 免费优先路由
```

### 项目知识

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # 知道之前的决策！
relay project knowledge proj-id                     # 查看累积的知识
```

---

## 🖥️ TUI 界面

```
 工作者 (1-9 选择)         │ 状态
                           │  配置：balanced
 1 🧠 architect    ○ idle  │  费用：$0.00
 2 🔍 researcher   ○ idle  │  待处理：0
 3 ⭐ coder        ○ idle  │
 4 🎯 reviewer     ○ idle  │ 操作
 5 🐛 debugger     ○ idle  │  f=free  b=balanced
                           │  o=opencode  c=claude
═══════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

键盘驱动，无需鼠标。一键切换配置或工作者。

---

## 🗺️ 能力图谱

当你输入 `relay session plan "Build a payment system"`，RelayOS 会生成：

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     研究需求
       gemini-2.5-flash                FREE

  [2] architecture 设计系统架构
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       审查架构决策
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
每步仅传递相关数据（非完整文本）。
约 800 tokens/步，比简单方法少 7 倍。
```

---

## 🔧 支持的终端（21 种）

自动检测你已安装的工具：

| 状态 | 终端 | 默认模型 |
|--------|----------|---------------|
| ✅ | **Claude Code** | claude-sonnet-4-20250514 |
| ✅ | **Mimo Code** | gpt-4o |
| ✅ | **OpenCode** | deepseek-chat |
| ✅ | **Pi Coding Agent** | gpt-4o |
| ✅ | **Cursor** | gpt-4o |
| ✅ | **OpenClaw** | gpt-4o |
| ✅ | **GitHub Copilot** | gpt-4o |
| ✅ | **HuggingFace CLI** | gpt-4o |
| ⬜ | OpenAI Codex | gpt-4o |
| ⬜ | Gemini CLI | gemini-2.5-flash |
| ⬜ | Aider | gpt-4o |
| ⬜ | ShellGPT | gpt-4o |
| ⬜ | Fabric | gpt-4o |
| ⬜ | ChatGPT CLI | gpt-4o |
| ⬜ | LLM CLI | gpt-4o |
| ⬜ | Kimi (Moonshot) | moonshot-v1-8k |
| ⬜ | Qwen CLI | qwen2.5:7b |
| ⬜ | Open Interpreter | gpt-4o |
| ⬜ | Continue | gpt-4o |
| ⬜ | Copilot Extension | gpt-4o |
| ⚡ | Custom | (可配置) |

**将任何 CLI 添加为终端：**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 全部命令

| 命令 | 功能 |
|---------|-------------|
| `relay` | 打开控制面板 |
| `relay session chat` | 单次 AI 对话 |
| `relay session ask` | 自动分解 + 执行 |
| `relay session group` | 多工作者讨论 |
| `relay session plan` | 显示能力图谱 |
| `relay session list` | 最近的会话 |
| `relay use <terminal>` | 切换默认终端 |
| `relay use <profile>` | 切换成本配置 |
| `relay focus <worker>` | SSH 进入工作者 |
| `relay team create` | 从模板创建团队 |
| `relay project create` | 创建知识项目 |
| `relay project knowledge` | 显示项目记忆 |
| `relay plan "task"` | 显示执行计划 |
| `relay estimate "task"` | 显示成本估算 |
| `relay run workflow.yaml` | 运行 YAML 工作流 |
| `relay config detect` | 扫描已安装的终端 |
| `relayos plugin add` | 注册自定义 CLI |
| `relayos serve` | Web 仪表盘（可选） |

---

## 🏗️ 架构

```
终端 (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                     │
│  (会话路由 + 能力检测)                       │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                    │
│  (schema 感知、artifact 传递、DAG 执行)      │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                       │
│  (15 个模型 × 7 种能力，成本感知)            │
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  适配器      │     │  知识库             │
│  (21 终端)   │     │  (SQLite, project)  │
└─────────────┘     └────────────────────┘
```

### 存储（全部本地，零基础设施）

```
~/.relayos/           ← 单目录，可移植
├── config.yaml       ← 你的模型/配置设置
├── state.db          ← 项目状态 + 决策
├── sessions.db       ← 会话历史 + 消息
├── knowledge.db      ← 跨会话记忆
├── artifacts.db      ← 结构化步骤输出
└── workers.db        ← 持久工作者
```

### 设计理念

| 原则 | 原因 |
|-----------|-----|
| **终端优先** | 开发者生活在终端中。无需浏览器。 |
| **状态，而非对话** | 保存决策，而非对话。约紧凑 200 倍。 |
| **能力路由** | 绑定到任务类型，而非模型。模型会变，任务不会。 |
| **零基础设施** | 单进程，本地 SQLite。无需 Docker、Postgres、Redis。 |
| **成本感知** | 优先使用免费层。无需费心就能省钱。 |

---

## 📈 版本历史

| 版本 | 内容 |
|---------|------|
| **V0.1** | 模型路由——5 个提供商适配器，YAML 工作流 |
| **V0.2** | 终端池——多 CLI，成本追踪 |
| **V0.3** | 工作者系统——8 个角色，持久化，TUI |
| **V0.4** | 状态编译器——结构化状态，事件溯源 |
| **V0.5** | 模型调度器——15 个模型，3 种成本配置 |
| **V0.6** | 会话系统——chat/ask/group 模式 |
| **V0.7** | 能力图谱——多步骤任务分解 |
| **V0.8** | 任务图执行——schema 感知的 artifact 传递 |
| **V0.9** | 跨会话记忆——项目知识库 |

---

## 💪 技术栈

| 组件 | 技术 |
|-----------|------|
| **语言** | Python 3.10+ |
| **CLI 框架** | Click 8.0+ |
| **HTTP 客户端** | HTTPX 0.27+ |
| **终端 UI** | Rich |
| **存储** | SQLite（无外部数据库） |
| **模型** | 15 个评分模型，21 种终端类型 |
| **许可证** | Apache 2.0 |

### 依赖项

| 库 | 许可证 | 用途 |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | CLI 框架 |
| [PyYAML](https://pyyaml.org/) | MIT | YAML 解析 |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | 模型 API 的 HTTP 客户端 |
| [Rich](https://rich.readthedocs.io/) | MIT | 终端 UI 渲染 |

### Credits

- **Claude Code** (Anthropic) — Primary development platform
- **OpenCode** — Terminal adapter & testing partner
- **MimoCode** — Terminal adapter for frontend workflows
- **OpenAI Codex** — Terminal adapter for coding tasks
- **ECC plugin system** — Agent orchestration patterns
- **MCP (Model Context Protocol)** — Tool integration protocol

---

## 📦 安装

### pip

```bash
pip install relayos
```

### 可选：Web 仪表盘

```bash
pip install relayos[server]
relayos serve --open
```

### 从源码安装

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker（仅 Web 仪表盘）

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 语言

- [English](README.md)
- [中文](README_ZH.md)
- [Deutsch](README_DE.md)
- [Français](README_FR.md)
- [Español](README_ES.md)
- [日本語](README_JP.md)
- [한국어](README_KR.md)

---

## 📄 License

[Apache 2.0](LICENSE) Copyright 2026 [jjjjjjjjnnjnn](https://github.com/jjjjjjjjnnjnn)

---

<p align="center">
  <strong>不要再在 AI 工具之间复制粘贴了。<br>
  让它们协作起来。</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-快速开始"><img src="https://img.shields.io/badge/开始使用-10B981?style=for-the-badge" alt="开始使用"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
