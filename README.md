<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>You use Claude, GPT, Gemini, DeepSeek, and local models.<br>
  RelayOS makes them work together — automatically.</strong><br>
  <br>
  A terminal-native AI runtime that routes tasks to the right model,<br>
  remembers project context across sessions, and saves you money.
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-10B981?style=for-the-badge&logo=python" alt="Quick Start"></a>
  <a href="#%EF%B8%8F-features"><img src="https://img.shields.io/badge/Features-3B82F6?style=for-the-badge" alt="Features"></a>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-installation"><img src="https://img.shields.io/badge/pip_install_relayos-FF6F00?style=for-the-badge&logo=pypi" alt="Install"></a>
</p>

<p align="center">
  <a href="README_ZH.md"><img src="https://img.shields.io/badge/中文-EA4335?style=flat-square" alt="中文"></a>
  <a href="README_DE.md"><img src="https://img.shields.io/badge/Deutsch-FFD700?style=flat-square" alt="Deutsch"></a>
  <a href="README_ES.md"><img src="https://img.shields.io/badge/Español-00C853?style=flat-square" alt="Español"></a>
  <a href="README_FR.md"><img src="https://img.shields.io/badge/Français-1E90FF?style=flat-square" alt="Français"></a>
  <a href="README_JP.md"><img src="https://img.shields.io/badge/日本語-FF4081?style=flat-square" alt="日本語"></a>
  <a href="README_KR.md"><img src="https://img.shields.io/badge/한국어-03C75A?style=flat-square" alt="한국어"></a>
</p>

---

## 👋 The Problem

You open 5 browser tabs. ChatGPT for reasoning, Claude for architecture, Gemini for research, DeepSeek for coding. You copy output from one, paste it into the next. You burn premium tokens on tasks a free model could handle.

**You waste 30% of your time managing tools instead of building.**

## 🎯 The Solution

RelayOS is the coordination layer that makes your AI tools work like a real team:

```
┌─ You ──────────────────────────────────────┐
│                                             │
│   relay session ask "Build a payment sys"   │
│                                             │
└─────────────────────┬───────────────────────┘
                      │
┌─────────────────────▼───────────────────────┐
│              RelayOS                         │
│                                              │
│  1. Research competitors   → Gemini (FREE)   │
│  2. Design architecture   → Claude           │
│  3. Implement the code    → GPT              │
│  4. Security review       → DeepSeek (CHEAP) │
│  5. Document the API      → Gemini (FREE)    │
│                                              │
│  Total cost: $0.01    Time: 45s              │
└──────────────────────────────────────────────┘
```

**Zero infrastructure.** `pip install relayos && relay`. No Docker, no server, no browser.

---

## ✨ What Makes RelayOS Different

| Feature | What It Does | Benefit |
|---------|-------------|---------|
| 🧠 **Smart Routing** | Auto-selects the best model for each task | Free models first, premium only when needed |
| 🔄 **Multi-Step Plans** | Decomposes tasks into execution graphs | One command, many AI models working together |
| 💾 **Project Memory** | Knowledge persists across sessions | Workers never forget what they learned |
| 💰 **Cost Control** | Per-model tracking + budget limits | No surprise bills |
| 🔌 **21 Terminal Types** | Claude, GPT, Gemini, DeepSeek, local, and 16+ more | Bring your own tools |
| ⌨️ **Terminal Native** | htop-style TUI, no browser needed | Stays in your workflow |

---

## ⚡ Quick Start

### Installation

```bash
pip install relayos
```

Try it — literally one command:

```bash
relay
```

Opens the control panel. Like `htop`, but for your AI team.

### Chat with any model

```bash
# Auto-routes to best model
relay session chat "Explain Kubernetes architecture"

# Or target a specific worker
relay session chat "Design this API" -w architect
```

### Execute a multi-step task

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS will automatically decompose, route, and execute across the best models for each step.

### Plan before you spend

```bash
relay session plan "Build a payment system"
# Shows cost estimates before execution
```

### Group discussion (multiple AI workers)

```bash
relay session group "Review this architecture"
# Each worker contributes: researcher → architect → reviewer
```

### Switch models instantly

```bash
relay use opencode     # All tasks → OpenCode (free)
relay use mimo         # All tasks → Mimo (free)
relay use claude       # All tasks → Claude (premium)
relay use free         # Free-first routing
```

### Project knowledge

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # Knows previous decisions!
relay project knowledge proj-id                     # See accumulated knowledge
```

---

## 🖥️ The TUI

```
 Workers (1-9 select)         │ Status
                               │  Profile: balanced
 1 🧠 architect    ○ idle     │  Cost: $0.00
 2 🔍 researcher   ○ idle     │  Pending: 0
 3 ⭐ coder        ○ idle     │
 4 🎯 reviewer     ○ idle     │ Actions
 5 🐛 debugger     ○ idle     │  f=free  b=balanced
                               │  o=opencode  c=claude
═══════════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

Keyboard-driven, no mouse needed. One key to switch profiles or workers.

---

## 🗺️ Capability Graph

