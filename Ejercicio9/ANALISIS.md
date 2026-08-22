# Ejercicio 9 - Análisis (Museo de Arte)

## 1. Sustantivos detectados

| Sustantivo | ¿Clase o atributo? |
|---|---|
| Museo | Clase contenedora del dominio |
| Objeto de Arte | Clase abstracta (ObjetoDeArte) |
| Pintura | Clase concreta hija de ObjetoDeArte |
| Escultura | Clase concreta hija de ObjetoDeArte |
| Otro | Clase concreta hija de ObjetoDeArte |
| Pertenencia | Clase abstracta (estado legal/administrativo de una obra) |
| Colección Permanente | Clase hija de Pertenencia |
| En Préstamo | Clase hija de Pertenencia |
| Artista | Clase independiente |
| Colección Externa | Clase independiente |
| Exposición | Clase (Exposicion) |
| Nº identificación, título, descripción, año de creación, país, cultura, época | Atributos de ObjetoDeArte |
| Tipo de pintura, soporte, estilo | Atributos de Pintura |
| Material, altura, peso, estilo | Atributos de Escultura |
| Fecha de adquisición, coste, en exposición | Atributos de ColeccionPermanente |
| Fecha de recepción, fecha de devolución | Atributos de EnPrestamo |
| nombre, fecha de nacimiento/defunción, país de origen, época, estilo, descripción | Atributos de Artista |
| nombre, tipo, dirección, teléfono, contacto | Atributos de ColeccionExterna |
| nombre, fecha de inicio, fecha de fin | Atributos de Exposicion |

## 2. Verbos que conectan clases

| Frase | Relación |
|---|---|
| tener (colección de objetos/exposiciones) | Un Museo compone a ObjetoDeArte y agrega a Exposicion |
| clasificarse en / distinguirse | Herencia entre ObjetoDeArte y sus subtipos (Pintura, Escultura, Otro), y entre Pertenencia y sus subtipos |
| crear / ser creado por | Asociación entre ObjetoDeArte y Artista |
| pertenecer a (colección externa) | Asociación entre EnPrestamo y ColeccionExterna |
| exhibir / incluir | Una Exposicion agrega a ObjetoDeArte (Agregación) |

## 3. Restricciones / reglas

- El artista y el año de creación pueden ser desconocidos (atributos opcionales, multiplicidad 0..1).
- El nombre del artista y el nombre de la colección externa son únicos (identificadores clave).
- Una obra pertenece exclusivamente a una modalidad: o es de la colección permanente del museo o está en calidad de préstamo.
- Una exposición agrupa un conjunto de objetos de arte durante un intervalo de tiempo definido.

## 4. Justificación composición/agregación y multiplicidades

- **Un Museo compone a ObjetoDeArte (1 a \*)**: El catálogo de inventario pertenece al museo. Las obras no tienen existencia fuera del museo que las registra.
- **Un ObjetoDeArte compone a Pertenencia (1 a 1)**: Cada obra posee estrictamente un único estado de pertenencia que define sus datos administrativos. Se utiliza composición para evitar problemas de herencia múltiple en Java (evitando clases como PinturaPermanente o PinturaEnPrestamo).
- **Una Exposicion agrega a ObjetoDeArte (\* a 1..\*)**: Se modela como agregación porque las obras existen de forma independiente a la exposición temporal; la finalización de una exposición no destruye las obras exhibidas.
- **Un Museo agrega a Exposicion (1 a \*)**: El museo organiza eventos que tienen un ciclo de vida propio delimitado por fechas.
- **Un ObjetoDeArte se asocia a Artista (\* a 0..1)**: Un artista puede tener varias obras en el museo, pero una obra puede ser anónima (0..1).
- **Un EnPrestamo se asocia a ColeccionExterna (\* a 1)**: Muchas obras en préstamo pueden provenir de la misma colección externa o institución prestamista.
- **Una Exposicion se asocia a ObjetoDeArte (\* a 1..\*)**: Una exposición exhibe al menos un objeto de arte, y un objeto puede haber participado en múltiples exposiciones históricas.
