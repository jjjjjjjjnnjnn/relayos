# RelayOS Roadmap

## v0.3 — "Workforce" (Current)

**Goal**: Persistent AI workers with terminal-native UX.

- [x] Worker Pool (8 default roles with emoji/description)
- [x] Worker Inbox (inter-worker messaging, SQLite)
- [x] Flow Router (task-type → optimal provider)
- [x] Context Compression (70-90% token savings)
- [x] Terminal UI (Rich-based, htop-style workers view)
- [x] Cost Manager (per-provider token tracking)
- [x] CLI relay command (opens TUI, zero infrastructure)

**In progress:**
- Worker persistence (survive restarts, saved to SQLite)
- TUI tabs (workers, tasks, inbox, memory, logs)
- relay worker CLI group (create/list/remove/exec)
- Prompt Cache (duplicate task detection)

## v0.4 — "Teams"

**Goal**: Team templates and workflow orchestration.

- Worker-to-worker task handoff via inbox
- Team config presets (startup, research, writing)
- DAG workflow (non-linear, parallel execution)
- Worker summary auto-compression (<500 tokens)
- TUI focus command (SSH into a worker)
- Shared workspace (project-level context)

## v0.5 — "Mesh"

**Goal**: Tool routing and plugin system.

- MCP Tool Router (agent → relayos → tool)
- Plugin system for custom worker types
- Prompt fingerprint cache (hash-based dedup)
- Embedding cache (semantic retrieval)
- Workflow replay (like LangSmith timeline)

## v1.0 — "Stable"

**Goal**: Production-ready AI workforce manager.

- SDK for embedding workers in other tools
- Multi-machine worker pool (SSH agents)
- Event-sourced inbox with full history
- Vector memory (local via sqlite-vss)
- Plugin registry (community worker templates)

## Non-Goals

- Web Dashboard as primary UI (TUI is primary; web is optional via `relayos serve`)
- User auth / multi-tenant
- Kubernetes-scale clustering
- Plugin marketplace (v2)
- Mobile app
