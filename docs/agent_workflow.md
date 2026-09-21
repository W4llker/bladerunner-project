# agent_workflow.md — How an AI agent works in this repository

This guide defines the operational workflow that **any AI agent**
(Claude Code, Cursor, Cline, Aider, Continue, etc.) must follow when working
on Bladerunner.

If you are an AI agent, follow these steps **in order** every session.

---

## Step 0 — Setup (first time only)

1. Verify the repo is cloned and the virtual environment is active.
2. Run `make install-dev` to install dependencies.
3. Run `make pre-commit-install` to install the hooks.
4. Verify with `make test` that all tests pass.

---

## Step 1 — Orientation

At the start of EVERY session:

1. Read `AGENTS.md` in full.
2. Read `MASTER_WORKFLOW.md` for general context.
3. Read `TASKS.md` and find the **"🎯 Current task"** section.
4. Read `DEFINITION_OF_DONE.md` to know when the task will be done.
5. If the task involves a new component, read `docs/plugins.md`.
6. If the task involves tests, read `docs/testing.md`.
7. If the task involves an architectural decision, read `docs/decisions.md`.

**Expected outcome:** you know exactly which task you're working on and
what its acceptance criteria are.

---

## Step 2 — Branch setup

```bash
# Update main
git checkout main
git pull origin main

# Create a branch based on the task type
git checkout -b feat/task-NNN-short-description
# or fix/, docs/, chore/, test/, security/ as appropriate
```

---

## Step 3 — Implementation

1. If the task requires an architectural decision:
   - Add an ADR to `docs/decisions.md` with status `proposed`.
2. Implement the code following the conventions in `AGENTS.md`.
3. Add tests following `docs/testing.md`.
4. Add an entry to `CHANGELOG.md` under `[Unreleased]` in the correct
   category.
5. Update the documentation in `docs/` if applicable.

---

## Step 4 — Local verification

Run, in order:

```bash
make lint         # ruff check
make test-cov     # pytest with coverage
make demo         # end-to-end demo (optional but recommended)
```

**Pass criteria:**
- [ ] `make lint` passes with no errors.
- [ ] `make test-cov` passes and coverage did not drop.
- [ ] `make demo` works if the task affects the main flow.

If something fails, **fix it before continuing**. Do not accumulate errors.

---

## Step 5 — Update TASKS.md

1. Mark all the task's acceptance criteria with `[x]`.
2. Move the task from **"🎯 Current task"** to **"✅ Completed"**.
3. Add the completion date: `(completed YYYY-MM-DD)`.
4. Promote the next task from **"📋 Pending"** to **"🎯 Current task"**.

---

## Step 6 — Commit

```bash
git add .
git commit -m "feat(task-NNN): short description

- First point of the change
- Second point of the change

Closes #NNN"
```

**Rules:**
- Use Conventional Commits.
- A subject line under 72 characters.
- A body with details if needed.
- Reference the issue with `Closes #NNN` or `Refs #NNN`.

**Pre-commit hooks run automatically.** If they fail, fix them and commit
again.

---

## Step 7 — Push and PR

```bash
git push origin feat/task-NNN-short-description
```

Open a PR on GitHub **using the template** (it loads automatically).
Fill in every field.

**Wait for CI to pass.** If it fails, fix it and push again.

---

## Step 8 — Report to the user

At the end of the session, report:

```
=== Work session — Bladerunner ===

Task completed: [TASK-NNN] Title
Branch: feat/task-NNN-description
PR: #NNN (URL)

Changes:
  - Files modified: N
  - Tests added: N
  - Coverage: X% (before Y%)

Verification:
  - make lint: PASS
  - make test-cov: PASS
  - make demo: PASS

Next task: [TASK-NNN+1] Title

Questions / blockers:
  - (none)
```

---

## Special rules

### If you find a bug while working on something else

1. Open an issue using the bug template.
2. Add a new task to `TASKS.md` under "📋 Pending".
3. **Do not fix the bug on the current branch.** Finish the task in
   progress first.

### If the task is too large (>1 day of work)

1. Split the task into subtasks in `TASKS.md`.
2. Work on one subtask at a time.
3. Mark the original task as "🚫 Blocked until the subtasks are completed".

### If the task requires an architectural decision

1. Stop.
2. Write an ADR in `docs/decisions.md` with status `proposed`.
3. Ask the user before implementing.
4. Do not continue until you have approval.

### If you don't know what to do

1. Check `TASKS.md`, `docs/roadmap.md`, `docs/decisions.md`.
2. If it's still unclear, **stop and ask the user**.
3. **Never improvise** an unspecified solution.

### If you break something

1. Don't panic.
2. Identify what you broke: `git diff`, `git log`.
3. If you can't fix it in 15 minutes, revert:
   ```bash
   git checkout main
   git branch -D feat/task-NNN-description
   ```
4. Report to the user what happened.

---

## Anti-patterns (what you must NEVER do)

- ❌ Work on two tasks at once.
- ❌ Commit without tests.
- ❌ Commit without updating `CHANGELOG.md` and `TASKS.md`.
- ❌ Silence errors with `try/except: pass`.
- ❌ Lower test coverage.
- ❌ Add dependencies without justification.
- ❌ Run `git push --force` on `main`.
- ❌ Modify `.ai/` or `.env`.
- ❌ Default to `enforce` mode.
- ❌ Execute offensive actions outside the perimeter.
- ❌ Improvise when there is ambiguity.

---

## Full cycle (visual summary)

```
┌──────────────────────────────────────────────────────┐
│ 1. Orientation                                       │
│    AGENTS.md → MASTER_WORKFLOW.md → TASKS.md → DoD   │
├──────────────────────────────────────────────────────┤
│ 2. Branch                                            │
│    git checkout -b feat/task-NNN-description         │
├──────────────────────────────────────────────────────┤
│ 3. Implementation                                    │
│    code + tests + CHANGELOG + docs                   │
├──────────────────────────────────────────────────────┤
│ 4. Verification                                      │
│    make lint && make test-cov && make demo           │
├──────────────────────────────────────────────────────┤
│ 5. Update TASKS.md                                   │
│    mark completed, promote the next one              │
├──────────────────────────────────────────────────────┤
│ 6. Commit                                            │
│    git commit -m "feat(task-NNN): ..."               │
├──────────────────────────────────────────────────────┤
│ 7. Push and PR                                       │
│    git push → open PR with the template               │
├──────────────────────────────────────────────────────┤
│ 8. Report                                            │
│    summary for the user                              │
└──────────────────────────────────────────────────────┘
```
