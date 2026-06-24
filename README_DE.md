<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Dauerhafte KI-Arbeiter für Entwickler.</strong><br>
  Eine terminalnative KI-Ausführungslaufzeit — leite Aufgaben an Claude, GPT, Gemini, DeepSeek und lokale Modelle weiter,<br>
  mit fähigkeitsbewusster Planung, gemeinsamem Projektgedächtnis und mehrstufigen Ausführungsgraphen.
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

## 📋 Inhaltsverzeichnis

| Abschnitt | Beschreibung |
|-----------|--------------|
| [🎯 Überblick](#-overview) | Was RelayOS ist und warum es existiert |
| [✨ Funktionen](#-features) | Alle Fähigkeiten (V0.1–V0.9) |
| [⚡ Schnellstart](#-quick-start) | Installation und Start |
| [🔧 CLI-Referenz](#-cli-reference) | Alle 22 Befehle |
| [🏗️ Architektur](#%EF%B8%8F-architecture) | Systemdesign |
| [🛣️ Fahrplan](#%EF%B8%8F-roadmap) | Versionshistorie und Zukunft |
| [🙏 Danksagungen](#%EF%B8%8F-credits) | Anerkennungen |
| [📄 Lizenz](#-license) | Apache 2.0 |

---

## 🎯 Überblick

**RelayOS** ist eine terminalnative KI-Ausführungslaufzeit. Wie htop für dein KI-Team.

Du hast mehrere KI-Werkzeuge (Claude Code, ChatGPT, Gemini, DeepSeek, lokale Modelle). Jedes ist exzellent. Sie reden nicht miteinander. RelayOS ist die Koordinationsschicht, die Aufgaben an das richtige Modell weiterleitet, sich projektübergreifend Kontext merkt und mehrstufige Pläne ausführt — alles von deinem Terminal aus, null Infrastruktur.

### Die Entwicklung

```
V0.1  Modell-Routing      →  das richtige Modell wählen
V0.2  Terminal-Pool       →  CLI-Arbeiter verwalten
V0.3  Arbeitersystem      →  dauerhafte KI-Teammitglieder
V0.4  Zustandscompiler    →  strukturierter Zustand, nicht Chat-Verlauf
V0.5  Modell-Scheduler    →  kostenbewusst (zuerst kostenlos, dann eskalieren)
V0.6  Sitzungssystem      →  Chat-/Ask-/Group-Modi
V0.7  Fähigkeitsgraph     →  mehrstufige Aufgabenzerlegung
V0.8  Graph-Ausführung    →  schema-bewusste Artefaktübergabe
V0.9  Sitzungsübergreifendes Gedächtnis →  Projektwissensdatenbank
```

---

## ✨ Funktionen

### 🤖 Modell-Scheduling (V0.1–V0.5)

| Funktion | Detail |
|----------|--------|
| **5 Anbieter-Adapter** | OpenAI, Anthropic, Google, DeepSeek, Ollama |
| **15 Modelle bewertet** | Jeweils 7 Fähigkeiten (Programmieren, Architektur, Review, Recherche, Reasoning, Schnell, Schreiben) |
| **3 Kostenprofile** | `free` (lokal zuerst), `balanced` (günstig zuerst), `quality` (beste zuerst) |
| **Terminal-Wechsel** | `relay use opencode` — sofortiger Wechsel zwischen CLI-Terminals |
| **Auto-Eskalation** | Kostenlos → günstig → Premium bei niedriger Konfidenz |

### 🧠 Arbeitersystem (V0.3)

| Funktion | Detail |
|----------|--------|
| **8 Standard-Arbeiter** | architect, researcher, coder, reviewer, debugger, writer, assistant, data-engineer |
| **Arbeiter-Persistenz** | SQLite-gestützt, überlebt Neustarts |
| **Arbeiter-Posteingang** | Aufgabenbasierte Nachrichten zwischen Arbeitern |
| **Fokus-Ansicht** | `relay focus <worker>` — SSH in den Geist eines Arbeiters |

### 💬 Sitzungssystem (V0.6–V0.7)

| Funktion | Detail |
|----------|--------|
| **3 Modi** | `chat` (einzeln), `ask` (automatisch ausführen), `group` (mehrere Arbeiter) |
| **Fähigkeits-Routing** | Verfolgt, welche Aufgabe du machst, nicht welches Modell du verwendest |
| **Fähigkeitsgraph** | Zerlegt Aufgaben in mehrstufige DAGs |
| **Haftende Fähigkeit** | Sitzung merkt sich Programmieren/Architektur, Scheduler wählt das Modell |

### 🔄 Aufgaben-Graph-Ausführung (V0.8)

| Funktion | Detail |
|----------|--------|
| **Schritt-Schemata** | 6 Schritt-Typen mit Eingabe-/Ausgabe-Verträgen |
| **Artefakt-Übergabe** | Strukturierte Feldreferenzen, nicht vollständiger Text |
| **Token-Effizienz** | ~800 Token/Schritt vs. ~3000 ohne Schema |
| **Fortsetzen** | Überspringe abgeschlossene Schritte, fahre nach Fehlern fort |
| **Kostenschätzung** | Kosten pro Schritt und gesamt vor der Ausführung |

### 🗄️ Sitzungsübergreifendes Gedächtnis (V0.9)

| Funktion | Detail |
|----------|--------|
| **Projektwissen** | Fakten sammeln sich über Sitzungen hinweg an |
| **KnowledgeCompiler** | Reine Code-Extraktion aus Artefakten |
| **Überspring-Anweisungen** | Bekanntes Wissen wird in Prompts injiziert (kein Wiederentdecken) |
| **~43% Ersparnis** | Bei wiederholten Sitzungen |

### 🖥️ Terminal-UI

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

## ⚡ Schnellstart

### Installation

```bash
pip install relayos
```

### Verwendung

```bash
relay             # TUI öffnen (htop-artiges Bedienfeld)
relay use free    # Zuerst kostenlose Modelle verwenden
```

### Chat / Ask / Group

```bash
# Einzel-KI-Gespräch (automatisch weitergeleitet)
relay session chat "Explain Kubernetes architecture"

# Mehrstufige Aufgabenausführung
relay session ask "Build a JWT auth system in FastAPI"

# Mehr-Arbeiter-Gruppendiskussion
relay session group "Design a payment system"
```

### Terminals sofort wechseln

```bash
relay use opencode   # Alle Aufgaben → OpenCode (kostenlos)
relay use mimo       # Alle Aufgaben → Mimo (kostenlos)
relay use claude     # Alle Aufgaben → Claude (Premium)
```

### Projektwissen

```bash
relay project create payment-system       # Projekt erstellen
relay project knowledge <project-id>      # Gesammeltes Wissen anzeigen
relay session chat "Add refund" -p <pid>  # Sitzung auf Projekt beschränken
```

### Vor der Ausführung planen

```bash
relay session plan "Build a payment system"
# Zeigt: research(gemini free) → architecture(claude) → review(deepseek)
```

---

## 🔧 CLI-Referenz

| Befehl | Beschreibung |
|--------|--------------|
| `relay` | TUI-Bedienfeld öffnen |
| `relay session chat` | Einzel-KI-Gespräch |
| `relay session ask` | Aufgabe automatisch zerlegen und ausführen |
| `relay session group` | Mehr-Arbeiter-Gruppendiskussion |
| `relay session plan` | Fähigkeitsgraph anzeigen ohne Ausführung |
| `relay session list` | Letzte Sitzungen auflisten |
| `relay use` | Standard-Terminal/Profil wechseln |
| `relay profile` | Routing-Profil festlegen |
| `relay focus` | Arbeiter-Fokusansicht |
| `relay team create` | Team aus Vorlage erstellen |
| `relay project create` | Projekt für Wissensdatenbank erstellen |
| `relay project knowledge` | Projektwissen anzeigen |
| `relay plan` | Ausführungsplan für eine Aufgabe anzeigen |
| `relay estimate` | Kostenschätzungen anzeigen |
| `relay run` | YAML-Workflow ausführen |
| `relay config` | Konfigurationsassistent |
| `relay plugin add` | Benutzerdefiniertes CLI-Terminal registrieren |
| `relayos serve` | Optionales Web-Dashboard |

### Tastenkombinationen (im TUI)

| Taste | Aktion |
|-------|--------|
| `f` | Kostenloses Profil |
| `b` | Ausgeglichenes Profil |
| `o` | OpenCode-Terminal |
| `m` | Mimo-Terminal |
| `c` | Claude-Terminal |
| `1-9` | Arbeiter auswählen |
| `q` | Beenden |
| `r` | Aktualisieren |

---

## 🏗️ Architektur

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

### Kernmodule

| Modul | Rolle |
|-------|-------|
| `relayos/core/scheduler.py` | 15-Modell-kostenbewusster Scheduler |
| `relayos/core/session.py` | Sitzungslebenszyklus + Nachrichten |
| `relayos/core/conversation.py` | Chat-/Ask-/Group-Engines |
| `relayos/core/planner.py` | Fähigkeitsgraphen + Ausführung |
| `relayos/core/knowledge.py` | Sitzungsübergreifendes Projektgedächtnis |
| `relayos/core/state.py` | Strukturierter Zustandsspeicher |
| `relayos/core/schemas.py` | Schritt-Eingabe-/Ausgabe-Verträge |
| `relayos/core/artifacts.py` | Strukturierte Artefaktspeicherung |
| `relayos/tui/app.py` | Tastaturgesteuerte TUI |

### Speicher (alles lokales SQLite, null Infrastruktur)

```
~/.relayos/
├── config.yaml        # Benutzerkonfiguration
├── state.db           # Projektzustand + Entscheidungen + Ereignisse
├── sessions.db        # Sitzungsverlauf + Nachrichten
├── knowledge.db       # Sitzungsübergreifendes Projektwissen
├── artifacts.db       # Strukturierte Schrittausgaben
└── workers.db         # Dauerhafte Arbeiterdefinitionen
```

---

## 🛣️ Fahrplan

### Abgeschlossen (V0.1–V0.9)

| Version | Kernfunktion | Status |
|---------|--------------|--------|
| V0.1 | Modell-Routing (5 Adapter, YAML-Workflows) | ✅ |
| V0.2 | Terminal-Pool (Multi-CLI, Kostenverfolgung) | ✅ |
| V0.3 | Arbeitersystem (8 Rollen, Persistenz, TUI) | ✅ |
| V0.4 | Zustandscompiler (strukturierter Zustand, Event Sourcing) | ✅ |
| V0.5 | Modell-Scheduler (15 Modelle, 3 Kostenprofile) | ✅ |
| V0.6 | Sitzungssystem (Chat-/Ask-/Group-Modi) | ✅ |
| V0.7 | Fähigkeitsgraph (mehrstufige Aufgabenzerlegung) | ✅ |
| V0.8 | Aufgaben-Graph-Ausführung (schema-bewusste Artefaktübergabe) | ✅ |
| V0.9 | Sitzungsübergreifendes Gedächtnis (Projektwissensdatenbank) | ✅ |

### Geplant

- **V1.0** — Plugin-Ökosystem, MCP-Router, verteilte Arbeiter
- **V1.1** — Workflow-Wiedergabe (LangSmith-artige Zeitleiste)
- **V1.2** — Multi-Maschinen-Arbeiterpool

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
- [Français (French)](README_FR.md)
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
