"""Configuration commands — setup wizard, auto-detect, recommended settings.

Usage:
    relayos config              → interactive setup wizard
    relayos config init         → auto-detect + generate config
    relayos config recommend    → show recommended settings
    relayos config detect       → scan environment
    relayos config show         → current config
    relayos plugin list         → installed plugins
    relayos plugin install      → install a plugin
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import click
import yaml

from relayos.config import get_config_dir, load_config


@click.group()
def config():
    """Configure RelayOS — setup wizard, auto-detect, plugins."""
    pass


@config.command("init")
@click.option("--force", is_flag=True, help="Overwrite existing config")
@click.option("--interactive", "-i", is_flag=True, help="Interactive wizard")
def config_init(force: bool, interactive: bool):
    """Auto-detect environment and generate optimal config."""
    config_dir = get_config_dir()
    config_path = config_dir / "config.yaml"

    if config_path.exists() and not force:
        click.echo(f"[OK] Config exists: {config_path}")
        click.echo("  Use --force to overwrite, or --interactive for guided setup")
        return

    from relayos.core.provider_registry import suggest_config, detect_installed_terminals, detect_env_api_keys

    # Detect environment
    terminals = detect_installed_terminals()
    api_keys = detect_env_api_keys()
    suggested = suggest_config()

    if interactive:
        _interactive_wizard(config_path, suggested, terminals, api_keys)
        return

    # Non-interactive: write suggested config
    config_dir.mkdir(parents=True, exist_ok=True)

    # Build YAML
    providers_yaml = {}
    for name, pcfg in suggested.get("providers", {}).items():
        providers_yaml[name] = {
            "model": pcfg["model"],
        }

    terminals_yaml = suggested.get("terminals", [])

    config_content = {
        "providers": providers_yaml,
        "terminals": terminals_yaml,
        "routing": suggested.get("routing", {"default": "balanced", "policies": {}}),
        "memory": {"type": "sqlite", "path": "~/.relayos/memory.db"},
        "mcp_servers": {},
    }

    config_path.write_text(yaml.dump(config_content, default_flow_style=False, allow_unicode=True), encoding="utf-8")
    click.echo(f"[OK] Generated config: {config_path}")

    # Summary
    api_keys_found = sum(1 for v in api_keys.values() if v)
    terminals_found = sum(1 for t in terminals if t["installed"])
    click.echo(f"  Detected: {api_keys_found} API keys, {terminals_found} CLI terminals")
    click.echo(f"  Configured: {len(providers_yaml)} providers, {len(terminals_yaml)} terminals")


@config.command("show")
def config_show():
    """Show current configuration."""
    cfg = load_config()
    config_path = get_config_dir() / "config.yaml"
    if config_path.exists():
        click.echo(f"Config: {config_path}")
        click.echo(config_path.read_text(encoding="utf-8"))
    else:
        click.echo(f"[WARN] No config found at {config_path}")
        click.echo("  Run: relayos config init")


@config.command("detect")
def config_detect():
    """Scan environment for installed AI tools and API keys."""
    from relayos.core.provider_registry import detect_installed_terminals, detect_env_api_keys, list_providers

    click.echo("=== Environment Detection ===")
    click.echo("")

    # API Keys
    click.echo("API Keys:")
    api_keys = detect_env_api_keys()
    for name, found in api_keys.items():
        status = "[OK]" if found else "[ERR]"
        click.echo(f"  {status} {name}")

    click.echo("")

    # CLI Terminals
    click.echo("AI CLI Terminals:")
    terminals = detect_installed_terminals()
    for t in terminals:
        status = "[OK]" if t["installed"] else "[-]"
        click.echo(f"  {status} {t['label']:<30} {t['binary']:<15} {t['path'] or ''}")

    click.echo("")

    # Suggest custom terminals
    from relayos.core.plugin import discover_custom_terminals
    custom = discover_custom_terminals()
    if custom:
        click.echo("Other AI tools found (not yet configured):")
        for c in custom:
            click.echo(f"  [?] {c['label']:<30} {c['binary']:<15} {c['path']}")
        click.echo("  Run: relayos plugin add <name> to integrate")


@config.command("recommend")
def config_recommend():
    """Show recommended settings based on your environment."""
    from relayos.core.provider_registry import suggest_config, detect_installed_terminals, detect_env_api_keys

    api_keys = detect_env_api_keys()
    terminals = detect_installed_terminals()
    suggested = suggest_config()

    click.echo("=== Recommended Configuration ===")
    click.echo("")

    click.echo("Providers:")
    for name, pcfg in suggested.get("providers", {}).items():
        click.echo(f"  [OK] {name}: {pcfg['model']}")

    click.echo("")
    click.echo("Terminals:")
    for t in suggested.get("terminals", []):
        click.echo(f"  [OK] {t['name']}: type={t['type']}, model={t.get('model', 'default')}")

    click.echo("")
    click.echo("Routing Policies:")
    for task_type, policy in suggested.get("routing", {}).get("policies", {}).items():
        click.echo(f"  {task_type}: {policy}")

    click.echo("")
    click.echo(f"To apply: relayos config init")
    click.echo(f"To edit:  relayos config show > ~/.relayos/config.yaml")


# ── Interactive Wizard ──────────────────────────────────────


def _interactive_wizard(config_path, suggested, terminals, api_keys):
    """Run interactive configuration wizard."""
    click.echo("")
    click.echo("=== RelayOS Setup Wizard ===")
    click.echo("Press Enter to accept defaults.")
    click.echo("")

    config_dir = config_path.parent
    config_dir.mkdir(parents=True, exist_ok=True)

    config_content = {
        "providers": {},
        "terminals": [],
        "routing": {
            "default": "balanced",
            "policies": {},
        },
        "memory": {"type": "sqlite", "path": "~/.relayos/memory.db"},
        "mcp_servers": {},
    }

    # Provider setup
    click.echo("Step 1: Configure Providers")
    for name, found in api_keys.items():
        from relayos.core.provider_registry import get_provider
        p = get_provider(name)
        if not p:
            continue
        if found:
            use = click.prompt(f"  Enable {name}?", default="y", type=click.Choice(["y", "n"]))
            if use == "y":
                model = click.prompt(f"  Model for {name}", default=p.default_model)
                config_content["providers"][name] = {"model": model}
        else:
            key = click.prompt(f"  {name} API key (or Enter to skip)", default="")
            if key:
                os.environ[name.upper() + "_API_KEY"] = key
                config_content["providers"][name] = {"model": p.default_model}

    # Terminal setup
    click.echo("")
    click.echo("Step 2: Configure CLI Terminals")
    from relayos.core.provider_registry import detect_installed_terminals
    for t in detect_installed_terminals():
        if t["installed"]:
            use = click.prompt(f"  Add {t['label']}?", default="y", type=click.Choice(["y", "n"]))
            if use == "y":
                entry = {"name": t["type"], "type": t["type"]}
                config_content["terminals"].append(entry)

    # Add custom terminal
    add_custom = click.prompt("  Add custom terminal?", default="n", type=click.Choice(["y", "n"]))
    if add_custom == "y":
        binary = click.prompt("    Binary path/name (e.g., cursor)")
        type_name = click.prompt("    Type name", default=binary)
        name = click.prompt("    Display name", default=type_name)
        model = click.prompt("    Default model", default="gpt-4o")
        config_content["terminals"].append({
            "name": name,
            "type": type_name,
            "binary": binary,
            "model": model,
        })

    # Write config
    config_path.write_text(yaml.dump(config_content, default_flow_style=False, allow_unicode=True), encoding="utf-8")
    click.echo(f"\n[OK] Configuration saved: {config_path}")
    click.echo("Run 'relay' to start the TUI")


# ── Plugin Commands ─────────────────────────────────────────


@click.group()
def plugin():
    """Manage plugins — extend RelayOS with custom terminals and adapters."""
    pass


@plugin.command("list")
def plugin_list():
    """List installed plugins and extensions."""
    from relayos.core.plugin import get_plugin_manager, discover_custom_terminals
    pm = get_plugin_manager()
    plugins = pm.list_plugins()

    click.echo("Installed plugins:")
    if not plugins:
        click.echo("  (none)")
    for p in plugins:
        click.echo(f"  {p.name:<25} {p.type:<12} {p.description or p.entry_point}")

    click.echo("")
    click.echo("Registered terminal types:")
    from relayos.terminals import list_terminal_types
    for t in list_terminal_types():
        status = "[OK]" if t["available"] else "[-]"
        click.echo(f"  {status} {t['type']:<15} {t['binary']:<15} {t.get('default_model', '')}")

    click.echo("")
    custom = discover_custom_terminals()
    if custom:
        click.echo("Detected unregistered AI tools:")
        for c in custom:
            click.echo(f"  [?] {c['label']:<30} {c['binary']}")
        click.echo("  Run: relayos plugin add <name> to register")


@plugin.command("add")
@click.argument("binary")
@click.option("-n", "--name", help="Display name")
@click.option("-m", "--model", default="gpt-4o", help="Default model")
@click.option("-t", "--type-name", help="Type identifier")
@click.option("--command-template", help="Command template with {binary} {prompt} {model}")
def plugin_add(binary: str, name: str | None, model: str, type_name: str | None, command_template: str | None):
    """Register a custom AI CLI terminal.

    Example: relayos plugin add cursor
    """
    from relayos.core.plugin import get_plugin_manager
    pm = get_plugin_manager()

    name = name or binary
    type_name = type_name or binary
    pm.register_custom_terminal(
        name=name,
        binary=binary,
        model=model,
        command_template=command_template,
        type_name=type_name,
    )

    click.echo(f"[OK] Registered custom terminal: {name} ({binary})")
    click.echo(f"  Type: {type_name}, Model: {model}")
    click.echo(f"  Now you can use: relay terminal create {type_name} -n {name}")
