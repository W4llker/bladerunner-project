# DEFINITION_OF_DONE.md — "Done" criteria

> **Instructions for the AI agent:** a task is done **only if it meets ALL
> the criteria for its type**. If one is missing, the task is not done. Do
> not move it to "✅ Completed" until all of them are met.

---

## Criteria by task type

### 🟢 Feature (new functionality)

- [ ] Code implemented in the correct path.
- [ ] Inherits from the corresponding base class (if applicable).
- [ ] Has a unique `name` (if it's a component).
- [ ] Handles errors without propagating exceptions to the orchestrator.
- [ ] Unit test with at least 3 cases (success, failure, edge).
- [ ] Integration test if it affects the sensor→detector→actuator flow.
- [ ] Registered in `cli.py` if it should be used by default.
- [ ] Documented in `docs/architecture.md` or `docs/plugins.md`.
- [ ] Entry in `CHANGELOG.md` under `[Unreleased] / Added`.
- [ ] `ruff check .` passes.
- [ ] `pytest -v` passes.
- [ ] Global coverage does not drop.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

### 🔴 Bugfix

- [ ] Bug reproduced with a regression test (fails before the fix).
- [ ] Fix implemented.
- [ ] Regression test now passes.
- [ ] No other tests are broken.
- [ ] Root cause documented in the PR.
- [ ] Entry in `CHANGELOG.md` under `[Unreleased] / Fixed`.
- [ ] `ruff check .` and `pytest -v` pass.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

### 📚 Docs (documentation only)

- [ ] Content written with runnable examples where applicable.
- [ ] Internal links verified (no broken links).
- [ ] Spelling and grammar reviewed.
- [ ] If it describes behavior, it matches the current code.
- [ ] Entry in `CHANGELOG.md` under `[Unreleased] / Changed` or `Added`.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

### ♻️ Refactor

- [ ] No functional changes (existing tests still pass unchanged).
- [ ] If behavior changes, it is treated as a feature.
- [ ] Test coverage does not drop.
- [ ] Documentation updated if applicable.
- [ ] Entry in `CHANGELOG.md` under `[Unreleased] / Changed`.
- [ ] `ruff check .` and `pytest -v` pass.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

### 🧪 Test (tests only)

- [ ] Added tests cover the specified case.
- [ ] Global coverage goes up or stays the same.
- [ ] Existing tests are not modified just to "make them pass".
- [ ] If the test uncovers a bug, an issue or new task is opened.
- [ ] Entry in `CHANGELOG.md` if it adds visible value.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

### 🔧 Chore (maintenance)

- [ ] Minimal, localized change.
- [ ] Does not break the build, lint, or tests.
- [ ] Documented in the PR if it affects other contributors.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

### 🔒 Security

- [ ] Vulnerability identified and documented.
- [ ] Fix implemented with a regression test.
- [ ] Maintainers notified if critical (see `SECURITY.md`).
- [ ] Entry in `CHANGELOG.md` under `[Unreleased] / Security`.
- [ ] Task moved to "✅ Completed" in `TASKS.md`.

---

## Cross-cutting criteria (apply to EVERY type)

- [ ] Branch with the correct name (`feat/`, `fix/`, `docs/`, etc.).
- [ ] Commits using Conventional Commits.
- [ ] PR opened with the full template filled in.
- [ ] CI (GitHub Actions) passes green.
- [ ] At least one reviewer assigned (or self-review with the checklist checked).
- [ ] No `TODO` without an associated issue.
- [ ] No secrets, `.env`, `.ai/`, or personal data in the diff.
- [ ] No code commented out "just in case".
- [ ] No new dependencies without justification in the PR.

---

## Anti-criteria (the task is NOT done if...)

- ❌ The test "passes" but doesn't actually test what it claims to.
- ❌ An error is silenced with `try/except: pass`.
- ❌ `# type: ignore` is added without justification.
- ❌ Global coverage drops.
- ❌ Code is commented out without a tracking issue.
- ❌ `git push --force` is done to `main`.
- ❌ It is merged without green CI.
- ❌ It is merged without updating `CHANGELOG.md`.
- ❌ It is merged without updating `TASKS.md`.
- ❌ `enforce` mode is left as the default.

---

## Final rule

**When in doubt, ask yourself:** "If another contributor clones the repo
tomorrow, will they understand what was done, why, and be able to verify
it?" If the answer is no, the task is not done.
