<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Claude、GPT、Gemini、DeepSeek、ローカルモデルを使いこなすあなたへ。<br>
  RelayOS がそれらを自動的に連携させます。</strong><br>
  <br>
  ターミナルネイティブの AI 実行ランタイム。タスクを最適なモデルにルーティングし、<br>
  セッションを越えてプロジェクトコンテキストを記憶し、コストを削減します。
</p>

<p align="center">
  <a href="#-クイックスタート"><img src="https://img.shields.io/badge/クイックスタート-10B981?style=for-the-badge&logo=python" alt="クイックスタート"></a>
  <a href="#%EF%B8%8F-機能"><img src="https://img.shields.io/badge/機能-3B82F6?style=for-the-badge" alt="機能"></a>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-インストール"><img src="https://img.shields.io/badge/pip_install_relayos-FF6F00?style=for-the-badge&logo=pypi" alt="インストール"></a>
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

## 👋 問題点

5 つのブラウザタブを開いている。ChatGPT は推論、Claude はアーキテクチャ、Gemini は調査、DeepSeek はコーディング。あるツールの出力をコピーして、次のツールに貼り付ける。無料モデルで十分なタスクにプレミアムトークンを浪費している。

**あなたは時間の 30% を構築ではなくツール管理に費やしている。**

## 🎯 解決策

RelayOS は、あなたの AI ツールを真のチームとして機能させる協調レイヤーです：

```
┌─ あなた ──────────────────────────────────────┐
│                                                 │
│   relay session ask "Build a payment sys"       │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              RelayOS                             │
│                                                  │
│  1. 競合を調査         → Gemini (無料)           │
│  2. アーキテクチャ設計  → Claude                 │
│  3. コードを実装       → GPT                    │
│  4. セキュリティレビュー → DeepSeek (低コスト)    │
│  5. API をドキュメント化 → Gemini (無料)          │
│                                                  │
│  総コスト：$0.01    時間：45 秒                    │
└──────────────────────────────────────────────────┘
```

**インフラはゼロ。** `pip install relayos && relay`。Docker もサーバーもブラウザも不要。

---

## ✨ RelayOS の差別化要因

| 機能 | 動作 | 価値 |
|---------|-------------|---------|
| 🧠 **スマートルーティング** | 各タスクに最適なモデルを自動選択 | 無料モデル優先、プレミアムは必要な時のみ |
| 🔄 **マルチステップ計画** | タスクを実行グラフに分解 | 1 つのコマンドで複数の AI モデルが連携 |
| 💾 **プロジェクトメモリ** | セッション間で知識が持続 | ワーカーは学習したことを決して忘れない |
| 💰 **コスト管理** | モデル別追跡 + 予算制限 | 驚きの請求額なし |
| 🔌 **21 のターミナルタイプ** | Claude、GPT、Gemini、DeepSeek、ローカル＋16 以上 | 自分のツールを使える |
| ⌨️ **ターミナルネイティブ** | htop スタイルの TUI、ブラウザ不要 | ワークフローから離れない |

---

## ⚡ クイックスタート

### インストール

```bash
pip install relayos
```

試してみよう——本当に 1 コマンドだけ：

```bash
relay
```

コントロールパネルが開く。`htop` のようなものだが、AI チーム向け。

### 任意のモデルとチャット

```bash
# 最適なモデルに自動ルーティング
relay session chat "Explain Kubernetes architecture"

# または特定のワーカーを指定
relay session chat "Design this API" -w architect
```

### マルチステップタスクを実行

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS が自動的に分解、ルーティングし、各ステップに最適なモデルで実行します。

### 実行前に計画

```bash
relay session plan "Build a payment system"
# 実行前にコスト見積もりを表示
```

### グループ討論（複数 AI ワーカー）

```bash
relay session group "Review this architecture"
# 各ワーカーが貢献：リサーチャー → アーキテクト → レビュアー
```

### モデルを瞬時に切り替え

```bash
relay use opencode     # 全タスク → OpenCode (無料)
relay use mimo         # 全タスク → Mimo (無料)
relay use claude       # 全タスク → Claude (プレミアム)
relay use free         # 無料優先ルーティング
```

### プロジェクト知識

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # 以前の決定を把握！
relay project knowledge proj-id                     # 蓄積された知識を表示
```

---

## 🖥️ TUI

```
 ワーカー (1-9 選択)        │ ステータス
                            │  プロファイル：balanced
 1 🧠 architect    ○ idle  │  コスト：$0.00
 2 🔍 researcher   ○ idle  │  保留中：0
 3 ⭐ coder        ○ idle  │
 4 🎯 reviewer     ○ idle  │ アクション
 5 🐛 debugger     ○ idle  │  f=free  b=balanced
                            │  o=opencode  c=claude
════════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

キーボード駆動、マウス不要。1 キーでプロファイルやワーカーを切り替え。

---

## 🗺️ ケイパビリティグラフ

