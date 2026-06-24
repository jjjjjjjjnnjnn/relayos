# RelayOS Development Tasks

## Current Status
- Release v0.1.0a1 created
- `pip install relayos` — needs PyPI token for publishing
- Install locally: `pip install -e .` (already done)
- Wheel available: github.com/jjjjjjjjnnjnn/relayos/releases

## Collaboration Tasks

### For mimo (frontend/TUI review)
```bash
mimo run "Review relayos/tui/app.py for UX improvements and suggest changes"
mimo run "Review relayos/server/static/index.html for UI flow"
```

### For opencode (code quality/data)
```bash
opencode run "Scan relayos/core/ for type hints and code quality issues"
opencode run "Check relayos/cli/main.py for Python patterns"
opencode run "Review all relayos/*/__init__.py for consistent exports"
```

### Team structure
| Worker | Type | Model | Task |
|--------|------|-------|------|
| architect | anthropic | claude-sonnet | architecture review |
| ceo | anthropic | claude-sonnet | decisions |
| backend | openai | gpt-4o | implementation |
| frontend | openai | gpt-4o | UI work |
| reviewer | deepseek | deepseek-chat | code review |

### Check results
```bash
relayos memory-list
relay session list
```

### Publish to PyPI (one-time)
```bash
python -m twine upload dist/*
# username: __token__
# password: <token from pypi.org>
```
