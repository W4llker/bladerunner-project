# ADRs — Architecture Decision Record log

## Format

- Date, status, context, decision, alternatives, consequences.

## ADR-001: Python 3.10+

Accepted. AI/ML ecosystem, ease of contribution.
Alternatives: Rust, Go, TypeScript.

## ADR-002: FastAPI + Uvicorn

Accepted. Typing with Pydantic, automatic docs, native async.
Alternatives: Flask, Django REST, Litestar.

## ADR-003: Graduated countermeasures

Accepted. Fixed `Severity → ActionKind` mapping.
Alternatives: configurable policies, RL.

## ADR-004: External observation with psutil

Accepted. Works as a black box.
Alternatives: eBPF, APM, instrumentation.

## ADR-005: `monitor` mode by default

Accepted. Secure by default.
Alternatives: enforce by default.

## ADR-006: Apache 2.0

Accepted. Commercial use, patent clause.
Alternatives: MIT, GPL, AGPL.

## How to add an ADR

Number them sequentially, status `proposed` → PR → `accepted`.
