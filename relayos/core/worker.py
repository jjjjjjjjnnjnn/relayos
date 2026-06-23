"""Worker Manager — persistent AI team members.

A Worker is a logical entity with:
- A role (architect, researcher, coder, reviewer)
- A provider/model assignment
- Persistent memory (project context it knows)
- An inbox for receiving tasks
- Status tracking across sessions

Workers are the user-facing concept. They bridge between:
- Provider adapters (for API calls)
- Terminal types (for CLI execution)
- The user's mental model ("my architect knows my project")
"""
from __future__ import annotations

import logging
import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from relayos.adapters import get_adapter, list_adapters
from relayos.config import load_config
from relayos.core.inbox import WorkerInbox
from relayos.memory.store import MemoryStore
from relayos.orchestrator.pool import TerminalPool

logger = logging.getLogger(__name__)

# Default worker roles with recommended provider/model
DEFAULT_ROLES: dict[str, dict[str, str]] = {
    "architect": {
        "provider": "anthropic",
        "model": "claude-sonnet-4-20250514",
        "emoji": "🧠",
        "description": "System design, architecture decisions",
    },
    "researcher": {
        "provider": "google",
        "model": "gemini-2.5-flash",
        "emoji": "🔍",
        "description": "Research, analysis, data gathering",
    },
    "coder": {
        "provider": "openai",
        "model": "gpt-4o",
        "emoji": "⭐",
        "description": "Code generation, implementation",
    },
    "reviewer": {
        "provider": "deepseek",
        "model": "deepseek-chat",
        "emoji": "🎯",
        "description": "Code review, security audit",
    },
    "debugger": {
        "provider": "openai",
        "model": "gpt-4o-mini",
        "emoji": "🐛",
        "description": "Debugging, error analysis",
    },
    "writer": {
        "provider": "openai",
        "model": "gpt-4o",
        "emoji": "✍️",
        "description": "Documentation, writing",
    },
    "assistant": {
        "provider": "anthropic",
        "model": "claude-haiku-4-20251001",
        "emoji": "💡",
        "description": "General assistant, quick tasks",
    },
    "data-engineer": {
        "provider": "deepseek",
        "model": "deepseek-chat",
        "emoji": "📊",
        "description": "Data processing, ETL, analysis",
    },
}


@dataclass
class Worker:
    name: str
    role: str
    provider: str
    model: str
    emoji: str = "🤖"
    status: str = "idle"  # idle | busy | error
    description: str = ""
    task_count: int = 0
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    last_used: Optional[str] = None


