# Almacenamiento de Datos

## 1. Sistemas de Ficheros
Un sistema de ficheros organiza y almacena datos en dispositivos como discos duros, SSD, cintas o DVDs. Existen múltiples tipos: FAT32, NTFS, EXT4, entre otros.

### 1.1 RAID
RAID distribuye datos en múltiples unidades para aumentar capacidad, seguridad o rendimiento:
- **RAID 0**: Sin redundancia, combina discos para mayor capacidad y velocidad.
- **RAID 1**: Replicación automática, prioriza seguridad.
- **RAID 5**: Distribuye datos y paridad, tolera fallos de un disco.

### 1.2 Sistemas de Ficheros Distribuidos
Distribuyen datos entre varias máquinas de un clúster, simulando un único sistema:
- **Ejemplos**: HDFS (Hadoop), Amazon S3, Google Cloud Storage.
- **En memoria**: Minimiza latencia; ideal para analítica en tiempo real o consultas iterativas.

#### 1.3 Hadoop Distributed File System (HDFS)
- Divide ficheros en bloques grandes (128 MB por defecto).
- Incluye características como "rack awareness" para optimizar rendimiento.

## 2. Bases de Datos NoSQL
Bases de datos no relacionales diseñadas para manejar grandes volúmenes de datos distribuidos.

### 2.1 Conceptos Generales
- **Sharding**: Divide datos en subconjuntos distribuidos en un clúster.
- **Replicación**: Crea copias de datos en diferentes nodos.
- **Sharding con replicación**: Combina ambas técnicas para mayor escalabilidad y seguridad.

### 2.2 Tipos de NoSQL
- **Documentales**: Clave-documento, típicamente en JSON.
- **Clave-Valor**: Clave identifica un valor arbitrario.
- **Columnares**: Almacenan datos por columnas (inspirados en BigTable de Google).
- **Orientadas a grafo**: Modelan nodos y relaciones con propiedades.

## 3. Primeros Pasos con MongoDB
Introducción a MongoDB, una de las bases de datos NoSQL más populares, destacada por su enfoque en documentos.
