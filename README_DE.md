<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Du nutzt Claude, GPT, Gemini, DeepSeek und lokale Modelle.<br>
  RelayOS bringt sie zusammen — automatisch.</strong><br>
  <br>
  Eine terminal-native AI-Laufzeitumgebung, die Aufgaben an das richtige Modell weiterleitet,<br>
  sich Projektkontext über Sitzungen hinweg merkt und dir Geld spart.
</p>

<p align="center">
  <a href="#-schnellstart"><img src="https://img.shields.io/badge/Schnellstart-10B981?style=for-the-badge&logo=python" alt="Schnellstart"></a>
  <a href="#%EF%B8%8F-funktionen"><img src="https://img.shields.io/badge/Funktionen-3B82F6?style=for-the-badge" alt="Funktionen"></a>
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

## 👋 Das Problem

Du offnest 5 Browser-Tabs. ChatGPT fur Reasoning, Claude fur Architektur, Gemini fur Recherche, DeepSeek fur Code. Du kopierst Ausgaben von einem und fugst sie in den nachsten ein. Du verschwendest Premium-Tokens fur Aufgaben, die ein kostenloses Modell erledigen konnte.

**Du verschwendest 30% deiner Zeit mit der Verwaltung von Werkzeugen, anstatt zu bauen.**

## 🎯 Die Losung

RelayOS ist die Koordinationsebene, die deine AI-Werkzeuge wie ein richtiges Team zusammenarbeiten lasst:

```
┌─ Du ──────────────────────────────────────────┐
│                                                 │
│   relay session ask "Build a payment sys"       │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              RelayOS                             │
│                                                  │
│  1. Wettbewerb recherchieren → Gemini (KOSTENLOS)│
│  2. Architektur entwerfen    → Claude            │
│  3. Code implementieren      → GPT               │
│  4. Sicherheitsprufung       → DeepSeek (GUNSTIG)│
│  5. API dokumentieren        → Gemini (KOSTENLOS)│
│                                                  │
│  Gesamtkosten: $0.01   Zeit: 45s                  │
└──────────────────────────────────────────────────┘
```

**Null Infrastruktur.** `pip install relayos && relay`. Kein Docker, kein Server, kein Browser.

---

## ✨ Was RelayOS auszeichnet

| Funktion | Was sie tut | Nutzen |
|---------|-------------|---------|
| 🧠 **Smartes Routing** | Wahlt automatisch das beste Modell pro Aufgabe | Kostenlose Modelle zuerst, Premium nur bei Bedarf |
| 🔄 **Mehrschritt-Plane** | Zerlegt Aufgaben in Ausfuhrungsgraphen | Ein Befehl, viele AI-Modelle arbeiten zusammen |
| 💾 **Projektspeicher** | Wissen bleibt uber Sitzungen erhalten | Arbeiter vergessen nicht, was sie gelernt haben |
| 💰 **Kostenkontrolle** | Pro-Modell-Verfolgung + Budgetgrenzen | Keine Uberraschungsrechnungen |
| 🔌 **21 Terminal-Typen** | Claude, GPT, Gemini, DeepSeek, lokal und 16+ weitere | Nutze deine eigenen Werkzeuge |
| ⌨️ **Terminal-nativ** | htop-artiges TUI, kein Browser notig | Bleibt in deinem Workflow |

---

## ⚡ Schnellstart

### Installation

```bash
pip install relayos
```

Probier es aus — wirklich nur ein Befehl:

```bash
relay
```

Offnet das Bedienfeld. Wie `htop`, aber fur dein AI-Team.

### Mit jedem Modell chatten

```bash
# Automatische Routenwahl zum besten Modell
relay session chat "Explain Kubernetes architecture"

# Oder einen bestimmten Arbeiter ansprechen
relay session chat "Design this API" -w architect
```

### Mehrschritt-Aufgabe ausfuhren

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS zerlegt, routet und fuhrt automatisch uber die besten Modelle fur jeden Schritt aus.

### Planen, bevor du ausgibst

```bash
relay session plan "Build a payment system"
# Zeigt Kostenschatzungen vor der Ausfuhrung
```

### Gruppendiskussion (mehrere AI-Arbeiter)

```bash
relay session group "Review this architecture"
# Jeder Arbeiter tragt bei: Researcher → Architect → Reviewer
```

### Modelle sofort wechseln

```bash
relay use opencode     # Alle Aufgaben → OpenCode (kostenlos)
relay use mimo         # Alle Aufgaben → Mimo (kostenlos)
relay use claude       # Alle Aufgaben → Claude (Premium)
relay use free         # Kostenlos-zuerst-Routing
```

### Projektwissen

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # Kennt fruhere Entscheidungen!
relay project knowledge proj-id                     # Zeigt gesammeltes Wissen
```

---

## 🖥️ Das TUI

```
 Arbeiter (1-9 Auswahl)    │ Status
                           │  Profil: balanced
 1 🧠 architect    ○ idle  │  Kosten: $0.00
 2 🔍 researcher   ○ idle  │  Ausstehend: 0
 3 ⭐ coder        ○ idle  │
 4 🎯 reviewer     ○ idle  │ Aktionen
 5 🐛 debugger     ○ idle  │  f=free  b=balanced
                           │  o=opencode  c=claude
═══════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

Tastaturgesteuert, keine Maus notig. Ein Tastendruck zum Wechseln von Profilen oder Arbeitern.

---

## 🗺️ Fahigkeitsgraph

