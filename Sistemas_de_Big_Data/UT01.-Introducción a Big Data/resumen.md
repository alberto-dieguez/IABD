# Introducción a Big Data

## 1. ¿Por qué Big Data?
Big Data surge para procesar grandes y complejos volúmenes de datos que requieren herramientas no tradicionales.

### 1.1. Las 5 Vs
1. **Volumen**: Gran cantidad de datos (usuarios, transacciones, etc.).
2. **Velocidad**: Datos generados y procesados rápidamente.
3. **Variedad**:
   - **Estructurados**: Tablas de bases de datos.
   - **No estructurados**: Videos, imágenes.
   - **Semiestructurados**: CSV, XML, JSON.
4. **Veracidad**: Datos de calidad variable (ruido vs. señal).
5. **Valor**: Utilidad de los datos para empresas o personas.

### 1.2. Qué conseguimos gracias a Big Data
Big Data permite:
- Capturar, integrar y almacenar datos de forma distribuida.
- Procesarlos con múltiples máquinas en paralelo.
- Crear modelos predictivos mediante minería de datos.
- Apoyar decisiones con visualizaciones y análisis.

**Beneficios:**
- Optimizar operaciones empresariales.
- Predecir tendencias y detectar fraudes.
- Apoyar descubrimientos científicos y médicos.

### 1.2.1. Desde los eventos al valor
- **Datos**: Observaciones (ej. "Llueve 4 mm").
- **Información**: Contexto de los datos.
- **Conocimiento**: Relaciones entre datos.
- **Sabiduría**: Predicciones basadas en modelos.
- **Valor**: Mejores decisiones basadas en datos.

## 2. Clusters de computadoras
Un clúster es un conjunto de computadoras conectadas que trabajan como una sola unidad, ofreciendo:
- **Alto rendimiento**: Más recursos combinados.
- **Alta disponibilidad**: Respaldo ante fallos.
- **Equilibrado de carga**: Distribución eficiente del trabajo.
- **Escalabilidad**:
  - **Vertical**: Mejora de hardware.
  - **Horizontal**: Añadir más nodos.

## 3. Conceptos de almacenamiento de datos
### 3.1. Base de datos relacional
Almacena información en tablas organizadas en filas y columnas.

### 3.2. Dataset
Colección de datos relacionados, como:
- Tweets.
- Posts.

### 3.3. Almacén de datos
Repositorio central para datos históricos y actuales.

### 3.4. Data lake
Repositorio para datos en bruto:
- **Estructurados**: Datos estándar (Excel).
- **No estructurados**: Videos, imágenes.
- **Semiestructurados**: HTML, correos electrónicos.

### 3.5. ACID
Propiedades de bases de datos transaccionales:
- **Atomicidad**: Operaciones completas o nulas.
- **Consistencia**: Estados válidos.
- **Aislamiento**: Procesos independientes.
- **Durabilidad**: Datos permanentes tras confirmación.

### 3.6. Teorema CAP
Bases de datos distribuidas pueden cumplir máximo 2 de 3 propiedades:
- **Consistencia**.
- **Disponibilidad**.
- **Tolerancia a particionamiento**.

### 3.7. BASE
Modelo de diseño flexible para bases de datos distribuidas:
- **Básicamente disponible**.
- **Estado blando**.
- **Consistencia eventual**.

## 4. Conceptos de procesamiento de datos
### Procesamiento en paralelo
Varias tareas ejecutadas simultáneamente en un procesador.

### Procesamiento distribuido
Tareas ejecutadas en múltiples máquinas conectadas en red.

### Estrategias de procesamiento
- **OLTP**: Procesamiento transaccional en tiempo real.
- **OLAP**: Procesamiento analítico para consultas.

### Principio SCV
Propiedades en sistemas distribuidos:
- **Velocidad**.
- **Consistencia**.
- **Volumen**.

## 5. Arquitectura por capas de Big Data
1. **Capa de ingestión**: Obtención de datos desde múltiples fuentes.
2. **Capa de colección**: Unificación y estructuración de datos.
3. **Capa de almacenamiento**: Sistemas distribuidos para guardar datos.
4. **Capa de procesamiento**: Infraestructura para análisis.
5. **Capa de consulta y analítica**: Generación de valor con algoritmos y análisis.
6. **Capa de visualización**: Interacción mediante reportes y dashboards.
7. **Capa de seguridad**: Protección física y lógica de datos.
8. **Capa de monitorización**: Auditoría y control para garantizar calidad.

## 6. El paisaje de Big Data
Herramientas y tecnologías:
- **Hadoop**.
- **HDFS, Sqoop**.
- **Spark**.
- **Kafka**.

### 6.1. Roles y empleos
- Administrador de bases de datos.
- Ingeniero de datos.
- Analista de datos.
- Científico de datos.
