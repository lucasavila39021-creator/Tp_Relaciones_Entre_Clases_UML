# Análisis - Ejercicio 5 (Restaurantes y Platos)

## 1. Sustantivos detectados
* **Restaurante:** Queda como Clase.
* **Sucursal:** Queda como Clase.
* **Plato:** Queda como Clase.
* **Persona:** Queda como Clase.
* **PlatoServido:** Queda como Clase intermedia (resolución de la relación compleja de gustos).

## 2. Verbos que conectan clases
* tiene (Restaurante tiene Sucursales).
* ofrece (Restaurante ofrece Platos).
* frecuenta (Persona frecuenta Restaurantes).
* le gusta (Persona gusta de un PlatoServido en un Restaurante).

## 3. Restricciones o reglas del enunciado
* Un restaurante ofrece un máximo de 20 platos.
* A las personas les gustan los platos dependiendo de cómo los sirven en un restaurante específico, no el plato por sí mismo.

## 4. Justificación de decisiones (Composición/Agregación y Multiplicidad)
* **Restaurante y Sucursal (Composición):** Una sucursal física no existe de manera independiente sin la marca/entidad del Restaurante al que pertenece. Multiplicidad `1` a `1..*`.
* **Clase Intermedia "PlatoServido":** Como el gusto de la persona depende de la combinación Restaurante + Plato, se modela una clase `PlatoServido` que vincula ambas cosas.
* **Restaurante y PlatoServido (Asociación):** Un restaurante ofrece platos. Multiplicidad `1` a `0..20` por la restricción de que no pueden ser más de 20.
* **Persona y Restaurante (Asociación):** Relación de "frecuenta". Multiplicidad `*` a `*` (muchos a muchos).
* **Persona y PlatoServido (Asociación):** Relación de "le gusta". Multiplicidad `*` a `*`.

## 5. Dudas abiertas o problemas encontrados
* La relación "le gusta" originalmente era una asociación ternaria entre Persona, Plato y Restaurante. Se optó por simplificarla creando la clase `PlatoServido` para mantener el diagrama claro y legible en Markdown.