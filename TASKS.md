# TASKS.md — Bladerunner live backlog

> **Instructions for the AI agent:** this is your backlog. At the start of
> each session, find the **"🎯 Current task"** section and work on it. When
> you finish it, move it to **"✅ Completed"** and promote the next one from
> **"📋 Pending"** to **"🎯 Current task"**.
>
> Format for each task:
> ```
> ### [TASK-NNN] Short title
> - **Type:** feature | bugfix | docs | refactor | test | chore | security
> - **Milestone:** v0.2 | v0.3 | ...
> - **Priority:** high | medium | low
> - **Effort:** S (hours) | M (days) | L (weeks)
> - **Depends on:** [TASK-XXX] (optional)
> - **Description:** what needs to be done.
> - **Acceptance criteria:** a verifiable list.
> - **Documents to update:** CHANGELOG.md, docs/X.md, etc.
> ```

---

## 🎯 Current task

### [TASK-001] Network sensor (network_sensor.py)
- **Type:** feature
- **Milestone:** v0.2
- **Priority:** high
- **Effort:** M
- **Depends on:** —
- **Description:** create `src/bladerunner/sensors/network_sensor.py` to
  monitor a process's outbound network connections and emit `Event`s with
  visited domains/IPs, ports, and traffic volume.
- **Acceptance criteria:**
  - [ ] File created at the correct path.
  - [ ] Inherits from `BaseSensor`.
  - [ ] Has `name = "network_sensor"`.
  - [ ] Emits events with `kind=EventKind.NETWORK`.
  - [ ] Unit test in `tests/test_network_sensor.py` with at least 3 cases.
  - [ ] Registered in `cli.py::watch` as a `--network` option.
  - [ ] Documented in `docs/architecture.md`.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`, `TASKS.md`.

---

## 📋 Pending (ordered by priority)

### [TASK-002] Isolation actuator (isolation_actuator.py)
- **Type:** feature
- **Milestone:** v0.2
- **Priority:** high
- **Effort:** M
- **Depends on:** TASK-001
- **Description:** create `src/bladerunner/actuators/isolation_actuator.py`
  to isolate a process by blocking its outbound traffic via `iptables`
  (Linux) or `pfctl` (macOS). Must be reversible.
- **Acceptance criteria:**
  - [ ] Inherits from `BaseActuator`.
  - [ ] Implements `execute()` and `revert()` (idempotent).
  - [ ] Detects the OS and uses the correct tool.
  - [ ] Safe fallback if there are no permissions.
  - [ ] Unit test with a subprocess mock.
  - [ ] Documented in `docs/plugins.md` as an advanced example.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-003] SQLite persistence
- **Type:** feature
- **Milestone:** v0.2
- **Priority:** medium
- **Effort:** M
- **Depends on:** —
- **Description:** add a persistence layer with SQLite for events,
  verdicts, and actions. Use SQLModel or SQLAlchemy.
- **Acceptance criteria:**
  - [ ] Module `src/bladerunner/core/storage.py`.
  - [ ] Tables: `events`, `verdicts`, `actions`.
  - [ ] The orchestrator persists every action executed.
  - [ ] Integration tests with in-memory SQLite.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-004] Complete REST API
- **Type:** feature
- **Milestone:** v0.2
- **Priority:** medium
- **Effort:** M
- **Depends on:** TASK-003
- **Description:** extend `src/bladerunner/api/main.py` with endpoints:
  `GET /events`, `GET /verdicts`, `GET /actions`, `GET /stats`,
  `POST /agents/{id}/kill`, `POST /agents/{id}/isolate`.
- **Acceptance criteria:**
  - [ ] Endpoints implemented with Pydantic models.
  - [ ] Automatic documentation at `/docs`.
  - [ ] Integration tests with TestClient.
  - [ ] Update `docs/api_reference.md`.
- **Documents to update:** `CHANGELOG.md`, `docs/api_reference.md`.

### [TASK-005] ML detector — Random Forest
- **Type:** feature
- **Milestone:** v0.3
- **Priority:** medium
- **Effort:** L
- **Depends on:** —
- **Description:** implement `src/bladerunner/detectors/ml.py` with a
  `RandomForestDetector` that loads a trained model and evaluates events.
- **Acceptance criteria:**
  - [ ] `RandomForestDetector(BaseDetector)` class.
  - [ ] Loads the model in `__init__`, not in `evaluate`.
  - [ ] Unit test with a dummy model.
  - [ ] Script `scripts/train_baseline.py` that trains on NSL-KDD.
  - [ ] Documented in `docs/training.md`.
- **Documents to update:** `CHANGELOG.md`, `docs/training.md`.

### [TASK-006] Minimal web dashboard (HTMX)
- **Type:** feature
- **Milestone:** v0.2
- **Priority:** low
- **Effort:** M
- **Depends on:** TASK-004
- **Description:** create a simple web dashboard with HTMX + Jinja2 showing
  events, verdicts, and actions in real time.
- **Acceptance criteria:**
  - [ ] `/dashboard` route in FastAPI.
  - [ ] Auto-refreshing table every 5s.
  - [ ] No heavy JS dependencies.
- **Documents to update:** `CHANGELOG.md`, `README.md`.

### [TASK-007] Human in the loop (approval webhook)
- **Type:** feature
- **Milestone:** v0.2
- **Priority:** medium
- **Effort:** M
- **Depends on:** TASK-002
- **Description:** add an `approval` mode where destructive actions
  (ISOLATE, KILL) require manual approval via webhook.
- **Acceptance criteria:**
  - [ ] New `approval` mode in `Orchestrator`.
  - [ ] Sends a webhook with the proposed action's payload.
  - [ ] Waits for a response with a configurable timeout.
  - [ ] Documented in `docs/architecture.md`.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-008] Test coverage >80%
- **Type:** test
- **Milestone:** v0.2
- **Priority:** high
- **Effort:** M
- **Depends on:** —
- **Description:** add the missing tests to reach the target coverage
  defined in `docs/testing.md`.
- **Acceptance criteria:**
  - [ ] `pytest --cov=src/bladerunner` reports >80% overall.
  - [ ] `core/` >90%, `detectors/` >85%, `sensors/` >80%.
  - [ ] CI blocks PRs that lower coverage.
- **Documents to update:** `CHANGELOG.md`.

### [TASK-009] Advanced examples documentation
- **Type:** docs
- **Milestone:** v0.2
- **Priority:** low
- **Effort:** S
- **Depends on:** —
- **Description:** add `examples/` with real-world use cases: monitoring a
  Discord bot, containing a scraping script, monitoring an LLM agent with
  LangChain.
- **Acceptance criteria:**
  - [ ] 3 working examples in `examples/`.
  - [ ] Each one with its own README.
  - [ ] Documented in `README.md`.
- **Documents to update:** `README.md`, `CHANGELOG.md`.

### [TASK-010] Internal security audit
- **Type:** security
- **Milestone:** v0.2
- **Priority:** high
- **Effort:** M
- **Depends on:** —
- **Description:** review every command-execution point (`subprocess`,
  `os.system`) and ensure there is no possible injection.
- **Acceptance criteria:**
  - [ ] List of execution points in `docs/security_review.md`.
  - [ ] All of them use list-style arguments, not strings.
  - [ ] No `shell=True` without explicit justification.
  - [ ] Add a regression test for each critical point.
- **Documents to update:** `docs/security_review.md` (new), `CHANGELOG.md`.

---

## ✅ Completed

(empty for now)

---

## 🚫 Discarded / Blocked

(empty for now)

---

## 📝 How to update this file

1. When finishing the "Current task":
   - Move it to "✅ Completed" with the completion date.
   - Mark all its acceptance criteria with `[x]`.
2. Promote the next task from "📋 Pending" to "🎯 Current task".
3. If a new task comes up during development, add it to "📋 Pending" using
   the standard format.
4. If a task gets blocked, move it to "🚫 Discarded / Blocked" with the
   reason.

## 🔄 Golden rule

**Never work on two tasks at once.** Finish, verify, document, close, and
only then move on to the next one.
