# Contribuir a Bladerunner

¡Gracias por tu interés!

## Cómo contribuir

1. Lee AGENTS.md, MASTER_WORKFLOW.md y CONTRIBUTING.md.
2. Busca o abre un issue describiendo el cambio.
3. Fork del repo, rama: `git checkout -b feat/mi-aporte`.
4. Implementa siguiendo docs/plugins.md.
5. Escribe tests siguiendo docs/testing.md.
6. Añade entrada en CHANGELOG.md bajo [Unreleased].
7. Ejecuta `ruff check . && pytest -v`.
8. Commit con Conventional Commits.
9. Push a tu fork y abre Pull Request.

## Estilo de código

- Python 3.10+.
- `ruff format` y `ruff check`.
- Tipado en funciones públicas.

## Cobertura de tests

- Core: >90%
- Detectors: >85%
- Sensors/Actuators: >80%
- Global: >80%

PRs que bajen la cobertura se rechazan.

## Proceso de review

- Un maintainer revisa.
- Se resuelven comentarios.
- CI debe pasar.
- Merge a main.

## Código de conducta

Ver [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
