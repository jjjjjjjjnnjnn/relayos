<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Persistent AI Workers for Developers.</strong><br>
  A terminal-native AI execution runtime — route tasks across Claude, GPT, Gemini, DeepSeek and local models<br>
  with capability-aware scheduling, shared project memory, and multi-step execution graphs.
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/-Quick_Start-10B981?style=flat-square" alt="Quick Start"></a>
  <a href="#-features"><img src="https://img.shields.io/badge/-Features-3B82F6?style=flat-square" alt="Features"></a>
  <a href="#-cli-reference"><img src="https://img.shields.io/badge/-CLI_Reference-8B5CF6?style=flat-square" alt="CLI Reference"></a>
  <a href="#%EF%B8%8F-architecture"><img src="https://img.shields.io/badge/-Architecture-EC4899?style=flat-square" alt="Architecture"></a>
  <a href="#%EF%B8%8F-credits"><img src="https://img.shields.io/badge/-Credits-6366F1?style=flat-square" alt="Credits"></a>
  <a href="README.md"><img src="https://img.shields.io/badge/English-Doc-FFFFFF?style=flat-square" alt="English"></a>
  <a href="README_ZH.md"><img src="https://img.shields.io/badge/中文-文档-EA4335?style=flat-square" alt="中文"></a>
  <a href="README_DE.md"><img src="https://img.shields.io/badge/Deutsch-Dokument-FFD700?style=flat-square" alt="Deutsch"></a>
  <a href="README_ES.md"><img src="https://img.shields.io/badge/Español-Doc-00C853?style=flat-square" alt="Español"></a>
  <a href="README_FR.md"><img src="https://img.shields.io/badge/Français-Doc-1E90FF?style=flat-square" alt="Français"></a>
  <a href="README_JP.md"><img src="https://img.shields.io/badge/日本語-ドキュメント-FF4081?style=flat-square" alt="日本語"></a>
  <a href="README_KR.md"><img src="https://img.shields.io/badge/한국어-문서-03C75A?style=flat-square" alt="한국어"></a>
</p>

---

## 📋 Index

