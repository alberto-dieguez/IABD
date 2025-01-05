# Almacenamiento y Procesamiento en Hadoop

## Componentes Principales
- **HDFS (Hadoop Distributed File System)**: Capa de almacenamiento.
- **YARN (Yet Another Resource Negotiator)**: Gestor de procesos en el clúster.
- **MapReduce**: Modelo de programación para tareas de procesamiento de datos.

## 1. HDFS

### 1.1 Introducción
- HDFS es un sistema de almacenamiento distribuido.
- Inspirado en el Google File System.
- Diseñado para ejecutarse sobre hardware commodity.
- Optimizado para almacenar ficheros de gran tamaño.
- Escalabilidad horizontal.
- Sin restricciones sobre los tipos de datos.
- Filosofía "write-once, read-many".

### 1.2 Arquitectura
- **Namenode**: Actúa como maestro, gestiona la estructura de directorios, metadatos y ubicación de bloques. Coordina todas las operaciones de lectura y escritura.
- **Secondary Namenode**: Almacena puntos de control de los metadatos del Namenode. No es un nodo de respaldo, pero reduce el tiempo de arranque del Namenode.
  - **FsImage**: Instantánea de los metadatos.
  - **EditLog**: Registro de cambios en los metadatos.
- **Datanodes**: Almacenan o leen bloques. Envían informes al Namenode y detectan corrupción de bloques mediante checksums.

### 1.3 Funcionamiento

#### Lectura
1. El cliente solicita al Namenode información sobre los bloques del fichero.
2. El Namenode devuelve una lista ordenada de Datanodes que contienen los bloques.
3. El cliente se comunica directamente con los Datanodes para leer los bloques.

#### Escritura
1. El cliente solicita al Namenode la creación del fichero.
2. Tras verificar permisos y existencia del fichero, el Namenode devuelve un OK.
3. El cliente divide el fichero en bloques y solicita al Namenode dónde escribir cada bloque.
4. El cliente escribe directamente en el primer Datanode. Este Datanode replica el bloque a otros Datanodes.

### 1.4 Uso
- Operaciones soportadas: lectura, escritura, borrado de ficheros, creación de directorios, gestión de usuarios, grupos y permisos.
- Interfaces disponibles: CLI, Java API, RESTful API (WebHDFS), NFS Gateway, Librería C.

## 2. YARN

### 2.1 Introducción
- YARN gestiona recursos y coordina la ejecución de aplicaciones en el clúster.
- Funciones:
  - Ofrece una API más flexible que MapReduce.
  - Ejecuta código en diferentes nodos.
  - Sincroniza y monitoriza aplicaciones.
  - Gestiona recursos y disponibilidad de nodos.

### 2.2 Arquitectura

#### Contenedores
- Unidad mínima de recursos, incluyendo memoria, núcleos de CPU, disco, y red.

#### Nodos y Servicios
- **ResourceManager**: Nodo maestro que coordina tareas, asigna y controla recursos.
  - **ApplicationsMaster**: Recibe peticiones de ejecución.
  - **Scheduler**: Establece prioridades y asigna recursos.
    - **Capacity Scheduler**: Define colas de ejecución.
    - **Fair Scheduler**: Asigna recursos de forma equitativa.
    - **FIFO Scheduler**: Prioriza según el orden de llegada.
- **NodeManager**: Ejecuta en nodos worker, monitoriza recursos y supervisa contenedores.
- **ApplicationMaster**: Proceso por aplicación que negocia recursos con el ResourceManager.

### 2.3 Funcionamiento
1. El cliente solicita al ResourceManager la ejecución de una aplicación.
2. El ApplicationsMaster, tras verificar disponibilidad de recursos, solicita la creación de un contenedor.
3. El NodeManager crea y ejecuta el contenedor.
4. El ApplicationMaster gestiona la ejecución de la aplicación y reporta el estado al ResourceManager.

## 3. MapReduce

### 3.1 Introducción
- Framework diseñado para procesar grandes volúmenes de datos en paralelo.
- Basado en la filosofía "Divide y Vencerás".
- Ejecución distribuida en múltiples nodos de hardware commodity.
- Confiable y tolerante a fallos.

### 3.2 Funcionamiento
Un trabajo de MapReduce se compone de cinco etapas:
1. **Envío del trabajo**: El cliente envía el trabajo al clúster.
2. **Fase map**: Se ejecutan funciones de mapeo para procesar cada entrada.
3. **Fase shuffle**: Se agrupan los resultados intermedios.
4. **Fase order**: Se ordenan los datos para la fase final.
5. **Fase reduce**: Se combinan los resultados en la salida final.

