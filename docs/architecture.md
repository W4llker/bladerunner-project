# Arquitectura de Bladerunner

## Visión general

Cuatro capas desacopladas comunicadas por un bus de eventos:

1. Sensores → generan `Event`s.
2. Detectores → consumen `Event`s y producen `Verdict`s.
3. Orquestador → agrega veredictos y decide `Action`.
4. Actuadores → ejecutan la `Action`.

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

## Principios de diseño

- Observación externa: no requiere acceso al código del agente.
- Contramedidas graduadas: log → alert → restrict → isolate → kill.
- Humano en el circuito opcional: `monitor` vs `enforce`.
- Extensible: plugins para sensores/detectores/actuadores.
- Defensivo por diseño.
- Auditable.

## Componentes MVP

- `ProcessSensor` (psutil).
- `RuleBasedDetector` (CPU>90, connections>100, open_files>500).
- `AnomalyDetector` (z-score).
- `LogOnlyActuator`, `ProcessKillerActuator`.
- `Orchestrator`.

## Modelo de datos

- `Event` (timestamp, kind, source, agent_id, data).
- `Verdict` (is_anomalous, severity, reason, score).
- `Action` (kind, target_agent_id, severity, reason).

## Mapeo severidad → acción

| Severidad | Acción |
|---|---|
| INFO | LOG |
| LOW | LOG |
| MEDIUM | ALERT |
| HIGH | ISOLATE |
| CRITICAL | KILL |

En modo `monitor`, ISOLATE y KILL se degradan a ALERT.
