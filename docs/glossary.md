# Glossary

| Term | Definition |
|---|---|
| Agent | An autonomous system that executes actions. |
| Agent hunter | A system that detects and neutralizes rogue agents. |
| Sensor | Generates telemetry `Event`s. |
| Detector | Analyzes `Event`s, produces `Verdict`s. |
| Actuator | Executes `Action`s. |
| Orchestrator | Coordinates sensors, detectors, and actuators. |
| Event | Raw telemetry. |
| Verdict | A detector's output. |
| Action | A decision: LOG, ALERT, RESTRICT, ISOLATE, KILL. |
| Severity | INFO, LOW, MEDIUM, HIGH, CRITICAL. |
| monitor | Log/alert only. |
| enforce | Allows ISOLATE and KILL. |
| ADR | Architecture Decision Record. |
| Sandbox | An isolated environment. |
| Baseline | Learned normal behavior. |