When you type `relay session plan "Build a payment system"`, RelayOS generates:

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     Research requirements
       gemini-2.5-flash                FREE

  [2] architecture Design system architecture
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       Review architecture decisions
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
Each step passes only relevant data (not full text).
~800 tokens/step, ~7x less than naive approaches.
```

---

## 🔧 Supported Terminals (21 types)

Automatically detects what you have installed:

| Status | Terminal | Default Model |
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
| ⚡ | Custom | (configurable) |

**Add any CLI as a terminal:**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 All Commands

| Command | What it does |
|---------|-------------|
| `relay` | Open control panel |
| `relay session chat` | Single AI conversation |
| `relay session ask` | Auto-decompose + execute |
| `relay session group` | Multi-worker discussion |
| `relay session plan` | Show capability graph |
| `relay session list` | Recent sessions |
| `relay use <terminal>` | Switch default terminal |
| `relay use <profile>` | Switch cost profile |
| `relay focus <worker>` | SSH into a worker |
| `relay team create` | Create team from template |
| `relay project create` | Create knowledge project |
| `relay project knowledge` | Show project memory |
| `relay plan "task"` | Show execution plan |
| `relay estimate "task"` | Show cost estimates |
| `relay run workflow.yaml` | Run YAML workflow |
| `relay config detect` | Scan installed terminals |
| `relayos plugin add` | Register a custom CLI |
| `relayos serve` | Web dashboard (optional) |

---

## 🏗️ Architecture

```
Terminal (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                    │
│  (session routing + capability detection)  │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                   │
│  (schema-aware, artifact-passing, DAG exec) │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                      │
│  (15 models × 7 capabilities, cost-aware)   │
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  Adapters   │     │  Knowledge Base     │
│  (21 terms) │     │  (SQLite, project)   │
└─────────────┘     └────────────────────┘
```

### Storage (all local, zero infrastructure)

```
~/.relayos/           ← Single directory, portable
├── config.yaml       ← Your model/profiles config
├── state.db          ← Project state + decisions
├── sessions.db       ← Session history + messages
├── knowledge.db      ← Cross-session memory
├── artifacts.db      ← Structured step outputs
└── workers.db        ← Persistent workers
```

### Design Philosophy

| Principle | Why |
|-----------|-----|
| **Terminal-first** | Developers live in the terminal. No browser needed. |
| **State, not chat** | Save decisions, not conversations. ~200x more compact. |
| **Capability routing** | Bind to task type, not model. Models change; tasks don't. |
| **Zero infrastructure** | Single process, local SQLite. No Docker, no Postgres, no Redis. |
| **Cost-awareness** | Free tiers first. Save money without thinking about it. |

---

## 📈 Version History

| Version | What |
|---------|------|
| **V0.1** | Model routing — 5 provider adapters, YAML workflows |
| **V0.2** | Terminal pool — multi-CLI, cost tracking |
| **V0.3** | Worker system — 8 roles, persistence, TUI |
| **V0.4** | State compiler — structured state, event sourcing |
| **V0.5** | Model scheduler — 15 models, 3 cost profiles |
| **V0.6** | Session system — chat/ask/group modes |
| **V0.7** | Capability graph — multi-step task decomposition |
| **V0.8** | Task graph execution — schema-aware artifact passing |
| **V0.9** | Cross-session memory — project knowledge base |

---

## 💪 Built With

| Component | Tech |
|-----------|------|
| **Language** | Python 3.10+ |
| **CLI Framework** | Click 8.0+ |
| **HTTP Client** | HTTPX 0.27+ |
| **Terminal UI** | Rich |
| **Storage** | SQLite (no external DB) |
| **Models** | 15 scored models, 21 terminal types |
| **License** | Apache 2.0 |

### Dependencies

| Library | License | Purpose |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | CLI framework |
| [PyYAML](https://pyyaml.org/) | MIT | YAML parsing |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | HTTP client for model APIs |
| [Rich](https://rich.readthedocs.io/) | MIT | Terminal UI rendering |

### Credits

- **Claude Code** (Anthropic) — Primary development platform
- **OpenCode** — Terminal adapter & testing partner
- **MimoCode** — Terminal adapter for frontend workflows
- **OpenAI Codex** — Terminal adapter for coding tasks
- **ECC plugin system** — Agent orchestration patterns
- **MCP (Model Context Protocol)** — Tool integration protocol

---

## 📦 Installation

### pip

```bash
pip install relayos
```

### Optional: web dashboard

```bash
pip install relayos[server]
relayos serve --open
```

### From source

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker (web dashboard only)

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 Languages

- [English](README.md)
- [中文 (Chinese)](README_ZH.md)
- [Deutsch (German)](README_DE.md)
- [Français (French)](README_FR.md)
- [Español (Spanish)](README_ES.md)
- [日本語 (Japanese)](README_JP.md)
- [한국어 (Korean)](README_KR.md)

---

## 📄 License

[Apache 2.0](LICENSE) Copyright 2026 [jjjjjjjjnnjnn](https://github.com/jjjjjjjjnnjnn)

---

<p align="center">
  <strong>Stop copy-pasting between AI tools.<br>
  Let them work together.</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Get_Started-10B981?style=for-the-badge" alt="Get Started"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