`relay session plan "Build a payment system"` と入力すると、RelayOS は以下を生成：

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     要件を調査
       gemini-2.5-flash                FREE

  [2] architecture システムアーキテクチャを設計
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       アーキテクチャ決定をレビュー
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
各ステップは関連データのみを渡す（全文ではなく）。
約 800 tokens/ステップ、単純なアプローチの約 7 分の 1。
```

---

## 🔧 サポートされているターミナル（21 種類）

インストール済みのものを自動検出：

| ステータス | ターミナル | デフォルトモデル |
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
| ⚡ | Custom | (設定可能) |

**任意の CLI をターミナルとして追加：**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 全コマンド

| コマンド | 機能 |
|---------|-------------|
| `relay` | コントロールパネルを開く |
| `relay session chat` | 単一 AI との会話 |
| `relay session ask` | 自動分解 + 実行 |
| `relay session group` | 複数ワーカー討論 |
| `relay session plan` | ケイパビリティグラフを表示 |
| `relay session list` | 最近のセッション |
| `relay use <terminal>` | デフォルトターミナルを切り替え |
| `relay use <profile>` | コストプロファイルを切り替え |
| `relay focus <worker>` | ワーカーに SSH |
| `relay team create` | テンプレートからチーム作成 |
| `relay project create` | 知識プロジェクトを作成 |
| `relay project knowledge` | プロジェクトメモリを表示 |
| `relay plan "task"` | 実行計画を表示 |
| `relay estimate "task"` | コスト見積もりを表示 |
| `relay run workflow.yaml` | YAML ワークフローを実行 |
| `relay config detect` | インストール済みターミナルをスキャン |
| `relayos plugin add` | カスタム CLI を登録 |
| `relayos serve` | Web ダッシュボード（オプション） |

---

## 🏗️ アーキテクチャ

```
ターミナル (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                     │
│  (セッションルーティング + 能力検出)         │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                    │
│  (スキーマ認識、アーティファクト受け渡し)     │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                       │
│  (15 モデル × 7 能力、コスト認識)            │
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  アダプター  │     │  知識ベース         │
│  (21 端末)  │     │  (SQLite, project)  │
└─────────────┘     └────────────────────┘
```

### ストレージ（全てローカル、インフラゼロ）

```
~/.relayos/           ← 単一ディレクトリ、ポータブル
├── config.yaml       ← モデル/プロファイル設定
├── state.db          ← プロジェクト状態 + 決定
├── sessions.db       ← セッション履歴 + メッセージ
├── knowledge.db      ← セッション間メモリ
├── artifacts.db      ← 構造化されたステップ出力
└── workers.db        ← 永続的なワーカー
```

### 設計哲学

| 原則 | 理由 |
|-----------|-----|
| **ターミナルファースト** | 開発者はターミナルで作業する。ブラウザは不要。 |
| **状態、チャットではない** | 会話ではなく決定を保存。約 200 倍コンパクト。 |
| **能力ルーティング** | モデルではなくタスクタイプにバインド。モデルは変わるが、タスクは変わらない。 |
| **インフラゼロ** | 単一プロセス、ローカル SQLite。Docker、Postgres、Redis は不要。 |
| **コスト認識** | まず無料枠を利用。考えずにコスト削減。 |

---

## 📈 バージョン履歴

| バージョン | 内容 |
|---------|------|
| **V0.1** | モデルルーティング — 5 プロバイダアダプター、YAML ワークフロー |
| **V0.2** | ターミナルプール — マルチ CLI、コスト追跡 |
| **V0.3** | ワーカーシステム — 8 ロール、永続性、TUI |
| **V0.4** | 状態コンパイラ — 構造化状態、イベントソーシング |
| **V0.5** | モデルスケジューラー — 15 モデル、3 コストプロファイル |
| **V0.6** | セッションシステム — chat/ask/group モード |
| **V0.7** | ケイパビリティグラフ — マルチステップタスク分解 |
| **V0.8** | タスクグラフ実行 — スキーマ認識アーティファクト受け渡し |
| **V0.9** | セッション間メモリ — プロジェクト知識ベース |

---

## 💪 構築に使用した技術

| コンポーネント | 技術 |
|-----------|------|
| **言語** | Python 3.10+ |
| **CLI フレームワーク** | Click 8.0+ |
| **HTTP クライアント** | HTTPX 0.27+ |
| **ターミナル UI** | Rich |
| **ストレージ** | SQLite（外部 DB 不要） |
| **モデル** | 15 のスコアリングモデル、21 のターミナルタイプ |
| **ライセンス** | Apache 2.0 |

### 依存関係

| ライブラリ | ライセンス | 目的 |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | CLI フレームワーク |
| [PyYAML](https://pyyaml.org/) | MIT | YAML 解析 |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | モデル API 用 HTTP クライアント |
| [Rich](https://rich.readthedocs.io/) | MIT | ターミナル UI レンダリング |

### Credits

- **Claude Code** (Anthropic) — Primary development platform
- **OpenCode** — Terminal adapter & testing partner
- **MimoCode** — Terminal adapter for frontend workflows
- **OpenAI Codex** — Terminal adapter for coding tasks
- **ECC plugin system** — Agent orchestration patterns
- **MCP (Model Context Protocol)** — Tool integration protocol

---

## 📦 インストール

### pip

```bash
pip install relayos
```

### オプション：Web ダッシュボード

```bash
pip install relayos[server]
relayos serve --open
```

### ソースから

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker（Web ダッシュボードのみ）

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 言語

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
  <strong>AI ツール間のコピーペーストにもうさようなら。<br>
  連携させて仕事をさせよう。</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-クイックスタート"><img src="https://img.shields.io/badge/始める-10B981?style=for-the-badge" alt="始める"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
