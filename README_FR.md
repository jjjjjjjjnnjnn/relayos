<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Des travailleurs IA persistants pour les développeurs.</strong><br>
  Un runtime d'exécution IA natif pour le terminal — achemine les tâches vers Claude, GPT, Gemini, DeepSeek et les modèles locaux<br>
  avec une ordonnancement conscient des capacités, une mémoire de projet partagée et des graphes d'exécution multi-étapes.
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

## 📋 Table des matières

| Section | Description |
|---------|-------------|
| [🎯 Aperçu](#-overview) | Ce qu'est RelayOS et pourquoi il existe |
| [✨ Fonctionnalités](#-features) | Toutes les capacités (V0.1–V0.9) |
| [⚡ Démarrage rapide](#-quick-start) | Installation et démarrage |
| [🔧 Référence CLI](#-cli-reference) | Les 22 commandes |
| [🏗️ Architecture](#%EF%B8%8F-architecture) | Conception du système |
| [🛣️ Feuille de route](#%EF%B8%8F-roadmap) | Historique des versions et futur |
| [🙏 Remerciements](#%EF%B8%8F-credits) | Reconnaissances |
| [📄 Licence](#-license) | Apache 2.0 |

---

## 🎯 Aperçu

**RelayOS** est un runtime d'exécution IA natif pour le terminal. Comme htop pour votre équipe IA.

Vous avez plusieurs outils IA (Claude Code, ChatGPT, Gemini, DeepSeek, modèles locaux). Chacun est excellent. Ils ne communiquent pas entre eux. RelayOS est la couche de coordination qui achemine les tâches vers le bon modèle, mémorise le contexte du projet entre les sessions et exécute des plans multi-étapes — tout depuis votre terminal, zéro infrastructure.

### L'évolution

```
V0.1  Routage de modèles     →  choisir le bon modèle
V0.2  Pool de terminaux      →  gérer les travailleurs CLI
V0.3  Système de travailleurs →  membres d'équipe IA persistants
V0.4  Compilateur d'état     →  état structuré, pas d'historique de chat
V0.5  Ordonnanceur de modèles →  conscient des coûts (gratuit d'abord, escalade)
V0.6  Système de sessions    →  modes chat / ask / group
V0.7  Graphe de capacités    →  décomposition de tâches multi-étapes
V0.8  Exécution de graphe    →  passage d'artefacts avec schémas
V0.9  Mémoire inter-sessions →  base de connaissances du projet
```

---

## ✨ Fonctionnalités

### 🤖 Ordonnancement des modèles (V0.1–V0.5)

| Fonctionnalité | Détail |
|----------------|--------|
| **5 Adaptateurs fournisseurs** | OpenAI, Anthropic, Google, DeepSeek, Ollama |
| **15 Modèles notés** | 7 capacités chacun (codage, architecture, révision, recherche, raisonnement, rapide, écriture) |
| **3 Profils de coût** | `free` (local d'abord), `balanced` (pas cher d'abord), `quality` (meilleur d'abord) |
| **Commutation de terminal** | `relay use opencode` — bascule instantanée entre terminaux CLI |
| **Auto-escalade** | Gratuit → pas cher → premium sur faible confiance |

### 🧠 Système de travailleurs (V0.3)

| Fonctionnalité | Détail |
|----------------|--------|
| **8 Travailleurs par défaut** | architect, researcher, coder, reviewer, debugger, writer, assistant, data-engineer |
| **Persistance des travailleurs** | Basée sur SQLite, survit aux redémarrages |
| **Boîte de réception** | Messagerie inter-travailleurs basée sur les tâches |
| **Vue Focus** | `relay focus <worker>` — SSH dans l'esprit d'un travailleur |

### 💬 Système de sessions (V0.6–V0.7)

| Fonctionnalité | Détail |
|----------------|--------|
| **3 Modes** | `chat` (simple), `ask` (exécution automatique), `group` (multi-travailleur) |
| **Routage par capacité** | Suit le type de tâche, pas le modèle utilisé |
| **Graphe de capacités** | Décompose les tâches en DAG multi-étapes |
| **Capacité persistante** | La session se souvient du codage/architecture, l'ordonnanceur choisit le modèle |

### 🔄 Exécution de graphe de tâches (V0.8)

| Fonctionnalité | Détail |
|----------------|--------|
| **Schémas d'étapes** | 6 types d'étapes avec contrats d'entrée/sortie |
| **Passage d'artefacts** | Références de champs structurées, pas de texte intégral |
| **Efficacité des tokens** | ~800 tokens/étape vs ~3000 sans schéma |
| **Reprise** | Ignorer les étapes terminées, continuer après une erreur |
| **Estimation des coûts** | Coût par étape et total avant exécution |

### 🗄️ Mémoire inter-sessions (V0.9)

| Fonctionnalité | Détail |
|----------------|--------|
| **Connaissances projet** | Les faits s'accumulent entre les sessions |
| **KnowledgeCompiler** | Extraction de code pur à partir d'artefacts |
| **Instructions de saut** | Informations connues injectées dans les prompts (pas de redécouverte) |
| **~43% d'économie** | Sur les sessions répétées |

### 🖥️ Interface utilisateur du terminal

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

## ⚡ Démarrage rapide

### Installation

```bash
pip install relayos
```

### Utilisation

```bash
relay             # Ouvrir la TUI (panneau de contrôle style htop)
relay use free    # Passer d'abord aux modèles gratuits
```

### Chat / Ask / Group

```bash
# Conversation IA unique (acheminement automatique)
relay session chat "Explain Kubernetes architecture"

# Exécution de tâche multi-étape
relay session ask "Build a JWT auth system in FastAPI"

# Discussion de groupe multi-travailleur
relay session group "Design a payment system"
```

### Changer de terminal instantanément

```bash
relay use opencode   # Toutes les tâches → OpenCode (gratuit)
relay use mimo       # Toutes les tâches → Mimo (gratuit)
relay use claude     # Toutes les tâches → Claude (premium)
```

### Connaissances projet

```bash
relay project create payment-system       # Créer un projet
relay project knowledge <project-id>      # Afficher les connaissances accumulées
relay session chat "Add refund" -p <pid>  # Session limitée au projet
```

### Planifier avant d'exécuter

```bash
relay session plan "Build a payment system"
# Affiche : research(gemini free) → architecture(claude) → review(deepseek)
```

---

## 🔧 Référence CLI

| Commande | Description |
|----------|-------------|
| `relay` | Ouvrir le panneau de contrôle TUI |
| `relay session chat` | Conversation IA unique |
| `relay session ask` | Décomposer et exécuter automatiquement une tâche |
| `relay session group` | Discussion de groupe multi-travailleur |
| `relay session plan` | Afficher le graphe de capacités sans exécuter |
| `relay session list` | Lister les sessions récentes |
| `relay use` | Changer le terminal/profil par défaut |
| `relay profile` | Définir le profil de routage |
| `relay focus` | Vue focus d'un travailleur |
| `relay team create` | Créer une équipe à partir d'un modèle |
| `relay project create` | Créer un projet pour la base de connaissances |
| `relay project knowledge` | Afficher les connaissances du projet |
| `relay plan` | Afficher le plan d'exécution d'une tâche |
| `relay estimate` | Afficher les estimations de coût |
| `relay run` | Exécuter un workflow YAML |
| `relay config` | Assistant de configuration |
| `relay plugin add` | Enregistrer un terminal CLI personnalisé |
| `relayos serve` | Tableau de bord Web optionnel |

### Raccourcis clavier (dans la TUI)

| Touche | Action |
|--------|--------|
| `f` | Profil gratuit |
| `b` | Profil équilibré |
| `o` | Terminal OpenCode |
| `m` | Terminal Mimo |
| `c` | Terminal Claude |
| `1-9` | Sélectionner un travailleur |
| `q` | Quitter |
| `r` | Actualiser |

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

### Modules principaux

| Module | Rôle |
|--------|------|
| `relayos/core/scheduler.py` | Ordonnanceur conscient des coûts (15 modèles) |
| `relayos/core/session.py` | Cycle de vie des sessions + messages |
| `relayos/core/conversation.py` | Moteurs chat/ask/group |
| `relayos/core/planner.py` | Graphes de capacités + exécution |
| `relayos/core/knowledge.py` | Mémoire projet inter-sessions |
| `relayos/core/state.py` | Stockage d'état structuré |
| `relayos/core/schemas.py` | Contrats d'entrée/sortie des étapes |
| `relayos/core/artifacts.py` | Stockage structuré d'artefacts |
| `relayos/tui/app.py` | TUI pilotée par le clavier |

### Stockage (tout en SQLite local, zéro infrastructure)

```
~/.relayos/
├── config.yaml        # Configuration utilisateur
├── state.db           # État du projet + décisions + événements
├── sessions.db        # Historique des sessions + messages
├── knowledge.db       # Connaissances projet inter-sessions
├── artifacts.db       # Sorties structurées des étapes
└── workers.db         # Définitions persistantes des travailleurs
```

---

## 🛣️ Feuille de route

### Terminé (V0.1–V0.9)

| Version | Fonctionnalité principale | Statut |
|---------|---------------------------|--------|
| V0.1 | Routage de modèles (5 adaptateurs, workflows YAML) | ✅ |
| V0.2 | Pool de terminaux (multi-CLI, suivi des coûts) | ✅ |
| V0.3 | Système de travailleurs (8 rôles, persistance, TUI) | ✅ |
| V0.4 | Compilateur d'état (état structuré, event sourcing) | ✅ |
| V0.5 | Ordonnanceur de modèles (15 modèles, 3 profils de coût) | ✅ |
| V0.6 | Système de sessions (modes chat/ask/group) | ✅ |
| V0.7 | Graphe de capacités (décomposition multi-étapes) | ✅ |
| V0.8 | Exécution de graphe de tâches (passage d'artefacts avec schémas) | ✅ |
| V0.9 | Mémoire inter-sessions (base de connaissances projet) | ✅ |

### Planifié

- **V1.0** — Écosystème de plugins, routeur MCP, travailleurs distribués
- **V1.1** — Relecture de workflows (timeline style LangSmith)
- **V1.2** — Pool de travailleurs multi-machines

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
