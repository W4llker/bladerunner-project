# agent_workflow.md — Cómo trabaja un agente IA en este repositorio

Esta guía define el flujo operativo que debe seguir **cualquier agente IA**
(Claude Code, Cursor, Cline, Aider, Continue, etc.) al trabajar en Bladerunner.

Si eres un agente IA, sigue estos pasos **en orden** en cada sesión.

---

## Paso 0 — Preparación (solo la primera vez)

1. Verifica que el repo está clonado y el entorno virtual activo.
2. Ejecuta `make install-dev` para instalar dependencias.
3. Ejecuta `make pre-commit-install` para instalar los hooks.
4. Verifica con `make test` que todos los tests pasan.

---

## Paso 1 — Orientación

Al inicio de CADA sesión:

1. Lee `AGENTS.md` completo.
2. Lee `MASTER_WORKFLOW.md` para el contexto general.
3. Lee `TASKS.md` y localiza la sección **"🎯 Tarea actual"**.
4. Lee `DEFINITION_OF_DONE.md` para saber cuándo la tarea estará terminada.
5. Si la tarea involucra un componente nuevo, lee `docs/plugins.md`.
6. Si la tarea involucra tests, lee `docs/testing.md`.
7. Si la tarea involucra una decisión arquitectónica, lee `docs/decisions.md`.

**Salida esperada:** sabes exactamente en qué tarea vas a trabajar y cuáles
son los criterios de aceptación.

---

## Paso 2 — Preparación de la rama

```bash
# Actualiza main
git checkout main
git pull origin main

# Crea rama según el tipo de tarea
git checkout -b feat/task-NNN-descripcion-corta
# o fix/, docs/, chore/, test/, security/ según corresponda
```

---

## Paso 3 — Implementación

1. Si la tarea requiere una decisión arquitectónica:
   - Añade una ADR en `docs/decisions.md` con estado `propuesta`.
2. Implementa el código siguiendo las convenciones de `AGENTS.md`.
3. Añade tests siguiendo `docs/testing.md`.
4. Añade entrada en `CHANGELOG.md` bajo `[Unreleased]` en la categoría correcta.
5. Actualiza la documentación en `docs/` si aplica.

---

## Paso 4 — Verificación local

Ejecuta en orden:

```bash
make lint         # ruff check
make test-cov     # pytest con cobertura
make demo         # demo end-to-end (opcional pero recomendado)
```

**Criterios de paso:**
- [ ] `make lint` pasa sin errores.
- [ ] `make test-cov` pasa y la cobertura no bajó.
- [ ] `make demo` funciona si la tarea afecta al flujo principal.

Si algo falla, **arregla antes de continuar**. No acumules errores.

---

## Paso 5 — Actualizar TASKS.md

1. Marca todos los criterios de aceptación de la tarea con `[x]`.
2. Mueve la tarea de **"🎯 Tarea actual"** a **"✅ Completadas"**.
3. Añade la fecha de fin: `(completada YYYY-MM-DD)`.
4. Promueve la siguiente tarea de **"📋 Pendientes"** a **"🎯 Tarea actual"**.

---

## Paso 6 — Commit

```bash
git add .
git commit -m "feat(task-NNN): descripción corta

- Punto 1 del cambio
- Punto 2 del cambio

Cierra #NNN"
```

**Reglas:**
- Usa Conventional Commits.
- Una línea de asunto de <72 caracteres.
- Cuerpo con detalles si es necesario.
- Referencia el issue con `Closes #NNN` o `Refs #NNN`.

**Los hooks de pre-commit se ejecutan automáticamente.** Si fallan,
arréglalos y repite el commit.

---

## Paso 7 — Push y PR

```bash
git push origin feat/task-NNN-descripcion-corta
```

Abre un PR en GitHub **usando la plantilla** (se carga automáticamente).
Rellena todos los campos.

**Espera a que CI pase.** Si falla, arregla y vuelve a hacer push.

