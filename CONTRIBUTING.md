# Contributing to Bladerunner

Thanks for your interest!

## How to contribute

1. Read AGENTS.md, MASTER_WORKFLOW.md, and CONTRIBUTING.md.
2. Find or open an issue describing the change.
3. Fork the repo, branch: `git checkout -b feat/my-contribution`.
4. Implement following docs/plugins.md.
5. Write tests following docs/testing.md.
6. Add an entry to CHANGELOG.md under [Unreleased].
7. Run `ruff check . && pytest -v`.
8. Commit using Conventional Commits.
9. Push to your fork and open a Pull Request.

## Code style

- Python 3.10+.
- `ruff format` and `ruff check`.
- Typing on public functions.

## Test coverage

- Core: >90%
- Detectors: >85%
- Sensors/Actuators: >80%
- Global: >80%

PRs that lower coverage will be rejected.

## Review process

- A maintainer reviews the PR.
- Comments are resolved.
- CI must pass.
- Merge to main.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