class WorkerManager:
    """Manages the AI workforce — create, list, assign tasks to workers.

    Workers are the primary user-facing concept. Each worker has:
    - A name and role (user gives it identity)
    - A provider + model (what powers it)
    - Persistent memory (remembers project context)
    - An inbox (receives messages from other workers/user)
    - Persistence across sessions (SQLite)
    """

    def __init__(self, config_path: Optional[str] = None):
        self._workers: dict[str, Worker] = {}
        self._lock = threading.Lock()
        self.memory = MemoryStore()
        self.inbox = WorkerInbox()
        self.config = load_config(Path(config_path) if config_path else None)
        self._init_db()
        self._load_from_db()

    def _init_db(self):
        from pathlib import Path as _Path
        db_path = _Path("~/.relayos/workers.db").expanduser()
        db_path.parent.mkdir(parents=True, exist_ok=True)
        import sqlite3
        with sqlite3.connect(str(db_path)) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS workers (
                    name TEXT PRIMARY KEY,
                    role TEXT NOT NULL,
                    provider TEXT NOT NULL,
                    model TEXT NOT NULL,
                    emoji TEXT DEFAULT '🤖',
                    status TEXT DEFAULT 'idle',
                    description TEXT DEFAULT '',
                    task_count INTEGER DEFAULT 0,
                    created_at TEXT NOT NULL,
                    last_used TEXT
                )
            """)
            conn.commit()

    def _load_from_db(self):
        import sqlite3
        db_path = Path("~/.relayos/workers.db").expanduser()
        if not db_path.exists():
            self._load_defaults()
            self._save_all()
            return
        with sqlite3.connect(str(db_path)) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute("SELECT * FROM workers ORDER BY created_at").fetchall()
        if not rows:
            self._load_defaults()
            self._save_all()
            return
        for r in rows:
            emoji = r["emoji"] if r["emoji"] else "🤖"
            desc = r["description"] if r["description"] else ""
            w = Worker(
                name=r["name"], role=r["role"], provider=r["provider"],
                model=r["model"], emoji=emoji,
                status=r["status"], description=desc,
                task_count=r["task_count"] or 0,
                created_at=r["created_at"], last_used=r["last_used"],
            )
            self._workers[w.name] = w

    def _save_all(self):
        import sqlite3
        db_path = Path("~/.relayos/workers.db").expanduser()
        with sqlite3.connect(str(db_path)) as conn:
            conn.execute("DELETE FROM workers")
            for w in self._workers.values():
                conn.execute(
                    "INSERT INTO workers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (w.name, w.role, w.provider, w.model, w.emoji, w.status,
                     w.description, w.task_count, w.created_at, w.last_used),
                )
            conn.commit()

    def _save_worker(self, w: Worker):
        import sqlite3
        db_path = Path("~/.relayos/workers.db").expanduser()
        with sqlite3.connect(str(db_path)) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO workers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (w.name, w.role, w.provider, w.model, w.emoji, w.status,
                 w.description, w.task_count, w.created_at, w.last_used),
            )
            conn.commit()

    def _load_defaults(self):
        """Create default workers on first run."""
        for name, role_def in DEFAULT_ROLES.items():
            self.create(name=name, role=name, **role_def)

    def create(self, name: str, role: str, provider: str, model: str,
               emoji: str = "🤖", description: str = "") -> Worker:
        """Create a new worker and persist to DB."""
        w = Worker(
            name=name, role=role, provider=provider, model=model,
            emoji=emoji, description=description,
        )
        with self._lock:
            self._workers[name] = w
        self._save_worker(w)
        logger.info(f"Worker '{name}' created — {provider}/{model}")
        return w

    def get(self, name: str) -> Optional[Worker]:
        return self._workers.get(name)

    def list(self) -> list[Worker]:
        return list(self._workers.values())

    def remove(self, name: str) -> bool:
        with self._lock:
            if name in self._workers:
                del self._workers[name]
        # Remove from DB
        import sqlite3
        db_path = Path("~/.relayos/workers.db").expanduser()
        with sqlite3.connect(str(db_path)) as conn:
            conn.execute("DELETE FROM workers WHERE name = ?", (name,))
            conn.commit()
        return True

    def run(self, worker_name: str, prompt: str, **kwargs) -> str:
        """Run a prompt on a specific worker via its provider adapter."""
        w = self.get(worker_name)
        if not w:
            raise ValueError(f"Worker '{worker_name}' not found")

        w.status = "busy"
        w.last_used = datetime.now(timezone.utc).isoformat()
        w.task_count += 1

        try:
            adapter = get_adapter(w.provider, {
                "api_key": self.config.resolve_api_key(w.provider),
                "model": w.model,
            })
            response = adapter.chat(prompt, **kwargs)

            # Auto-store in worker's memory
            self.memory.set(f"{worker_name}:last_task", prompt)
            self.memory.set(f"{worker_name}:last_output", response.content)

            w.status = "idle"
            return response.content
        except Exception as e:
            w.status = "error"
            raise

    def send_task(self, from_worker: str, to_worker: str, task: str) -> int:
        """Send a task from one worker to another via inbox."""
        return self.inbox.send(to=to_worker, body=task, subject="task", from_worker=from_worker)

    def get_team(self) -> list[dict[str, Any]]:
        """Get the full team status (like 'htop' for AI workers)."""
        result = []
        for w in self.list():
            unread = self.inbox.count_unread(w.name)
            mem = self.memory.get_all()
            worker_keys = {k: v for k, v in mem.items() if k.startswith(f"{w.name}:")}
            result.append({
                "name": w.name,
                "role": w.role,
                "provider": w.provider,
                "model": w.model,
                "emoji": w.emoji,
                "status": w.status,
                "description": w.description,
                "task_count": w.task_count,
                "unread": unread,
                "memory_keys": len(worker_keys),
            })
        return result

    def stats(self) -> dict:
        return {
            "total_workers": len(self._workers),
            "idle": sum(1 for w in self._workers.values() if w.status == "idle"),
            "busy": sum(1 for w in self._workers.values() if w.status == "busy"),
            "error": sum(1 for w in self._workers.values() if w.status == "error"),
            "total_tasks": sum(w.task_count for w in self._workers.values()),
        }
