# Ecosistema Hadoop

## 1. Introducción al ecosistema Hadoop
Hadoop Core está compuesto por:
- **HDFS**: Capa de almacenamiento.
- **YARN**: Gestor de procesos en el clúster.
- **MapReduce**: Modelo de programación para procesamiento de datos.

Para dotar a Hadoop de funcionalidades adicionales, se utilizan proyectos open-source de Apache, formando el **ecosistema Hadoop**:

### Componentes principales:
- **Acceso y procesamiento de datos**: Apache Pig, Apache Hive.
- **Ingesta y flujos de trabajo**: Apache Sqoop, Apache Flume.
- **Interfaces y herramientas**: Apache Hue, Apache Zeppelin.
- **Procesamiento en streaming**: Apache Kafka, Apache Spark.

---

## 2. Componentes de acceso y procesamiento de datos

### 2.1. Apache Pig
- Proporciona comandos para filtrar, agrupar, leer, cargar, guardar y unir datos.

### 2.2. Apache Hive
- Componente muy utilizado que ofrece un lenguaje de consultas llamado **HQL**.
- Define una estructura relacional y usa motores estándar de Hadoop.

#### **2.2.1. Conceptos generales**
- Hadoop necesita programación en MapReduce para explotación de datos.
- Hive permite consultas estructuradas sin necesidad de MapReduce.

#### **2.2.2. Arquitectura**
- **Cliente**: Thrift Server, Cliente JDBC, Cliente ODBC.
- **Servicios Hive**: HiveServer, Driver, Metastore.
- **Hadoop**: Ejecuta consultas mediante YARN.

#### **2.2.3. HQL (Hive Query Language)**
- **DDL** (Data Definition Language): Crea y modifica estructuras de datos.
- **DML** (Data Manipulation Language): Inserción, modificación y consulta de datos.

### 2.3. Apache Impala
- Alta velocidad para consultas.
- Soporta almacenamiento en **HBase** y **HDFS**.

### 2.4. Apache HBase
- Base de datos NoSQL sobre Hadoop.
- Modelo **clave-valor**, almacena datos en **HDFS**.
- Accesible mediante API (Thrift, Avro, HTTP RestFul).

### 2.5. Apache Phoenix
- Capa SQL sobre HBase.
- Permite conexiones JDBC y consultas SQL con alto rendimiento.

### 2.6. Apache Spark
- Plataforma de procesamiento en paralelo.
- Permite almacenamiento en memoria para mejorar rendimiento.

#### **2.6.1. Arquitectura y componentes**
- **Spark SQL**: Consultas SQL.
- **Structured Streaming**: Procesamiento en tiempo real.
- **MLLib**: Machine Learning.
- **GraphX**: Modelos basados en grafos.
- **SparkR**: Conexión con R.

#### **2.6.2. Detalle de componentes**
- **Spark Core**: Núcleo de la plataforma.
- **SparkSQL**: Procesamiento de datos estructurados.
- **GraphX**: Computación de grafos.
- **MLLib**: Machine Learning en Hadoop.

#### **2.6.3. Ventajas y desventajas**
- API rica y eficiente.
- Uso de memoria para persistencia temporal.
- Optimización compleja.

---

## 3. Componentes de ingesta de datos y flujos de trabajo

### 3.1. Apache Sqoop
- Transfiere datos entre **Hadoop** y bases de datos relacionales.

### 3.2. Apache Flume
- Sistema distribuido de recolección de datos.
- **Componentes**:
  - **Sources**: Obtienen datos de fuentes externas.
  - **Channels**: Almacenan datos temporalmente.
  - **Sinks**: Envía datos a almacenamiento (ej. HDFS).

### 3.3. Apache Oozie
- Automatiza flujos de trabajo en Hadoop.

---

## 4. Interfaces y herramientas de trabajo

### 4.1. Hue
- Interfaz web para consultas y navegación en Hadoop.

### 4.2. Apache Zeppelin
- Herramienta para análisis de datos interactivo.

### 4.3. Apache Ambari y Cloudera Manager
- Monitoreo y administración de clústeres Hadoop.

---

## 5. Procesamiento en streaming
- **Apache Spark (Structured Streaming)**
- **Apache Flink**
- **Apache Storm**

---

## 6. Guía práctica Hive y Pig
- **Hive**: Consultas estructuradas sobre datos en Hadoop.
- **Pig**: Transformaciones de datos con un lenguaje más flexible.