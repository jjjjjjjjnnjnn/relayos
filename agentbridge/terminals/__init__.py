"""Terminal registry — discover and create terminal instances."""
from __future__ import annotations

from agentbridge.terminals.base import BaseTerminal
from agentbridge.terminals.adapters import (
    ClaudeCodeTerminal,
    CodexTerminal,
    CustomTerminal,
    MimoCodeTerminal,
    OpenCodeTerminal,
    QCodeTerminal,
)

REGISTRY: dict[str, type[BaseTerminal]] = {
    "claude": ClaudeCodeTerminal,
    "mimo": MimoCodeTerminal,
    "opencode": OpenCodeTerminal,
    "codex": CodexTerminal,
    "qcode": QCodeTerminal,
    "custom": CustomTerminal,
}


def get_terminal_class(type_name: str) -> type[BaseTerminal]:
    cls = REGISTRY.get(type_name)
    if not cls:
        available = ", ".join(sorted(REGISTRY))
        raise ValueError(f"Unknown terminal type '{type_name}'. Available: {available}")
    return cls


def register_terminal(type_name: str, cls: type[BaseTerminal]):
    REGISTRY[type_name] = cls


def list_terminal_types() -> list[dict]:
    """List all available terminal types with their status."""
    results = []
    for name, cls in REGISTRY.items():
        inst = cls()
        results.append({
            "type": name,
            "binary": getattr(inst, "binary", ""),
            "default_model": getattr(inst, "default_model", ""),
            "available": inst.check_available(),
        })
    return results
