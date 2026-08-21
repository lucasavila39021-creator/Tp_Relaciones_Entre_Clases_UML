# Análisis - Ejercicio 8 (Aeródromo)

## 1. Sustantivos detectados
* **Avión:** Queda como Clase.
* **TipoAvion:** Queda como Clase (separado de avión porque varios aviones pueden ser del mismo tipo).
* **Hangar:** Queda como Clase.
* **Persona:** Queda como Clase (Superclase).
* **Piloto:** Queda como Clase (Subclase de Persona).
* **Mecánico:** Queda como Clase (Subclase de Persona).
* **Propietario:** Queda como Clase.
* **Servicio:** Queda como Clase intermedia (resuelve la relación M:N entre Mecánico y Avión).

## 2. Verbos que conectan clases
* se guarda (Avión en Hangar).
* es de tipo (Avión es de TipoAvion).
* es dueño de (Propietario tiene Aviones).
* realiza mantenimiento (Mecánico realiza Servicio a Avión).
* está autorizado a volar (Piloto vuela TipoAvion).
* puede dar mantenimiento (Mecánico repara TipoAvion).

## 3. Restricciones o reglas del enunciado
* No puede haber dos servicios realizados al mismo avión en la misma fecha con el mismo tipo de trabajo.

## 4. Justificación de decisiones (Herencia, Composición/Agregación y Multiplicidad)
* **Persona, Piloto y Mecánico (Herencia):** El enunciado especifica atributos comunes para "Persona" (SSN, nombre, dirección, teléfono) y luego suma atributos específicos para Mecánicos (salario, turno) y Pilotos (licencia, restricciones). Se aplica herencia (`Piloto --> Persona` y `Mecanico --> Persona`).
* **Avión y Hangar (Asociación):** Un avión se guarda en un hangar (`*` a `1`). No es composición porque el avión existe independientemente de si el hangar es destruido.
* **Mecánico, Avión y Servicio (Clase Intermedia):** Un mecánico repara muchos aviones y un avión es reparado por muchos mecánicos. Esta asociación de muchos a muchos genera datos propios (fecha, horas, tipo de trabajo), por lo que se crea la clase `Servicio`.
* **Propietario y Avión (Agregación):** El propietario es el "todo" lógico en la relación de posesión de los aviones (las partes), pero el avión tiene vida independiente.

## 5. Dudas abiertas o problemas encontrados
* El enunciado dice "fecha de adquisición por su propietario actual". Este atributo se colocó en la relación entre Avión y Propietario (o directamente en Avión, asumiendo que solo se guarda el actual).