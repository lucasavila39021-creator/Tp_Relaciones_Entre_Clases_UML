2.
Museo se quedo como una clase Contenedora del dominio

Objeto de Arte quedo como una clase abstracta

Pintura, Escultura, Otro quedaron como subclases de ObjetoDeArte

Pertenencia/Coleccion/ Permanente/En Prestamo quedaron como Clases (estado legal, administrativo, etc)

Artista quedo como una clase independiente

Coleccion Externa quedo como una clase independiente

Exposicion quedo como clase

Nº identificación, título, descripción, año de creación, país, cultura, época quedaron como los atributos de ObjetoDeArte

Tipo de pintura, soporte, estilo quedaron como atributos de la clase Pintura

Material, altura, peso, estilo quedaron como atributos en Escultura

Fecha de adquisición, coste, en exposición quedaron como atributos en ColeccionPermanente

Fecha de recepción, fecha de devolución quedaron como atributos en EnPrestamo

nombre, fecha de nacimiento/defunción, país de origen, época, estilo, descripción: Quedaron como Atributos en Artista

nombre, tipo, dirección, teléfono, contacto: Quedaron como Atributos en ColeccionExterna

nombre, fecha de inicio, fecha de fin: Quedaron como Atributos en Exposicion

##Verbos encontrados que conectan clases##

Tener (como una coleccionde objetos/exposiciones) -> Relacion de Composicion/Agregacion desde Museo

Clasificarse en / distinguirse ->Relacion de Herencia entre ObjetoDeArte y sus subtipos, y entre Pertenencia y sus subtipos

Crear / ser creado por: Relación de Asociación entre ObjetoDeArte y Artista.

Pertenecer a (colección externa): Relación de Asociación entre EnPrestamo y ColeccionExterna.

Exhibir / incluir: Relación de Agregación entre Exposicion y ObjetoDeArte.

Restricciones y Reglas del Enunciado:

El artista y el año de creación pueden ser desconocidos (atributos opcionales / multiplicidad 0..1).

El nombre del artista y el nombre de la colección externa son únicos (identificadores clave).

Una obra pertenece exclusivamente a una modalidad: o es de la colección permanente del museo o está en calidad de préstamo.

Una exposición agrupa un conjunto de objetos de arte durante un intervalo de tiempo definido.

3. Diseño

Relaciones Todo-Parte (Composición vs. Agregación):

Un Museo compone a ObjetoDeArte (Composición, 1 a *): El catálogo de inventario pertenece al museo.

Un ObjetoDeArte compone a Pertenencia (Composición, 1 a 1): Cada objeto posee estrictamente un único estado de pertenencia que define sus datos administrativos. Se utiliza composición para evitar problemas de herencia múltiple en lenguajes como Java (permitiendo que una Pintura sea ColeccionPermanente sin duplicar clases como PinturaPermanente o PinturaEnPrestamo).

Una Exposicion agrega a ObjetoDeArte (Agregación, * a 1..*): Se modela como agregación porque las obras de arte existen de forma independiente a la exposición temporal; la finalización de una exposición no destruye las obras exhibidas.

Un Museo agrega a Exposicion (Agregación, 1 a *): El museo organiza eventos que tienen un ciclo de vida propio delimitado por fechas.

Multiplicidades Elegidas:

ObjetoDeArte conoce al Artista (* a 0..1): Un artista puede tener varias obras en el museo, pero una obra puede ser anónima (0..1).

Un EnPrestamo se asocia a ColeccionExterna (* a 1): Muchas obras en préstamo pueden provenir de la misma colección externa o institución prestamista.

Una Exposicion se asocia a ObjetoDeArte (* a 1..*): Una exposición exhibe al menos un objeto de arte, y un objeto puede haber participado en múltiples exposiciones históricas.