# Apache Hadoop

## 1. Motivación y Origen
- Inspirado en dos artículos de Google:
  - **The Google File System**.
  - **MapReduce: Simplified Data Processing on Large Clusters**.
- Año de origen: **2006**.
- Primera versión estable (1.0): diciembre de **2011**.

---

## 2. Apache Hadoop a Alto Nivel

### 2.1 ¿Qué es Apache Hadoop?
- Plataforma *opensource* que permite **almacenar y procesar grandes volúmenes de datos**.
- Ofrece:
  - **Bajo coste** frente a sistemas tradicionales.
  - Capacidad de **procesar datos sin importar su estructura**.
  - Arquitectura distribuida, escalable y tolerante a fallos.
  - Uso de hardware commodity (*bajo coste* y no especializado).
  - Paradigma: **procesar datos donde se almacenan**.

- Características falsas a evitar:
  - Hadoop no tiene unos requerimientos de hardware muy específicos.
  - Hadoop es escalable tanto en almacenamiento como en procesamiento.
  - Su coste es menor que el de sistemas tradicionales.

---

### 2.2 Ecosistema Hadoop y Distribuciones
- **Componentes principales**:
  - **HDFS**:
    - Sistema de archivos distribuido.
    - Organiza los datos en directorios y subdirectorios.
  - **YARN**:
    - Gestor de recursos y procesamiento.
    - Permite ejecutar aplicaciones sobre datos en HDFS.
  - **MapReduce**:
    - Motor para procesamiento masivo de datos.
    - Uso directo mediante programación o a través de aplicaciones.

- Herramientas populares:
  - **Apache Spark**: procesamiento rápido.
  - **Apache Hive**: consultas tipo SQL.
  - **Apache Kafka**: mensajería en tiempo real.

- **Estado del mercado**:
  - Auge del **cloud computing** (AWS, Azure, Google Cloud).
  - Estas plataformas ofrecen servicios Hadoop gestionados (pago por uso).
  - Muchas empresas migran de **infraestructura on-premise** al cloud.

- Resultado: la principal competencia de Cloudera no son otras distribuciones, sino los proveedores de servicios cloud.

---

### Autoevaluación: Caso de Uso
- Objetivo:
  - Integrar datos desde una base de datos relacional.
  - Almacenar los datos.
  - Consultar y procesar con un lenguaje similar a SQL.
- **Combinación adecuada de componentes**: `HDFS + YARN + Sqoop + Hive`.

---

### 2.3 Arquitectura
Hadoop utiliza un modelo distribuido instalado en múltiples servidores que trabajan conjuntamente.

- **Tipos de nodos**:
  1. **Nodos master**:
     - Controlan almacenamiento y ejecución.
     - Generalmente hay dos nodos por servicio (activo-pasivo).
  2. **Nodos worker**:
     - Ejecutan las tareas.
     - Replican datos en varios nodos para tolerancia a fallos.
  3. **Nodos edge**:
     - Interfaz entre el clúster y redes externas.
     - No son críticos pero suelen estar replicados.

- **Tolerancia a fallos**:
  - **Nodos master**:
    - Nodos en modo activo-pasivo.
    - El nodo pasivo almacena copias exactas de datos y operaciones del nodo activo.
  - **Nodos worker**:
    - Réplicas múltiples de datos.
    - El nodo master coordina tareas y monitoriza el estado de los workers.
  - **Nodos edge**:
    - Servicios redundantes para evitar puntos únicos de fallo.

- **Requisitos de hardware para nodos master**:
  - **Discos**: 2-4 TB en RAID.
  - **CPU**: 2 CPUs de 6-8 núcleos.
  - **RAM**: 128-256 GB.
  - **Red**: alta velocidad para evitar cuellos de botella.
  - **Fuente de alimentación**: redundante.

---

### 2.4 Beneficios, Desventajas y Dificultades

#### Beneficios:
- Almacena y procesa **cualquier tipo de información**.
- Los datos no necesitan un esquema fijo.
- Solución **escalable y de bajo coste**.
- Herramientas variadas para múltiples casos de uso.

#### ¿Cuándo usar Hadoop?
- **Volumen**: Datos mayores a la capacidad de sistemas tradicionales.
- **Variedad**: Datos diversos o con cambios frecuentes.
- **Escalabilidad**: Altos requerimientos en almacenamiento y procesamiento.
- **Flexibilidad**: Plataforma única para múltiples casos de uso.

#### ¿Cuándo no usar Hadoop?
- **Requisitos tradicionales**:
  - Casos donde los sistemas tradicionales son suficientes.
  - Formatos de datos fijos y sin cambios frecuentes.
- **Requisitos de transaccionalidad estrictos**:
  - Ejemplo: operaciones críticas en bancos (transferencias, pagos, etc.).
- **Casos de uso muy específicos**:
  - Situaciones de Big Data que no requieren toda la complejidad de Hadoop.

---

### Resumen de Características de Hadoop
- Almacena y procesa grandes volúmenes de datos.
- Escalable en almacenamiento y procesamiento.
- Bajo coste.
- Uso de hardware no especializado.
- Flexibilidad para diferentes tipos y volúmenes de datos.
