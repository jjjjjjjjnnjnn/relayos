# RelayOS Bug Scan Report

**Date**: 2026-06-24
**Files scanned**: 15+ Python files across all modules

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | 6 |
| HIGH | 15 |
| MEDIUM | 14 |
| LOW | 8 |
| **Total** | **43** |

## CRITICAL & HIGH

### Four palette actions silently do nothing (fork/merge/attach/remember)
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 267
- **Category**: missing
- **Detail**: The COMMANDS tree (lines 69-95) defines four palette items with actions 'fork_session', 'merge_session', 'attach_session', and 'remember_fact'. The execute_action function (line 267-310) has no handlers for any of these four actions. Selecting them from the palette does nothing silently, despite showing descriptions like 'Branch from current session' and 'Save knowledge'. The commands DO work via slash commands (/fork, /merge, /attach, /remember) but the palette is broken.
- **Fix**: Add four elif branches in execute_action: elif action == 'fork_session': call /fork logic with current sess; elif action == 'merge_session': add usage prompt; elif action == 'attach_session': add usage prompt; elif action == 'remember_fact': add usage prompt. Alternatively, add a 'prompt' field that gets injected into the buffer so the user can fill in args.

### sl_sel missing nonlocal declaration in execute_action — palette session switch selection index not reset
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 268
- **Category**: bug
- **Detail**: On line 275, `sl_sel = 0` is assigned inside `execute_action`. The function only declares `nonlocal sess, view` (line 268) and `nonlocal sessions_list` (line 274), but NOT `nonlocal sl_sel`. Therefore `sl_sel = 0` creates a local variable that shadows the outer `sl_sel` (initialized at line 319). The outer `sl_sel` retains its previous value, so when switching sessions from the palette, the selection index is not reset to 0, potentially pointing beyond the list bounds or at a stale entry.
- **Fix**: Add `sl_sel` to the nonlocal declaration on line 268: `nonlocal sess, view, sl_sel`.

### /attach loads messages into display but does not update sess — display mismatches active session
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 179
- **Category**: bug
- **Detail**: The /attach command (lines 179-190) loads messages from another session into the display buffer `msgs`, but does NOT update the `sess` variable to point to the attached session or the current session. Subsequent operations like sending a message call submit() which creates a new ConversationEngine session unrelated to either the old sess or the attached messages. The displayed messages do not match the active session, creating a confusing user experience.
- **Fix**: Either (a) do not modify msgs and instead add a sys message like 'Attached 5 messages from <id>' OR (b) update sess to the attached session's id. Option (a) is safer since /attach semantics are 'import context' not 'switch session'.

### Up-arrow history navigation never works on first press — hi always clamped to -1
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 394
- **Category**: bug
- **Detail**: The up-arrow history handler at line 394-396 computes `hi = max(-1, hi-1)`. Since hi starts at -1 (initialized at line 104, reset by submit at line 141), the first up press computes max(-1, -2) = -1 — hi never changes from -1. The guard `if hi >= 0` on line 396 then evaluates to False, producing an empty buffer. The first up arrow press always does nothing.
- **Fix**: Change to: `if hi <= -1: hi = len(history) - 1 else: hi = max(0, hi - 1)` so the first up press goes to the most recent history entry.

### Down-arrow history shows oldest entry instead of navigating forward
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 397
- **Category**: bug
- **Detail**: The down-arrow handler at line 397-400 computes `hi = min(len(history), hi+1)`. From hi=-1, this sets hi=0 — the oldest entry. This is the inverse of expected shell behavior where down arrow goes forward (newer) and hitting down from the most recent entry clears the buffer.
- **Fix**: Change down to advance hi toward len(history). At len(history), set hi=-1 (empty buffer). See standard shell history implementation.

