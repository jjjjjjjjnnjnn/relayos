"""RelayOS TUI — OpenCode-style chat workspace.

Layout: Status bar (top) | Messages (scrollable) | Input (bottom)

Keys:
  Ctrl+P    Command palette
  Ctrl+X    Leader key (then n/s/m/c/p/?)
  Tab       Switch provider
  Esc       Cancel / close overlay
  Enter     Submit
  Up/Down   History
"""
from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from relayos.core.session import SessionStore, Session
from relayos.providers import detect_providers, create_provider
from relayos.providers.router import ProviderRouter
from relayos.core.budget import BudgetGuard, BudgetLimits

logger = logging.getLogger(__name__)

# ── Key codes ─────────────────────────────────────────────────
CTRL_P = "\x10"
CTRL_X = "\x18"
CTRL_C = "\x03"
CTRL_N = "\x0e"
CTRL_S = "\x13"
CTRL_M = "\x0d"
CTRL_A = "\x01"
CTRL_E = "\x05"
CTRL_K = "\x0b"
CTRL_U = "\x15"
CTRL_L = "\x0c"
TAB = "\x09"
ESC = "\x1b"
ENTER = "\r"
BACKSPACE = "\x7f"


def _getch() -> str:
    """Non-blocking single key read. Returns '' if no key."""
    if sys.platform == "win32":
        import msvcrt, ctypes
        try:
            if not msvcrt.kbhit():
                return ""
            cp = ctypes.windll.kernel32.GetConsoleCP()
            raw = msvcrt.getch()
            # Extended keys (arrows, F-keys)
            if raw in (b'\xe0', b'\x00'):
                msvcrt.getch()
                return ""
            return raw.decode(f'cp{cp}')
        except Exception:
            return ""
    else:
        import termios, tty, select
        try:
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            tty.setraw(fd)
            try:
                if select.select([sys.stdin], [], [], 0.03)[0]:
                    ch = sys.stdin.read(1)
                    if ch == ESC:
                        # Try to read more for escape sequences
                        rest = ""
                        if select.select([sys.stdin], [], [], 0.01)[0]:
                            rest = sys.stdin.read(1)
                            if rest == "[":
                                if select.select([sys.stdin], [], [], 0.01)[0]:
                                    rest += sys.stdin.read(1)
                        if rest.startswith("["):
                            return f"^{rest[1:]}"  # ^A, ^B, ^C, ^D for arrows
                        return ESC
                    return ch
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
        except Exception:
            pass
        return ""


def _ctrl_name(ch: str) -> str:
    """Convert control char to name for display."""
    names = {
        CTRL_P: "Ctrl+P", CTRL_X: "Ctrl+X", CTRL_C: "Ctrl+C",
        CTRL_N: "Ctrl+N", CTRL_S: "Ctrl+S",
        TAB: "Tab", ESC: "Esc", ENTER: "Enter",
    }
    return names.get(ch, repr(ch))


# ── Command palette entries ───────────────────────────────────

PALETTE_ITEMS = [
    ("New conversation", "ctrl-x n", "新建对话"),
    ("Session list", "ctrl-x s", "对话列表"),
    ("Switch provider", "tab", "切换 Provider"),
    ("Provider settings", "ctrl-x p", "Provider 设置"),
    ("Cost report", "ctrl-x c", "消费报告"),
    ("Toggle mode", "ctrl-x m", "切换模式"),
    ("Help", "ctrl-x ?", "帮助"),
]

# ── Main TUI ───────────────────────────────────────────────────

