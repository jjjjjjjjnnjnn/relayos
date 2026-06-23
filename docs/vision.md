# RelayOS — Persistent AI Workers for Developers

## Problem

Every AI tool today is an island. You use Claude Code for architecture, ChatGPT for reasoning, Gemini for research, DeepSeek for coding. Each is excellent. They don't talk to each other. You copy-paste context between them.

Existing solutions either force you into a browser chat UI or require Kubernetes infrastructure. There's nothing for the terminal-native developer who wants persistent AI teammates.

## Solution

RelayOS is a terminal-native AI workforce manager. Think of it as tmux for your AI agents:

- Spawn persistent workers (architect, researcher, coder)
- Workers keep project context across sessions
- Workers collaborate through a shared inbox
- All from your terminal -- zero infrastructure required

## Principles

1. **Terminal-native.** Primary interface is `relay`. Web UI is optional.
2. **Workers, not API calls.** A worker is a persistent team member with identity, memory, and inbox.
3. **Persistent by default.** Workers survive across sessions. Tomorrow they remember today.
4. **Zero infrastructure.** `pip install relayos && relay`. No Docker, no Postgres, no Redis.
5. **Cost-aware.** Free tiers first, smart routing, context compression between steps.

## Target

```
Primary:   Solo developer with 3+ AI subscriptions
           Terminal-native, hates context switching
           Wants persistent AI teammates, not chat windows

Secondary: Small team sharing a pool of AI workers
           Wants shared memory and inter-worker messaging
```

## Core Metaphor

> RelayOS is to AI agents what tmux is to terminal sessions:
> a persistent workspace manager that keeps your team alive.
>
> Or what htop is to processes:
> a live dashboard of your AI workforce.
