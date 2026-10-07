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
8. Commit using Conventional Commits, signing off every commit (`git commit -s`, see below).
9. Push to your fork and open a Pull Request.

## Developer Certificate of Origin (DCO)

Every commit must be signed off to certify that you wrote the contribution or
otherwise have the right to submit it under the project's license, as defined
in the [Developer Certificate of Origin 1.1](https://developercertificate.org/).

Sign off by adding the `-s` flag:

```bash
git commit -s -m "feat(task-NNN): short description"
```

This appends a line like the following to your commit message, using your
`user.name` and `user.email` from git:

```
Signed-off-by: Your Name <your.email@example.com>
```

Commits without a valid `Signed-off-by` line will not be merged. If you forgot
to sign off, amend with `git commit --amend -s` (or
`git rebase --signoff main` for several commits) and force-push to your branch.

## License of contributions

By contributing, you agree that your contributions are licensed under the
[Apache License 2.0](LICENSE), and that the project's copyright and
attribution notices (see [NOTICE](NOTICE)) remain in place. You keep the
copyright on your own contributions.

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