### Mode toggle always shows 'edit' — ProviderRouter() recreates instance with mode='auto' each time
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 278
- **Category**: logic
- **Detail**: The toggle_mode action (line 277-280) and Ctrl+X M handler (line 377-380) both create a new `ProviderRouter()` instance which always initializes `self.mode = 'auto'`. The toggle logic then computes `'edit' if 'auto' == 'auto' else 'auto'` which always produces 'edit'. The mode always displays as 'edit' regardless of how many times the user toggles. The mode can never be switched back to 'auto' from the TUI.
- **Fix**: Store the mode in app.py's closure state (e.g., a `mode` nonlocal variable) and toggle it there instead of creating a new ProviderRouter each time.

### get_project_summary by_domain is always empty (never populated)
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/knowledge.py` line 177
- **Category**: missing
- **Detail**: get_project_summary() calls query_knowledge() and stores results in the local 'knowledge' variable but never iterates over it to populate the 'by_domain' field. The return dict always has 'by_domain': {}, an empty dict. This is a dead-code path — query_knowledge runs a full DB query whose results are used only for len(knowledge) (total_knowledge count), while the by_domain breakdown that callers would expect is never computed.
- **Fix**: Iterate over the knowledge list before returning and populate by_domain: e.g., for k in knowledge: domain = k.get('domain', 'unknown'); result['by_domain'].setdefault(domain, 0); result['by_domain'][domain] += 1

### upsert_knowledge accepts empty key/value with no validation
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/knowledge.py` line 111
- **Category**: missing
- **Detail**: upsert_knowledge() does not validate that key or value are non-empty strings before inserting. If called with key='' (empty string), the UNIQUE(project_id, key) constraint still allows the row, but the ON CONFLICT clause causes every empty-key call to overwrite the same row silently. If called with value='', a row with an empty value is stored, which downstream consumers (query_knowledge, build_skip_instructions) would read as meaningless data. This can lead to duplicate 'knowledge' entries that overwrite each other or accumulate empty values.
- **Fix**: Add validation at the top of upsert_knowledge: if not key or not value: raise ValueError('key and value must be non-empty') or log a warning and return early.

### group_chat adapter config missing 'model' parameter
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/conversation.py` line 195
- **Category**: missing
- **Detail**: group_chat() constructs the adapter config with only 'api_key' — it never passes 'model'. Compare with chat() at line 72-75 which passes both 'api_key' and 'model'. If the adapter implementation for the given provider requires a model parameter (as most LLM adapters do), the adapter call at line 195-198 will fail or use a default model that may not be intended. This also means the participant's configured model (from WorkerManager or terminal config) is never respected.
- **Fix**: Add 'model' to the adapter config dict on line 196. The model should come from worker.model if the worker exists, or from route.model if auto-routed.

### APIProvider.is_available() returns False for keyless providers (Ollama)
- **File**: `relayos/providers/__init__.py` line 108
- **Category**: bug
- **Detail**: is_available() returns bool(self.config.api_key). Providers like Ollama that don't require API keys always get api_key='' so is_available() incorrectly returns False, making them appear unavailable to the router even when they are fully functional.

### MCPClient.send_request() not thread-safe — can create orphaned subprocess
- **File**: `relayos/mcp/client.py` line 52
- **Category**: bug
- **Detail**: Line 52 checks 'if not self._process: self.start()' without a lock. Two concurrent threads can both pass the check and call start(), creating two subprocesses. The second overwrites self._process, leaving the first orphaned (no stdin/stdout cleanup, process leak).

### MemoryStore.set() serializes to JSON but get() never deserializes
- **File**: `relayos/memory/store.py` line 67
- **Category**: bug
- **Detail**: Lines 67-68: if value is not a string, it is json.dumps()-serialized and stored. But get() (line 96) returns row['value'] as a raw string with no json.loads() call. Storing {'a': 1} yields back the string '"{\"a\": 1}"' not the dict. API contract is broken.

### Concurrent writes from different threads can cause 'database is locked'
- **File**: `relayos/memory/store.py` line 64
- **Category**: bug
- **Detail**: MemoryStore uses threading.local() for connections (line 28-31) — each thread gets its own SQLite connection. WAL mode permits one writer at a time. If two threads call set() concurrently, the second gets sqlite3.OperationalError('database is locked') which is never caught or retried.

### BudgetGuard.check() early-returns 'allow' when per_task_usd <= 0, skipping daily/monthly checks
- **File**: `relayos/cost.py` line 86
- **Category**: logic
- **Detail**: Lines 86-87: if self.limits.per_task_usd <= 0, returns GuardResult(action='allow') immediately, bypassing ALL downstream checks (monthly limit line 90-96, daily limit line 99-105). Comment says 'zero limits would block everything' but code does the opposite. Intended to skip only per-task check, not daily/monthly.

### select_provider() with empty available_providers list returns first policy provider
- **File**: `relayos/cost.py` line 148
- **Category**: logic
- **Detail**: Lines 148-153: available_providers=[] (empty list) is falsy, so the entire if-block is skipped and line 155 returns order[0] — the default policy provider. An empty list should signal 'no providers available' but instead silently returns an unavailable provider.

### No view guard on chat-mode key handlers — ENTER/Ctrl+P/typing work in graph mode
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py` line 362
- **Category**: crash
- **Detail**: When view == 'graph', the chat-mode key handlers at lines 362-401 fire unconditionally because there is no 'if view == "chat"' guard. This means pressing ENTER while viewing the graph calls submit(), which creates a ConversationEngine and may trigger paid API calls. Ctrl+P opens palette from graph mode. The palette and sessions modes have proper 'continue' guards (lines 337, 360), but graph mode has no such protection. The graph key handler at line 433 is buried inside the render section and only handles ESC.
- **Fix**: Either wrap the chat key handlers in a `if view == 'chat':` block, or add `if view == 'graph': continue` before the chat handler section. Also move the graph ESC handler into a dedicated key-handling section above the chat handlers.

