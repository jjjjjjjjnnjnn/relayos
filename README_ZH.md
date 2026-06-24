<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>为开发者打造的持久化 AI 工作进程。</strong><br>
  一个终端原生的 AI 执行运行时 —— 将任务路由至 Claude、GPT、Gemini、DeepSeek 及本地模型，<br>
  支持能力感知调度、共享项目记忆与多步执行图。
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/-Quick_Start-10B981?style=flat-square" alt="快速开始"></a>
  <a href="#-features"><img src="https://img.shields.io/badge/-Features-3B82F6?style=flat-square" alt="功能特性"></a>
  <a href="#-cli-reference"><img src="https://img.shields.io/badge/-CLI_Reference-8B5CF6?style=flat-square" alt="CLI 参考"></a>
  <a href="#%EF%B8%8F-architecture"><img src="https://img.shields.io/badge/-Architecture-EC4899?style=flat-square" alt="架构"></a>
  <a href="#%EF%B8%8F-credits"><img src="https://img.shields.io/badge/-Credits-6366F1?style=flat-square" alt="致谢"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/English-Doc-FFFFFF?style=flat-square" alt="English"></a>
  <a href="README_ZH.md"><img src="https://img.shields.io/badge/中文-文档-EA4335?style=flat-square" alt="中文"></a>
  <a href="README_DE.md"><img src="https://img.shields.io/badge/Deutsch-Dokument-FFD700?style=flat-square" alt="Deutsch"></a>
  <a href="README_ES.md"><img src="https://img.shields.io/badge/Español-Doc-00C853?style=flat-square" alt="Español"></a>
  <a href="README_FR.md"><img src="https://img.shields.io/badge/Français-Doc-1E90FF?style=flat-square" alt="Français"></a>
  <a href="README_JP.md"><img src="https://img.shields.io/badge/日本語-ドキュメント-FF4081?style=flat-square" alt="日本語"></a>
  <a href="README_KR.md"><img src="https://img.shields.io/badge/한국어-문서-03C75A?style=flat-square" alt="한국어"></a>
</p>

---

## 📋 目录

