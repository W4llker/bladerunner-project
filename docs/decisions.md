# ADRs — Architecture Decision Record log

## Format

- Date, status, context, decision, alternatives, consequences.

## ADR-001: Python 3.10+

Accepted. AI/ML ecosystem, ease of contribution.
Alternatives: Rust, Go, TypeScript.

## ADR-002: FastAPI + Uvicorn

Accepted. Typing with Pydantic, automatic docs, native async.
Alternatives: Flask, Django REST, Litestar.

## ADR-003: Graduated countermeasures

Accepted. Fixed `Severity → ActionKind` mapping.
Alternatives: configurable policies, RL.

## ADR-004: External observation with psutil

Accepted. Works as a black box.
Alternatives: eBPF, APM, instrumentation.

## ADR-005: `monitor` mode by default

Accepted. Secure by default.
Alternatives: enforce by default.

## ADR-006: Apache 2.0

Accepted. Commercial use, patent clause.
Alternatives: MIT, GPL, AGPL.

## ADR-007: Pivot to on-demand hunting, containment and governance on Kubernetes

- **Date:** 2026-10-06
- **Status:** proposed
- **Source:** internal technical specification *"BladeRunner Project — Caza
  bajo demanda, contención y gobernanza de agentes autónomos"* (Spanish,
  2026-10-06). This ADR is its English summary for the repo; the
  specification is the detailed reference.
- **Supersedes, once accepted:** ADR-003 (fixed `Severity → ActionKind`
  mapping) and ADR-004 (psutil as the only observation method). Refines
  ADR-005 (`monitor` by default becomes `observe` by default).

### Context

The v0.1 MVP is a host-level watcher: `ProcessSensor` (psutil) feeds
detectors, and a fixed severity mapping can kill a process in `enforce`
mode. That design does not fit the target environment: autonomous agents
running as containers in a Kubernetes cluster that the organization owns,
where killing a process does not stop an agent whose credentials are still
alive, a Deployment recreates a deleted pod, and GitOps or an HPA can undo a
containment. It also leaves the irreversible actions in the hands of an
automatic mapping, with no signed human approval and no evidence trail.

### Decision

Bladerunner becomes an **incident-response kit for autonomous agents**: it
is deployed on demand, hunts inside an explicit perimeter for a bounded
time, proposes containment, and only executes irreversible actions with a
signed human approval. It is **not** a permanent EDR.

**Non-negotiable principles**

1. The LLM never holds the kill switch: it observes, classifies and
   proposes. A deterministic policy engine decides what is eligible and a
   human signs what is irreversible.
2. Everything observed is data, never an instruction. Logs, outputs,
   prompts and traffic of the suspect agent are treated as hostile content.
3. Bounded by design: every session has an explicit scope, TTL and mode,
   and closes itself when the TTL expires.
4. From reversible to irreversible: containment goes up one rung at a time;
   de-escalating is always available.
5. Fail-closed on evidence: missing data means "no evidence", never "clean".
6. The watcher is watched: hunters can be suspended, and there is an
   emergency shutdown that does not depend on Bladerunner's code.
7. `observe` by default; `enforce` is declared explicitly per session.
8. Only inside the organization's own perimeter; never hack back.

**Scope of v1:** agents running in pods of a Kubernetes cluster owned by
the organization, in namespaces declared as huntable. Sessions are opened
manually by an operator or by a tripwire. Out of scope: continuous
EDR-style monitoring, prevention, any action outside the own perimeter,
autonomous approval of irreversible actions, and third-party SaaS agents.

**Architecture.** A permanent, lightweight control plane (namespace
`bladerunner-system`) with four components: *Sessions* (creates the
`HuntSession`, deploys sensors, enforces the TTL), *Policies*
(deterministic: validates the proposal schema, scope, namespace allow-list
and thresholds, and decides which rung is eligible), *Approvals* (verifies
signatures) and *Evidence* (append-only store with a manifest). Everything
else exists only while a session lasts: an ephemeral container with sensors
attached to the target pod (no restart, no model, no shell), a per-session
node agent for network visibility, and an inference service with GPU that
scales to zero. Sensors and the hunter never talk to actuators; the only
path to an actuator goes through the policy engine and, for irreversible
rungs, a human signature. The controller holds read-only permissions at
rest and receives a just-in-time `RoleBinding` per session.

**Hunt lifecycle.** A state machine with a single final state:
`Triggered → Preparing → Observing → Proposal → Containing → Verifying →
Closed`. A rejected proposal returns to `Observing`; a containment that did
not hold returns to `Proposal`. Abort is available from any state.
Extending the TTL requires a signature; a closed session is never reopened.

**Containment ladder.**

