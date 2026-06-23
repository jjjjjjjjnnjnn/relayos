# Changelog

All notable changes to RelayOS will be documented in this file.

## [0.1.0a1] - 2026-06-23

### Added — V0.1: Model Routing

- Agent adapters: OpenAI (GPT-4o), Anthropic (Claude), Google (Gemini), DeepSeek, Ollama
- YAML workflow engine with sequential and parallel execution
- Shared memory (SQLite-backed key-value store)
- MCP client (stdio-based tool integration)
- CLI commands: run, chat, agents, terminal, remember, recall, memory-list, init
- Multi-language README (EN, ZH, DE, FR, ES, JP, KR)

### Added — V0.2: Terminal Pool + Cost

- Terminal pool with SQLite persistence
- Terminal types: claude, mimo, opencode, codex, qcode, custom
- Cost Manager with per-provider token tracking
- Dockerfile + docker-compose.yml (optional web dashboard)
- Web Dashboard (FastAPI + SPA)

### Added — V0.3: Worker System

- Worker Pool: 8 default roles (architect, researcher, coder, etc.)
- Worker persistence across sessions (SQLite)
- Flow Router: task-type based provider selection
- Context Compression: 70-90% token reduction between steps
- Worker Inbox: inter-worker messaging
- Terminal UI (Rich-based, htop-style)
- `relay` command opens TUI by default

### Added — V0.4: State Compiler

- State Store: 5 unified tables (workers, state, decisions, events, tasks)
- Structured context builder with 1200 token budget
- State Compiler: pure code state transitions (zero LLM)
- Event Sourcing: append-only event log
- Worker Identity + Focus TUI + Team Templates

### Added — V0.5: Model Scheduler

- Cost-Aware Model Router with 15 models x 7 capabilities
- 3 profiles: free, balanced, quality
- Escalation routing on low confidence
- `relay use` instant terminal switching
- Capability Registry with scoring

### Added — V0.6: Session System

- Session abstraction (3 modes: chat, ask, group)
- Session-aware routing (remembers last capability)
- Multi-worker group discussion
- Execution Planner with 5 task patterns
- TUI with keyboard-driven control panel

### Added — V0.7: Capability Graph

- Multi-capability task decomposition
- Capability Graph Engine (DAG generation)
- `relay session plan` shows graph without executing
- Auto-routing per capability

### Added — V0.8: Task Graph Execution

- Step Schemas: input/output contracts per capability
- Artifact Store: structured step outputs with field-level extraction
- TaskGraphExecutor: schema-aware artifact passing (~800t/step)
- Resume capability: skip completed steps
- ~7x token reduction via structured field passing

### Added — V0.9: Cross-Session Memory

- Project knowledge: cross-session fact storage
- KnowledgeCompiler: pure code extraction from artifacts
- Session summaries with token tracking
- Skip instructions prevent rediscovery (~43% savings)
- `relay project` commands

### Infrastructure

- Plugin system for custom terminals
- Auto-detection of installed AI CLIs
- 7 language READMEs
- Apache 2.0 License
- CI workflow (GitHub Actions)

## Stats

- **76 files**, **7100+ Python lines**, **30 modules**
- **15 models** x **7 capabilities** scored
- **3 profiles**: free, balanced, quality
- **6 step types** with schemas
- **3 databases**: state, sessions, knowledge
