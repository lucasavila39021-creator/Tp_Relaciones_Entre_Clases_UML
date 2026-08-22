# Ejercicio 1 - Análisis (Figuras Geométricas)

## 1. Sustantivos detectados

| Sustantivo | ¿Clase o atributo? |
|---|---|
| Figura | Clase abstracta (base de la jerarquía) |
| Figura Compuesta | Clase (FiguraCompuesta, implementa el patrón Composite) |
| Elipse | Clase concreta hija de Figura |
| Círculo | Clase concreta hija de Elipse |
| Cuadrilátero | Clase abstracta hija de Poligono |
| Rectángulo | Clase concreta hija de Cuadrilatero |
| Cuadrado | Clase concreta hija de Rectangulo |
| Triángulo | Clase concreta hija de Poligono |
| Polígono | Clase abstracta hija de Figura |
| Lado | Clase |
| Punto | Clase |
| Número de lados | Atributo (numeroLados: int) en Poligono |
| Coordenada x / Coordenada y | Atributos (x: double, y: double) en Punto |

## 2. Verbos que conectan clases

| Frase | Relación |
|---|---|
| estar compuesta por | FiguraCompuesta compone a Figura (Composición) |
| ser un tipo particular de | Herencia entre subtipos y tipos base (ej. Círculo extiende Elipse, Cuadrado extiende Rectangulo) |
| tener (número de lados) | Atributo interno en Poligono |
| estar definidos por | Poligono compone a Lado, y Lado compone a Punto (Composición) |

## 3. Restricciones / reglas

- Un círculo es obligatoriamente una especialización de Elipse.
- Un cuadrado es una especialización de Rectángulo, y este a su vez de Cuadrilátero.
- Cuadriláteros y triángulos son exclusivamente polígonos.
- Todo lado se define de forma estricta por exactamente 2 puntos.
- Los polígonos requieren un mínimo de 3 lados para existir geométricamente.

## 4. Justificación composición/agregación y multiplicidades

- Una FiguraCompuesta compone a Figura (1 a *): Se modela mediante el patrón Composite. La figura compuesta gestiona el ciclo de vida y la agregación de figuras para tratarlas de forma uniforme y calcular áreas consolidadas.
- Un Poligono compone a Lado (1 a 3..*): Es composición porque los lados no tienen existencia independiente fuera del polígono que delimitan. Multiplicidad mínima de 3 lados por definición geométrica.
- Un Lado compone a Punto (1 a 2): Es composición fuerte porque un segmento depende existencialmente de sus dos extremos. Multiplicidad fija: exactamente 2 puntos por lado.
- Se utilizó Poligono como clase abstracta intermedia para centralizar la estructura de lados y vértices, separándola de las figuras curvas (Elipse), las cuales no poseen lados rectos ni vértices discretos.
