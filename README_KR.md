<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>개발자를 위한 영구적 AI 워커.</strong><br>
  터미널 네이티브 AI 실행 런타임 — Claude, GPT, Gemini, DeepSeek 및 로컬 모델로 작업을 라우팅하고,<br>
  기능 인식 스케줄링, 공유 프로젝트 메모리, 다중 단계 실행 그래프를 제공합니다.
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

## 📋 목차

| 섹션 | 설명 |
|------|------|
| [🎯 개요](#-overview) | RelayOS가 무엇이고 왜 필요한지 |
| [✨ 기능](#-features) | 모든 기능 (V0.1–V0.9) |
| [⚡ 빠른 시작](#-quick-start) | 설치 및 시작 |
| [🔧 CLI 참조](#-cli-reference) | 전체 22개 명령어 |
| [🏗️ 아키텍처](#%EF%B8%8F-architecture) | 시스템 설계 |
| [🛣️ 로드맵](#%EF%B8%8F-roadmap) | 버전 기록 및 미래 계획 |
| [🙏 크레딧](#%EF%B8%8F-credits) | 감사의 말 |
| [📄 라이선스](#-license) | Apache 2.0 |

---

## 🎯 개요

**RelayOS**는 터미널 네이티브 AI 실행 런타임입니다. AI 팀을 위한 htop과 같습니다.

여러분은 여러 AI 도구(Claude Code, ChatGPT, Gemini, DeepSeek, 로컬 모델)를 가지고 있습니다. 각각은 훌륭하지만, 서로 대화하지 못합니다. RelayOS는 작업을 올바른 모델로 라우팅하고, 세션 간에 프로젝트 컨텍스트를 기억하며, 다중 단계 계획을 실행하는 조정 계층입니다 — 모두 터미널에서, 인프라 없이.

### 진화 과정

```
V0.1  모델 라우팅          → 올바른 모델 선택
V0.2  터미널 풀            → CLI 워커 관리
V0.3  워커 시스템          → 영구적 AI 팀원
V0.4  상태 컴파일러        → 채팅 기록이 아닌 구조화된 상태
V0.5  모델 스케줄러        → 비용 인식 (무료 우선, 단계적 업그레이드)
V0.6  세션 시스템          → chat / ask / group 모드
V0.7  기능 그래프          → 다중 단계 작업 분해
V0.8  그래프 실행          → 스키마 인식 아티팩트 전달
V0.9  교차 세션 메모리     → 프로젝트 지식 베이스
```

---

## ✨ 기능

### 🤖 모델 스케줄링 (V0.1–V0.5)

| 기능 | 세부 사항 |
|------|----------|
| **5개 제공자 어댑터** | OpenAI, Anthropic, Google, DeepSeek, Ollama |
| **15개 모델 점수화** | 각각 7가지 능력 (코딩, 아키텍처, 리뷰, 연구, 추론, 빠른 작업, 작성) |
| **3가지 비용 프로필** | `free` (로컬 우선), `balanced` (저비용 우선), `quality` (최고 우선) |
| **터미널 전환** | `relay use opencode` — CLI 터미널 간 즉시 전환 |
| **자동 에스컬레이션** | 낮은 신뢰도 시 무료 → 저비용 → 프리미엄 |

### 🧠 워커 시스템 (V0.3)

| 기능 | 세부 사항 |
|------|----------|
| **8개 기본 워커** | architect, researcher, coder, reviewer, debugger, writer, assistant, data-engineer |
| **워커 영속성** | SQLite 기반, 재시작 후에도 유지 |
| **워커 받은 편지함** | 작업 기반 워커 간 메시징 |
| **포커스 뷰** | `relay focus <worker>` — 워커의 마음 속으로 SSH |

### 💬 세션 시스템 (V0.6–V0.7)

| 기능 | 세부 사항 |
|------|----------|
| **3가지 모드** | `chat` (단일), `ask` (자동 실행), `group` (다중 워커) |
| **기능 라우팅** | 사용한 모델이 아니라 수행 중인 작업 유형 추적 |
| **기능 그래프** | 작업을 다중 단계 DAG로 분해 |
| **고정 기능** | 세션이 코딩/아키텍처를 기억, 스케줄러가 모델 선택 |

### 🔄 작업 그래프 실행 (V0.8)

| 기능 | 세부 사항 |
|------|----------|
| **단계 스키마** | 입출력 계약이 있는 6가지 단계 유형 |
| **아티팩트 전달** | 전체 텍스트가 아닌 구조화된 필드 참조 |
| **토큰 효율성** | 스키마 없이 ~3000 대비 단계당 ~800 토큰 |
| **재개** | 완료된 단계 건너뛰기, 실패 지점에서 계속 |
| **비용 추정** | 실행 전 단계별 및 총 비용 표시 |

### 🗄️ 교차 세션 메모리 (V0.9)

| 기능 | 세부 사항 |
|------|----------|
| **프로젝트 지식** | 세션 간에 지식 축적 |
| **KnowledgeCompiler** | 아티팩트에서 순수 코드 추출 |
| **건너뛰기 명령** | 알려진 정보를 프롬프트에 주입 (재발견 불필요) |
| **약 43% 절감** | 반복 세션에서의 효율성 |

### 🖥️ 터미널 UI

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

## ⚡ 빠른 시작

### 설치

```bash
pip install relayos
```

### 사용법

```bash
relay             # TUI 열기 (htop 스타일 제어판)
relay use free    # 무료 모델 우선 사용으로 전환
```

### Chat / Ask / Group

```bash
# 단일 AI 대화 (자동 라우팅)
relay session chat "Explain Kubernetes architecture"

# 다중 단계 작업 실행
relay session ask "Build a JWT auth system in FastAPI"

# 다중 워커 그룹 토론
relay session group "Design a payment system"
```

### 터미널 즉시 전환

```bash
relay use opencode   # 모든 작업 → OpenCode (무료)
relay use mimo       # 모든 작업 → Mimo (무료)
relay use claude     # 모든 작업 → Claude (프리미엄)
```

### 프로젝트 지식

```bash
relay project create payment-system       # 프로젝트 생성
relay project knowledge <project-id>      # 축적된 지식 표시
relay session chat "Add refund" -p <pid>  # 프로젝트 범위의 세션
```

### 실행 전 계획

```bash
relay session plan "Build a payment system"
# 표시: research(gemini free) → architecture(claude) → review(deepseek)
```

---

## 🔧 CLI 참조

| 명령어 | 설명 |
|--------|------|
| `relay` | TUI 제어판 열기 |
| `relay session chat` | 단일 AI 대화 |
| `relay session ask` | 작업 자동 분해 및 실행 |
| `relay session group` | 다중 워커 그룹 토론 |
| `relay session plan` | 실행 없이 기능 그래프 표시 |
| `relay session list` | 최근 세션 목록 |
| `relay use` | 기본 터미널/프로필 전환 |
| `relay profile` | 라우팅 프로필 설정 |
| `relay focus` | 워커 포커스 뷰 |
| `relay team create` | 템플릿에서 팀 생성 |
| `relay project create` | 지식 베이스용 프로젝트 생성 |
| `relay project knowledge` | 프로젝트 지식 표시 |
| `relay plan` | 작업 실행 계획 표시 |
| `relay estimate` | 비용 추정 표시 |
| `relay run` | YAML 워크플로 실행 |
| `relay config` | 설정 마법사 |
| `relay plugin add` | 사용자 정의 CLI 터미널 등록 |
| `relayos serve` | 선택적 웹 대시보드 |

### 키보드 단축키 (TUI 내)

| 키 | 동작 |
|----|------|
| `f` | 무료 프로필 |
| `b` | 균형 프로필 |
| `o` | OpenCode 터미널 |
| `m` | Mimo 터미널 |
| `c` | Claude 터미널 |
| `1-9` | 워커 선택 |
| `q` | 종료 |
| `r` | 새로고침 |

---

## 🏗️ 아키텍처

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

### 핵심 모듈

| 모듈 | 역할 |
|------|------|
| `relayos/core/scheduler.py` | 15개 모델 비용 인식 스케줄러 |
| `relayos/core/session.py` | 세션 라이프사이클 + 메시지 |
| `relayos/core/conversation.py` | Chat/Ask/Group 엔진 |
| `relayos/core/planner.py` | 기능 그래프 + 실행 |
| `relayos/core/knowledge.py` | 교차 세션 프로젝트 메모리 |
| `relayos/core/state.py` | 구조화된 상태 저장소 |
| `relayos/core/schemas.py` | 단계 입출력 계약 |
| `relayos/core/artifacts.py` | 구조화된 아티팩트 저장소 |
| `relayos/tui/app.py` | 키보드 구동 TUI |

### 저장소 (모두 로컬 SQLite, 인프라 제로)

```
~/.relayos/
├── config.yaml        # 사용자 설정
├── state.db           # 프로젝트 상태 + 결정 + 이벤트
├── sessions.db        # 세션 기록 + 메시지
├── knowledge.db       # 교차 세션 프로젝트 지식
├── artifacts.db       # 구조화된 단계 출력
└── workers.db         # 영구적 워커 정의
```

---

## 🛣️ 로드맵

### 완료 (V0.1–V0.9)

| 버전 | 핵심 기능 | 상태 |
|------|----------|------|
| V0.1 | 모델 라우팅 (5개 어댑터, YAML 워크플로) | ✅ |
| V0.2 | 터미널 풀 (다중 CLI, 비용 추적) | ✅ |
| V0.3 | 워커 시스템 (8개 역할, 영속성, TUI) | ✅ |
| V0.4 | 상태 컴파일러 (구조화된 상태, 이벤트 소싱) | ✅ |
| V0.5 | 모델 스케줄러 (15개 모델, 3개 비용 프로필) | ✅ |
| V0.6 | 세션 시스템 (chat/ask/group 모드) | ✅ |
| V0.7 | 기능 그래프 (다중 단계 작업 분해) | ✅ |
| V0.8 | 작업 그래프 실행 (스키마 인식 아티팩트 전달) | ✅ |
| V0.9 | 교차 세션 메모리 (프로젝트 지식 베이스) | ✅ |

### 계획됨

- **V1.0** — 플러그인 생태계, MCP 라우터, 분산 워커
- **V1.1** — 워크플로 재생 (LangSmith 스타일 타임라인)
- **V1.2** — 다중 머신 워커 풀

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
- [中文 (Chinese)](README_ZH.md)
- [Deutsch (German)](README_DE.md)
- [Français (French)](README_FR.md)
- [Español (Spanish)](README_ES.md)
- [日本語 (Japanese)](README_JP.md)

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