def run_tui():
    """Run the RelayOS TUI workspace."""
    ss = SessionStore()
    router = ProviderRouter()
    bg = BudgetGuard()
    start_time = time.time()
    config_exists = (get_config_dir() / "config.yaml").exists()

    # State
    input_buffer: list[str] = []
    cursor_pos = 0
    messages: list[dict] = []      # rendered messages
    history: list[str] = []        # command history
    history_idx = -1
    current_session: Session | None = None
    current_provider_idx = 0
    providers = detect_providers()
    enabled = [p for p in providers if p.enabled]

    # UI mode
    mode: str = "input"            # input | palette | sessions | help
    palette_filter = ""
    palette_selected = 0
    sessions_list = ss.list_sessions(limit=20)
    session_list_idx = 0

    layout = Layout()
    layout.split_column(
        Layout(name="header", size=1),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=4),
    )

    def get_provider_name() -> str:
        if enabled and current_provider_idx < len(enabled):
            p = enabled[current_provider_idx]
            return p.model or p.provider
        return "none"

    def get_mode_label() -> str:
        return f"[{'AUTO' if router.mode == 'auto' else 'EDIT'}]"

    def add_msg(role: str, worker: str, content: str):
        messages.append({"role": role, "from": worker, "content": content})

    def submit_input():
        nonlocal history_idx
        text = "".join(input_buffer).strip()
        if not text:
            return

        history.append(text)
        history_idx = -1

        # Check for slash commands
        if text.startswith("/"):
            cmd = text[1:].split()[0].lower()
            if cmd == "new":
                import uuid
                name = f"Conv-{uuid.uuid4().hex[:6]}"
                sess = ss.create_session(name)
                nonlocal current_session
                current_session = sess
                add_msg("system", "", f"New session: {sess.id}")
            elif cmd == "clear":
                messages.clear()
            elif cmd == "help":
                show_help()
            elif cmd == "cost":
                s = bg.get_status()
                add_msg("system", "", f"Today: ${s['today']:.4f} / Monthly: ${s['monthly']:.4f}")
            else:
                add_msg("system", "", f"Unknown command: /{cmd}")
        else:
            # Auto-dispatch
            add_msg("user", "you", text)
            try:
                from relayos.core.conversation import ConversationEngine
                eng = ConversationEngine()
                result = eng.chat(text)
                content = result.get("content", "")
                worker = result.get("worker", "ai")
                add_msg("assistant", worker, content[:500])
            except Exception as e:
                add_msg("system", "", f"Error: {e}")

        input_buffer.clear()
        cursor_pos = 0

    def show_help():
        messages.clear()
        add_msg("system", "", "RelayOS Help")
        add_msg("system", "", "")
        add_msg("system", "", "Ctrl+P  Command palette")
        add_msg("system", "", "Ctrl+X  Leader key (n=new, s=sessions, m=mode, c=cost, p=providers, ?=help)")
        add_msg("system", "", "Tab     Switch provider")
        add_msg("system", "", "Esc     Cancel / close")
        add_msg("system", "", "Enter   Submit")
        add_msg("system", "", "Up/Dn   History")
        add_msg("system", "", "/new    New session")
        add_msg("system", "", "/clear  Clear messages")
        add_msg("system", "", "/help   This help")
        add_msg("system", "", "/cost   Cost report")

    def cycle_provider(delta: int = 1):
        nonlocal current_provider_idx
        if enabled:
            current_provider_idx = (current_provider_idx + delta) % len(enabled)
            p = enabled[current_provider_idx]
            add_msg("system", "", f"Switched to: {p.display_name} ({p.model or p.provider})")

    # Build palette render
    def render_palette(filter_str: str) -> list[str]:
        lines = [" Command Palette  (Ctrl+P to close)"]
        lines.append(" " + "-" * 50)
        filtered = [it for it in PALETTE_ITEMS if not filter_str or
                    filter_str.lower() in it[0].lower() or
                    filter_str.lower() in it[2].lower()]
        for i, (name, key, cn) in enumerate(filtered):
            sel = " >" if i == palette_selected else "  "
            lines.append(f"{sel} {name:<30} {key:<12} {cn}")
        lines.append("")
        lines.append(" Type to filter...")
        lines.append(f" > {filter_str}")
        return lines

    # ── Main loop ──
    with Live(layout, refresh_per_second=8, screen=True) as live:
        try:
            while True:
                key = _getch()

                # ── Global handlers ──
                if mode == "palette":
                    if key == ESC or key == CTRL_P:
                        mode = "input"
                    elif key == ENTER:
                        # Execute selected palette item
                        items = [it for it in PALETTE_ITEMS if not palette_filter or
                                 palette_filter.lower() in it[0].lower() or
                                 palette_filter.lower() in it[2].lower()]
                        if 0 <= palette_selected < len(items):
                            name = items[palette_selected][0]
                            add_msg("system", "", f"Executing: {name}")
                            if "Provider" in name and "settings" not in name:
                                cycle_provider(1)
                            elif "Cost" in name:
                                s = bg.get_status()
                                add_msg("system", "", f"Today: ${s['today']:.4f} / ${s['daily_limit']:.2f}")
                            elif "Help" in name:
                                show_help()
                            elif "Toggle" in name:
                                router.mode = "edit" if router.mode == "auto" else "auto"
                                add_msg("system", "", f"Mode: {router.mode}")
                        mode = "input"
                    elif key == BACKSPACE:
                        palette_filter = palette_filter[:-1]
                    elif key and len(key) == 1 and key.isprintable():
                        palette_filter += key
                    elif key == "^A":  # Up arrow
                        palette_selected = max(0, palette_selected - 1)
                    elif key == "^B":  # Down arrow
                        palette_selected += 1
                    continue

                if mode == "sessions":
                    if key == ESC:
                        mode = "input"
                    elif key == ENTER and sessions_list:
                        idx = session_list_idx
                        if 0 <= idx < len(sessions_list):
                            sid = sessions_list[idx]["id"]
                            sess = ss.get_session(sid)
                            if sess:
                                current_session = sess
                                add_msg("system", "", f"Switched to: {sess.name}")
                            mode = "input"
                    elif key == "^A":  # Up
                        session_list_idx = max(0, session_list_idx - 1)
                    elif key == "^B":  # Down
                        session_list_idx = min(len(sessions_list) - 1, session_list_idx + 1)
                    continue

                # ── Input mode ──
                if key == CTRL_P:
                    mode = "palette"
                    palette_filter = ""
                    palette_selected = 0
                elif key == TAB:
                    cycle_provider(1)
                elif key == ESC:
                    pass  # clear input if not empty
                    if input_buffer:
                        input_buffer.clear()
                        cursor_pos = 0
                elif key == ENTER:
                    submit_input()
                elif key == BACKSPACE:
                    if cursor_pos > 0:
                        cursor_pos -= 1
                        input_buffer.pop(cursor_pos)
                elif key == CTRL_X:
                    # Leader key — wait for next key
                    time.sleep(0.1)
                    next_key = _getch()
                    if next_key == "n":
                        import uuid
                        name = f"Conv-{uuid.uuid4().hex[:6]}"
                        sess = ss.create_session(name)
                        current_session = sess
                        add_msg("system", "", f"New session: {sess.id}")
                        messages.clear()
                    elif next_key == "s":
                        mode = "sessions"
                        sessions_list = ss.list_sessions(limit=20)
                        session_list_idx = 0
                    elif next_key == "m":
                        router.mode = "edit" if router.mode == "auto" else "auto"
                        add_msg("system", "", f"Mode: {router.mode}")
                    elif next_key == "c":
                        s = bg.get_status()
                        add_msg("system", "", f"Today: ${s['today']:.4f} / ${s['daily_limit']:.2f}")
                    elif next_key == "p":
                        add_msg("system", "", "Provider settings: edit ~/.relayos/config.yaml")
                    elif next_key == "?":
                        show_help()
                elif key == CTRL_C:
                    break
                elif key == CTRL_U:
                    input_buffer.clear()
                    cursor_pos = 0
                elif key == CTRL_A:
                    cursor_pos = 0
                elif key == CTRL_E:
                    cursor_pos = len(input_buffer)
                elif key == "^A":  # Up arrow
                    if history:
                        history_idx = max(-1, history_idx - 1)
                        if history_idx >= 0:
                            input_buffer = list(history[min(history_idx, len(history)-1)])
                        else:
                            input_buffer = []
                        cursor_pos = len(input_buffer)
                elif key == "^B":  # Down arrow
                    if history:
                        history_idx = min(len(history), history_idx + 1)
                        if history_idx < len(history):
                            input_buffer = list(history[history_idx])
                        else:
                            input_buffer = []
                        cursor_pos = len(input_buffer)
                elif key and len(key) == 1:
                    input_buffer.insert(cursor_pos, key)
                    cursor_pos += 1

                # ── Build header ──
                sess_id = current_session.id[:12] if current_session else "no session"
                provider = get_provider_name()
                budget = bg.get_status()
                cost_str = f"${budget['today']:.3f}" if budget['today'] > 0 else "$0"
                h = Text()
                h.append(" RelayOS  ", style="bold blue")
                h.append(f" {sess_id}  ", style="cyan")
                h.append(f" {provider}  ", style="green")
                h.append(f" {get_mode_label()}  ", style="yellow")
                h.append(f" {cost_str}", style="dim")
                layout["header"].update(Panel(h, style="bold", height=1))

                # ── Build body ──
                body_lines = []

                if mode == "palette":
                    body_lines.extend(render_palette(palette_filter))
                elif mode == "sessions":
                    body_lines.append(" Sessions  (Esc to close)")
                    body_lines.append(" " + "-" * 50)
                    for i, s in enumerate(sessions_list):
                        sel = " >" if i == session_list_idx else "  "
                        name = s.get("name", "?")[:30]
                        age = s.get("updated_at", 0)
                        ago = ""
                        if age:
                            mins = int((time.time() - age) / 60)
                            ago = f"{mins}min ago" if mins < 120 else f"{mins//60}h ago"
                        body_lines.append(f"{sel} {name:<34} {ago}")
                    body_lines.append("")
                    body_lines.append(" Enter=open  Esc=close")
                else:
                    if not messages:
                        body_lines.append("")
                        body_lines.append("  RelayOS — Agent Workspace")
                        body_lines.append("  " + "-" * 40)
                        body_lines.append("")
                        body_lines.append("  Type your task below and press Enter.")
                        body_lines.append("  Ctrl+P for commands. Tab to switch provider.")
                        body_lines.append("")

                    for m in messages[-30:]:
                        role = m.get("role", "")
                        worker = m.get("from", "")
                        content = m.get("content", "")
                        if role == "system":
                            body_lines.append(f"  {content}")
                        elif role == "user":
                            for line in content.split("\n")[:3]:
                                body_lines.append(f"  > {line}")
                        else:
                            worker_label = worker or "ai"
                            for line in content.split("\n")[:10]:
                                if len(body_lines) > 100:
                                    body_lines.append("  ... [truncated]")
                                    break
                                body_lines.append(f"  [{worker_label}] {line}")

                layout["body"].update(Panel("\n".join(body_lines[-80:]), border_style="dim"))

                # ── Build footer (input area) ──
                input_str = "".join(input_buffer)
                foot_lines = [f"> {input_str}" + ("█" if mode == "input" else "")]
                if mode == "input":
                    foot_lines.append("  Ctrl+P palette  Tab=provider  Enter=send")
                layout["footer"].update(Panel("\n".join(foot_lines), style="green", height=4))

                live.refresh()
                time.sleep(0.03)

        except KeyboardInterrupt:
            pass

    print("\033[2J\033[H", end="")


def get_config_dir() -> Path:
    from relayos.config import get_config_dir as _g
    return _g()


def main():
    """Entry for `relay` command."""
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("cmd", nargs="?")
    p.add_argument("args", nargs="*")
    a = p.parse_args()

    if a.cmd and a.cmd not in ("ui", "tui", ""):
        task = a.cmd + " " + " ".join(a.args)
        try:
            result = auto_dispatch(task)
            print(result.get("content", ""))
        except Exception as e:
            print(f"[ERR] {e}", file=sys.stderr)
        return

    run_tui()


def auto_dispatch(task: str) -> dict:
    from relayos.core.conversation import ConversationEngine
    eng = ConversationEngine()
    return eng.chat(task)


if __name__ == "__main__":
    main()
