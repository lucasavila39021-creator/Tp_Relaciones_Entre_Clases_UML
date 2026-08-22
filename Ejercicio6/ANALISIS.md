Comunidad Autónoma (CA): Quedó como Clase.

Organismo Responsable: Quedó como Clase (o atributo dentro de ComunidadAutonoma).

Parque Natural (PN): Quedó como Clase.

Área: Quedó como Clase.

Entrada: Quedó como Clase.

Especie: Quedó como Clase Abstracta base.

Especie Vegetal, Especie Animal: Quedaron como Clases Hijas (Subclases) de Especie.

Herbívoras, Carnívoras, Omnívoras: Quedó como un Enum (TipoAlimentacion).

Censo / Población: Quedó como Clase de Asociación (CensoEspecie) para registrar individuos por área.

Visitante: Quedó como Clase.

Alojamiento: Quedó como Clase.

Estancia: Quedó como Clase de Asociación entre Visitante y Alojamiento.

Excursión: Quedó como Clase.

Personal: Quedó como Clase base de datos personales/laborales.

Cargo / Rol: Quedó como Clase Abstracta (patrón Role).

Guarda, Celador, Investigador: Quedaron como Clases Hijas (Subclases) de Cargo.

Vehículo: Atributos en Guarda (tipo, matricula).

Registro de Visita: Quedó como Clase gestionada por Celador.

Proyecto de Investigación: Quedó como Clase.

Atributos identificativos/descriptivos: DNI, nombres, sueldos, teléfonos, fechas, km2, presupuestos, etc.

Verbos que Conectan Clases:

Extenderse por (CAs): Relación de Asociación *..* entre ComunidadAutonoma y ParqueNatural.

Dividirse en / poseer (áreas, entradas, alojamientos): Relaciones de Composición desde ParqueNatural.

Residir en / censar: Relación mediante la clase intermedia CensoEspecie entre Area y Especie.

Servir de alimento a (cadena trófica): Relación de Asociación recursiva *..* en EspecieAnimal hacia Especie.

Utilizar / alojarse: Relación mediante la clase intermedia Estancia entre Visitante y Alojamiento.

Organizar (excursiones): Relación de Asociación *..* entre Alojamiento y Excursion.

Inscribirse en: Relación de Asociación *..* entre Visitante y Excursion.

Desempeñar (cargos): Relación de Composición 1 a 1..* entre Personal y Cargo.

Asignar a (área/entrada): Asociaciones de Guarda hacia Area y de Celador hacia Entrada.

Registrar (visitas): Composición/Asociación entre Celador, RegistroVisita y Visitante.

Participar en / investigar: Asociación *..* entre Investigador, ProyectoInvestigacion y Especie.

Restricciones y Reglas del Enunciado:

Un parque puede abarcar varias CAs y una CA puede tener varios parques.

Los nombres de parques son únicos a nivel global.

Los nombres de áreas y alojamientos son únicos dentro de su respectivo parque (dependencia de contexto).

Las entradas se numeran secuencialmente del 1 al N para cada parque.

Una persona puede desempeñar múltiples cargos simultáneos (ej. Guarda e Investigador).

Varios guardas pueden estar asignados a una misma área y varios celadores a una misma entrada.

El censo de individuos es específico para cada combinación de área y especie.

3. Justificación de Decisiones de Diseño

Patrón Role para Personal (Composición vs. Herencia directa):

Para satisfacer la regla de que “una persona puede desempeñar varios cargos al mismo tiempo”, se desacopló la identidad de la persona (Personal) de sus funciones (Cargo). Si se usara herencia simple (Personal <|-- Guarda), no se podría modelar a alguien con dos cargos sin recurrir a herencia múltiple (inexistente en Java).

Clases de Asociación Intermedias (CensoEspecie y Estancia):

CensoEspecie: El número de individuos no pertenece ni al área sola ni a la especie sola, sino a la intersección de ambas.

Estancia: Permite almacenar el número de habitación, fecha de inicio y fecha de fin para cada visita de un usuario a un alojamiento.

Composición en Elementos del Parque:

Un ParqueNatural compone a Area, Entrada y Alojamiento (Composición): Es composición porque estas entidades no tienen ciclo de vida ni sentido de existencia fuera del parque al que pertenecen.

4. Dudas Abiertas o Problemas Encontrados

Sueldo Único vs. Sueldo por Cargo: El enunciado indica "para todos ellos se guarda su sueldo", ubicándolo a nivel de la persona (Personal). Si en el futuro se requiriera liquidar sueldos independientes por cada rol desempeñado, el atributo debería migrar a la clase Cargo.

Control de Capacidad en Alojamientos: Se modeló la capacidad total como atributo numérico en Alojamiento, quedando para la capa de lógica de negocio validar que la concurrencia de Estancias no supere dicho límite.

Asignación de Vehículos: Se asumió que los datos del vehículo (tipo y matrícula) son propios de la asignación del Guarda. Si los vehículos pertenecieran a una flota compartida del parque, convendría modelar una entidad independiente Vehiculo.