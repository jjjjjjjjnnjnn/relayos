<p align="center">
  <picture>
    <img src="https://img.shields.io/badge/RelayOS-v0.1.0a1-8B5CF6?style=for-the-badge" alt="RelayOS">
  </picture>
</p>

<h1 align="center">RelayOS</h1>

<p align="center">
  <strong>Usas Claude, GPT, Gemini, DeepSeek y modelos locales.<br>
  RelayOS los hace trabajar juntos — automaticamente.</strong><br>
  <br>
  Un runtime de IA nativo del terminal que enruta tareas al modelo correcto,<br>
  recuerda el contexto del proyecto entre sesiones y te ahorra dinero.
</p>

<p align="center">
  <a href="#-inicio-rapido"><img src="https://img.shields.io/badge/Inicio_rapido-10B981?style=for-the-badge&logo=python" alt="Inicio rapido"></a>
  <a href="#%EF%B8%8F-caracteristicas"><img src="https://img.shields.io/badge/Caracteristicas-3B82F6?style=for-the-badge" alt="Caracteristicas"></a>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-instalacion"><img src="https://img.shields.io/badge/pip_install_relayos-FF6F00?style=for-the-badge&logo=pypi" alt="Instalacion"></a>
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

## 👋 El problema

Abres 5 pestañas del navegador. ChatGPT para razonamiento, Claude para arquitectura, Gemini para investigacion, DeepSeek para codigo. Copias la salida de una, la pegas en la siguiente. Quemas tokens premium en tareas que un modelo gratuito podria manejar.

**Pierdes el 30% de tu tiempo gestionando herramientas en lugar de construir.**

## 🎯 La solucion

RelayOS es la capa de coordinacion que hace que tus herramientas de IA funcionen como un equipo real:

```
┌─ Tu ──────────────────────────────────────────┐
│                                                 │
│   relay session ask "Build a payment sys"       │
│                                                 │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              RelayOS                             │
│                                                  │
│  1. Investigar competencia → Gemini (GRATIS)    │
│  2. Disenar arquitectura  → Claude              │
│  3. Implementar codigo    → GPT                 │
│  4. Revision de seguridad → DeepSeek (BARATO)   │
│  5. Documentar la API     → Gemini (GRATIS)     │
│                                                  │
│  Costo total: $0.01    Tiempo: 45s               │
└──────────────────────────────────────────────────┘
```

**Infraestructura cero.** `pip install relayos && relay`. Sin Docker, sin servidor, sin navegador.

---

## ✨ Que hace diferente a RelayOS

| Caracteristica | Que hace | Beneficio |
|---------|-------------|---------|
| 🧠 **Enrutamiento inteligente** | Selecciona automaticamente el mejor modelo para cada tarea | Modelos gratuitos primero, premium solo cuando es necesario |
| 🔄 **Planes multipaso** | Descompone tareas en grafos de ejecucion | Un comando, muchos modelos de IA trabajando juntos |
| 💾 **Memoria de proyecto** | El conocimiento persiste entre sesiones | Los trabajadores nunca olvidan lo que aprendieron |
| 💰 **Control de costos** | Seguimiento por modelo + limites de presupuesto | Sin facturas sorpresa |
| 🔌 **21 Tipos de terminal** | Claude, GPT, Gemini, DeepSeek, local y 16+ mas | Usa tus propias herramientas |
| ⌨️ **Nativo del terminal** | TUI estilo htop, sin necesidad de navegador | Se mantiene en tu flujo de trabajo |

---

## ⚡ Inicio rapido

### Instalacion

```bash
pip install relayos
```

Pruébalo — literalmente un solo comando:

```bash
relay
```

Abre el panel de control. Como `htop`, pero para tu equipo de IA.

### Chatear con cualquier modelo

```bash
# Enrutamiento automatico al mejor modelo
relay session chat "Explain Kubernetes architecture"

# O apuntar a un trabajador especifico
relay session chat "Design this API" -w architect
```

### Ejecutar una tarea multipaso

```bash
relay session ask "Build a JWT auth system in FastAPI"
```

RelayOS descompondra, enrutara y ejecutara automaticamente en los mejores modelos para cada paso.

### Planificar antes de gastar

```bash
relay session plan "Build a payment system"
# Muestra estimaciones de costo antes de la ejecucion
```

