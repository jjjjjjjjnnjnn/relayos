"""MCO Bridge — optional execution backend for multi-agent consensus.

RelayOS = control plane (routing, planning, memory, session)
MCO    = execution plane (multi-agent fan-out, consensus, findings)

Install: pip install relayos[executor]  # also installs mco

Usage:
    from relayos.executor.mco import MCOBridge
    bridge = MCOBridge()
    results = bridge.run("Review this code", agents=["claude", "opencode", "gemini"])
"""
from __future__ import annotations

import json
import logging
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)


class MCOBridge:
    """Bridge between RelayOS and MCO execution engine.

    Dispatches tasks to MCO for multi-agent parallel execution
    with consensus/merge. Results come back as structured findings.
    """

    def __init__(self):
        self._available = self._check_mco()

    def _check_mco(self) -> bool:
        """Check if MCO is installed and available."""
        try:
            result = subprocess.run(
                [sys.executable, "-m", "mco", "--help"],
                capture_output=True, text=True, timeout=10,
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, Exception):
            return False

    @property
    def available(self) -> bool:
        return self._available

    def run(self, prompt: str, agents: Optional[list[str]] = None,
            repo_path: str = ".", timeout: int = 300) -> dict[str, Any]:
        """Run a prompt through MCO's multi-agent execution.

        Args:
            prompt: The task/request to execute
            agents: List of agent providers (claude, opencode, gemini, etc.)
            repo_path: Repository root for context
            timeout: Per-agent timeout in seconds

        Returns:
            dict with findings/results from MCO
        """
        if not self._available:
            return {"error": "MCO not installed. Run: pip install mco"}

        agents = agents or ["opencode", "gemini"]
        agent_flags = []
        for a in agents:
            agent_flags.extend(["--agent", a])

        cmd = [
            sys.executable, "-m", "mco", "review",
            "--repo", repo_path,
            "--timeout", str(timeout),
            *agent_flags,
            "--prompt", prompt,
            "--format", "json",
        ]

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=timeout + 30,
            )
            if result.returncode != 0:
                return {
                    "error": f"MCO exit code {result.returncode}",
                    "stderr": result.stderr[:500],
                }

            # Parse JSON output
            try:
                data = json.loads(result.stdout)
                return {
                    "provider": "mco",
                    "findings": data.get("findings", []),
                    "consensus": data.get("consensus", {}),
                    "raw": data,
                }
            except json.JSONDecodeError:
                return {
                    "provider": "mco",
                    "findings": [],
                    "raw_text": result.stdout[:2000],
                }

        except subprocess.TimeoutExpired:
            return {"error": "MCO execution timed out"}
        except Exception as e:
            return {"error": f"MCO execution failed: {e}"}

    def review(self, prompt: str, agents: Optional[list[str]] = None,
               repo_path: str = ".", divide_by: str = "") -> dict[str, Any]:
        """Run MCO review with structured findings.

        MCO can divide by dimensions or files for parallel review.
        """
        if not self._available:
            return {"error": "MCO not installed"}

        agents = agents or ["claude", "opencode", "gemini", "qwen"]
        agent_flags = []
        for a in agents:
            agent_flags.extend(["--agent", a])

        cmd = [
            sys.executable, "-m", "mco", "review",
            "--repo", repo_path,
            "--stream", "findings",
            *agent_flags,
            "--prompt", prompt,
            "--format", "json",
        ]
        if divide_by:
            cmd.extend(["--divide", divide_by])

        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, timeout=600,
            )
            if result.returncode != 0:
                return {"error": f"MCO review failed: {result.stderr[:500]}"}

            try:
                data = json.loads(result.stdout)
                return {
                    "provider": "mco",
                    "type": "review",
                    "findings": data.get("findings", []),
                    "consensus": data.get("consensus", {}),
                    "summary": data.get("summary", ""),
                }
            except json.JSONDecodeError:
                return {"provider": "mco", "type": "review", "raw": result.stdout[:2000]}

        except subprocess.TimeoutExpired:
            return {"error": "MCO review timed out"}
        except Exception as e:
            return {"error": f"MCO review failed: {e}"}

    def doctor(self) -> dict[str, Any]:
        """Run MCO doctor to check available providers."""
        if not self._available:
            return {"available": False, "error": "MCO not installed"}

        try:
            result = subprocess.run(
                [sys.executable, "-m", "mco", "doctor"],
                capture_output=True, text=True, timeout=30,
            )
            return {
                "available": result.returncode == 0,
                "output": result.stdout[:1000],
            }
        except Exception as e:
            return {"available": False, "error": str(e)}
