# ADRs — Registro de decisiones arquitectónicas

## Formato

- Fecha, estado, contexto, decisión, alternativas, consecuencias.

## ADR-001: Python 3.10+

Aceptada. Ecosistema IA/ML, facilidad de contribución.
Alternativas: Rust, Go, TypeScript.

## ADR-002: FastAPI + Uvicorn

Aceptada. Tipado con Pydantic, docs automáticas, async nativo.
Alternativas: Flask, Django REST, Litestar.

## ADR-003: Contramedidas graduadas

Aceptada. Mapeo fijo `Severity → ActionKind`.
Alternativas: políticas configurables, RL.

## ADR-004: Observación externa con psutil

Aceptada. Funciona con caja negra.
Alternativas: eBPF, APM, instrumentación.

## ADR-005: Modo `monitor` por defecto

Aceptada. Seguridad por defecto.
Alternativas: enforce por defecto.

## ADR-006: Apache 2.0

Aceptada. Uso comercial, cláusula de patentes.
Alternativas: MIT, GPL, AGPL.

## Cómo añadir una ADR

Numerar secuencialmente, estado `propuesta` → PR → `aceptada`.
