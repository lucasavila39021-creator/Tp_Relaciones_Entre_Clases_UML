2. Análisis de Texto del Enunciado

Sustantivos Detectados:

Figura: Quedó como Clase Abstracta (base de la jerarquía).

Figura Básica / Compuesta: Quedó como Clase FiguraCompuesta (implementa el patrón Composite).

Elipse, Círculo, Cuadrilátero, Rectángulo, Cuadrado, Triángulo: Quedaron como Clases concretas/hijas.

Polígono: Quedó como Clase Abstracta.

Lado: Quedó como Clase.

Punto: Quedó como Clase.

Número de lados: Quedó como Atributo (numeroLados: int) en Poligono.

Coordenada x / Coordenada y: Quedaron como Atributos (x: double, y: double) en Punto.

Verbos que Conectan Clases:

Estar compuesta por: Relación estructural de Composición entre FiguraCompuesta y Figura.

Ser un tipo particular de: Relación de Herencia (Generalización / Especialización) entre subtipos y tipos base (ej. Círculo ➔ Elipse, Cuadrado ➔ Rectángulo ➔ Cuadrilátero ➔ Polígono ➔ Figura).

Tener (número de lados): Atributo interno en Poligono.

Estar definidos por: Relación de Composición entre Lado y Punto, y entre Poligono y Lado.

Restricciones y Reglas del Enunciado:

Un círculo es obligatoriamente una especialización de elipse.

Un cuadrado es una especialización de rectángulo, y este a su vez de cuadrilátero.

Cuadriláteros y triángulos son exclusivamente polígonos.

Todo lado se define de forma estricta por exactamente 2 puntos.

Los polígonos requieren un mínimo de 3 lados para existir geométricamente.

3. Justificación de Decisiones de Diseño

Relaciones Todo-Parte:

Una FiguraCompuesta compone a Figura (Composición, 1 a *): Se modela mediante el patrón Composite. La figura compuesta gestiona el ciclo de vida y la agregación de figuras para tratarlas de forma uniforme y calcular áreas consolidadas.

Un Poligono compone a Lado (Composición, 1 a 3..*): Es composición porque los lados no tienen existencia independiente fuera del polígono que delimitan. Multiplicidad: un polígono posee como mínimo 3 lados (3..*).

Un Lado compone a Punto (Composición, 1 a 2): Es composición fuerte debido a que un segmento/lado geométrico depende existencialmente de sus dos extremos. Multiplicidad: exactamente 2 puntos por lado (1 a 2).

Jerarquía de Herencia:

Se utilizó Poligono como clase abstracta intermedia para centralizar la estructura de lados y vértices, separándola de las figuras curvas (Elipse), las cuales no poseen lados rectos ni vértices discretos.