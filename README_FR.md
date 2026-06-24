<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Tu utilises Claude, GPT, Gemini, DeepSeek et des modeles locaux.<br>
  RelayOS les fait travailler ensemble — automatiquement.</strong><br>
  <br>
  Un environnement d'execution IA natif pour le terminal qui achemine les tâches vers le bon modele,<br>
  se souvient du contexte du projet entre les sessions et te fait economiser de l'argent.
</p>

<p align="center">
  <a href="#-demarrage-rapide"><img src="https://img.shields.io/badge/Demarrage_rapide-10B981?style=for-the-badge&logo=python" alt="Demarrage rapide"></a>
  <a href="#%EF%B8%8F-fonctionnalites"><img src="https://img.shields.io/badge/Fonctionnalites-3B82F6?style=for-the-badge" alt="Fonctionnalites"></a>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-installation"><img src="https://img.shields.io/badge/pip_install_relayos-FF6F00?style=for-the-badge&logo=pypi" alt="Installation"></a>
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

## 👋 Le probleme

Tu ouvres 5 onglets de navigateur. ChatGPT pour le raisonnement, Claude pour l'architecture, Gemini pour la recherche, DeepSeek pour le code. Tu copies les resultats de l'un, tu les colles dans le suivant. Tu brules des tokens premium sur des tâches qu'un modele gratuit pourrait traiter.

**Tu perds 30% de ton temps a gerer des outils au lieu de construire.**

## 🎯 La solution

RelayOS est la couche de coordination qui fait travailler tes outils IA comme une veritable equipe :

```
┌─ Toi ─────────────────────────────────────────┐
│                                                 │
│   relay session ask "Build a payment sys"       │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              RelayOS                             │
│                                                  │
│  1. Rechercher concurrents  → Gemini (GRATUIT)   │
│  2. Concevoir architecture → Claude              │
│  3. Implementer le code    → GPT                 │
│  4. Revue securite         → DeepSeek (BON MARCHE)│
│  5. Documenter l'API       → Gemini (GRATUIT)    │
│                                                  │
│  Cout total : $0.01    Temps : 45s               │
└──────────────────────────────────────────────────┘
```

**Zero infrastructure.** `pip install relayos && relay`. Pas de Docker, pas de serveur, pas de navigateur.

---

## ✨ Ce qui rend RelayOS different

| Fonctionnalite | Ce qu'elle fait | Avantage |
|---------|-------------|---------|
| 🧠 **Routage intelligent** | Selectionne automatiquement le meilleur modele pour chaque tâche | Modeles gratuits d'abord, premium seulement si necessaire |
| 🔄 **Plans multi-etapes** | Decompose les tâches en graphes d'execution | Une commande, plusieurs modeles IA collaborant |
| 💾 **Memoire de projet** | Les connaissances persistent entre les sessions | Les travailleurs n'oublient jamais ce qu'ils ont appris |
| 💰 **Controle des couts** | Suivi par modele + limites budgetaires | Pas de factures surprises |
| 🔌 **21 Types de terminaux** | Claude, GPT, Gemini, DeepSeek, local et 16+ autres | Utilise tes propres outils |
| ⌨️ **Natif du terminal** | TUI style htop, pas de navigateur necessaire | Reste dans ton flux de travail |

---

## ⚡ Demarrage rapide

### Installation

```bash
pip install relayos
```

Essaie-le — vraiment une seule commande :

```bash
relay
```

Ouvre le panneau de controle. Comme `htop`, mais pour ton equipe IA.

### Discuter avec n'importe quel modele

```bash
# Routage automatique vers le meilleur modele
relay session chat "Explain Kubernetes architecture"

# Ou cibler un travailleur specifique
relay session chat "Design this API" -w architect
```

### Executer une tâche multi-etapes

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS decomposera, routera et executera automatiquement sur les meilleurs modeles pour chaque etape.

### Planifier avant de depenser

```bash
relay session plan "Build a payment system"
# Affiche les estimations de cout avant execution
```

### Discussion de groupe (plusieurs travailleurs IA)

```bash
relay session group "Review this architecture"
# Chaque travailleur contribue : chercheur → architecte → relecteur
```

### Changer de modele instantanement

```bash
relay use opencode     # Toutes les tâches → OpenCode (gratuit)
relay use mimo         # Toutes les tâches → Mimo (gratuit)
relay use claude       # Toutes les tâches → Claude (premium)
relay use free         # Routage gratuit d'abord
```

### Connaissances projet

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # Connait les decisions precedentes !
relay project knowledge proj-id                     # Voir les connaissances accumulees
```

---

## 🖥️ La TUI

```
 Travailleurs (1-9 selection) │ Statut
                              │  Profil : balanced
 1 🧠 architect    ○ idle    │  Cout : $0.00
 2 🔍 researcher   ○ idle    │  En attente : 0
 3 ⭐ coder        ○ idle    │
 4 🎯 reviewer     ○ idle    │ Actions
 5 🐛 debugger     ○ idle    │  f=free  b=balanced
                              │  o=opencode  c=claude
══════════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

Pilotee au clavier, pas de souris necessaire. Une touche pour changer de profil ou de travailleur.

---

## 🗺️ Graphe de capacites

