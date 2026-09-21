# Bladerunner Architecture

## Overview

Four decoupled layers connected by an event bus:

1. Sensors → generate `Event`s.
2. Detectors → consume `Event`s and produce `Verdict`s.
3. Orchestrator → aggregates verdicts and decides on an `Action`.
4. Actuators → execute the `Action`.

```
+-----------+  Event   +----------+  Verdict  +--------------+
|  Sensor   | -------> | Detector | --------> | Orchestrator |
+-----------+          +----------+           +--------------+
                                                    |
                                                 Action
                                                    v
                                              +-----------+
                                              | Actuator  |
                                              +-----------+
```

## Design principles

- External observation: does not require access to the agent's code.
- Graduated countermeasures: log → alert → restrict → isolate → kill.
- Optional human in the loop: `monitor` vs. `enforce`.
- Extensible: plugins for sensors/detectors/actuators.
- Defensive by design.
- Auditable.

## MVP components

- `ProcessSensor` (psutil).
- `RuleBasedDetector` (CPU>90, connections>100, open_files>500).
- `AnomalyDetector` (z-score).
- `LogOnlyActuator`, `ProcessKillerActuator`.
- `Orchestrator`.

## Data model

- `Event` (timestamp, kind, source, agent_id, data).
- `Verdict` (is_anomalous, severity, reason, score).
- `Action` (kind, target_agent_id, severity, reason).

## Severity → action mapping

| Severity | Action |
|---|---|
| INFO | LOG |
| LOW | LOG |
| MEDIUM | ALERT |
| HIGH | ISOLATE |
| CRITICAL | KILL |

In `monitor` mode, ISOLATE and KILL are downgraded to ALERT.
