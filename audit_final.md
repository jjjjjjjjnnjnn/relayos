# RelayOS Final Audit Report

**Files audited**: providers/, core/budget.py, i18n.py, cli/wizard.py, tui/app.py, config.py, cost.py

## Summary

| Severity | Count |
|----------|-------|
| HIGH | 10 |
| MEDIUM | 11 |
| LOW | 4 |
| CRITICAL | 5 |
| **Total** | **30** |

## CRITICAL

- **_getch() leaves terminal in raw mode on every successful read** (`relayos/tui/app.py`) — On Unix, _getch() calls tty.setraw(fd) to enter raw mode, then on success (select returns data) returns early WITHOUT calling termios.tcsetattr to restore terminal attributes. The restore only runs on the no-input path. This means after the first successful keystroke, stdin stays in raw mode for the entire session, breaking subsequent print() calls in main() and potentially leaving the terminal in a broken state after exit. The print('\033[2J\033[H') at the end of run_tui() may not render correctly.
  Fix: undefined

- **_getch() does not consume multi-byte escape sequences on Unix, causing garbage in input buffer** (`relayos/tui/app.py`) — Arrow keys and function keys send multi-byte sequences like \x1b[A. The Unix branch reads only 1 byte per call: first byte \x1b matches the ESC handler (clears buffer), but the '[' and 'A' bytes arrive on subsequent calls. Both are printable and get appended to input_buffer as literal characters. This means pressing an arrow key corrupts the input buffer with '[A'.
  Fix: undefined

- **Wizard triggered unconditionally even with piped input due to dead-code guard** (`relayos/tui/app.py`) — Lines 290-297: The condition 'if sys.stdin.isatty() or not (sys.stdin.read(0) == "" and True): pass' is logically always True. 'sys.stdin.read(0)' always returns '' regardless of pipe state, so 'not ("" == "" and True)' is False. Combined with OR, the overall expression is always True -> always enters the 'pass' block -> always runs the wizard. The intent was to skip the wizard when stdin is piped, but the guard is dead code.
  Fix: undefined

- **sys.stdin.read(0) consumes piped data before wizard runs** (`relayos/tui/app.py`) — When stdin is piped, sys.stdin.read(0) can consume the first buffered bytes (0-length reads may still advance the buffer in some Python/stdin implementations). Combined with the dead-code guard above, piped input data is partially consumed before the wizard's input() calls interact with the terminal. Then sys.stdin.read().strip() on line 305 returns empty, losing the task.
  Fix: undefined

- **Dead-code CLI fallback in select() iterates over empty list** (`relayos/providers/router.py`) — Line 40-43: Inside 'if not enabled:' (enabled list is empty), the fallback loop does '[p for p in enabled if isinstance(...)]' which iterates over the SAME empty enabled list. So 'cli' is always empty and the fallback to CLI never works. The intent was likely to iterate over self.providers (the config list) instead. Users with all API providers disabled but CLI providers configured get RuntimeError instead of CLI fallback.
  Fix: undefined

## HIGH

- **{stdin} detection in CLIProvider.complete() is broken** (`relayos/providers/__init__.py`) — Line 139: 'input=prompt if "{stdin}" in str(cmd) else None' checks if the substring '{stdin}' appears in the Python string representation of a list (e.g., "['claude', '-p', 'prompt text']"). No command in typed_cmds contains '{stdin}', and the default args are just ['--prompt', prompt]. So stdin is NEVER piped to any CLI command, even for hypothetical providers whose args reference {stdin}. The check is effectively dead code.
  Fix: undefined

- **daily_usd=0 or per_task_usd=0 silently blocks or confirms every task** (`relayos/core/budget.py`) — If per_task_usd=0, every positive-cost task triggers 'confirm'. If daily_usd=0, line 89 'today_spent + estimated_cost > 0' is always true (assuming non-negative costs), which blocks every task. While these are extreme values, there's no validation or warning when limits are set to zero, and the error messages don't explain that zero limits are the cause.
  Fix: undefined

- **BudgetGuard._sum_costs lacks WAL pragma, risking SQLITE_BUSY errors** (`relayos/core/budget.py`) — CostManager._conn sets PRAGMA journal_mode=WAL for concurrent reads. BudgetGuard._sum_costs opens its own connection WITHOUT WAL mode. If CostManager is concurrently writing (track()), BudgetGuard's read can fail with 'database is locked'. The try/except silently returns 0.0, making a cost check return 0 when the real cost might be non-zero, potentially bypassing daily/monthly budget limits.
  Fix: undefined

- **monthly_usd limit is never checked in check()** (`relayos/core/budget.py`) — The check() method only checks per_task_usd (confirm) and daily_usd (block). The monthly_usd limit is defined and available in get_monthly_spend() and get_status(), but is never enforced in the pre-execution guard. A user could blow through their monthly budget in a single day without any warning.
  Fix: undefined

- **_LANG global is not thread-safe** (`relayos/i18n.py`) — _LANG is a module-level global modified by set_lang() without a lock. The i18n module is likely to be called from multiple threads (logging, async adapter calls). A race on set_lang() could cause t() to read a half-written _LANG value, returning translations from the wrong language or raising an AttributeError.
  Fix: undefined

- **CLIProvider referenced via fragile __import__() hack instead of top-level import** (`relayos/providers/router.py`) — Line 41 uses __import__('relayos.providers', fromlist=['CLIProvider']).CLIProvider instead of importing CLIProvider at the top. This is fragile (no type checker catches breakage), and it's only used inside dead code anyway (the empty-enabled-list fallback block). If the dead code were fixed, this import would need to change as well.
  Fix: undefined

- **API keys written to config file in plaintext without permission check** (`relayos/cli/wizard.py`) — Line 106 writes api_key: '...' into the YAML config file. There's no permission setting (config file is world-readable by default on Unix). If the key is already in an environment variable (check on line 66), it's still written to the plaintext file. There's no option to use env-var-only mode or any encryption/warning.
  Fix: undefined

- **wizard crashes with PermissionError if config_dir is not writable** (`relayos/cli/wizard.py`) — Line 124 calls config_path.write_text() with no try/except. If ~/.relayos/ cannot be written (permissions, disk full, filesystem errors), the wizard crashes rather than displaying a user-friendly error. The config_dir.mkdir() on line 34 has parents=True but also lacks error handling.
  Fix: undefined

- **import os inside for loop is unconventional** (`relayos/cli/wizard.py`) — Line 64 does 'import os' inside the for-loop body. While functionally correct (Python caches imports), it's unconventional and should be at the top of the file.
  Fix: undefined

- **select_provider returns provider not in available list when none match** (`relayos/cost.py`) — Lines 148-152: If available_providers is given but none of the policy-ordered providers appear in it, the function returns order[0] anyway — which is NOT guaranteed to be in available_providers. The caller could get back a provider it didn't list as available, causing an error when attempting to use it.
  Fix: undefined