### Discusion en grupo (multiples trabajadores de IA)

```bash
relay session group "Review this architecture"
# Cada trabajador contribuye: investigador → arquitecto → revisor
```

### Cambiar de modelo al instante

```bash
relay use opencode     # Todas las tareas → OpenCode (gratis)
relay use mimo         # Todas las tareas → Mimo (gratis)
relay use claude       # Todas las tareas → Claude (premium)
relay use free         # Enrutamiento gratuito primero
```

### Conocimiento del proyecto

```bash
relay project create my-app
relay session ask "Design the database" -p proj-id
relay session ask "Add caching later"   -p proj-id  # Sabe decisiones anteriores
relay project knowledge proj-id                     # Ver conocimiento acumulado
```

---

## 🖥️ La TUI

```
 Trabajadores (1-9 seleccion) │ Estado
                              │  Perfil: balanced
 1 🧠 architect    ○ idle    │  Costo: $0.00
 2 🔍 researcher   ○ idle    │  Pendiente: 0
 3 ⭐ coder        ○ idle    │
 4 🎯 reviewer     ○ idle    │ Acciones
 5 🐛 debugger     ○ idle    │  f=free  b=balanced
                              │  o=opencode  c=claude
══════════════════════════════╪══════════════════════════════
 9w 9i 0b | inbox:0 | $0.00 | [balanced] | q=quit
```

Impulsada por teclado, sin necesidad de raton. Una tecla para cambiar de perfil o trabajador.

---

## 🗺️ Grafo de capacidades

Cuando escribes `relay session plan "Build a payment system"`, RelayOS genera:

```
Capability Graph: Build a payment system
Profile: balanced  |  Estimated cost: $0.0084
──────────────────────────────────────────────────────
  [1] research     Investigar requisitos
       gemini-2.5-flash                FREE

  [2] architecture Disenar arquitectura del sistema
       claude-sonnet-4-20250514        $0.0083  → research

  [3] review       Revisar decisiones de arquitectura
       deepseek-chat                   $0.0002  → architecture

──────────────────────────────────────────────────────
Cada paso pasa solo datos relevantes (no el texto completo).
~800 tokens/paso, ~7x menos que enfoques ingenuos.
```

---

## 🔧 Terminales soportados (21 tipos)

Detecta automaticamente lo que tienes instalado:

| Estado | Terminal | Modelo por defecto |
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

**Anade cualquier CLI como terminal:**
```bash
relayos plugin add my-tool -m gpt-4o
```

---

## 🔧 Todos los comandos

| Comando | Funcion |
|---------|-------------|
| `relay` | Abrir panel de control |
| `relay session chat` | Conversacion unica con IA |
| `relay session ask` | Descomponer + ejecutar automaticamente |
| `relay session group` | Discusion multi-trabajador |
| `relay session plan` | Mostrar grafo de capacidades |
| `relay session list` | Sesiones recientes |
| `relay use <terminal>` | Cambiar terminal por defecto |
| `relay use <profile>` | Cambiar perfil de costo |
| `relay focus <worker>` | SSH dentro de un trabajador |
| `relay team create` | Crear equipo desde plantilla |
| `relay project create` | Crear proyecto de conocimiento |
| `relay project knowledge` | Mostrar memoria del proyecto |
| `relay plan "task"` | Mostrar plan de ejecucion |
| `relay estimate "task"` | Mostrar estimaciones de costo |
| `relay run workflow.yaml` | Ejecutar workflow YAML |
| `relay config detect` | Escanear terminales instalados |
| `relayos plugin add` | Registrar CLI personalizada |
| `relayos serve` | Panel web (opcional) |

---

## 🏗️ Arquitectura

```
Terminal (relay / relayos)
         │
         ▼
┌────────────────────────────────────────────┐
│      ConversationEngine                     │
│  (enrutamiento de sesion + deteccion capac.)│
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        TaskGraphExecutor                    │
│  (consciente de esquemas, paso de artefact.)│
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│        ModelScheduler                       │
│  (15 modelos × 7 capacidades, costo-consci.)│
└──────┬──────────────────────┬──────────────┘
       │                      │
┌──────▼──────┐     ┌─────────▼──────────┐
│  Adaptadores│     │  Base de           │
│  (21 terms) │     │  conocimientos     │
│             │     │  (SQLite, proy.)   │
└─────────────┘     └────────────────────┘
```