| Section | Description |
|---------|-------------|
| [🎯 Overview](#-overview) | What RelayOS is and why it exists |
| [✨ Features](#-features) | All capabilities (V0.1–V0.9) |
| [⚡ Quick Start](#-quick-start) | Install and start |
| [🔧 CLI Reference](#-cli-reference) | All 22 commands |
| [🏗️ Architecture](#%EF%B8%8F-architecture) | System design |
| [🛣️ Roadmap](#%EF%B8%8F-roadmap) | Version history & future |
| [🙏 Credits](#%EF%B8%8F-credits) | Acknowledgements |
| [📄 License](#-license) | Apache 2.0 |

---

## 🎯 Overview

**RelayOS** is a terminal-native AI execution runtime. Like htop for your AI team.

You have multiple AI tools (Claude Code, ChatGPT, Gemini, DeepSeek, local models). Each is excellent. They don't talk to each other. RelayOS is the coordination layer that routes tasks to the right model, remembers project context across sessions, and executes multi-step plans — all from your terminal, zero infrastructure.

### The Evolution

```
V0.1  Model Routing       →  pick the right model
V0.2  Terminal Pool       →  manage CLI workers
V0.3  Worker System       →  persistent AI team members
V0.4  State Compiler      →  structured state, not chat history
V0.5  Model Scheduler     →  cost-aware (free first, escalate)
V0.6  Session System      →  chat / ask / group modes
V0.7  Capability Graph    →  multi-step task decomposition
V0.8  Graph Execution     →  schema-aware artifact passing
V0.9  Cross-Session Mem   →  project knowledge base
```

---

## ✨ Features

### 🤖 Model Scheduling (V0.1–V0.5)

| Feature | Detail |
|---------|--------|
| **5 Provider Adapters** | OpenAI, Anthropic, Google, DeepSeek, Ollama |
| **15 Models Scored** | 7 capabilities each (coding, architecture, review, research, reasoning, quick, writing) |
| **3 Cost Profiles** | `free` (local first), `balanced` (cheap first), `quality` (best first) |
| **Terminal Switching** | `relay use opencode` — instant switch between CLI terminals |
| **Auto-Escalation** | Free → cheap → premium on low confidence |

### 🧠 Worker System (V0.3)

| Feature | Detail |
|---------|--------|
| **8 Default Workers** | architect, researcher, coder, reviewer, debugger, writer, assistant, data-engineer |
| **Worker Persistence** | SQLite-backed, survive restarts |
| **Worker Inbox** | Task-based inter-worker messaging |
| **Focus View** | `relay focus <worker>` — SSH into a worker's mind |

### 💬 Session System (V0.6–V0.7)

| Feature | Detail |
|---------|--------|
| **3 Modes** | `chat` (single), `ask` (auto-execute), `group` (multi-worker) |
| **Capability Routing** | Tracks what task type you're doing, not what model you used |
| **Capability Graph** | Decomposes tasks into multi-step DAGs |
| **Sticky Capability** | Session remembers coding/architecture, scheduler picks the model |

### 🔄 Task Graph Execution (V0.8)

| Feature | Detail |
|---------|--------|
| **Step Schemas** | 6 step types with input/output contracts |
| **Artifact Passing** | Structured field references, not full text |
| **Token Efficiency** | ~800 tokens/step vs ~3000 without schema |
| **Resume** | Skip completed steps, continue from failure |
| **Cost Estimation** | Per-step and total cost before execution |

### 🗄️ Cross-Session Memory (V0.9)

| Feature | Detail |
|---------|--------|
| **Project Knowledge** | Facts accumulate across sessions |
| **KnowledgeCompiler** | Pure code extraction from artifacts |
| **Skip Instructions** | Known info injected into prompts (no rediscovery) |
| **~43% Savings** | On repeated sessions |

### 🖥️ Terminal UI

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

## ⚡ Quick Start

### Install

```bash
pip install relayos
```

### Use

```bash
relay             # Open TUI (htop-style control panel)
relay use free    # Switch to free models first
```

### Chat / Ask / Group

```bash
# Single AI conversation (auto-routed)
relay session chat "Explain Kubernetes architecture"

# Multi-step task execution
relay session ask "Build a JWT auth system in FastAPI"

# Multi-worker group discussion
relay session group "Design a payment system"
```

### Switch Terminals Instantly

```bash
relay use opencode   # All tasks → OpenCode (free)
relay use mimo       # All tasks → Mimo (free)
relay use claude     # All tasks → Claude (premium)
```

### Project Knowledge

```bash
relay project create payment-system       # Create project
relay project knowledge <project-id>      # Show accumulated knowledge
relay session chat "Add refund" -p <pid>  # Session scoped to project
```

### Plan Before Executing

```bash
relay session plan "Build a payment system"
# Shows: research(gemini free) → architecture(claude) → review(deepseek)
```

---

## 🔧 CLI Reference

| Command | Description |
|---------|-------------|
| `relay` | Open TUI control panel |
| `relay session chat` | Single AI conversation |
| `relay session ask` | Auto-decompose + execute task |
| `relay session group` | Multi-worker group discussion |
| `relay session plan` | Show capability graph without executing |
| `relay session list` | List recent sessions |
| `relay use` | Switch default terminal/profile |
| `relay profile` | Set routing profile |
| `relay focus` | Worker focus view |
| `relay team create` | Create team from template |
| `relay project create` | Create project for knowledge base |
| `relay project knowledge` | Show project knowledge |
| `relay plan` | Show execution plan for a task |
| `relay estimate` | Show cost estimates |
| `relay run` | Run YAML workflow |
| `relay config` | Configuration wizard |
| `relay plugin add` | Register custom CLI terminal |
| `relayos serve` | Optional web dashboard |

### Keyboard Shortcuts (in TUI)

| Key | Action |
|-----|--------|
| `f` | Free profile |
| `b` | Balanced profile |
| `o` | OpenCode terminal |
| `m` | Mimo terminal |
| `c` | Claude terminal |
| `1-9` | Select worker |
| `q` | Quit |
| `r` | Refresh |

---

## 🏗️ Architecture

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

### Core Modules

| Module | Role |
|--------|------|
| `relayos/core/scheduler.py` | 15-model cost-aware scheduler |
| `relayos/core/session.py` | Session lifecycle + messages |
| `relayos/core/conversation.py` | Chat/ask/group engines |
| `relayos/core/planner.py` | Capability graphs + execution |
| `relayos/core/knowledge.py` | Cross-session project memory |
| `relayos/core/state.py` | Structured state store |
| `relayos/core/schemas.py` | Step input/output contracts |
| `relayos/core/artifacts.py` | Structured artifact storage |
| `relayos/tui/app.py` | Keyboard-driven TUI |

### Storage (all local SQLite, zero infrastructure)

```
~/.relayos/
├── config.yaml        # User configuration
├── state.db           # Project state + decisions + events
├── sessions.db        # Session history + messages
├── knowledge.db       # Cross-session project knowledge
├── artifacts.db       # Structured step outputs
└── workers.db         # Persistent worker definitions
```

---

## 🛣️ Roadmap

### Completed (V0.1–V0.9)

| Version | Core Feature | Status |
|---------|-------------|--------|
| V0.1 | Model Routing (5 adapters, YAML workflows) | ✅ |
| V0.2 | Terminal Pool (multi-CLI, cost tracking) | ✅ |
| V0.3 | Worker System (8 roles, persistence, TUI) | ✅ |
| V0.4 | State Compiler (structured state, event sourcing) | ✅ |
| V0.5 | Model Scheduler (15 models, 3 cost profiles) | ✅ |
| V0.6 | Session System (chat/ask/group modes) | ✅ |
| V0.7 | Capability Graph (multi-step task decomposition) | ✅ |
| V0.8 | Task Graph Execution (schema-aware artifact passing) | ✅ |
| V0.9 | Cross-Session Memory (project knowledge base) | ✅ |

### Planned

- **V1.0** — Plugin ecosystem, MCP router, distributed workers
- **V1.1** — Workflow replay (LangSmith-style timeline)
- **V1.2** — Multi-machine worker pool

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

- [中文 (Chinese)](README_ZH.md)
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