Wenn du `relay session plan "Build a payment system"` eingibst, erzeugt RelayOS:

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     Anforderungen recherchieren
       gemini-2.5-flash                FREE

  [2] architecture Systemarchitektur entwerfen
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       Architekturentscheidungen prufen
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
Jeder Schritt ubergibt nur relevante Daten (nicht den vollstandigen Text).
~800 Tokens/Schritt, ~7x weniger als naive Ansatze.
```

---

## 🔧 Unterstutzte Terminals (21 Typen)

Erkennt automatisch, was du installiert hast:

| Status | Terminal | Standardmodell |
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
| ⚡ | Custom | (konfigurierbar) |

**Jede CLI als Terminal hinzufugen:**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 Alle Befehle

| Befehl | Funktion |
|---------|-------------|
| `relay` | Bedienfeld offnen |
| `relay session chat` | Einzelne AI-Unterhaltung |
| `relay session ask` | Automatisch zerlegen + ausfuhren |
| `relay session group` | Multi-Arbeiter-Diskussion |
| `relay session plan` | Fahigkeitsgraph anzeigen |
| `relay session list` | Letzte Sitzungen |
| `relay use <terminal>` | Standardterminal wechseln |
| `relay use <profile>` | Kostenprofil wechseln |
| `relay focus <worker>` | SSH in einen Arbeiter |
| `relay team create` | Team aus Vorlage erstellen |
| `relay project create` | Wissensprojekt erstellen |
| `relay project knowledge` | Projektspeicher anzeigen |
| `relay plan "task"` | Ausfuhrungsplan anzeigen |
| `relay estimate "task"` | Kostenschatzung anzeigen |
| `relay run workflow.yaml` | YAML-Workflow ausfuhren |
| `relay config detect` | Installierte Terminals scannen |
| `relayos plugin add` | Benutzerdefinierte CLI registrieren |
| `relayos serve` | Web-Dashboard (optional) |

---

## 🏗️ Architektur

```
Terminal (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                     │
│  (Sitzungs-Routing + Fahigkeitserkennung)  │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                    │
│  (schema-bewusst, Artifakt-Ubergabe, DAG)   │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                       │
│  (15 Modelle × 7 Fahigkeiten, kostenbewusst)│
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  Adapter    │     │  Wissensbasis       │
│  (21 Terms) │     │  (SQLite, Projekt)  │
└─────────────┘     └────────────────────┘
```

### Speicher (alles lokal, null Infrastruktur)

```
~/.relayos/           ← Einzelnes Verzeichnis, portabel
├── config.yaml       ← Deine Modell-/Profilkonfiguration
├── state.db          ← Projektstatus + Entscheidungen
├── sessions.db       ← Sitzungsverlauf + Nachrichten
├── knowledge.db      ← Sitzungsubergreifender Speicher
├── artifacts.db      ← Strukturierte Schrittausgaben
└── workers.db        ← Permanente Arbeiter
```

### Design-Philosophie

| Prinzip | Warum |
|-----------|-----|
| **Terminal-zuerst** | Entwickler leben im Terminal. Kein Browser notig. |
| **Zustand, nicht Chat** | Speichere Entscheidungen, nicht Gesprache. ~200x kompakter. |
| **Fahigkeits-Routing** | Binde an Aufgabentyp, nicht an Modell. Modelle andern sich; Aufgaben nicht. |
| **Null Infrastruktur** | Einzelner Prozess, lokales SQLite. Kein Docker, Postgres, Redis. |
| **Kostenbewusstsein** | Kostenlose Stufen zuerst. Spare Geld, ohne daruber nachzudenken. |

---

## 📈 Versionsverlauf

| Version | Inhalt |
|---------|------|
| **V0.1** | Modell-Routing — 5 Provider-Adapter, YAML-Workflows |
| **V0.2** | Terminal-Pool — Multi-CLI, Kostenverfolgung |
| **V0.3** | Arbeiter-System — 8 Rollen, Persistenz, TUI |
| **V0.4** | Zustands-Compiler — Strukturierter Zustand, Event Sourcing |
| **V0.5** | Modell-Scheduler — 15 Modelle, 3 Kostenprofile |
| **V0.6** | Sitzungssystem — Chat/Ask/Group-Modi |
| **V0.7** | Fahigkeitsgraph — Mehrschritt-Aufgabenzerlegung |
| **V0.8** | Aufgaben-Graph-Ausfuhrung — Schema-bewusste Artifakt-Ubergabe |
| **V0.9** | Sitzungsubergreifender Speicher — Projekt-Wissensbasis |

---

## 💪 Erstellt mit

| Komponente | Technik |
|-----------|------|
| **Sprache** | Python 3.10+ |
| **CLI-Framework** | Click 8.0+ |
| **HTTP-Client** | HTTPX 0.27+ |
| **Terminal-UI** | Rich |
| **Speicher** | SQLite (keine externe DB) |
| **Modelle** | 15 bewertete Modelle, 21 Terminal-Typen |
| **Lizenz** | Apache 2.0 |

### Abhangigkeiten

| Bibliothek | Lizenz | Zweck |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | CLI-Framework |
| [PyYAML](https://pyyaml.org/) | MIT | YAML-Parsing |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | HTTP-Client fur Modell-APIs |
| [Rich](https://rich.readthedocs.io/) | MIT | Terminal-UI-Rendering |

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

### Optional: Web-Dashboard

```bash
pip install relayos[server]
relayos serve --open
```

### Aus dem Quellcode

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker (nur Web-Dashboard)

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 Sprachen

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
  <strong>Hore auf, zwischen AI-Werkzeugen zu kopieren und einzufugen.<br>
  Lass sie zusammenarbeiten.</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-schnellstart"><img src="https://img.shields.io/badge/Los_gehts-10B981?style=for-the-badge" alt="Los gehts"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
