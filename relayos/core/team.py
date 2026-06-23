"""Team Templates — pre-configured AI teams for common workflows.

Usage:
    relay team create startup    -> CEO, Architect, Backend, Frontend, Reviewer
    relay team create research   -> Researcher, Analyst, Writer, Reviewer
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from relayos.core.worker import WorkerManager


@dataclass
class TeamTemplate:
    name: str
    description: str
    workers: list[dict] = field(default_factory=list)


TEAM_TEMPLATES: dict[str, TeamTemplate] = {
    "startup": TeamTemplate(
        name="startup",
        description="Full-stack startup team: CEO, Architect, Backend, Frontend, Reviewer",
        workers=[
            {"name": "ceo", "role": "CEO", "provider": "anthropic", "model": "claude-sonnet-4-20250514",
             "emoji": "👔", "description": "Product strategy, requirements, decision-making"},
            {"name": "architect", "role": "Architect", "provider": "anthropic", "model": "claude-sonnet-4-20250514",
             "emoji": "🧠", "description": "System design, architecture decisions, tech stack"},
            {"name": "backend", "role": "Backend", "provider": "openai", "model": "gpt-4o",
             "emoji": "⚙️", "description": "API development, database, business logic"},
            {"name": "frontend", "role": "Frontend", "provider": "openai", "model": "gpt-4o",
             "emoji": "🎨", "description": "UI components, responsive design, user experience"},
            {"name": "reviewer", "role": "Reviewer", "provider": "deepseek", "model": "deepseek-chat",
             "emoji": "🎯", "description": "Code review, security audit, best practices"},
        ],
    ),
    "research": TeamTemplate(
        name="research",
        description="Research team: Researcher, Analyst, Writer, Reviewer",
        workers=[
            {"name": "researcher", "role": "Researcher", "provider": "google", "model": "gemini-2.5-flash",
             "emoji": "🔍", "description": "Literature review, data gathering, trend analysis"},
            {"name": "analyst", "role": "Analyst", "provider": "deepseek", "model": "deepseek-chat",
             "emoji": "📊", "description": "Data analysis, statistics, pattern recognition"},
            {"name": "writer", "role": "Writer", "provider": "openai", "model": "gpt-4o",
             "emoji": "✍️", "description": "Reports, papers, documentation, editing"},
            {"name": "reviewer", "role": "Reviewer", "provider": "anthropic", "model": "claude-sonnet-4-20250514",
             "emoji": "🎯", "description": "Critical review, consistency check, citation validation"},
        ],
    ),
    "devops": TeamTemplate(
        name="devops",
        description="DevOps team: SRE, Infra, Security, Monitoring",
        workers=[
            {"name": "sre", "role": "SRE", "provider": "anthropic", "model": "claude-haiku-4-20251001",
             "emoji": "🛡️", "description": "Reliability, incident response, SLO tracking"},
            {"name": "infra", "role": "Infrastructure", "provider": "openai", "model": "gpt-4o",
             "emoji": "🏗️", "description": "Cloud infra, Docker, K8s, CI/CD pipelines"},
            {"name": "security", "role": "Security", "provider": "deepseek", "model": "deepseek-chat",
             "emoji": "🔒", "description": "Security audit, vulnerability scanning, compliance"},
            {"name": "monitor", "role": "Monitoring", "provider": "google", "model": "gemini-2.5-flash",
             "emoji": "📈", "description": "Observability, logging, metrics, alerting"},
        ],
    ),
    "writing": TeamTemplate(
        name="writing",
        description="Content team: Editor, Writer, Reviewer, Publisher",
        workers=[
            {"name": "editor", "role": "Editor", "provider": "anthropic", "model": "claude-sonnet-4-20250514",
             "emoji": "📝", "description": "Outline, structure, tone, audience analysis"},
            {"name": "writer", "role": "Writer", "provider": "openai", "model": "gpt-4o",
             "emoji": "✍️", "description": "Content creation, drafting, storytelling"},
            {"name": "reviewer", "role": "Reviewer", "provider": "deepseek", "model": "deepseek-chat",
             "emoji": "🎯", "description": "Fact-check, grammar, style guide compliance"},
            {"name": "publisher", "role": "Publisher", "provider": "google", "model": "gemini-2.5-flash",
             "emoji": "🚀", "description": "SEO optimization, formatting, distribution"},
        ],
    ),
}


def create_team(template_name: str, wm: WorkerManager) -> list[str]:
    """Create workers from a team template. Returns list of worker names."""
    tmpl = TEAM_TEMPLATES.get(template_name)
    if not tmpl:
        available = ", ".join(sorted(TEAM_TEMPLATES))
        raise ValueError(f"Unknown team template '{template_name}'. Available: {available}")

    created = []
    for w_def in tmpl.workers:
        # Skip if worker already exists
        if wm.get(w_def["name"]):
            continue
        wm.create(
            name=w_def["name"],
            role=w_def["role"],
            provider=w_def["provider"],
            model=w_def["model"],
            emoji=w_def["emoji"],
            description=w_def["description"],
        )
        created.append(w_def["name"])
    return created


def list_templates() -> list[dict]:
    """List available team templates."""
    return [
        {"name": t.name, "description": t.description, "worker_count": len(t.workers)}
        for t in TEAM_TEMPLATES.values()
    ]
