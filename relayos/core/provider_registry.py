"""Provider Registry — all known providers, models, pricing, and capabilities.

Used for:
- Model selection in config wizard
- Cost estimation
- Capability-aware routing
- Free tier detection
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ModelInfo:
    id: str
    provider: str
    description: str = ""
    context_window: int = 8192
    max_output: int = 4096
    cost_per_1k_input: float = 0.0  # USD
    cost_per_1k_output: float = 0.0
    has_free_tier: bool = False
    is_default: bool = False
    capabilities: list[str] = field(default_factory=lambda: ["chat"])


@dataclass
class ProviderInfo:
    name: str
    description: str = ""
    env_key: str = ""
    api_url: str = ""
    default_model: str = ""
    models: list[ModelInfo] = field(default_factory=list)
    is_local: bool = False
    is_free: bool = False

    def get_model(self, model_id: str) -> Optional[ModelInfo]:
        for m in self.models:
            if m.id == model_id:
                return m
        return None

    def default(self) -> Optional[ModelInfo]:
        for m in self.models:
            if m.is_default:
                return m
        return self.models[0] if self.models else None


# ── All known providers ─────────────────────────────────────

PROVIDERS: dict[str, ProviderInfo] = {
    "openai": ProviderInfo(
        name="openai",
        description="OpenAI GPT-4o and GPT-4o-mini",
        env_key="OPENAI_API_KEY",
        api_url="https://api.openai.com/v1",
        default_model="gpt-4o",
        models=[
            ModelInfo("gpt-4o", "openai", "Best all-round model", 128000, 16384, 0.0025, 0.01, capabilities=["chat", "vision", "code"]),
            ModelInfo("gpt-4o-mini", "openai", "Fast, cheap, good enough", 128000, 16384, 0.00015, 0.0006, is_default=True, capabilities=["chat", "vision"]),
            ModelInfo("o3-mini", "openai", "Strong reasoning", 200000, 100000, 0.004, 0.016, capabilities=["chat", "reasoning"]),
        ],
    ),
    "anthropic": ProviderInfo(
        name="anthropic",
        description="Anthropic Claude models",
        env_key="ANTHROPIC_API_KEY",
        api_url="https://api.anthropic.com/v1",
        default_model="claude-sonnet-4-20250514",
        models=[
            ModelInfo("claude-sonnet-4-20250514", "anthropic", "Best for architecture/code", 200000, 8192, 0.003, 0.015, is_default=True, capabilities=["chat", "code", "reasoning"]),
            ModelInfo("claude-haiku-4-20251001", "anthropic", "Fast, cheap, good for quick tasks", 200000, 8192, 0.001, 0.005, capabilities=["chat", "code"]),
            ModelInfo("claude-opus-4-20250514", "anthropic", "Maximum reasoning", 200000, 8192, 0.015, 0.075, capabilities=["chat", "code", "reasoning"]),
        ],
    ),
    "google": ProviderInfo(
        name="google",
        description="Google Gemini models (free tier available)",
        env_key="GEMINI_API_KEY",
        api_url="https://generativelanguage.googleapis.com/v1beta",
        default_model="gemini-2.5-flash",
        is_free=True,
        models=[
            ModelInfo("gemini-2.5-flash", "google", "Fast, free tier, 1M context", 1048576, 8192, 0.0, 0.0, has_free_tier=True, is_default=True, capabilities=["chat", "research", "vision"]),
            ModelInfo("gemini-2.5-pro", "google", "Strong reasoning, premium", 1048576, 8192, 0.00125, 0.005, capabilities=["chat", "reasoning", "code"]),
        ],
    ),
    "deepseek": ProviderInfo(
        name="deepseek",
        description="DeepSeek — cheap, strong code analysis",
        env_key="DEEPSEEK_API_KEY",
        api_url="https://api.deepseek.com/v1",
        default_model="deepseek-chat",
        models=[
            ModelInfo("deepseek-chat", "deepseek", "Cheap, good for review/analysis", 64000, 8192, 0.00014, 0.00028, is_default=True, capabilities=["chat", "code", "analysis"]),
            ModelInfo("deepseek-reasoner", "deepseek", "Deep reasoning, chain-of-thought", 64000, 8192, 0.00055, 0.00219, capabilities=["reasoning"]),
        ],
    ),
    "ollama": ProviderInfo(
        name="ollama",
        description="Local models via Ollama (private, free)",
        env_key="",
        api_url="http://localhost:11434",
        default_model="qwen2.5:7b",
        is_local=True,
        is_free=True,
        models=[
            ModelInfo("qwen2.5:7b", "ollama", "Good general 7B model", 32768, 4096, 0.0, 0.0, is_default=True, capabilities=["chat", "code"]),
            ModelInfo("qwen2.5:32b", "ollama", "Strong 32B model", 32768, 4096, 0.0, 0.0, capabilities=["chat", "code", "reasoning"]),
            ModelInfo("llama3.1:8b", "ollama", "Meta LLaMA 3.1 8B", 128000, 4096, 0.0, 0.0, capabilities=["chat"]),
            ModelInfo("codellama:7b", "ollama", "Code-focused model", 16384, 4096, 0.0, 0.0, capabilities=["code"]),
            ModelInfo("mistral:7b", "ollama", "Mistral 7B fast", 32768, 4096, 0.0, 0.0, capabilities=["chat"]),
        ],
    ),
}


def get_provider(name: str) -> Optional[ProviderInfo]:
    return PROVIDERS.get(name)


def list_providers() -> dict[str, ProviderInfo]:
    return dict(PROVIDERS)


def detect_installed_terminals() -> list[dict]:
    """Auto-detect which AI CLI terminals are installed on the system."""
    import shutil
    results = []
    terminals = [
        ("claude", "claude", "Claude Code (Anthropic)"),
        ("mimo", "mimo", "Mimo Code"),
        ("opencode", "opencode", "OpenCode"),
        ("codex", "codex", "OpenAI Codex CLI"),
        ("q", "qcode", "QCode CLI"),
    ]
    for binary, type_name, label in terminals:
        path = shutil.which(binary)
        results.append({
            "type": type_name,
            "binary": binary,
            "label": label,
            "installed": path is not None,
            "path": path,
        })
    return results


def detect_env_api_keys() -> dict[str, bool]:
    """Check which API keys are available in the environment."""
    import os
    keys = {}
    for name, provider in PROVIDERS.items():
        if provider.env_key:
            keys[name] = os.environ.get(provider.env_key, "") != ""
        else:
            keys[name] = True  # local, always available
    return keys


def suggest_config() -> dict:
    """Generate recommended configuration based on environment."""
    installed_terminals = detect_installed_terminals()
    api_keys = detect_env_api_keys()

    providers_config = {}
    terminals_config = []

    # For each provider with API key, add recommended config
    for name, provider in PROVIDERS.items():
        if api_keys.get(name, False):
            providers_config[name] = {
                "model": provider.default_model,
            }
            # Add recommended terminal
            model = provider.default()
            if model:
                terminals_config.append({
                    "name": f"{name}-default",
                    "type": name,
                    "model": model.id,
                })

    # Add detected CLI terminals
    for t in installed_terminals:
        if t["installed"]:
            # Check if we already have this type
            existing = any(ct["type"] == t["type"] for ct in terminals_config)
            if not existing:
                terminals_config.append({
                    "name": f"{t['type']}-cli",
                    "type": t["type"],
                })

    # Auto-routing rules based on available providers
    routing = {
        "default": "balanced",
        "policies": {},
    }
    if api_keys.get("google"):
        routing["policies"]["research"] = "free_first"
    if api_keys.get("anthropic"):
        routing["policies"]["architecture"] = "quality"
    if api_keys.get("deepseek"):
        routing["policies"]["review"] = "cheapest"
    if api_keys.get("openai"):
        routing["policies"]["coding"] = "balanced"

    return {
        "providers": providers_config,
        "terminals": terminals_config,
        "routing": routing,
    }