---

## Paso 8 — Reporte al usuario

Al terminar la sesión, reporta:

```
=== Sesión de trabajo — Bladerunner ===

Tarea completada: [TASK-NNN] Título
Rama: feat/task-NNN-descripcion
PR: #NNN (URL)

Cambios:
  - Archivos modificados: N
  - Tests añadidos: N
  - Cobertura: X% (antes Y%)

Verificación:
  - make lint: PASS
  - make test-cov: PASS
  - make demo: PASS

Próxima tarea: [TASK-NNN+1] Título

Dudas / bloqueos:
  - (ninguno)
```

---

## Reglas especiales

### Si encuentras un bug mientras trabajas en otra cosa

1. Abre un issue con la plantilla de bug.
2. Añade una tarea nueva en `TASKS.md` en "📋 Pendientes".
3. **No arregles el bug en la rama actual.** Termina la tarea en curso.

### Si la tarea es demasiado grande (>1 día de trabajo)

1. Divide la tarea en subtareas en `TASKS.md`.
2. Trabaja en una subtarea a la vez.
3. Marca la tarea original como "🚫 Bloqueada hasta que se completen las subtareas".

### Si la tarea requiere una decisión arquitectónica

1. Detente.
2. Escribe una ADR en `docs/decisions.md` con estado `propuesta`.
3. Pregunta al usuario antes de implementar.
4. No sigas hasta tener aprobación.

### Si no sabes qué hacer

1. Consulta `TASKS.md`, `docs/roadmap.md`, `docs/decisions.md`.
2. Si sigue sin estar claro, **detente y pregunta al usuario**.
3. **Nunca improvises** una solución no especificada.

### Si rompes algo

1. No entres en pánico.
2. Identifica qué rompiste: `git diff`, `git log`.
3. Si no puedes arreglarlo en 15 minutos, revierte:
   ```bash
   git checkout main
   git branch -D feat/task-NNN-descripcion
   ```
4. Reporta al usuario qué pasó.

---

## Anti-patrones (lo que NUNCA debes hacer)

- ❌ Trabajar en dos tareas a la vez.
- ❌ Commitear sin tests.
- ❌ Commitear sin actualizar `CHANGELOG.md` y `TASKS.md`.
- ❌ Silenciar errores con `try/except: pass`.
- ❌ Bajar la cobertura de tests.
- ❌ Añadir dependencias sin justificar.
- ❌ Hacer `git push --force` a `main`.
- ❌ Modificar `.ai/` o `.env`.
- ❌ Modo `enforce` por defecto.
- ❌ Ejecutar acciones ofensivas fuera del perímetro.
- ❌ Improvisar cuando hay ambigüedad.

---

## Ciclo completo (resumen visual)

```
┌──────────────────────────────────────────────────────┐
│ 1. Orientación                                       │
│    AGENTS.md → MASTER_WORKFLOW.md → TASKS.md → DoD   │
├──────────────────────────────────────────────────────┤
│ 2. Rama                                              │
│    git checkout -b feat/task-NNN-descripcion         │
├──────────────────────────────────────────────────────┤
│ 3. Implementación                                    │
│    código + tests + CHANGELOG + docs                 │
├──────────────────────────────────────────────────────┤
│ 4. Verificación                                      │
│    make lint && make test-cov && make demo           │
├──────────────────────────────────────────────────────┤
│ 5. Actualizar TASKS.md                               │
│    marcar completada, promover siguiente             │
├──────────────────────────────────────────────────────┤
│ 6. Commit                                            │
│    git commit -m "feat(task-NNN): ..."               │
├──────────────────────────────────────────────────────┤
│ 7. Push y PR                                         │
│    git push → abrir PR con plantilla                 │
├──────────────────────────────────────────────────────┤
│ 8. Reporte                                           │
│    resumen al usuario                                │
└──────────────────────────────────────────────────────┘
```
