"""Terminal Scheduler — routes tasks to the best available CLI terminal.

Unlike model-level routers, this operates at the TERMINAL level:
- "opencode has free models, good for coding"
- "mimo has free models, good for quick tasks"
- "claude is best for architecture"

Users switch terminals with one command.
"""
from __future__ import annotations

import shutil
from typing import Optional

# Terminal capability scores (1-10) for each task type
# These are about what each CLI TERMINAL is good at, not the model
TERMINAL_CAPABILITIES: dict[str, dict[str, int]] = {
    "claude": {
        "coding": 8, "architecture": 10, "review": 8, "research": 7,
        "reasoning": 10, "quick": 4, "writing": 8, "debug": 8,
        "cost": 10,  # expensive on a 1-10 scale where 10=most expensive
    },
    "opencode": {
        "coding": 8, "architecture": 5, "review": 7, "research": 5,
        "reasoning": 5, "quick": 9, "writing": 5, "debug": 7,
        "cost": 0,  # free (has free models)
    },
    "mimo": {
        "coding": 6, "architecture": 4, "review": 5, "research": 4,
        "reasoning": 4, "quick": 10, "writing": 6, "debug": 5,
        "cost": 0,  # free (has free models)
    },
    "codex": {
        "coding": 9, "architecture": 6, "review": 6, "research": 5,
        "reasoning": 7, "quick": 5, "writing": 6, "debug": 8,
        "cost": 7,
    },
    "qcode": {
        "coding": 6, "architecture": 4, "review": 5, "research": 5,
        "reasoning": 5, "quick": 7, "writing": 5, "debug": 5,
        "cost": 0,
    },
}


def get_installed_terminals() -> list[str]:
    """Get list of terminal types that are actually installed."""
    installed = []
    for ttype in TERMINAL_CAPABILITIES:
        binary = {"claude": "claude", "opencode": "opencode", "mimo": "mimo",
                  "codex": "codex", "qcode": "q"}.get(ttype, ttype)
        if shutil.which(binary):
            installed.append(ttype)
    return installed


def best_terminal(task_type: str = "coding", prefer_free: bool = True) -> str:
    """Find the best installed terminal for a task type.

    Args:
        task_type: Type of task (coding, architecture, review, etc.)
        prefer_free: If True, prefer free terminals when scores are close

    Returns:
        Terminal type name (e.g., 'opencode', 'claude')
    """
    installed = get_installed_terminals()
    if not installed:
        return "claude"  # fallback

    scored = []
    for ttype in installed:
        caps = TERMINAL_CAPABILITIES.get(ttype, {})
        cap_score = caps.get(task_type, 5)
        cost = caps.get("cost", 5)

        if prefer_free:
            # Free terminals get a bonus
            if cost == 0:
                cap_score += 1.5  # preference boost for free
            else:
                cap_score -= 1.0  # penalty for paid

        scored.append((ttype, cap_score, cost))

    # Sort by score descending, then cost ascending
    scored.sort(key=lambda x: (-x[1], x[2]))
    return scored[0][0]


def format_terminal_help() -> str:
    """Generate a help string showing available terminals and their strengths."""
    installed = get_installed_terminals()
    if not installed:
        return "No AI CLI terminals detected. Install opencode, mimo, or claude."

    lines = ["Available terminals:"]
    for ttype in installed:
        caps = TERMINAL_CAPABILITIES.get(ttype, {})
        best_at = sorted(caps.items(), key=lambda x: -x[1])[:3]
        best_str = ", ".join(f"{k}={v}" for k, v in best_at if k != "cost")
        cost = caps.get("cost", 5)
        cost_label = "free" if cost == 0 else "paid"
        lines.append(f"  {ttype:<12} {best_str:<40} ({cost_label})")

    lines.append("")
    lines.append("Switch: relay use <terminal>")
    return "\n".join(lines)
