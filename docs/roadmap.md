# Roadmap

## v0.1 (MVP) — current
- [x] Base structure
- [x] ProcessSensor
- [x] RuleBasedDetector + AnomalyDetector
- [x] LogOnlyActuator + ProcessKillerActuator
- [x] CLI and REST API
- [x] End-to-end demo
- [x] CI
- [x] Documentation

## Hunt track — pending ADR-007

On-demand hunting, containment and governance of agents on Kubernetes (see
ADR-007 in `docs/decisions.md`). Starts once the ADR is accepted; the
current task (network sensor) continues meanwhile.

- [ ] ADR-007 accepted
- [ ] HuntSession: scope, TTL, mode, state machine (TASK-011)
- [ ] Evidence manifest with hash chain (TASK-012)
- [ ] CCHIA ingestion (TASK-013)
- [ ] Ephemeral container with sensors (TASK-014)
- [ ] Signed approval and verifier (TASK-015)
- [ ] Rungs 1–2: suspend, isolate network (TASK-016)
- [ ] Inference service and hunter JSON contract (TASK-017)
- [ ] Rungs 3–4: revoke, terminate (TASK-018)
- [ ] Per-session node agent (TASK-019)
- [ ] Tripwires (TASK-020)
- [ ] Scenario simulator and QLoRA pipeline (TASK-021, Phase 2)

## v0.2
- [ ] Complete REST API
- [ ] Network sensor
- [ ] Isolation actuator (iptables/cgroups)
- [ ] SQLite persistence
- [ ] HTMX dashboard
- [ ] Human in the loop (webhook)
- [ ] Coverage >80%

## v0.3
- [ ] ML detector (RF, IF)
- [ ] Autoencoder (PyTorch)
- [ ] HF datasets integration
- [ ] LLM support (LangChain, AutoGPT)
- [ ] Docker/K8s connectors

## v0.4
- [ ] RL (Stable-Baselines3)
- [ ] CyberBattleSim, MininetGym
- [ ] Multi-agent

## v1.0
- [ ] Stable API
- [ ] Complete docs
- [ ] Coverage >90%
- [ ] PyPI
- [ ] External audit
