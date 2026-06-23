"""State Compiler — pure code state transitions, zero LLM.

Processes structured JSON output from workers and updates state.
No LLM calls, no prompt engineering, no drift.

Worker output format:
{
  "action": "complete | request_help | update_state | make_decision",
  "result": {},
  "state_updates": {},
  "new_decisions": [],
  "next_tasks": []
}
"""
from __future__ import annotations

import json
import logging
from typing import Any, Optional

from relayos.core.state import StateStore

logger = logging.getLogger(__name__)


class StateCompiler:
    """Compiles worker output into state changes.

    Every worker response goes through this compiler.
    It translates structured JSON into:
    - Project state updates (key-value)
    - Decision log entries (append-only)
    - Next task creation (worker-to-worker)
    - Current task resolution
    """

    def __init__(self, store: Optional[StateStore] = None):
        self.store = store or StateStore()

    def process(self, worker_id: str, task_id: str, output: dict) -> dict:
        """Process a worker's structured output and apply state changes.

        Args:
            worker_id: The worker that produced the output
            task_id: The task being processed
            output: Structured JSON from the worker

        Returns:
            Summary of what was compiled
        """
        changes = {
            "state_updates": 0,
            "new_decisions": 0,
            "next_tasks": 0,
            "errors": [],
        }

        # 1. Update project state
        for key, value in output.get("state_updates", {}).items():
            try:
                val = str(value) if not isinstance(value, str) else value
                self.store.set_state(key, val, updated_by=worker_id)
                changes["state_updates"] += 1
            except Exception as e:
                changes["errors"].append(f"state_update:{key}:{e}")

        # 2. Record decisions
        for d in output.get("new_decisions", []):
            try:
                self.store.add_decision(
                    worker_id=worker_id,
                    summary=d.get("summary", ""),
                    reason=d.get("reason", ""),
                    category=d.get("category", "general"),
                )
                changes["new_decisions"] += 1
            except Exception as e:
                changes["errors"].append(f"decision:{e}")

        # 3. Create next tasks (worker-to-worker handoff)
        for t in output.get("next_tasks", []):
            try:
                tid = self.store.create_task(
                    from_worker=worker_id,
                    to_worker=t.get("to", ""),
                    payload=t.get("payload", {}),
                    task_type=t.get("type", "request"),
                    parent_task_id=task_id,
                )
                changes["next_tasks"] += 1
                logger.info(f"Task {tid} created: {worker_id} → {t.get('to')}")
            except Exception as e:
                changes["errors"].append(f"next_task:{e}")

        # 4. Resolve current task
        action = output.get("action", "complete")
        if action in ("complete", "done"):
            self.store.resolve_task(task_id, "done")
            changes["task_resolved"] = True
        elif action == "failed":
            self.store.resolve_task(task_id, "failed")
            changes["task_resolved"] = True
            changes["failed"] = True
        elif action == "request_help":
            self.store.resolve_task(task_id, "blocked")
            changes["task_resolved"] = True

        # 5. Increment worker task count
        self.store.incr_task_count(worker_id)

        return changes

    def resolve(self, worker_id: str, output: dict) -> dict:
        """Alias for process() without requiring a task_id.

        Creates a synthetic task for standalone calls.
        """
        task_id = f"standalone-{id(output)}"
        return self.process(worker_id, task_id, output)

    def get_summary(self, worker_id: str) -> str:
        """Generate a compressed worker summary for context injection."""
        worker = self.store.get_worker(worker_id)
        if not worker:
            return f"Worker '{worker_id}' not found."

        state = self.store.get_all_state()
        decisions = self.store.get_decisions(worker_id, limit=5)
        inbox = self.store.get_inbox(worker_id)

        parts = [f"=== {worker_id} ({worker['role']}) ==="]

        if state:
            s = "; ".join(f"{k}={v}" for k, v in list(state.items())[:8])
            parts.append(f"State: {s}")

        if decisions:
            d_str = "; ".join(d["summary"] for d in decisions)
            parts.append(f"Decisions: {d_str}")

        if inbox:
            parts.append(f"Tasks: {len(inbox)} pending")

        result = "\n".join(parts)
        # Keep under 2000 chars (~500 tokens)
        if len(result) > 2000:
            result = result[:2000] + "\n..."
        return result
