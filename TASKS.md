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
> ⚠️ Superseded by TASK-016 (rung 2, `NetworkPolicy`) if ADR-007 is accepted.

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
> ⚠️ Superseded by TASK-012 (evidence manifest) if ADR-007 is accepted.

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
> ⚠️ Superseded by TASK-015 (signed approval) if ADR-007 is accepted.

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

### 🛰️ Hunt track — blocked until ADR-007 is accepted

> These tasks come from ADR-007 (on-demand hunting on Kubernetes). They map
> to the specification's provisional IDs TASK-002 to TASK-012. None of them
> starts until ADR-007 moves to `accepted`, and they never interrupt the
> current task. Milestones and efforts are provisional. Order follows the
> specification: first what makes the tool safe (session, evidence,
> signature), then what makes it powerful (irreversible actuators).

### [TASK-011] HuntSession: scope, TTL, mode and state machine
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** high
- **Effort:** M
- **Depends on:** ADR-007 accepted
- **Description:** model a `HuntSession` with explicit scope, TTL and mode,
  and its lifecycle `Triggered → Preparing → Observing → Proposal →
  Containing → Verifying → Closed`, with abort from any state. Rename the
  `monitor` mode to `observe`.
- **Acceptance criteria:**
  - [ ] Invalid transitions are rejected; `Closed` is final and never
        reopens.
  - [ ] The TTL closes the session automatically and never interrupts an
        action in progress.
  - [ ] Sessions opened by a tripwire can only be `observe`.
  - [ ] `observe` is the default mode; `monitor` is renamed everywhere.
  - [ ] Unit tests for every transition, TTL expiry and abort.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`,
  `docs/decisions.md` (ADR-005 note).

### [TASK-012] Evidence manifest with hash chain
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** high
- **Effort:** M
- **Depends on:** TASK-011
- **Description:** append-only evidence directory per session
  (`evidence/hs-<session_id>/`) with hash-chained events and a sealed
  SHA-256 `manifest.json`.
- **Acceptance criteria:**
  - [ ] Each event includes the hash of the previous one.
  - [ ] Altering or deleting an intermediate event breaks verification.
  - [ ] A failed sensor is recorded as `UNAVAILABLE`, never as "no
        activity".
  - [ ] Secret values are never written, only fingerprints.
  - [ ] Tests for sealing, verification and tampering detection.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-013] CCHIA assessment ingestion and validation
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** medium
- **Effort:** M
- **Depends on:** TASK-011
- **Description:** add the CCHIA Security Compiler as a git submodule
  pinned to a commit, run it as a subprocess before and after each hunt,
  and ingest its `assessment.json`.
- **Acceptance criteria:**
  - [ ] Submodule pinned to a commit; its `LICENSE` and `NOTICE.md` are
        kept.
  - [ ] Every run uses a fresh `--output` directory under
        `evidence/.../cchia/before` or `after`.
  - [ ] `assessment.json` is validated against CCHIA's JSON Schemas.
  - [ ] `NOT_ASSESSED`, `UNAVAILABLE` and `ERROR` are treated as "no
        evidence".
  - [ ] CCHIA code is excluded from ruff and mypy.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`,
  `NOTICE`.

### [TASK-014] Ephemeral container with sensors in a target pod
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** medium
- **Effort:** M
- **Depends on:** TASK-011
- **Description:** attach a minimal sensor container to the target pod via
  `pods/ephemeralcontainers`, without restarting it, emitting events to the
  control plane.
- **Acceptance criteria:**
  - [ ] Distroless-style image without shell, pinned by digest.
  - [ ] Shares the process namespace with the agent container when the
        runtime supports it.
  - [ ] Carries no model and has no Kubernetes API permissions.
  - [ ] Integration test on kind or k3d.
- **Documents to update:** `CHANGELOG.md`, `docs/deployment.md`.

### [TASK-015] Signed approval via CLI and verifier
- **Type:** security
- **Milestone:** TBD (hunt track)
- **Priority:** high
- **Effort:** M
- **Depends on:** TASK-012
- **Description:** `bladerunner approve` signs a canonical (RFC 8785)
  payload with `ssh-keygen -Y sign` (namespace `bladerunner-approval`); the
  controller verifies it right before executing.
