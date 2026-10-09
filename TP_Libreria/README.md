# TP Librería — FastAPI + PostgreSQL (UTN Programación III, Unid. 1–4)

Avance por ejercicio de la consigna. `[X]` = completado y verificado, `[]` = pendiente.

## Ejercicio 1 — Proyecto, conexión y ciclo de vida (10 pts)

- [X] Estructura modular (`app/core`, `app/modules/<modulo>`, `migrations/`, `test/`)
- [X] Entorno virtual `.venv` (Python 3.12) y `requirements.txt` con los mínimos (fastapi[standard]>=0.111, sqlmodel>=0.0.24, SQLAlchemy>=2.0, asyncpg>=0.30, alembic>=1.13, python-dotenv>=1.0, uvicorn)
- [X] `.env.example` con `DATABASE_URL` (+ `.gitignore` cubre `.env` y `.venv`, sin credenciales en el repo)
- [X] Motor asincrónico + `async_sessionmaker(expire_on_commit=False)` + `get_session` (`app/core/`)
- [X] `lifespan`: recursos en `app.state`, motor cerrado al apagar (`app/main.py`)
- [X] `GET /health/live` (sin base) y `GET /health/ready` (`SELECT 1`, 503 con mensaje propio)

## Ejercicio 2 — Modelos, restricciones y relaciones (25 pts)

- [X] 9 tablas en singular con columnas obligatorias (`editorial`, `genero`, `autor`, `libro`, `libro_autor`, `cliente`, `perfil_cliente`, `venta`, `renglon_venta`)
- [X] `Decimal` para dinero (`precio` 10,2 / `total` 12,2 / `precio_unitario` 10,2), `fecha` con zona horaria
- [X] UNIQUE: `isbn`, `email`, `nombre` (editorial y género), `perfil_cliente.cliente_id`
- [X] Los 7 CHECK (`precio > 0`, `stock >= 0`, `cantidad > 0`, `precio_unitario > 0`, `orden >= 1`, `total >= 0`, `rol` en la lista cerrada)
- [X] Índice en cada FK y `Relationship(back_populates=...)` en los dos extremos
- [X] `LibroAutor` como entidad (PK compuesta + `rol` + `orden`); `Cliente.perfil` escalar
- [X] Imports de módulo al pie de cada `models.py` (cualquier módulo importa aislado sin `InvalidRequestError`)

## Ejercicio 3 — Migraciones (10 pts)

- [X] Alembic con plantilla asincrónica (URL desde `DATABASE_URL`, sin secretos en `alembic.ini`)
- [X] Migración 1 autogenerada **sin** `genero` ni `libro.genero_id` (correcciones comentadas en el archivo); `upgrade head` / `downgrade -1` / `upgrade head` verificados
- [X] Migración 2 autogenerada: tabla `genero` + `libro.genero_id` (nullable, índice y FK), con `import sqlmodel` agregado a mano y comentado; `downgrade -1` corregido (nombre explícito `libro_genero_id_fkey`) — ciclo `downgrade`/`upgrade` y `alembic check` ("No new upgrade operations") verificados contra PostgreSQL real

## Ejercicio 4 — Contratos y CRUD (15 pts)

- [ ] DTOs por módulo (`Create` sin `id`, `Update` parcial con `exclude_unset`, `Read`) — los `schemas/` actuales son esqueletos provisorios
- [ ] Códigos 201/404/409/422, `IntegrityError` → 409 con mensaje propio (RN-12)
- [ ] Paginación `limit`/`offset` (RN-10) y filtro de título con parámetro ligado (RN-11)

## Ejercicio 5 — Altas con relaciones: ids y datos (20 pts)

- [ ] Alta de libro con `editorial_id`, `genero_id` y `autores` (`autor_id` + `rol` + `orden`); FK inexistente → 409 sin `if` previo
- [ ] Alta de venta con `cliente_id` + `renglones` anidados; precio copiado del libro y total calculado por el servidor (RN-04 a RN-07); sin `PATCH` de ventas (RN-08)

## Ejercicio 6 — Lecturas sin N+1 (10 pts)

- [ ] Carga anticipada (`joinedload` a uno, `selectinload` a colecciones); detalle de libro y de venta en N° fijo de consultas; cero carga perezosa

## Ejercicio 7 — Asincronía sin bloqueos (10 pts)

- [ ] Handlers `async def` sin llamadas bloqueantes; aviso de comprobante con `BackgroundTasks` (`asyncio.sleep(0.5)` + log)

## Entrega

- [X] Archivos `test/` C-01 a C-08 registrados, cada uno con su resultado esperado en comentarios
- [ ] Script de datos iniciales + ejecución de C-01 a C-08 contra los endpoints (requiere Fase 2)
- [ ] Evidencia C-07 (consultas en consola del detalle de libro y venta)
- [ ] Verificación final: `alembic upgrade head` sobre base vacía, app que levanta, `README` con pasos desde cero
