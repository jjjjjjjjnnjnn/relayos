# RelayOS 综合审核报告

> 审核日期：2026-06-25
> 审核范围：全项目 56 个 Python 源文件，~15,000 行代码
> 审核维度：架构、代码质量、测试覆盖

---

## 执行摘要

RelayOS 是一个快速迭代中的项目（从 v0.1 到 v0.2.0a20），架构整体方向正确但存在**基础设施碎片化**的积累债务。最关键的三个问题：**9 个 SQLite 数据库**无统一管理、**5 套并行路由系统**各自为政、**~6% 测试覆盖率**。

---

## Part 1: 架构审核

### 严重问题（v1.0 前必须修）

| ID | 发现问题 | 涉及文件 | 影响 |
|----|---------|---------|------|
| A-1 | **9 个独立 SQLite 数据库** — sessions/state/memory/knowledge/inbox/identity/cost/terminals/artifacts 各一个文件，无交叉查询 | 所有 `*Store`/`*Manager` | 无事务一致性、重复数据（messages 在 2 个库）、迁移需改 9 处 |
| A-2 | **5 套并行路由系统** — FlowRouter / ModelScheduler / ProviderRouter / CostManager.select / best_terminal 都在做同一件事 | `core/router.py`, `core/scheduler.py`, `providers/router.py`, `cost.py`, `terminals/scheduler.py` | 路由结果不一致，同一请求在不同入口会选不同模型 |

### 高优先级问题

| ID | 发现问题 | 涉及文件 |
|----|---------|---------|
| A-3 | `core/` 包有 21 个文件，沦为"垃圾桶"包，无 `__all__` | `core/__init__.py` |
| A-4 | `providers/` 和 `adapters/` 功能严重重叠 — 两套抽象解决同一个问题 | `providers/__init__.py`, `adapters/base.py` |
| A-5 | 无统一公共 API — `cli/main.py` 直接调用 8 个底层存储类 | `cli/main.py` (1027 行) |
| A-6 | WorkerManager 和 TerminalPool 概念重叠，互不关联 | `core/worker.py`, `orchestrator/pool.py` |
| A-7 | `core/` 反向依赖 `terminals/` — 设计分层违反 | `core/planner.py` -> `terminals/scheduler.py` |

### 中度问题

| ID | 发现问题 | 涉及文件 |
|----|---------|---------|
| A-8 | 三种注册表模式（`_REGISTRY` 私有/`REGISTRY` 公开/硬编码 PROVIDERS） | `adapters/`, `terminals/`, `core/provider_registry.py` |
| A-9 | `executor/` 包为存根 | `executor/mco.py` |
| A-10 | JSON-in-column 反模式（participants, constraints） | `core/session.py`, `core/state.py` |
| A-11 | 迁移策略临时性，无统一迁移框架 | `core/session.py:137-153` |
| A-12 | `conversation.py` 作为中心枢纽有 7 个内部导入 | `core/conversation.py` |

---

## Part 2: 代码质量审核

### 严重问题

| ID | 发现问题 | 位置 |
|----|---------|------|
| C-1 | **API 密钥以明文存储在 YAML 配置**中 — 向导写入明文 key，resolve_api_key 优先读配置而非环境变量 | `cli/wizard.py:105`, `config.py:59-66` |
| C-2 | **硬编码 CLI 命令参数重复** — `CLIProvider` 的 `typed_cmds` 与 `terminals/adapters.py` 的 `build_command()` 不一致，opencode 参数分歧 | `providers/__init__.py:126-139`, `terminals/adapters.py:38` |

### 高优先级问题

| ID | 发现问题 | 位置 |
|----|---------|------|
| C-3 | **静默吞异常** — 整个项目 15+ 处 bare except: pass | `tui/app.py` 多处, `core/session.py:152`, `server/api.py:161` |
| C-4 | **数据库连接不一致** — 部分方法用 `self._conn` 线程缓存，部分每次新建 `sqlite3.connect()` | `core/session.py:93,165,221,284` |
| C-5 | **`i18n.py` 跨线程竞态** — `t()` 在锁外读取字符串字典 | `i18n.py:8-9` |
| C-6 | **`TerminalPool.run()` 锁范围不足** — 锁内获取适配器、锁外执行 | `orchestrator/pool.py:164-190` |
| C-7 | **`MemoryStore.search()` LIKE 注入** — 未转义 % 和 _ | `memory/store.py:111-117` |
| C-8 | **submit() 内递归 import** — 每次对话都 import 模块 | `tui/app.py:287` |
| C-9 | **`_getch()` 空闲 CPU 旋转** — 30ms sleep 忙等 | `tui/app.py:35-93` |

---

## Part 3: 测试覆盖审核

### 现状

- 测试文件：**3 个**（test_capabilities.py、test_compress.py、test_team_schemas.py）
- 测试用例：**35 个**（全部通过）
- 覆盖模块：~4 个（共 56 个模块）
- **覆盖率：~6%**

### 零覆盖的高风险模块

| 风险级别 | 模块 | 行数 | 风险原因 |
|---------|------|------|---------|
| 🔴 **严重** | `core/session.py` | 459 | SQLite 持久化核心 — 数据丢失风险 |
| 🔴 **严重** | `core/planner.py` | 322 | 任务分解 DAG 引擎 — 依赖排序 |
| 🔴 **严重** | `core/conversation.py` | 234 | 整合 Router + Store + Worker — 最复杂编排 |
| 🔴 **严重** | `core/scheduler.py` | 203 | 模型路由 — 选错模型=烧钱 |
| 🔴 **严重** | `core/worker.py` | 240 | Worker CRUD — 所有 CLI 命令依赖 |
| 🔴 **严重** | `core/state.py` | 343 | 5 表事件溯源 — 数据损坏全挂 |
| 🟡 **高** | `core/budget.py` | 142 | 花钱的限额没测试 |
| 🟡 **高** | `core/knowledge.py` | 328 | 知识丢失静默降低 AI 质量 |
| 🟡 **高** | `core/router.py` | 151 | 正则模式匹配 — 没测试真实输入 |

---

## 建议修复优先级（按 Sprint 排序）

### Sprint 1：重建基础设施

1. 合并 9 个 SQLite 数据库 → 2 个
2. 合并 5 套路由 → 1 个 RoutingService
3. 为 `core/` 添加 `__all__`

### Sprint 2：修安全债

4. 向导停止写明文 API key → 只读环境变量
5. 统一 CLIProvider 命令生成与终端适配器
6. 修复所有 bare except

### Sprint 3：加测试

7. 新增测试文件：`test_session.py`, `test_scheduler.py`, `test_router.py`, `test_budget.py`
8. 新增测试：`test_planner.py`, `test_conversation.py`, `test_state.py`

---

## 积极观察

尽管有上述问题，项目在几个方面表现良好：

- ✅ 所有文件使用 `from __future__ import annotations`
- ✅ SQL 查询一致使用参数化（`?` 占位符）
- ✅ WAL 模式贯穿所有数据库
- ✅ 线程局部连接模式正确
- ✅ 类型注解覆盖所有函数签名
- ✅ 存储模式（Store 类）结构清晰