- **Acceptance criteria:**
  - [ ] Verification checks signer and role in `allowed_signers`, unused
        nonce, expiry, current target UID, evidence manifest hash, and
        session scope/TTL.
  - [ ] Any failure blocks the action and is logged as evidence.
  - [ ] Tests for replay, expired approval, recreated pod (UID change) and
        unknown signer.
  - [ ] Final CLI command names fixed and documented.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`,
  `SECURITY.md`.

### [TASK-016] Rung 1–2 actuators (suspend, isolate network)
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** medium
- **Effort:** M
- **Depends on:** TASK-014, TASK-015
- **Description:** reversible containment: suspend the agent's processes
  and isolate the pod with a `NetworkPolicy`.
- **Acceptance criteria:**
  - [ ] Both actions have an idempotent revert.
  - [ ] Pre-action evidence (process snapshot, active connections) is
        captured first.
  - [ ] GitOps reconcilers are paused and verification confirms the
        containment held.
  - [ ] In `observe`, both remain proposals.
  - [ ] Integration test on kind or k3d with Calico.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-017] Inference service and hunter JSON contract
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** medium
- **Effort:** L
- **Depends on:** TASK-012
- **Description:** in-cluster inference service that scales to zero, a
  normalizer that turns evidence into typed windows, and strict validation
  of the hunter's JSON output.
- **Acceptance criteria:**
  - [ ] Outputs with missing or out-of-domain fields are discarded.
  - [ ] `evidence_refs` must exist in the manifest.
  - [ ] Free text from the agent enters only quoted, truncated and marked
        as untrusted; text aimed at the analyzer raises suspicion.
  - [ ] Only the controller can reach the service (`NetworkPolicy`), with
        no egress.
  - [ ] Server choice (vLLM or Ollama) recorded with its benchmark.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`,
  `docs/decisions.md`.

### [TASK-018] Rung 3–4 actuators (revoke, terminate)
- **Type:** security
- **Milestone:** TBD (hunt track)
- **Priority:** medium
- **Effort:** L
- **Depends on:** TASK-015, TASK-016
- **Description:** irreversible containment, executed only with a verified
  signature: revoke credentials and access, then terminate.
- **Acceptance criteria:**
  - [ ] Revoke covers Secrets, RoleBindings, workload identity and scaling
        to zero, using the CCHIA credential inventory.
  - [ ] Terminate requires the managed workload to be at zero replicas.
  - [ ] Requires corroboration by a deterministic or ML detector.
  - [ ] Executes exactly the signed action on the signed UID.
  - [ ] Integration tests on kind or k3d.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-019] Per-session node agent for network visibility
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** medium
- **Effort:** M
- **Depends on:** TASK-001, TASK-014
- **Description:** privileged pod pinned to the target's node, created when
  the session opens and removed when it closes, feeding the network sensor.
- **Acceptance criteria:**
  - [ ] Not a permanent DaemonSet; exists only during the session.
  - [ ] Minimal signed image, no shell, no egress.
  - [ ] Removal verified when the session closes or aborts.
- **Documents to update:** `CHANGELOG.md`, `docs/deployment.md`.

### [TASK-020] Tripwires: honeytokens and trigger webhook
- **Type:** feature
- **Milestone:** TBD (hunt track)
- **Priority:** low
- **Effort:** M
- **Depends on:** TASK-011
- **Description:** honeytokens and an authenticated webhook that open
  hunting sessions.
- **Acceptance criteria:**
  - [ ] A tripwire only opens sessions in `observe`.
  - [ ] The trigger source is recorded in `session.json`.
  - [ ] Tests for honeytoken use and webhook authentication.
- **Documents to update:** `CHANGELOG.md`, `docs/architecture.md`.

### [TASK-021] Scenario simulator and QLoRA pipeline (Phase 2)
- **Type:** feature
- **Milestone:** TBD (Phase 2)
- **Priority:** low
- **Effort:** L
- **Depends on:** TASK-017
- **Description:** isolated local arena (k3d or kind) with scripted benign
  and rogue behaviors, labeled dataset, QLoRA fine-tuning of the hunter and
  acceptance gates. Uses `.ai/framework.md` and `.ai/TRAINING.md`.
- **Acceptance criteria:**
  - [ ] Arena without internet access and with fake credentials only.
  - [ ] Dataset split by scenario family and pinned by hash.
  - [ ] Acceptance gates implemented; thresholds set after the first round.
  - [ ] Model card with base version, dataset hash and metrics.
- **Documents to update:** `CHANGELOG.md`, `docs/training.md`.

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