Quand tu tapes `relay session plan "Build a payment system"`, RelayOS genere :

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     Rechercher les besoins
       gemini-2.5-flash                FREE

  [2] architecture Concevoir l'architecture systeme
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       Reviser les decisions d'architecture
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
Chaque etape ne transmet que les donnees pertinentes (pas le texte integral).
~800 tokens/etape, ~7x moins que les approches naives.
```

---

## 🔧 Terminaux supportes (21 types)

Detecte automatiquement ce que tu as installe :

| Statut | Terminal | Modele par defaut |
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

**Ajouter n'importe quelle CLI comme terminal :**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 Toutes les commandes

| Commande | Fonction |
|---------|-------------|
| `relay` | Ouvrir le panneau de controle |
| `relay session chat` | Conversation IA unique |
| `relay session ask` | Decomposer + executer automatiquement |
| `relay session group` | Discussion multi-travailleur |
| `relay session plan` | Afficher le graphe de capacites |
| `relay session list` | Sessions recentes |
| `relay use <terminal>` | Changer le terminal par defaut |
| `relay use <profile>` | Changer le profil de cout |
| `relay focus <worker>` | SSH dans un travailleur |
| `relay team create` | Creer une equipe depuis un modele |
| `relay project create` | Creer un projet de connaissances |
| `relay project knowledge` | Afficher la memoire du projet |
| `relay plan "task"` | Afficher le plan d'execution |
| `relay estimate "task"` | Afficher les estimations de cout |
| `relay run workflow.yaml` | Executer un workflow YAML |
| `relay config detect` | Scanner les terminaux installes |
| `relayos plugin add` | Enregistrer une CLI personnalisee |
| `relayos serve` | Tableau de bord Web (optionnel) |

---

## 🏗️ Architecture

```
Terminal (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                     │
│  (routage de session + detection capacite) │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                    │
│  (conscient des schemas, passage artefacts) │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                       │
│  (15 modeles × 7 capacites, cout-aware)     │
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  Adapteurs  │     │  Base de           │
│  (21 terms) │     │  connaissances     │
│             │     │  (SQLite, projet)  │
└─────────────┘     └────────────────────┘
```

### Stockage (tout en local, zero infrastructure)

```
~/.relayos/           ← Repertoire unique, portable
├── config.yaml       ← Configuration de tes modeles/profils
├── state.db          ← Etat du projet + decisions
├── sessions.db       ← Historique des sessions + messages
├── knowledge.db      ← Memoire inter-sessions
├── artifacts.db      ← Sorties structurees des etapes
└── workers.db        ← Travailleurs persistants
```

### Philosophie de conception

| Principe | Pourquoi |
|-----------|-----|
| **Terminal d'abord** | Les developpeurs vivent dans le terminal. Pas de navigateur necessaire. |
| **Etat, pas chat** | Sauvegarde les decisions, pas les conversations. ~200x plus compact. |
| **Routage par capacite** | Lie au type de tâche, pas au modele. Les modeles changent ; les tâches non. |
| **Zero infrastructure** | Processus unique, SQLite local. Pas de Docker, Postgres, Redis. |
| **Conscience des couts** | Niveaux gratuits d'abord. Economise de l'argent sans y penser. |

---

## 📈 Historique des versions

| Version | Contenu |
|---------|------|
| **V0.1** | Routage de modeles — 5 adaptateurs fournisseurs, workflows YAML |
| **V0.2** | Pool de terminaux — Multi-CLI, suivi des couts |
| **V0.3** | Systeme de travailleurs — 8 roles, persistance, TUI |
| **V0.4** | Compilateur d'etat — Etat structure, event sourcing |
| **V0.5** | Ordonnanceur de modeles — 15 modeles, 3 profils de cout |
| **V0.6** | Systeme de sessions — Modes chat/ask/group |
| **V0.7** | Graphe de capacites — Decomposition de tâches multi-etapes |
| **V0.8** | Execution de graphe de tâches — Passage d'artefacts avec schemas |
| **V0.9** | Memoire inter-sessions — Base de connaissances projet |

---

## 💪 Construit avec

| Composant | Technologie |
|-----------|------|
| **Langage** | Python 3.10+ |
| **Framework CLI** | Click 8.0+ |
| **Client HTTP** | HTTPX 0.27+ |
| **UI Terminal** | Rich |
| **Stockage** | SQLite (pas de base externe) |
| **Modeles** | 15 modeles scores, 21 types de terminaux |
| **Licence** | Apache 2.0 |

### Dependances

| Bibliotheque | Licence | Objectif |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | Framework CLI |
| [PyYAML](https://pyyaml.org/) | MIT | Parsing YAML |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | Client HTTP pour les API de modeles |
| [Rich](https://rich.readthedocs.io/) | MIT | Rendu UI terminal |

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

### Optionnel : tableau de bord Web

```bash
pip install relayos[server]
relayos serve --open
```

### Depuis les sources

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker (tableau de bord Web uniquement)

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 Langues

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
  <strong>Arrete de copier-coller entre outils IA.<br>
  Fais-les travailler ensemble.</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-demarrage-rapide"><img src="https://img.shields.io/badge/Commencer-10B981?style=for-the-badge" alt="Commencer"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
