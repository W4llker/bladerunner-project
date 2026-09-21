# DEFINITION_OF_DONE.md — Criterios de "terminado"

> **Instrucciones para el agente IA:** una tarea está terminada **solo si
> cumple TODOS los criterios de su tipo**. Si falta uno, la tarea no está
> terminada. No la muevas a "✅ Completadas" hasta cumplirlos todos.

---

## Criterios por tipo de tarea

### 🟢 Feature (nueva funcionalidad)

- [ ] Código implementado en la ruta correcta.
- [ ] Hereda de la clase base correspondiente (si aplica).
- [ ] Tiene `name` único (si es componente).
- [ ] Maneja errores sin propagar excepciones al orquestador.
- [ ] Test unitario con al menos 3 casos (éxito, fallo, borde).
- [ ] Test de integración si afecta al flujo sensor→detector→actuador.
- [ ] Registrado en `cli.py` si debe usarse por defecto.
- [ ] Documentado en `docs/architecture.md` o `docs/plugins.md`.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Added`.
- [ ] `ruff check .` pasa.
- [ ] `pytest -v` pasa.
- [ ] Cobertura global no baja.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🔴 Bugfix

- [ ] Bug reproducido con un test de regresión (falla antes del fix).
- [ ] Fix implementado.
- [ ] Test de regresión ahora pasa.
- [ ] No se rompen otros tests.
- [ ] Causa raíz documentada en el PR.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Fixed`.
- [ ] `ruff check .` y `pytest -v` pasan.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 📚 Docs (solo documentación)

- [ ] Contenido escrito con ejemplos ejecutables cuando aplique.
- [ ] Enlaces internos verificados (sin links roscos).
- [ ] Ortografía y gramática revisadas.
- [ ] Si describe comportamiento, coincide con el código actual.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Changed` o `Added`.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### ♻️ Refactor

- [ ] Sin cambios funcionales (tests existentes siguen pasando sin cambios).
- [ ] Si cambia comportamiento, se trata como feature.
- [ ] Cobertura de tests no baja.
- [ ] Documentación actualizada si aplica.
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Changed`.
- [ ] `ruff check .` y `pytest -v` pasan.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🧪 Test (solo tests)

- [ ] Tests añadidos cubren el caso especificado.
- [ ] Cobertura global sube o se mantiene.
- [ ] No se modifican tests existentes para "hacerlos pasar".
- [ ] Si el test descubre un bug, se abre un issue o una nueva tarea.
- [ ] Entrada en `CHANGELOG.md` si aporta valor visible.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🔧 Chore (mantenimiento)

- [ ] Cambio mínimo y localizado.
- [ ] No rompe build, lint ni tests.
- [ ] Documentado en el PR si afecta a otros contribuidores.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

### 🔒 Security

- [ ] Vulnerabilidad identificada y documentada.
- [ ] Fix implementado con test de regresión.
- [ ] Aviso a maintainers si es crítica (ver `SECURITY.md`).
- [ ] Entrada en `CHANGELOG.md` bajo `[Unreleased] / Security`.
- [ ] Tarea movida a "✅ Completadas" en `TASKS.md`.

---

## Criterios transversales (aplican a TODO tipo)

- [ ] Rama con nombre correcto (`feat/`, `fix/`, `docs/`, etc.).
- [ ] Commits con Conventional Commits.
- [ ] PR abierto con la plantilla completa.
- [ ] CI (GitHub Actions) pasa en verde.
- [ ] Al menos un revisor asignado (o self-review con checklist marcada).
- [ ] Sin `TODO` sin issue asociado.
- [ ] Sin secretos, `.env`, `.ai/` ni datos personales en el diff.
- [ ] Sin código comentado "por si acaso".
- [ ] Sin dependencias nuevas sin justificar en el PR.

---

## Anti-criterios (la tarea NO está terminada si...)

- ❌ El test "pasa" pero no prueba realmente lo que dice probar.
- ❌ Se silencia un error con `try/except: pass`.
- ❌ Se añade `# type: ignore` sin justificación.
- ❌ Se baja la cobertura global.
- ❌ Se comenta código sin issue que lo rastree.
- ❌ Se hace `git push --force` a `main`.
- ❌ Se mergea sin CI verde.
- ❌ Se mergea sin actualizar `CHANGELOG.md`.
- ❌ Se mergea sin actualizar `TASKS.md`.
- ❌ Se deja el modo `enforce` como default.

---

## Regla final

**Cuando dudes, pregúntate:** "¿si otro contribuidor clona el repo mañana,
entiende qué se hizo, por qué, y puede verificarlo?" Si la respuesta es no,
la tarea no está terminada.
