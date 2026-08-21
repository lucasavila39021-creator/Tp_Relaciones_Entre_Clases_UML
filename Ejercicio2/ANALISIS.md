# Análisis - Ejercicio 2 (Países y Provincias)

## 1. Sustantivos detectados
* **País:** Queda como Clase.
* **Provincia:** Queda como Clase.
* **Ciudad:** Queda como Clase.
* **Continente:** Queda como Clase.
* **Capital:** Queda como atributo booleano (esCapital) dentro de Ciudad, o como un rol en la asociación.

## 2. Verbos que conectan clases
* tiene (País tiene Provincias, Provincia tiene Ciudades).
* limita con (País con País, Provincia con Provincia, Provincia con País).
* se localiza en (País en Continente).

## 3. Restricciones o reglas del enunciado
* Una de las ciudades de una provincia es su capital.
* El país también tiene una capital (que lógicamente es una ciudad).
* Las provincias de un país limitan con provincias del mismo país y pueden limitar con otros países.

## 4. Justificación de decisiones (Composición/Agregación y Multiplicidad)
* **País y Provincia (Composición):** Una provincia no tiene existencia independiente ni sentido fuera del país al que pertenece. Si se elimina el sistema del país, sus provincias desaparecen. Multiplicidad `1` a `1..*` (un país se compone de una o más provincias).
* **Provincia y Ciudad (Composición):** Mismo criterio. La ciudad pertenece a esa provincia de forma exclusiva. Multiplicidad `1` a `1..*`.
* **Continente y País (Asociación Simple):** Es una relación de localización ("se localiza en"). No hay una dependencia de ciclo de vida estricta donde el continente administre la creación/destrucción de los países. Multiplicidad `1` a `1..*`.
* **Asociaciones de "Límite" (Asociación Reflexiva y Simple):** Un país limita con muchos países (`*` a `*`), una provincia limita con muchas provincias (`*` a `*`), y una provincia puede limitar con múltiples países (`*` a `*`).

## 5. Dudas abiertas o problemas encontrados
* El enunciado dice "un país tiene una capital" y "las provincias tienen ciudades y una de ellas es su capital". Se optó por modelar una asociación simple llamada "tiene capital" desde País y Provincia hacia la clase Ciudad para evitar redundancias de atributos.