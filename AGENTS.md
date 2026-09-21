# AGENTS.md — Guide for AI agents working on Bladerunner

## 1. Context

Bladerunner is a defensive cybersecurity framework. Read README.md,
MASTER_WORKFLOW.md, and docs/architecture.md first.

## 2. Structure

```
src/bladerunner/
├── core/       → Event, Sensor, Detector, Actuator, Orchestrator
├── sensors/    → sensor implementations
├── detectors/  → detector implementations
├── actuators/  → actuator implementations
├── api/        → REST API (FastAPI)
└── cli.py      → CLI (Typer)
```

## 3. Mandatory conventions

### Code
- Python 3.10+, strict typing on public functions.
- Formatting: `ruff format`. Linting: `ruff check`. Tests: `pytest`.
- One component = one file + one test.
- Do not add dependencies without justifying them in the PR.
- ML models are loaded in `__init__`, never in `evaluate`.

### Documentation
- Architectural decisions → ADR in docs/decisions.md before implementing.
- Every PR adds an entry to CHANGELOG.md under [Unreleased].
- Every feature is documented in docs/.

### Git
- Branches: `feat/`, `fix/`, `docs/`, `chore/`, `test/`, `security/`.
- Commits: Conventional Commits.
- Never `git push` without authorization.
- Never commit secrets, `.env`, `.ai/`, or data.

## 4. Flow for adding a feature

1. Read docs/architecture.md and docs/decisions.md.
2. If it affects more than one module → create an ADR.
3. Implement following the base classes in core/.
4. Write tests following docs/testing.md.
5. Add an entry to CHANGELOG.md.
6. Update docs/ if applicable.
7. Run `ruff check . && pytest -v`.

## 5. Flow for adding a component

Follow docs/plugins.md. Checklist:
- [ ] Inherits from the base class.
- [ ] Has a unique `name`.
- [ ] Handles errors without propagating exceptions.
- [ ] Has a unit test.
- [ ] Registered in cli.py if applicable.
- [ ] Documented in docs/architecture.md.
- [ ] `ruff check .` and `pytest -v` pass.

## 6. Security rules (non-negotiable)

- Never offensive actions outside the perimeter.
- Never `enforce` without testing in `monitor` first.
- Never commit secrets.
- Never disable `monitor` as the default.
- Never "hack back".
- Prefer reversible over destructive actions.
- Audit every action executed.

## 7. If you don't know what to do

1. Check docs/roadmap.md.
2. Look for issues labeled `good first issue`.
3. Open an issue describing the question.
4. When in doubt, choose the most conservative and defensive option.

## Related documentation

| [TASKS.md](TASKS.md) | Live backlog — always look for "🎯 Current task" |
| [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) | When a task is considered done |
| [docs/agent_workflow.md](docs/agent_workflow.md) | Full operational workflow for agents |
