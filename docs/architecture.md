# RelayOS Architecture

## Current (v0.3 — "Workforce")

```
Terminal (relay)
 │
 ├─ TUI (Rich-based dashboard)
 │    ├─ Workers view  (htop-style)
 │    ├─ Inbox view    (messages)
 │    └─ Commands      (run, create, send)
 │
 └─ CLI (relay/relayos commands)
      │
      ▼
┌──────────────────────────────────────────────┐
│              RelayOS Runtime                   │
│                                                │
│  ┌────────────────┐  ┌──────────────────┐    │
│  │  Worker Manager │  │  Worker Inbox    │    │
│  │  (persistent)   │  │  (SQLite msgs)   │    │
│  └───────┬────────┘  └──────────────────┘    │
│          │                                     │
│  ┌───────▼────────────────────────────────┐   │
│  │       Agent Adapter Layer               │   │
│  │  OpenAI │ Anthropic │ Google │ DeepSeek │   │
│  │  Ollama │ (5 providers, httpx-based)    │   │
│  └───────┬────────────────────────────────┘   │
│          │                                     │
│  ┌───────▼────────┐  ┌──────────────────┐    │
│  │  Flow Router   │  │ Context Compress  │    │
│  │ (smart routing)│  │ (70-90% savings)  │    │
│  ├────────────────┤  ├──────────────────┤    │
│  │  Cost Manager  │  │  Shared Memory   │    │
│  │ (token tracking)│  │  (SQLite)        │    │
│  └────────────────┘  └──────────────────┘    │
└──────────────────────────────────────────────┘
         │
         ▼
    ┌──────────┐  ┌──────────┐  ┌──────────┐
    │  OpenAI  │  │ Claude   │  │ Gemini   │
    │  GPT-4o  │  │ Sonnet   │  │ 2.5 Flash│
    └──────────┘  └──────────┘  └──────────┘
    ┌──────────┐  ┌──────────┐
    │ DeepSeek │  │ Ollama   │
    │  V3/R1   │  │ (Local)  │
    └──────────┘  └──────────┘
```

## Key Design Decisions

### 1. Terminal-native (primary interface)

`relay` command opens a Rich-based TUI (like htop/lazygit style). No browser needed for core usage. Web UI is optional via `relayos serve`.

### 2. Workers as the core primitive

Workers are persistent AI team members. Each has:
- A name and role (architect, researcher, coder)
- A provider + model assignment
- Persistent memory (project context)
- An inbox (inter-worker messaging)
- Lifecycle across sessions (SQLite-backed)

### 3. Zero infrastructure

Single process, local SQLite, no external dependencies. `pip install relayos && relay` is all you need.

### 4. Smart routing

Flow Router analyzes prompt content and routes to the optimal provider:
- Architecture → Claude
- Research → Gemini (free tier)
- Coding → GPT-4o
- Review → DeepSeek (cheap)
- Policy support: free_first, quality, cheapest

### 5. Context compression

Each step output is compressed before passing to the next agent, saving 70-90% on tokens. Strategies: summary, extract, truncate, structured.

## Data Flow (Workflow Run)

```
1. User: relay run workflow.yaml
2. Workflow Engine parses YAML steps
3. For each step, Flow Router selects optimal provider
4. Agent Adapter calls the provider API
5. Result stored in Shared Memory (SQLite)
6. Cost tracked in Cost Manager
7. Before next step, Context Compression reduces output
8. Next agent receives compressed context + new prompt
9. All steps logged to TUI in real-time
```

## Optional: Web Dashboard

```
relayos serve --open
  └── http://127.0.0.1:8080
        ├── Workers panel (same info as TUI)
        ├── Workflow runner with SSE streaming
        └── Memory browser
```

## Storage

All data in `~/.relayos/`:
```
~/.relayos/
├── config.yaml     # User configuration
├── memory.db       # Shared memory
├── workers.db      # Worker definitions
├── inbox.db        # Worker messages
└── cost.db         # Usage tracking
```