| Rung | Action | Reversal | Authorized by |
|---|---|---|---|
| 0 · Observe | Read-only sensors | n/a | Opening the session |
| 1 · Suspend | Freeze the agent's processes | Resume | Policy in `enforce` + immediate notice |
| 2 · Isolate network | `NetworkPolicy` denying ingress/egress except Bladerunner's channel | Delete the `NetworkPolicy` | Policy in `enforce` + immediate notice |
| 3 · Revoke | Rotate/delete Secrets, remove RoleBindings, revoke workload identity, scale to zero | Not reversible | Human signature |
| 4 · Terminate | Delete the pod (workload already at zero) | Not reversible | Human signature |

In `observe` mode every rung stays a proposal. Rungs 3–4 also require a
deterministic or ML detector to corroborate the hunter.

**Signed approval.** Rungs 3–4 require an approval signed by an authorized
operator (proposed: `ssh-keygen -Y sign`, namespace `bladerunner-approval`,
ed25519 keys, ideally hardware-backed). The signed payload is canonical JSON
(RFC 8785) and covers the action, rung, target (including its UID), the
SHA-256 of the evidence manifest the operator reviewed, a single-use nonce
and an expiry. Signers live in a versioned `allowed_signers` file. Any
verification failure means the action is not executed, and it is logged.

**Evidence and chain of custody.** Each session writes an append-only
directory `evidence/hs-<session_id>/` (`session.json`, `cchia/before`,
`cchia/after`, `events/`, `detections/`, `proposals/`, `approvals/`,
`actions/`, `manifest.json`). Events are hash-chained and the manifest is
sealed with SHA-256. Secret values are never stored, only fingerprints.

**Hunter model.** A small open-weights model (7–8B, quantized, fine-tuned
with QLoRA locally) served inside the cluster, with a 3–4B CPU fallback. It
has no tools, credentials or egress, answers only with a fixed JSON
contract (`classification`, `confidence`, `evidence_refs`,
`proposed_rung`), and cites evidence that must exist in the manifest. The
policy may lower its proposed rung, never raise it.

**CCHIA framework.** The CCHIA Security Compiler is integrated as a git
submodule pinned to a commit and invoked as a subprocess, read-only, before
and after each hunt (target prioritization, credential inventory for rung
3, re-verification) and to audit `bladerunner-system` itself. Its
`LICENSE` and `NOTICE.md` are kept; its code is excluded from ruff and mypy.

**Governance.** Five roles (hunt operator, security owner, cluster admin,
model maintainer, workload owner). Policies, the namespace allow-list,
signers and thresholds live as code in the repo (proposed path:
`policies/`) and change only through reviewed PRs.

### Alternatives considered

- **Keep the host-level psutil watcher** (ADR-003/004): does not reach
  containers, cannot revoke credentials, and leaves irreversible actions to
  an automatic mapping.
- **Permanent EDR-style monitoring:** higher cost and attack surface; the
  continuous, cheap posture reading is delegated to CCHIA checks and
  tripwires instead.
- **A closed-API LLM as the hunter:** evidence would leave the cluster, it
  fails during an isolated incident and is not reproducible. Kept only as an
  optional, disabled-by-default second opinion with redacted data.
- **Letting the model act:** rejected by principle 1.

### Consequences

- The existing backlog is reorganized: the hunt track is registered as
  TASK-011 to TASK-021 in `TASKS.md` (the specification's provisional IDs
  TASK-002 to TASK-012). TASK-001 (network sensor) continues unchanged and
  later feeds the node agent.
- Once accepted, TASK-002 (iptables isolation), TASK-003 (SQLite
  persistence) and TASK-007 (approval webhook) are superseded by rung 2,
  the evidence manifest and the signed approval respectively.
- The `monitor` mode will be renamed `observe`; the rename happens in the
  task that introduces `HuntSession` (TASK-011), not before.
- New dependencies (Kubernetes client, signature verification, inference
  server) will be justified in their own PRs.
- The v0.1 host-level components stay as they are until a task replaces
  them.

### Open decisions

Until each is closed, the system behaves with the most conservative option:

- Rungs 1–2 automatic in `enforce` (provisional) or also signed.
- Two-person rule for rung 4.
- Default session TTL and approval validity.
- Whether aborting reverts reversible containment (provisional: no; revert
  is a separate command).
- Inference server (vLLM or Ollama) and base model (Qwen, Llama, Gemma).
- Cloud provider (provisional: GKE Standard, Santiago region; development on
  k3d/kind with Calico).
- Suspend mechanism and its interaction with liveness probes.
- Evidence retention and personal data (legal review: Chilean Laws 21.663
  and 21.719, applicability to be confirmed).
- Adoption of dashAI for the ML detector (license and version to confirm).

## How to add an ADR

Number them sequentially, status `proposed` → PR → `accepted`.