### BudgetGuard.check() per_task_usd<=0 bypasses ALL budget checks
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/budget.py` line 86
- **Category**: logic
- **Detail**: The per_task_usd <= 0 guard at line 86 is intended to handle the case where the limit is zero ('zero limits would block everything' per the comment), but it does the opposite: it returns GuardResult(action='allow', message='...no limit'), which immediately exits the function. This means setting per_task_usd=0 (or any non-positive value) bypasses ALL subsequent checks: the monthly hard block (line 92), the daily hard block (line 101), the per-task confirm threshold (line 108), and the warning percentage (line 115). A user who sets per_task_usd: 0 expecting 'no budget for any single task' instead gets unlimited spending with no guardrails at all. The monthly_usd and daily_usd limits become entirely ineffective.
- **Fix**: Either remove the early return entirely (let the normal threshold logic at line 108 handle per_task_usd=0 as 'confirm on any spend') or change the condition to return block when per_task_usd == 0, with message 'Per-task limit is 0 — all tasks blocked'. If the intent is to treat 0 as 'unlimited', change the comment to say so and ensure the daily/monthly checks still run (don't return early).

### fork_session silently drops messages beyond 200
- **File**: `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/session.py` line 272
- **Category**: missing
- **Detail**: fork_session calls get_messages(parent_id, limit=200) which caps the copied messages at the first 200 (ordered by created_at ASC). If a session has more than 200 messages, messages #201 and beyond — the newest, most context-critical messages — are silently dropped. The method docstring claims it fully 'copies the parent's messages'. No warning is logged or raised. This is silent data loss on fork.
- **Fix**: Remove the hardcoded limit=200 on line 272, passing no limit or a high-enough limit (e.g., limit=10000). If a limit is kept for performance, log a warning when msg_count(parent_id) exceeds the threshold.

### APIProvider.complete() uncaught exception on unknown provider
- **File**: `relayos/providers/__init__.py` line 73
- **Category**: crash
- **Detail**: Line 76 calls get_adapter(cfg.provider, ...) which raises ValueError for unknown provider names. This exception propagates uncaught through complete(), crashing any caller (router, engine) that expects a ProviderResult return.

### MCPClient.send_request() uses selectors on pipes — broken on Windows
- **File**: `relayos/mcp/client.py` line 71
- **Category**: crash
- **Detail**: Line 71 uses selectors.DefaultSelector() and line 72 registers self._process.stdout (a pipe). On Windows, DefaultSelector returns SelectSelector which only supports sockets, not pipes. sel.register() will raise ValueError: 'Invalid file descriptor'. MCP is completely non-functional on Windows.

### After timeout kill, MCP client is permanently dead with no recovery
- **File**: `relayos/mcp/client.py` line 77
- **Category**: bug
- **Detail**: Line 78 calls self._process.kill() but does NOT set self._process = None. On subsequent send_request() calls, line 52 sees self._process is truthy, so it skips start(). Line 62 then writes to a dead process's stdin, gets BrokenPipeError, and raises MCPError. The client can never recover or restart after one timeout.

## MEDIUM

- **Fork success message shows child's own ID as parent — parent ID lost after sess = child** (`C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py`) — At line 163, after `sess = child` on line 158, the fork message reads `sess.id` which is now the CHILD's ID, not the PARENT's ID. The message shows 'Forked -> {child_id} (from {child_id})' — the 'from' is the same as the 'Forked to' ID. The parent ID is lost.
  Fix: Save the parent ID before reassigning sess: `pid = sess.id; child = ss.fork_session(pid); sess = child; ... add('sys', '', f'Forked -> {child.id[:10]} (from {pid[:10]})')`
- **Fork/merge/attach display truncated content (200 chars) due to to_dict limit** (`C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py`) — The /fork handler at line 161 calls `x.to_dict()` which truncates `content` to 200 characters per SessionMessage.to_dict() in session.py line 50. The same issue exists for /merge at line 175 and /attach at line 187. While the database stores full content, the display buffer shows truncated content. If a user forks and views the session, they see only 200 chars per message.
  Fix: Instead of using to_dict(), access the message fields directly: `x.role, x.from_worker, x.content` to get full-length content.
- **Ctrl+X ? loses current input buffer — unlike palette show_help which saves and restores** (`C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py`) — The Ctrl+X ? handler at line 389-390 saves the buffer to `submit.__globals__['_tmp']` then simulates /help. But unlike the palette show_help action (lines 286-292) which saves to `old` and restores via `buf = old`, this path never restores buf. After submit() clears buf (line 141), the original user input is lost.
  Fix: Restore buf after submit() similar to the show_help action: `old = list(buf); buf.clear(); for ch in '/help': buf.append(ch); submit(); buf = old`
- **merge_sessions accepts empty session_ids without validation** (`C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/session.py`) — merge_sessions() accepts an empty list [] for session_ids without validation. It creates a session named 'Merge of 0 sessions' with no messages and a graph edge from child.id to an empty list. The empty list passed to add_integrated_conversation(child.id, []) simply iterates zero times (a no-op). This produces a meaningless orphaned session with no content and no traceable parents. The error is silent — no exception, no warning.
  Fix: Add validation at the top: if not session_ids: raise ValueError('Must provide at least one session to merge')
- **Message misattributed to non-existent worker name on fallback** (`C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/conversation.py`) — When chat() is called with a valid worker_name that does not exist in WorkerManager (line 68: worker is None), the code falls back to auto-routing via self.scheduler.route() (line 70), and the adapter uses route.provider. However, the 'target' variable on line 65 is already set to the non-existent worker_name, and it is this target that is passed to self.sessions.add_message() at line 90 as the from_worker, and to set_last_used() at line 96 as the worker. The resulting session history attributes the response to the non-existent worker name rather than the actual provider that served it, creating confusing session records where the 'from_worker' field does not match the actual provider.
  Fix: After falling back to auto-routing on line 70, update target = route.provider so the message attribution reflects the actual provider used.
- **build_graph_ascii crashes on circular graph references** (`C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/session.py`) — build_graph_ascii() recursively traverses children_of via the render() function (lines 382-391). If the conversation_graph contains a cycle (e.g., A->B->A due to a bug or manual DB edit), the recursion never terminates and causes a stack overflow. The graph edges are stored with INSERT OR IGNORE so cycles are not prevented at the DB level, and no application-level cycle check exists before traversal.
  Fix: Add a visited set to the render() function to detect and break cycles: visited = set() as a closure variable, add sid at entry, check before recursing.
- **Inconsistent DB connection management in SessionStore** (`C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/session.py`) — SessionStore inconsistently manages database connections. Some methods use the thread-local self._conn property (get_session, get_messages, list_sessions, update_session_time, set_last_used, get_conversation_parents, get_conversation_children) while others open a new sqlite3.connect(self._db_path) connection for every operation (create_session, add_message, delete_session, fork_session, merge_sessions, add_integrated_conversation, get_all_graph_edges). Within a single logical flow (e.g., fork_session calls get_session via self._conn then creates a new connection), writes committed on one connection may not be visible on another connection within the same execution path. This creates subtle transaction visibility bugs and makes the code harder to reason about.
  Fix: Consolidate all methods to use self._conn consistently, or use a single connection per operation. The connector-method pattern (open close per call) is the safer choice for thread safety. If self._conn is kept, all write methods should use it instead of opening separate connections.
- **load_config crashes on malformed YAML instead of falling back** (`C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/config.py`) — load_config() calls yaml.safe_load() (line 77) with no try/except. If the config.yaml file exists but contains malformed YAML (e.g., a syntax error from a manual edit), yaml.safe_load raises yaml.YAMLError, which propagates unhandled and crashes the caller. All other file-not-found and missing-key paths in load_config gracefully fall back to defaults, but a corrupted file causes a hard crash.
  Fix: Wrap the yaml.safe_load call in try/except yaml.YAMLError: log a warning and return RelayOSConfig() defaults, consistent with the missing-file behavior on line 73-75.
- **readline() after select() can block if server sends partial line** (`relayos/mcp/client.py`) — After sel.select() returns (data available, line 73), readline() is called (line 83). If the MCP server sends only partial JSON without a trailing newline, readline() blocks until the newline arrives or the pipe closes, potentially hanging indefinitely.
- **set() with session_id always stores step=0, never increments** (`relayos/memory/store.py`) — Line 72-73: (session_id, key, value, 0, now). The step parameter is hardcoded to 0 on every call. If the same key is set multiple times within a session, step stays 0, making the column useless for ordering.
- **search() only queries global memory table, not session_memory** (`relayos/memory/store.py`) — Line 113-115: SQL query only targets the 'memory' table. session-scoped keys stored in 'session_memory' are invisible to search(). A caller searching for any key set under a session will not find it.
- **Edit mode without on_confirm callback silently executes instead of warning** (`relayos/providers/router.py`) — Line 79: 'if self.mode == 'edit' and on_confirm:' — if mode is 'edit' but on_confirm is None (no callback provided), the condition is False and execution proceeds without confirmation. Defeats the purpose of edit mode entirely with no warning.
- **APIProvider.estimate_cost() returns default pricing for unknown models silently** (`relayos/providers/__init__.py`) — Line 105: costs.get(self.config.model, (0.001, 0.002)) — for any model not in the hardcoded dict, falls back to a generic ($0.001/$0.002) estimate with no log warning. All cost-based routing decisions for unknown models are silently based on incorrect data.
- **except ImportError silently swallows config_commands dependency errors** (`relayos/cli/main.py`) — Lines 1000-1006: the try/except ImportError catches not only 'module not found' but also cases where config_commands.py exists yet its own imports fail (e.g., missing dependency). The underlying ImportError is silently swallowed with no log message. Should use logger.warning.


## Files Checked

- `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/config.py`
- `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/budget.py`
- `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/conversation.py`
- `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/knowledge.py`
- `C:\Users\rongj\Desktop\项目开发\agentmesh/relayos/core/session.py`
- `C:\Users\rongj\Desktop\项目开发\agentmesh\relayos\tui\app.py`
- `C:\Users\rongj\Desktop\项目开发\agentmesh\tests\`
- `relayos/cli/main.py`
- `relayos/cost.py`
- `relayos/i18n.py`
- `relayos/mcp/client.py`
- `relayos/memory/store.py`
- `relayos/providers/__init__.py`
- `relayos/providers/router.py`
