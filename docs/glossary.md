# Glosario

| Término | Definición |
|---|---|
| Agente | Sistema autónomo que ejecuta acciones. |
| Caza-agentes | Sistema que detecta y neutraliza agentes descontrolados. |
| Sensor | Genera `Event`s de telemetría. |
| Detector | Analiza `Event`s, produce `Verdict`s. |
| Actuador | Ejecuta `Action`s. |
| Orquestador | Coordina sensores, detectores, actuadores. |
| Event | Telemetría cruda. |
| Verdict | Resultado de un detector. |
| Action | Decisión: LOG, ALERT, RESTRICT, ISOLATE, KILL. |
| Severidad | INFO, LOW, MEDIUM, HIGH, CRITICAL. |
| monitor | Solo log/alerta. |
| enforce | Permite ISOLATE y KILL. |
| ADR | Architecture Decision Record. |
| Sandbox | Entorno aislado. |
| Baseline | Comportamiento normal aprendido. |
