<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Claude, GPT, Gemini, DeepSeek, 로컬 모델을 사용하는 당신.<br>
  RelayOS가 자동으로 협업하게 만듭니다.</strong><br>
  <br>
  터미널 네이티브 AI 런타임으로, 작업을 적합한 모델로 라우팅하고,<br>
  세션 간 프로젝트 컨텍스트를 기억하며, 비용을 절약합니다.
</p>

<p align="center">
  <a href="#-빠른-시작"><img src="https://img.shields.io/badge/빠른_시작-10B981?style=for-the-badge&logo=python" alt="빠른 시작"></a>
  <a href="#%EF%B8%8F-기능"><img src="https://img.shields.io/badge/기능-3B82F6?style=for-the-badge" alt="기능"></a>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-설치"><img src="https://img.shields.io/badge/pip_install_relayos-FF6F00?style=for-the-badge&logo=pypi" alt="설치"></a>
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

## 👋 문제점

5개의 브라우저 탭을 열어놓고 있다. ChatGPT는 추론, Claude는 아키텍처, Gemini는 연구, DeepSeek는 코딩 용도로 사용한다. 한 도구의 출력을 복사해서 다른 도구에 붙여넣는다. 무료 모델로 충분한 작업에 프리미엄 토큰을 낭비하고 있다.

**시간의 30%를 구축이 아닌 도구 관리에 낭비하고 있습니다.**

## 🎯 해결책

RelayOS는 AI 도구들이 진정한 팀처럼 작동하도록 만드는 조정 계층입니다:

```
┌─ 사용자 ──────────────────────────────────────┐
│                                                 │
│   relay session ask "Build a payment sys"       │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              RelayOS                             │
│                                                  │
│  1. 경쟁사 조사        → Gemini (무료)           │
│  2. 아키텍처 설계      → Claude                 │
│  3. 코드 구현          → GPT                    │
│  4. 보안 검토          → DeepSeek (저렴)         │
│  5. API 문서화         → Gemini (무료)           │
│                                                  │
│  총 비용: $0.01    시간: 45초                    │
└──────────────────────────────────────────────────┘
```

**인프라 제로.** `pip install relayos && relay`. Docker, 서버, 브라우저가 필요 없습니다.

---

## ✨ RelayOS의 차별점

| 기능 | 설명 | 가치 |
|---------|-------------|---------|
| 🧠 **스마트 라우팅** | 각 작업에 최적의 모델을 자동 선택 | 무료 모델 우선, 프리미엄은 필요할 때만 |
| 🔄 **멀티스텝 계획** | 작업을 실행 그래프로 분해 | 하나의 명령으로 여러 AI 모델이 협업 |
| 💾 **프로젝트 메모리** | 세션 간 지식 지속 | 워커는 학습한 내용을 절대 잊지 않음 |
| 💰 **비용 관리** | 모델별 추적 + 예산 제한 | 예상치 못한 청구서 없음 |
| 🔌 **21가지 터미널 유형** | Claude, GPT, Gemini, DeepSeek, 로컬 및 16+ 추가 | 자신의 도구 사용 가능 |
| ⌨️ **터미널 네이티브** | htop 스타일 TUI, 브라우저 불필요 | 워크플로우를 떠나지 않음 |

---

## ⚡ 빠른 시작

### 설치

```bash
pip install relayos
```

시도해보세요 — 정말 하나의 명령어입니다:

```bash
relay
```

컨트롤 패널이 열립니다. `htop`과 같지만, AI 팀을 위한 것입니다.

### 모든 모델과 채팅

```bash
# 최적의 모델로 자동 라우팅
relay session chat "Explain Kubernetes architecture"

# 또는 특정 워커 지정
relay session chat "Design this API" -w architect
```

### 멀티스텝 작업 실행

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS가 자동으로 분해, 라우팅하고 각 단계에 최적의 모델에서 실행합니다.

