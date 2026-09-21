# Bladerunner — Open Source Agent Hunter

[![CI](https://github.com/W4llker/bladerunner-project/actions/workflows/ci.yml/badge.svg)](https://github.com/W4llker/bladerunner-project/actions/workflows/ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-261230.svg)](https://github.com/astral-sh/ruff)

**Bladerunner** is an open source framework to **detect, contain, and neutralize rogue autonomous agents** — LLM agents, automation bots, RL agents — without needing to inspect their internal code. It works as an "agent hunter": it observes external behavior, judges whether it is anomalous, and applies graduated countermeasures, up to termination.

> ⚠️ **Bladerunner is defensive by design.** It only acts within infrastructure you control, and it never performs offensive actions against third parties.

---

## Why Bladerunner

As autonomous agents proliferate — LLMs with tool access, automation bots, reinforcement-learning agents — so does the risk of unforeseen behavior: data exfiltration, privilege escalation, resource abuse, or an agent that simply stops responding to shutdown signals. Bladerunner provides a monitoring and containment layer that sits outside the agent itself, so it keeps working even if the agent is compromised, misaligned, or unresponsive.

## Key features

- **Black-box observation** — monitors process-level signals (CPU, open connections, file handles) without requiring access to the agent's source code or model weights.
- **Pluggable detection** — rule-based thresholds and statistical anomaly detection (z-score) out of the box; both a `Sensor` and `Detector` are extension points.
- **Graduated response** — actions escalate from `LOG` → `ALERT` → `RESTRICT` → `ISOLATE` → `KILL` based on severity, never jumping straight to termination unless warranted.
- **Monitor vs. enforce modes** — run in observe-only mode during rollout, then switch to `enforce` once you trust the detection rules.
- **Human-in-the-loop optional** — `monitor` mode downgrades destructive actions to alerts, keeping a human in control until you're ready to automate.
- **Auditable by default** — every event, verdict, and action is logged for after-the-fact review.

## Architecture

Four decoupled layers connected by an event stream:

```
[Target agent] --telemetry--> [Sensor] --Event--> [Detector] --Verdict--> [Orchestrator] --Action--> [Actuator]
                                                                                |
                                                                        [Dashboard / Logs]
```

| Layer | Responsibility | MVP implementation |
|---|---|---|
| Sensor | Emits `Event`s from raw telemetry | `ProcessSensor` (via `psutil`) |
| Detector | Turns `Event`s into `Verdict`s | `RuleBasedDetector`, `AnomalyDetector` |
| Orchestrator | Aggregates verdicts, decides the `Action` | `Orchestrator` |
| Actuator | Executes the `Action` | `LogOnlyActuator`, `ProcessKillerActuator` |

### Severity → action mapping

| Severity | Action (enforce mode) |
|---|---|
| INFO / LOW | LOG |
| MEDIUM | ALERT |
| HIGH | ISOLATE |
| CRITICAL | KILL |

In `monitor` mode, `ISOLATE` and `KILL` are downgraded to `ALERT` so nothing destructive happens without explicit opt-in.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

### Run the demo

Spins up a simulated rogue agent and watches Bladerunner detect and kill it end to end:

```bash
python examples/run_demo.py
```

### Watch a real process

```bash
python -m bladerunner.cli watch <PID> --agent-id my-agent --mode enforce --interval 1.0
```

- `--mode monitor` (default) only logs and alerts.
- `--mode enforce` allows Bladerunner to isolate or kill the process once severity reaches `HIGH`/`CRITICAL`.

## Documentation

| Doc | Purpose |
|---|---|
| [MASTER_WORKFLOW.md](MASTER_WORKFLOW.md) | Single entry point: project map, dev workflow, conventions |
| [docs/architecture.md](docs/architecture.md) | Full system design |
| [docs/deployment.md](docs/deployment.md) | Local, Docker, Kubernetes, and production deployment |
| [docs/roadmap.md](docs/roadmap.md) | Where the project is headed |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [SECURITY.md](SECURITY.md) | Reporting vulnerabilities |
| [AGENTS.md](AGENTS.md) | Guide for AI coding agents working in this repo |
| [TASKS.md](TASKS.md) | Live backlog — see "🎯 Current task" |
| [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) | Acceptance criteria for a task to be considered done |

If you're an AI agent contributing to this repo, start with [docs/agent_workflow.md](docs/agent_workflow.md).

## Development

```bash
make install-dev        # Install with dev dependencies
make pre-commit-install  # Install pre-commit hooks
make lint                # Ruff + mypy
make test-cov            # Tests with coverage
make demo                # Run the end-to-end demo
make help                 # See all available commands
```

## Project structure

```
src/bladerunner/
├── core/       → base classes, event bus, orchestrator
├── sensors/    → telemetry sensors (process, …)
├── detectors/  → rule-based and anomaly detectors
├── actuators/  → response actions (log, kill, …)
├── api/        → REST API
└── cli.py      → command-line interface
```

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md) before opening a PR, and check [TASKS.md](TASKS.md) for open work.

## Security

Please **do not** open a public issue for security vulnerabilities. See [SECURITY.md](SECURITY.md) for the responsible disclosure process.

## License

Apache 2.0 — see [LICENSE](LICENSE).
