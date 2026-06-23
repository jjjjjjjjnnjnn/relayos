"""Worker Focus TUI — SSH into a worker's mind.

Shows:
- Worker identity (role, responsibilities, emoji)
- Recent decisions
- Project state
- Inbox messages
- Memory summary

Usage: relay focus <worker-name>
"""
from __future__ import annotations

import sys
import time
from typing import Optional

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from relayos.core.identity import IdentityStore
from relayos.core.inbox import WorkerInbox
from relayos.core.worker import WorkerManager

console = Console()


def focus_worker(worker_name: str, duration: Optional[int] = None):
    """Display a focused view of a single worker.

    If duration is set, auto-exit after that many seconds.
    Otherwise blocks until 'q' or Ctrl+C.
    """
    wm = WorkerManager()
    worker = wm.get(worker_name)
    if not worker:
        all_w = [w.name for w in wm.list()]
        console.print(f"[red]Worker '{worker_name}' not found.[/red]")
        console.print(f"Available: {', '.join(all_w[:5])}...")
        return

    identity = IdentityStore()
    inbox = WorkerInbox()
    start_time = time.time()
    running = True

    def check_keys():
        nonlocal running
        import threading
        if sys.platform == "win32":
            import msvcrt
            while running:
                if msvcrt.kbhit():
                    k = msvcrt.getch().decode("utf-8", errors="ignore").lower()
                    if k == "q":
                        running = False
                time.sleep(0.1)
        else:
            import select
            import termios
            import tty
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                while running:
                    if select.select([sys.stdin], [], [], 0.1)[0]:
                        k = sys.stdin.read(1).lower()
                        if k == "q":
                            running = False
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

    import threading
    kt = threading.Thread(target=check_keys, daemon=True)
    kt.start()

    with Live(refresh_per_second=2, screen=True) as live:
        try:
            while running:
                if duration and (time.time() - start_time) > duration:
                    break
                live.update(_build_focus_layout(worker, identity, inbox, start_time))
                time.sleep(1)
        except KeyboardInterrupt:
            pass

    print("\033[2J\033[H", end="")


def _build_focus_layout(worker, identity: IdentityStore, inbox: WorkerInbox, start_time: float) -> Layout:
    """Build the focus layout for a single worker."""
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3),
    )
    layout["header"].update(_render_header(worker, start_time))
    layout["body"].update(_render_body(worker, identity, inbox))
    layout["footer"].update(_render_footer(worker))
    return layout


def _render_header(worker, start_time: float) -> Panel:
    elapsed = int(time.time() - start_time)
    text = Text()
    text.append(f" {worker.emoji} {worker.name}", style="bold blue")
    text.append(f"  {worker.role}", style="cyan")
    text.append(f"  |  {worker.provider}/{worker.model}", style="dim white")
    text.append(f"  |  tasks: {worker.task_count}", style="white")
    text.append(f"  [{elapsed}s]", style="dim white")
    return Panel(text, style="blue")


def _render_body(worker, identity: IdentityStore, inbox: WorkerInbox) -> Layout:
    body = Layout()
    body.split_row(
        Layout(name="main", ratio=2),
        Layout(name="sidebar", ratio=1),
    )

    # Main panel: decisions + project state
    main = Layout()
    main.split_column(
        Layout(name="decisions", ratio=2),
        Layout(name="project", ratio=1),
    )

    decisions = identity.get_decisions(worker.name, limit=5)
    if decisions:
        d_lines = []
        for d in decisions:
            ts = d.get("timestamp", "")[:16] if d.get("timestamp") else ""
            title = d.get("title", "")
            decision = d.get("decision", "")[:80]
            d_lines.append(f" [{ts}] {title}: {decision}")
        main["decisions"].update(Panel("\n".join(d_lines), title="[bold]Decisions[/bold]", border_style="dim"))
    else:
        main["decisions"].update(Panel("No decisions recorded yet.", title="[bold]Decisions[/bold]", border_style="dim"))

    state = identity.get_state(worker.name)
    if state:
        s_lines = [f"  {k}: {v[:100]}" for k, v in state.items()]
        main["project"].update(Panel("\n".join(s_lines), title="[bold]Project State[/bold]", border_style="dim"))
    else:
        main["project"].update(Panel("No project state yet.", title="[bold]Project State[/bold]", border_style="dim"))

    body["main"].update(main)

    # Sidebar: inbox + summary
    sb = Layout()
    sb.split_column(
        Layout(name="inbox", ratio=2),
        Layout(name="summary", ratio=1),
    )

    msgs = inbox.list_inbox(worker.name, unread_only=True)
    if msgs:
        i_lines = [f"  #{m['id']} from {m['from_worker']}: {m['body'][:60]}" for m in msgs[:5]]
        sb["inbox"].update(Panel("\n".join(i_lines), title="[bold]Inbox[/bold]", border_style="dim"))
    else:
        sb["inbox"].update(Panel("Inbox empty.", title="[bold]Inbox[/bold]", border_style="dim"))

    summary = identity.get_summary(worker.name)
    sb["summary"].update(Panel(summary[:300], title="[bold]Memory[/bold]", border_style="dim"))

    body["sidebar"].update(sb)
    return body


def _render_footer(worker) -> Panel:
    text = Text()
    text.append(f" FOCUS: {worker.name}", style="bold green")
    text.append("  |  ", style="dim")
    text.append("[q] back", style="italic dim")
    return Panel(text, style="green", height=3)