### 실행 전에 계획

```bash
relay session plan "Build a payment system"
# 실행 전 비용 추정 표시
```

### 그룹 토론 (여러 AI 워커)

```bash
relay session group "Review this architecture"
# 각 워커가 기여: 연구자 → 아키텍트 → 리뷰어
```

### 모델 즉시 전환

```bash
relay use opencode     # 모든 작업 → OpenCode (무료)
relay use mimo         # 모든 작업 → Mimo (무료)
relay use claude       # 모든 작업 → Claude (프리미엄)
relay use free         # 무료 우선 라우팅
```

### 프로젝트 지식

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # 이전 결정을 알고 있음!
relay project knowledge proj-id                     # 축적된 지식 확인
```

---

## 🖥️ TUI

```
 워커 (1-9 선택)           │ 상태
                           │  프로필: balanced
 1 🧠 architect    ○ idle  │  비용: $0.00
 2 🔍 researcher   ○ idle  │  대기 중: 0
 3 ⭐ coder        ○ idle  │
 4 🎯 reviewer     ○ idle  │ 액션
 5 🐛 debugger     ○ idle  │  f=free  b=balanced
                           │  o=opencode  c=claude
═══════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

키보드 기반, 마우스 불필요. 한 키로 프로필이나 워커를 전환합니다.

---

## 🗺️ 기능 그래프

