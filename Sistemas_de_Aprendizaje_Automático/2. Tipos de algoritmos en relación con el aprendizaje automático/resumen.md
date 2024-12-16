# Resumen: Tipos de algoritmos en Aprendizaje Automático

## Introducción
En esta unidad se profundiza en técnicas concretas utilizadas en **Aprendizaje Automático Supervisado y No Supervisado**, destacando cuáles son las óptimas según la aplicación práctica que se desee desarrollar. A continuación, se presentan los algoritmos más importantes:

---

## 1. Regresión Lineal
Se utiliza en problemas de **regresión supervisada** para estimar valores reales de variables continuas, como el precio de una vivienda o las ventas futuras. Es ideal para predecir tendencias basadas en datos históricos.

---

## 2. Regresión Logística
Aunque se denomine "regresión", es un algoritmo de **clasificación supervisada** que predice valores discretos (ejemplo: *sí/no*). Es útil para estimar probabilidades de eventos, como detectar fraudes o clasificar correos como *spam*.

---

## 3. Árbol de Decisión
Los árboles de decisión modelan decisiones basadas en atributos de los datos. Son rápidos, precisos y aplicables tanto a problemas de clasificación como de regresión. Destacan por ser fáciles de interpretar y constituyen una buena opción inicial en muchos casos.

---

## 4. Máquinas de Vector Soporte (SVM)
SVM es un algoritmo de **clasificación supervisada** que separa datos en diferentes categorías usando un **hiperplano**. Clasifica nuevos datos en función del espacio en el que se encuentren, logrando gran precisión en problemas de clasificación binaria.

---

## 5. Clustering
Es una técnica típica del **aprendizaje no supervisado**, útil para agrupar datos sin etiquetas en función de similitudes en sus características. Se aplica en etapas iniciales para explorar datos y descubrir correlaciones.

### 5.1. K-Means
Agrupa datos en "k" clusters según similitudes. Es iterativo y se utiliza cuando no se conocen etiquetas en los datos.

### 5.2. G-Means
Similar al K-Means, pero con la capacidad de determinar automáticamente la cantidad de clusters óptimos basándose en distribuciones gaussianas.

---

## Resumen Visual
Ejemplo práctico de **Regresión Lineal vs Regresión Logística**:
- **Regresión Lineal:** Predicción de un valor continuo, como ventas futuras.  
- **Regresión Logística:** Clasificación binaria, como decidir si un cliente comprará o no un producto. *(Adjunta una gráfica comparativa si es posible).*
