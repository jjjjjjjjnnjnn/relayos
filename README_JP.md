<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>開発者のための永続的AIワーカー。</strong><br>
  ターミナルネイティブのAI実行ランタイム — Claude、GPT、Gemini、DeepSeek、ローカルモデルへタスクをルーティング、<br>
  能力認識スケジューリング、共有プロジェクトメモリ、マルチステップ実行グラフを備えています。
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

## 📋 目次

| セクション | 説明 |
|-----------|------|
| [🎯 概要](#-overview) | RelayOSとは何か、なぜ存在するのか |
| [✨ 機能](#-features) | すべての機能 (V0.1–V0.9) |
| [⚡ クイックスタート](#-quick-start) | インストールと起動 |
| [🔧 CLIリファレンス](#-cli-reference) | 全22コマンド |
| [🏗️ アーキテクチャ](#%EF%B8%8F-architecture) | システム設計 |
| [🛣️ ロードマップ](#%EF%B8%8F-roadmap) | バージョン履歴と将来計画 |
| [🙏 クレジット](#%EF%B8%8F-credits) | 謝辞 |
| [📄 ライセンス](#-license) | Apache 2.0 |

---

## 🎯 概要

**RelayOS** は、ターミナルネイティブのAI実行ランタイムです。あなたのAIチームのためのhtopのようなものです。

あなたは複数のAIツール（Claude Code、ChatGPT、Gemini、DeepSeek、ローカルモデル）を持っています。それぞれ優れていますが、互いに通信することはありません。RelayOSは、タスクを適切なモデルにルーティングし、セッションを越えてプロジェクトコンテキストを記憶し、マルチステップの計画を実行する協調レイヤーです — すべてターミナルから、インフラゼロで。

### 進化の過程

```
V0.1  モデルルーティング     → 適切なモデルを選択
V0.2  ターミナルプール       → CLIワーカーを管理
V0.3  ワーカーシステム       → 永続的なAIチームメンバー
V0.4  状態コンパイラ         → 構造化された状態、チャット履歴ではなく
V0.5  モデルスケジューラー   → コスト認識（無料優先、段階的アップグレード）
V0.6  セッションシステム     → chat / ask / group モード
V0.7  ケイパビリティグラフ   → マルチステップタスク分解
V0.8  グラフ実行             → スキーマ認識アーティファクト受け渡し
V0.9  クロスセッションメモリ → プロジェクト知識ベース
```

---

## ✨ 機能

### 🤖 モデルスケジューリング (V0.1–V0.5)

| 機能 | 詳細 |
|------|------|
| **5つのプロバイダアダプター** | OpenAI、Anthropic、Google、DeepSeek、Ollama |
| **15のモデルをスコアリング** | 各7つの能力（コーディング、アーキテクチャ、レビュー、研究、推論、クイック、ライティング） |
| **3つのコストプロファイル** | `free`（ローカル優先）、`balanced`（低コスト優先）、`quality`（最高品質優先） |
| **ターミナル切り替え** | `relay use opencode` — CLI端末間の即時切り替え |
| **自動エスカレーション** | 低信頼度時に無料 → 低コスト → プレミアム |

### 🧠 ワーカーシステム (V0.3)

| 機能 | 詳細 |
|------|------|
| **8つのデフォルトワーカー** | architect、researcher、coder、reviewer、debugger、writer、assistant、data-engineer |
| **ワーカーの永続性** | SQLiteベース、再起動後も保持 |
| **ワーカー受信箱** | タスクベースのワーカー間メッセージング |
| **フォーカスビュー** | `relay focus <worker>` — ワーカーの頭の中にSSH |

### 💬 セッションシステム (V0.6–V0.7)

| 機能 | 詳細 |
|------|------|
| **3つのモード** | `chat`（単一）、`ask`（自動実行）、`group`（複数ワーカー） |
| **ケイパビリティルーティング** | 使用したモデルではなく、実行中のタスクタイプを追跡 |
| **ケイパビリティグラフ** | タスクをマルチステップDAGに分解 |
| **スティッキーケイパビリティ** | セッションがコーディング/アーキテクチャを記憶、スケジューラーがモデルを選択 |

### 🔄 タスクグラフ実行 (V0.8)

| 機能 | 詳細 |
|------|------|
| **ステップスキーマ** | 入出力コントラクト付き6種類のステップタイプ |
| **アーティファクト受け渡し** | 全文ではなく構造化フィールド参照 |
| **トークン効率** | スキーマなしの~3000に対して1ステップあたり~800トークン |
| **再開** | 完了したステップをスキップ、失敗箇所から続行 |
| **コスト見積もり** | 実行前にステップごとおよび合計コストを表示 |

### 🗄️ クロスセッションメモリ (V0.9)

| 機能 | 詳細 |
|------|------|
| **プロジェクト知識** | セッションを越えて知識が蓄積 |
| **KnowledgeCompiler** | アーティファクトからの純粋なコード抽出 |
| **スキップ命令** | 既知の情報をプロンプトに注入（再発見不要） |
| **約43%の削減** | 繰り返しセッションでの効率化 |

### 🖥️ ターミナルUI

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

## ⚡ クイックスタート

### インストール

```bash
pip install relayos
```

### 使用方法

```bash
relay             # TUIを開く（htopスタイルのコントロールパネル）
relay use free    # 無料モデルを優先して使用
```

### Chat / Ask / Group

```bash
# 単一AIとの会話（自動ルーティング）
relay session chat "Explain Kubernetes architecture"

# マルチステップタスク実行
relay session ask "Build a JWT auth system in FastAPI"

# 複数ワーカーによるグループ討論
relay session group "Design a payment system"
```

### ターミナルを瞬時に切り替え

```bash
relay use opencode   # すべてのタスク → OpenCode（無料）
relay use mimo       # すべてのタスク → Mimo（無料）
relay use claude     # すべてのタスク → Claude（プレミアム）
```

### プロジェクト知識

```bash
relay project create payment-system       # プロジェクトを作成
relay project knowledge <project-id>      # 蓄積された知識を表示
relay session chat "Add refund" -p <pid>  # プロジェクトにスコープされたセッション
```

### 実行前に計画

```bash
relay session plan "Build a payment system"
# 表示: research(gemini free) → architecture(claude) → review(deepseek)
```

---

## 🔧 CLIリファレンス

| コマンド | 説明 |
|---------|------|
| `relay` | TUIコントロールパネルを開く |
| `relay session chat` | 単一AIとの会話 |
| `relay session ask` | タスクを自動分解して実行 |
| `relay session group` | 複数ワーカーによるグループ討論 |
| `relay session plan` | 実行せずにケイパビリティグラフを表示 |
| `relay session list` | 最近のセッションを一覧表示 |
| `relay use` | デフォルトのターミナル/プロファイルを切り替え |
| `relay profile` | ルーティングプロファイルを設定 |
| `relay focus` | ワーカーフォーカスビュー |
| `relay team create` | テンプレートからチームを作成 |
| `relay project create` | 知識ベース用のプロジェクトを作成 |
| `relay project knowledge` | プロジェクト知識を表示 |
| `relay plan` | タスクの実行計画を表示 |
| `relay estimate` | コスト見積もりを表示 |
| `relay run` | YAMLワークフローを実行 |
| `relay config` | 設定ウィザード |
| `relay plugin add` | カスタムCLIターミナルを登録 |
| `relayos serve` | オプションのWebダッシュボード |

### キーボードショートカット（TUI内）

| キー | アクション |
|-----|----------|
| `f` | 無料プロファイル |
| `b` | バランスプロファイル |
| `o` | OpenCodeターミナル |
| `m` | Mimoターミナル |
| `c` | Claudeターミナル |
| `1-9` | ワーカーを選択 |
| `q` | 終了 |
| `r` | 更新 |

---

## 🏗️ アーキテクチャ

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

### コアモジュール

| モジュール | 役割 |
|-----------|------|
| `relayos/core/scheduler.py` | 15モデルのコスト認識スケジューラー |
| `relayos/core/session.py` | セッションライフサイクル + メッセージ |
| `relayos/core/conversation.py` | Chat/Ask/Groupエンジン |
| `relayos/core/planner.py` | ケイパビリティグラフ + 実行 |
| `relayos/core/knowledge.py` | クロスセッションのプロジェクトメモリ |
| `relayos/core/state.py` | 構造化状態ストア |
| `relayos/core/schemas.py` | ステップ入出力コントラクト |
| `relayos/core/artifacts.py` | 構造化アーティファクトストレージ |
| `relayos/tui/app.py` | キーボード駆動のTUI |

### ストレージ（全てローカルSQLite、インフラゼロ）

```
~/.relayos/
├── config.yaml        # ユーザー設定
├── state.db           # プロジェクト状態 + 決定 + イベント
├── sessions.db        # セッション履歴 + メッセージ
├── knowledge.db       # クロスセッションのプロジェクト知識
├── artifacts.db       # 構造化されたステップ出力
└── workers.db         # 永続的なワーカー定義
```

---

## 🛣️ ロードマップ

### 完了 (V0.1–V0.9)

| バージョン | コア機能 | ステータス |
|-----------|---------|----------|
| V0.1 | モデルルーティング（5アダプター、YAMLワークフロー） | ✅ |
| V0.2 | ターミナルプール（マルチCLI、コスト追跡） | ✅ |
| V0.3 | ワーカーシステム（8ロール、永続性、TUI） | ✅ |
| V0.4 | 状態コンパイラ（構造化状態、イベントソーシング） | ✅ |
| V0.5 | モデルスケジューラー（15モデル、3コストプロファイル） | ✅ |
| V0.6 | セッションシステム（chat/ask/groupモード） | ✅ |
| V0.7 | ケイパビリティグラフ（マルチステップタスク分解） | ✅ |
| V0.8 | タスクグラフ実行（スキーマ認識アーティファクト受け渡し） | ✅ |
| V0.9 | クロスセッションメモリ（プロジェクト知識ベース） | ✅ |

### 計画中

- **V1.0** — プラグインエコシステム、MCPルーター、分散ワーカー
- **V1.1** — ワークフローリプレイ（LangSmithスタイルのタイムライン）
- **V1.2** — マルチマシンワーカープール

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