| 章节 | 描述 |
|---------|-------------|
| [🎯 概述](#-overview) | RelayOS 是什么以及为何存在 |
| [✨ 功能特性](#-features) | 所有能力 (V0.1–V0.9) |
| [⚡ 快速开始](#-quick-start) | 安装与启动 |
| [🔧 CLI 参考](#-cli-reference) | 全部 22 个命令 |
| [🏗️ 架构](#%EF%B8%8F-architecture) | 系统设计 |
| [🛣️ 路线图](#%EF%B8%8F-roadmap) | 版本历史与未来规划 |
| [🙏 致谢](#%EF%B8%8F-credits) | 鸣谢 |
| [📄 许可](#-license) | Apache 2.0 |

---

## 🎯 概述

**RelayOS** 是一个终端原生的 AI 执行运行时。就像是你的 AI 团队的 htop。

你拥有多种 AI 工具（Claude Code、ChatGPT、Gemini、DeepSeek、本地模型）。每个都很出色，但它们彼此之间无法沟通。RelayOS 就是那个协调层——它将任务路由到正确的模型、跨会话记住项目上下文、并执行多步骤计划——全部在终端中完成，零基础设施。

### 演进路线

```
V0.1  模型路由          → 选择合适的模型
V0.2  终端池            → 管理 CLI 工作进程
V0.3  工作进程系统       → 持久化的 AI 团队成员
V0.4  状态编译器         → 结构化状态，而非聊天历史
V0.5  模型调度器         → 成本感知（先用免费的，逐步升级）
V0.6  会话系统           → chat / ask / group 模式
V0.7  能力图             → 多步骤任务分解
V0.8  图执行             → 模式感知的工件传递
V0.9  跨会话记忆         → 项目知识库
```

---

## ✨ 功能特性

### 🤖 模型调度 (V0.1–V0.5)

| 特性 | 详情 |
|---------|--------|
| **5 个提供商适配器** | OpenAI、Anthropic、Google、DeepSeek、Ollama |
| **15 个模型评分** | 每模型 7 项能力（编码、架构、审查、研究、推理、快速、写作） |
| **3 种成本配置** | `free`（本地优先）、`balanced`（廉价优先）、`quality`（最优优先） |
| **终端切换** | `relay use opencode` —— 在 CLI 终端间即时切换 |
| **自动升级** | 低置信度时：免费 → 廉价 → 高级 |

### 🧠 工作进程系统 (V0.3)

| 特性 | 详情 |
|---------|--------|
| **8 个默认工作进程** | architect、researcher、coder、reviewer、debugger、writer、assistant、data-engineer |
| **工作进程持久化** | 基于 SQLite，重启后依然存在 |
| **工作进程收件箱** | 基于任务的工作进程间消息传递 |
| **聚焦视图** | `relay focus <worker>` —— SSH 进入一个工作进程的"大脑" |

### 💬 会话系统 (V0.6–V0.7)

| 特性 | 详情 |
|---------|--------|
| **3 种模式** | `chat`（单轮）、`ask`（自动执行）、`group`（多工作进程） |
| **能力路由** | 追踪你正在做的任务类型，而非你用的模型 |
| **能力图** | 将任务分解为多步骤 DAG |
| **粘性能力** | 会话记住编码/架构任务，调度器选择模型 |

### 🔄 任务图执行 (V0.8)

| 特性 | 详情 |
|---------|--------|
| **步骤模式** | 6 种步骤类型，带输入/输出契约 |
| **工件传递** | 结构化字段引用，而非完整文本 |
| **Token 效率** | 约 800 tokens/步，无模式时约 3000 |
| **断点续传** | 跳过已完成步骤，从失败处继续 |
| **成本估算** | 执行前显示每一步和总成本 |

### 🗄️ 跨会话记忆 (V0.9)

| 特性 | 详情 |
|---------|--------|
| **项目知识** | 知识跨会话积累 |
| **KnowledgeCompiler** | 从工件中提取纯代码知识 |
| **跳过指令** | 已知信息注入提示词（无需重新发现） |
| **节约约 43%** | 重复会话场景 |

### 🖥️ 终端 UI

```
 Workers (1-9 select)         │ Status
                               │  Profile: balanced
 1 🧠 architect    ○ idle     │  Cost: $0.00
 2 🔍 researcher   ○ idle     │  Pending: 0
 3 ⭐ coder        ○ idle     │
 4 🎯 reviewer     ○ idle     │ Actions
 5 🐛 debugger     ○ idle     │  f=free  b=balanced
                               │  o=opencode  c=claude
═══════════════════════════════╪═══════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

---

## ⚡ 快速开始

### 安装

```bash
pip install relayos
```

### 使用

```bash
relay             # 打开 TUI（htop 风格的控制面板）
relay use free    # 切换为优先使用免费模型
```

### Chat / Ask / Group

```bash
# 单 AI 对话（自动路由）
relay session chat "Explain Kubernetes architecture"

# 多步骤任务执行
relay session ask "Build a JWT auth system in FastAPI"

# 多工作进程小组讨论
relay session group "Design a payment system"
```

### 即时切换终端

```bash
relay use opencode   # 所有任务 → OpenCode（免费）
relay use mimo       # 所有任务 → Mimo（免费）
relay use claude     # 所有任务 → Claude（高级）
```

### 项目知识

```bash
relay project create payment-system       # 创建项目
relay project knowledge <project-id>      # 查看已积累的知识
relay session chat "Add refund" -p <pid>  # 将会话限定到项目范围
```

### 执行前先规划

```bash
relay session plan "Build a payment system"
# Shows: research(gemini free) → architecture(claude) → review(deepseek)
```

---

## 🔧 CLI 参考

| 命令 | 描述 |
|---------|-------------|
| `relay` | 打开 TUI 控制面板 |
| `relay session chat` | 单 AI 对话 |
| `relay session ask` | 自动分解并执行任务 |
| `relay session group` | 多工作进程小组讨论 |
| `relay session plan` | 显示能力图（不执行） |
| `relay session list` | 列出最近的会话 |
| `relay use` | 切换默认终端/配置 |
| `relay profile` | 设置路由配置 |
| `relay focus` | 工作进程聚焦视图 |
| `relay team create` | 从模板创建团队 |
| `relay project create` | 创建项目知识库 |
| `relay project knowledge` | 查看项目知识 |
| `relay plan` | 显示任务的执行计划 |
| `relay estimate` | 显示成本估算 |
| `relay run` | 运行 YAML 工作流 |
| `relay config` | 配置向导 |
| `relay plugin add` | 注册自定义 CLI 终端 |
| `relayos serve` | 可选的 Web 仪表盘 |

### 键盘快捷键（TUI 中）

| 按键 | 操作 |
|-----|--------|
| `f` | 免费模式 |
| `b` | 均衡模式 |
| `o` | OpenCode 终端 |
| `m` | Mimo 终端 |
| `c` | Claude 终端 |
| `1-9` | 选择工作进程 |
| `q` | 退出 |
| `r` | 刷新 |

---

## 🏗️ 架构

```
Terminal / Pipe / TUI
         │
         ▼
┌──────────────────────────────────────────────┐
│         ConversationEngine                    │
│  (session routing + capability detection)     │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│           TaskGraphExecutor                   │
│  (schema-aware, artifact-passing, DAG exec)   │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│         ModelScheduler                        │
│  (15 models × 7 capabilities, cost-aware)     │
└──────┬───────────────────────┬───────────────┘
       │                       │
┌──────▼──────┐       ┌───────▼──────────┐
│  Adapters   │       │  Knowledge Base   │
│  (5 prov.)  │       │  (SQLite, proj.)  │
└─────────────┘       └──────────────────┘
```

### 核心模块

| 模块 | 角色 |
|--------|------|
| `relayos/core/scheduler.py` | 15 模型成本感知调度器 |
| `relayos/core/session.py` | 会话生命周期 + 消息 |
| `relayos/core/conversation.py` | Chat/ask/group 引擎 |
| `relayos/core/planner.py` | 能力图 + 执行 |
| `relayos/core/knowledge.py` | 跨会话项目记忆 |
| `relayos/core/state.py` | 结构化状态存储 |
| `relayos/core/schemas.py` | 步骤输入/输出契约 |
| `relayos/core/artifacts.py` | 结构化工件存储 |
| `relayos/tui/app.py` | 键盘驱动的 TUI |

### 存储（全部本地 SQLite，零基础设施）

```
~/.relayos/
├── config.yaml        # 用户配置
├── state.db           # 项目状态 + 决策 + 事件
├── sessions.db        # 会话历史 + 消息
├── knowledge.db       # 跨会话项目知识
├── artifacts.db       # 结构化步骤输出
└── workers.db         # 持久化工作进程定义
```

---

## 🛣️ 路线图

### 已完成 (V0.1–V0.9)

| 版本 | 核心特性 | 状态 |
|---------|-------------|--------|
| V0.1 | 模型路由（5 个适配器，YAML 工作流） | ✅ |
| V0.2 | 终端池（多 CLI，成本追踪） | ✅ |
| V0.3 | 工作进程系统（8 种角色，持久化，TUI） | ✅ |
| V0.4 | 状态编译器（结构化状态，事件溯源） | ✅ |
| V0.5 | 模型调度器（15 个模型，3 种成本配置） | ✅ |
| V0.6 | 会话系统（chat/ask/group 模式） | ✅ |
| V0.7 | 能力图（多步骤任务分解） | ✅ |
| V0.8 | 任务图执行（模式感知工件传递） | ✅ |
| V0.9 | 跨会话记忆（项目知识库） | ✅ |

### 规划中

- **V1.0** — 插件生态、MCP 路由器、分布式工作进程
- **V1.1** — 工作流回放（LangSmith 风格时间线）
- **V1.2** — 多机器工作进程池

---

## 🙏 Credits

### 🖥️ Terminal Platforms

| Platform | Credit |
|----------|--------|
| **[Claude Code](https://claude.ai)** — Powered by Anthropic | Primary development platform. [Terms](https://www.anthropic.com/legal) |
| **[OpenCode](https://opencode.ai)** | Terminal adapter target and testing partner |
| **[MimoCode](https://mimo.ai)** | Terminal adapter for multi-model frontend workflows |
| **OpenAI Codex** | Terminal adapter for coding tasks |

### 🤖 Models Used

- **Claude Opus 4.8 / Sonnet 4.6** (Anthropic) — Primary development models
- **Gemini 2.5 Flash** (Google) — Research tasks, competitive analysis
- **GPT-4o** (OpenAI) — Architecture evaluation and review
- **DeepSeek V3** (DeepSeek) — Code review and testing

### 📦 Dependencies

| Library | License | Purpose |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | CLI framework |
| [PyYAML](https://pyyaml.org/) | MIT | YAML parsing |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | HTTP client for model APIs |
| [Rich](https://rich.readthedocs.io/) | MIT | Terminal UI rendering |

### 🌍 Translations

- [English](README.md)
- [Deutsch (German)](README_DE.md)
- [Français (French)](README_FR.md)
- [Español (Spanish)](README_ES.md)
- [日本語 (Japanese)](README_JP.md)
- [한국어 (Korean)](README_KR.md)

---

## 📦 Publishing

Releases are automated via GitHub Actions. To publish a new version:

```bash
git tag v0.1.0 && git push origin v0.1.0
# Triggers .github/workflows/publish.yml → auto-builds → PyPI
```

**Install:** `pip install relayos`
**Source:** [github.com/jjjjjjjjnnjnn/relayos](https://github.com/jjjjjjjjnnjnn/relayos)
**License:** [Apache 2.0](LICENSE)

---

<p align="center">
  <strong>RelayOS</strong> — Persistent AI Workers for Developers.<br>
  <sub>Like htop for your AI team. No Docker, no server, no browser needed.</sub>
</p>