### Almacenamiento (todo local, infraestructura cero)

```
~/.relayos/           ← Directorio unico, portatil
├── config.yaml       ← Configuracion de modelos/perfiles
├── state.db          ← Estado del proyecto + decisiones
├── sessions.db       ← Historial de sesiones + mensajes
├── knowledge.db      ← Memoria entre sesiones
├── artifacts.db      ← Salidas estructuradas de pasos
└── workers.db        ← Trabajadores persistentes
```

### Filosofia de diseno

| Principio | Por que |
|-----------|-----|
| **Terminal primero** | Los desarrolladores viven en el terminal. Sin navegador necesario. |
| **Estado, no chat** | Guarda decisiones, no conversaciones. ~200x mas compacto. |
| **Enrutamiento por capacidad** | Vincula al tipo de tarea, no al modelo. Los modelos cambian; las tareas no. |
| **Infraestructura cero** | Proceso unico, SQLite local. Sin Docker, Postgres, Redis. |
| **Conciencia de costo** | Niveles gratuitos primero. Ahorra dinero sin pensar en ello. |

---

## 📈 Historial de versiones

| Version | Contenido |
|---------|------|
| **V0.1** | Enrutamiento de modelos — 5 adaptadores de proveedor, workflows YAML |
| **V0.2** | Pool de terminales — Multi-CLI, seguimiento de costos |
| **V0.3** | Sistema de trabajadores — 8 roles, persistencia, TUI |
| **V0.4** | Compilador de estado — Estado estructurado, event sourcing |
| **V0.5** | Planificador de modelos — 15 modelos, 3 perfiles de costo |
| **V0.6** | Sistema de sesiones — Modos chat/ask/group |
| **V0.7** | Grafo de capacidades — Descomposicion de tareas multipaso |
| **V0.8** | Ejecucion de grafo de tareas — Paso de artefactos con esquemas |
| **V0.9** | Memoria entre sesiones — Base de conocimiento del proyecto |

---

## 💪 Construido con

| Componente | Tecnologia |
|-----------|------|
| **Lenguaje** | Python 3.10+ |
| **Framework CLI** | Click 8.0+ |
| **Cliente HTTP** | HTTPX 0.27+ |
| **UI de Terminal** | Rich |
| **Almacenamiento** | SQLite (sin BD externa) |
| **Modelos** | 15 modelos puntuados, 21 tipos de terminal |
| **Licencia** | Apache 2.0 |

### Dependencias

| Libreria | Licencia | Proposito |
|---------|---------|---------|
| [Click](https://palletsprojects.com/p/click/) | BSD-3-Clause | Framework CLI |
| [PyYAML](https://pyyaml.org/) | MIT | Analisis YAML |
| [HTTPX](https://www.python-httpx.org/) | BSD-3-Clause | Cliente HTTP para APIs de modelos |
| [Rich](https://rich.readthedocs.io/) | MIT | Renderizado de UI en terminal |

### Credits

- **Claude Code** (Anthropic) — Primary development platform
- **OpenCode** — Terminal adapter & testing partner
- **MimoCode** — Terminal adapter for frontend workflows
- **OpenAI Codex** — Terminal adapter for coding tasks
- **ECC plugin system** — Agent orchestration patterns
- **MCP (Model Context Protocol)** — Tool integration protocol

---

## 📦 Instalacion

### pip

```bash
pip install relayos
```

### Opcional: panel web

```bash
pip install relayos[server]
relayos serve --open
```

### Desde codigo fuente

```bash
git clone https://github.com/jjjjjjjjnnjnn/relayos.git
cd relayos
pip install -e .
```

### Docker (solo panel web)

```bash
docker build -t relayos .
docker run -p 8080:8080 -v $(pwd)/config:/root/.relayos relayos
```

---

## 🌐 Idiomas

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
  <strong>Deja de copiar y pegar entre herramientas de IA.<br>
  Haz que trabajen juntas.</strong><br>
  <br>
  <a href="https://github.com/jjjjjjjjnnjnn/relayos"><img src="https://img.shields.io/badge/GitHub-★-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="#-inicio-rapido"><img src="https://img.shields.io/badge/Empezar-10B981?style=for-the-badge" alt="Empezar"></a>
  <br>
  <sub><code>pip install relayos && relay</code></sub>
</p>
