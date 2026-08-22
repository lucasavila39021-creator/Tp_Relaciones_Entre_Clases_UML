# Ejercicio 6 - Análisis (Parques Naturales)

## 1. Sustantivos detectados

| Sustantivo | ¿Clase o atributo? |
|---|---|
| Comunidad Autónoma (CA) | Clase (ComunidadAutonoma) |
| Organismo Responsable | Clase (o atributo dentro de ComunidadAutonoma) |
| Parque Natural (PN) | Clase (ParqueNatural) |
| Área | Clase (Area) |
| Entrada | Clase (Entrada) |
| Especie | Clase abstracta base (Especie) |
| Especie Vegetal, Especie Animal | Clases hijas de Especie |
| Herbívoras, Carnívoras, Omnívoras | Enum (TipoAlimentacion) |
| Censo / Población | Clase de asociación (CensoEspecie) para registrar individuos por área |
| Visitante | Clase (Visitante) |
| Alojamiento | Clase (Alojamiento) |
| Estancia | Clase de asociación entre Visitante y Alojamiento |
| Excursión | Clase (Excursion) |
| Personal | Clase base de datos personales/laborales |
| Cargo / Rol | Clase abstracta (patrón Role) |
| Guarda, Celador, Investigador | Clases hijas de Cargo |
| Vehículo | Atributos en Guarda (tipo, matricula) |
| Registro de Visita | Clase gestionada por Celador |
| Proyecto de Investigación | Clase (ProyectoInvestigacion) |
| DNI, nombres, sueldos, teléfonos, fechas, km2, presupuestos | Atributos identificativos/descriptivos en sus respectivas clases |

## 2. Verbos que conectan clases

| Frase | Relación |
|---|---|
| extenderse por (CAs) | Asociación \*..* entre ComunidadAutonoma y ParqueNatural |
| dividirse en / poseer (áreas, entradas, alojamientos) | Un ParqueNatural compone a Area, Entrada y Alojamiento (Composición) |
| residir en / censar | Relación mediante la clase intermedia CensoEspecie entre Area y Especie |
| servir de alimento a (cadena trófica) | Asociación recursiva \*..* en EspecieAnimal hacia Especie |
| utilizar / alojarse | Relación mediante la clase intermedia Estancia entre Visitante y Alojamiento |
| organizar (excursiones) | Asociación \*..* entre Alojamiento y Excursion |
| inscribirse en | Asociación \*..* entre Visitante y Excursion |
| desempeñar (cargos) | Un Personal compone a Cargo (Composición, 1 a 1..*) |
| asignar a (área/entrada) | Asociación de Guarda hacia Area y de Celador hacia Entrada |
| registrar (visitas) | Asociación entre Celador, RegistroVisita y Visitante |
| participar en / investigar | Asociación \*..* entre Investigador, ProyectoInvestigacion y Especie |

## 3. Restricciones / reglas

- Un parque puede abarcar varias CAs y una CA puede tener varios parques.
- Los nombres de parques son únicos a nivel global.
- Los nombres de áreas y alojamientos son únicos dentro de su respectivo parque (dependencia de contexto).
- Las entradas se numeran secuencialmente del 1 al N para cada parque.
- Una persona puede desempeñar múltiples cargos simultáneos (ej. Guarda e Investigador).
- Varios guardas pueden estar asignados a una misma área y varios celadores a una misma entrada.
- El censo de individuos es específico para cada combinación de área y especie.

## 4. Justificación composición/agregación y multiplicidades

- **Patrón Role para Personal**: Para satisfacer la regla de que "una persona puede desempeñar varios cargos al mismo tiempo", se desacopló la identidad de la persona (Personal) de sus funciones (Cargo). Si se usara herencia simple (Personal extiende Guarda), no se podría modelar a alguien con dos cargos sin recurrir a herencia múltiple (inexistente en Java).
- **Un ParqueNatural compone a Area, Entrada y Alojamiento**: Es composición porque estas entidades no tienen ciclo de vida ni sentido de existencia fuera del parque al que pertenecen.
- **CensoEspecie (clase de asociación)**: El número de individuos no pertenece ni al área sola ni a la especie sola, sino a la intersección de ambas.
- **Estancia (clase de asociación)**: Permite almacenar el número de habitación, fecha de inicio y fecha de fin para cada visita de un usuario a un alojamiento.

## 5. Dudas abiertas

- **Sueldo único vs. sueldo por cargo**: El enunciado indica "para todos ellos se guarda su sueldo", ubicándolo a nivel de la persona (Personal). Si en el futuro se requiriera liquidar sueldos independientes por cada rol desempeñado, el atributo debería migrar a la clase Cargo.
- **Control de capacidad en alojamientos**: Se modeló la capacidad total como atributo numérico en Alojamiento, quedando para la capa de lógica de negocio validar que la concurrencia de Estancias no supere dicho límite.
- **Asignación de vehículos**: Se asumió que los datos del vehículo (tipo y matrícula) son propios de la asignación del Guarda. Si los vehículos pertenecieran a una flota compartida del parque, convendría modelar una entidad independiente Vehiculo.