`relay session plan "Build a payment system"`을 입력하면 RelayOS가 생성합니다:

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     요구사항 조사
       gemini-2.5-flash                FREE

  [2] architecture 시스템 아키텍처 설계
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       아키텍처 결정 검토
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
각 단계는 관련 데이터만 전달합니다 (전체 텍스트 아님).
약 800 tokens/단계, 단순 접근 방식보다 약 7배 적음.
```

---

## 🔧 지원되는 터미널 (21가지 유형)

설치된 도구를 자동으로 감지합니다:

| 상태 | 터미널 | 기본 모델 |
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
| ⚡ | Custom | (구성 가능) |

**모든 CLI를 터미널로 추가:**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 전체 명령어

| 명령어 | 기능 |
|---------|-------------|
| `relay` | 컨트롤 패널 열기 |
| `relay session chat` | 단일 AI 대화 |
| `relay session ask` | 자동 분해 + 실행 |
| `relay session group` | 다중 워커 토론 |
| `relay session plan` | 기능 그래프 표시 |
| `relay session list` | 최근 세션 |
| `relay use <terminal>` | 기본 터미널 전환 |
| `relay use <profile>` | 비용 프로필 전환 |
| `relay focus <worker>` | 워커로 SSH |
| `relay team create` | 템플릿에서 팀 생성 |
| `relay project create` | 지식 프로젝트 생성 |
| `relay project knowledge` | 프로젝트 메모리 표시 |
| `relay plan "task"` | 실행 계획 표시 |
| `relay estimate "task"` | 비용 추정 표시 |
| `relay run workflow.yaml` | YAML 워크플로 실행 |
| `relay config detect` | 설치된 터미널 스캔 |
| `relayos plugin add` | 사용자 정의 CLI 등록 |
| `relayos serve` | 웹 대시보드 (선택 사항) |

---

## 🏗️ 아키텍처

```
터미널 (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                     │
│  (세션 라우팅 + 기능 감지)                   │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                    │
│  (스키마 인식, 아티팩트 전달, DAG 실행)      │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                       │
│  (15개 모델 × 7가지 능력, 비용 인식)         │
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  어댑터     │     │  지식 베이스        │
│  (21 터미널)│     │  (SQLite, project)  │
└─────────────┘     └────────────────────┘
```

### 저장소 (모두 로컬, 인프라 제로)

```
~/.relayos/           ← 단일 디렉토리, 이식 가능
├── config.yaml       ← 모델/프로필 설정
├── state.db          ← 프로젝트 상태 + 결정
├── sessions.db       ← 세션 기록 + 메시지
├── knowledge.db      ← 세션 간 메모리
├── artifacts.db      ← 구조화된 단계 출력
└── workers.db        ← 영구적 워커
```

### 설계 철학

| 원칙 | 이유 |
|-----------|-----|
| **터미널 우선** | 개발자는 터미널에서 작업한다. 브라우저 불필요. |
| **상태, 채팅 아님** | 대화가 아닌 결정을 저장. 약 200배 더 압축적. |
| **능력 라우팅** | 모델이 아닌 작업 유형에 바인딩. 모델은 변하지만 작업은 변하지 않음. |
| **인프라 제로** | 단일 프로세스, 로컬 SQLite. Docker, Postgres, Redis 불필요. |
| **비용 인식** | 무료 계층 우선 사용. 생각하지 않고도 비용 절감. |

---

## 📈 버전 기록

| 버전 | 내용 |
|---------|------|
| **V0.1** | 모델 라우팅 — 5개 제공자 어댑터, YAML 워크플로 |
| **V0.2** | 터미널 풀 — 멀티 CLI, 비용 추적 |
| **V0.3** | 워커 시스템 — 8개 역할, 영속성, TUI |
| **V0.4** | 상태 컴파일러 — 구조화된 상태, 이벤트 소싱 |
| **V0.5** | 모델 스케줄러 — 15개 모델, 3개 비용 프로필 |
| **V0.6** | 세션 시스템 — chat/ask/group 모드 |
| **V0.7** | 기능 그래프 — 멀티스텝 작업 분해 |
| **V0.8** | 작업 그래프 실행 — 스키마 인식 아티팩트 전달 |
| **V0.9** | 세션 간 메모리 — 프로젝트 지식 베이스 |

---

## 💪 기술 스택

| 구성 요소 | 기술 |
|-----------|------|
| **언어** | Python 3.10+ |
| **CLI 프레임워크** | Click 8.0+ |
| **HTTP 클라이언트** | HTTPX 0.27+ |
| **터미널 UI** | Rich |
| **저장소** | SQLite (외부 DB 불필요) |
| **모델** | 15개 점수화 모델, 21개 터미널 유형 |
| **라이선스** | Apache 2.0 |

### 의존성

| 라이브러리 | 라이선스 | 목적 |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | CLI 프레임워크 |
| [PyYAML](https://pyyaml.org/) | MIT | YAML 파싱 |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | 모델 API용 HTTP 클라이언트 |
| [Rich](https://rich.readthedocs.io/) | MIT | 터미널 UI 렌더링 |

### Credits

- **Claude Code** (Anthropic) — Primary development platform
- **OpenCode** — Terminal adapter & testing partner
- **MimoCode** — Terminal adapter for frontend workflows
- **OpenAI Codex** — Terminal adapter for coding tasks
- **ECC plugin system** — Agent orchestration patterns
- **MCP (Model Context Protocol)** — Tool integration protocol

---

## 📦 설치

### pip

```bash
pip install relayos
```

### 선택 사항: 웹 대시보드

```bash
pip install relayos[server]
relayos serve --open
```

### 소스에서 설치

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker (웹 대시보드만 해당)

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 언어

- [English](README.md)
- [中文](README_ZH.md)
- [Deutsch](README_DE.md)
- [Francais](README_FR.md)
- [Espanol](README_ES.md)
- [日本語](README_JP.md)
- [한국어](README_KR.md)

---

## 📄 License

[Apache 2.0](LICENSE) Copyright 2026 [jjjjjjjjnnjnn](https://github.com/jjjjjjjjnnjnn)

---

<p align="center">
  <strong>AI 도구 간 복사-붙여넣기는 그만.<br>
  함께 작업하게 하세요.</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-빠른-시작"><img src="https://img.shields.io/badge/시작하기-10B981?style=for-the-badge" alt="시작하기"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
