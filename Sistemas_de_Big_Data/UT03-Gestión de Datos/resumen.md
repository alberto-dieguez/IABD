# Gestión de Datos

En esta unidad de trabajo se aborda la gestión de datos en entornos de **Big Data**.

## 1. ETL

ETL (*Extract, Transform, Load*) es un proceso para unificar datos desde diversas fuentes y enviarlos a un almacenamiento de destino. Se compone de tres fases:

### 1.1. Fases de ETL
- **Extraer**: Obtención de datos desde múltiples fuentes.
- **Transformar**: Limpieza y conversión de datos al formato deseado.
- **Cargar**: Almacenamiento de los datos en su destino final.

### 1.1.1. Extraer
Se extraen datos de diversas fuentes, incluyendo flujos de datos (*streams*).

### 1.1.2. Transformar
Se aplican reglas para asegurar la calidad y formato de los datos.

### 1.1.3. Cargar
Proceso final de almacenamiento de los datos transformados.

### 1.2. Herramientas
- **Apache Sqoop**: Transferencia de datos desde bases de datos relacionales a Hadoop.
- **Apache Flume**: Recolección de datos en *streaming* desde fuentes no estructuradas.

## 2. Integración de Datos
Busca ofrecer una visión unificada de los datos.

### 2.1. Técnicas de Integración de Datos
- **Integración manual**: Acceso directo a los sistemas de origen.
- **Integración basada en aplicación**: Aplicaciones gestionan la integración.
- **Integración basada en middleware**: Se usa una capa intermedia.
- **Integración virtual**: Los datos permanecen en su origen y se accede mediante una vista unificada.

## 3. Normativa de Tratamiento de Datos
Regulada por el RGPD y otras normativas.

### 3.1. Definiciones clave
- **Datos personales**
- **Responsable del tratamiento**
- **Encargado del tratamiento**
- **Delegado de protección de datos (DPO)**

### 3.2. Ámbito de aplicación y bases legales
Regulado en los artículos 2 y 3 del RGPD.

### 3.3. Derechos de los Interesados
- **Derecho de acceso**: Obtener copia de los datos.
- **Derecho de rectificación**: Corregir datos erróneos.
- **Derecho al olvido**: Solicitar eliminación de datos.
- **Derecho a la portabilidad**: Transferencia de datos a otro responsable.

### 3.4. Gobierno y Rendición de Cuentas
Obligación de garantizar y demostrar el cumplimiento del RGPD.

### 3.5. Obligaciones de los Encargados del Tratamiento
Solo pueden tratar datos si cumplen con garantías técnicas y organizativas.

### 3.6. Seguridad de los Datos
Se requieren medidas como:
- **Seudonimización** de datos.
- **Cifrado** de información.

### 3.7. Otros aspectos normativos
Incluye regulaciones sobre:
- **Códigos de conducta y certificaciones** (Art. 40-43).
- **Transferencias internacionales de datos** (Art. 44-50).
- **Supervisión y sanciones** (Art. 51-84).

## 4. Gobierno de Datos
Control y comunicación sobre la gestión de datos.

### 4.1. Objetivos
- Gestionar datos como activos valiosos.
- Definir y aplicar políticas de datos.

### 4.2. Marco de Referencia
Incluye aspectos como:
- **Modelado de datos**
- **Seguridad e interoperabilidad**
- **Data Warehousing & Business Intelligence**
- **Metadatos y calidad de datos**

### 4.3. Roles
- **Chief Data Officer (CDO)**
- **Oficina de Gobierno del Dato**
- **Data Owners** (Propietarios del dato)
- **Data Stewards** (Administradores del dato)
- **Data Custodians** (Custodios del dato)
