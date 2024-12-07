# Justificación y Antecedentes del Aprendizaje Automático

## 1. Inteligencia Artificial Fuerte y Débil

La Inteligencia Artificial (IA) se clasifica en dos tipos:  
- **IA Fuerte (General):** Similar a la inteligencia humana, capaz de realizar cualquier tarea intelectual.  
- **IA Débil (Estrecha):** Especializada en tareas concretas con gran precisión.

### 1.1 Inteligencia Artificial Débil

Se refiere a agentes o modelos inteligentes que están diseñados para tareas específicas.

#### Ventajas de la IA Débil:
- Relativamente fácil de desarrollar e implementar.
- Más fácil de controlar y con menos comportamientos inesperados.
- Permite arquitecturas modulares para combinar capacidades según el entorno.

#### Inconvenientes de la IA Débil:
- Carece de contexto completo, lo que puede llevar a malinterpretar entradas inusuales.
- Está limitada a aplicaciones muy específicas.
- Menos personalizada e intuitiva en comparación con la interacción humana.

#### Ejemplos de IA Débil:
- Asistentes virtuales: Alexa, Siri, Google Assistant.
- AlphaGo.
- IBM Watson.

### 1.2 Inteligencia Artificial Fuerte

La IA Fuerte, o General, es un concepto más teórico o propio de la ciencia ficción. Representa el objetivo último en el desarrollo de la IA, pero no es alcanzable con los algoritmos actuales.

#### Conciencia Artificial:
- El desarrollo final de la IA sería construir sistemas capaces de representarse a sí mismos.
- Los investigadores deben entender y construir máquinas con conciencia.

---

## 2. Antecedentes del Machine Learning

El Aprendizaje Automático (Machine Learning, ML) combina principios estadísticos y avances computacionales de los últimos 70 años para resolver problemas y analizar datos.

### 2.1 Estadística y Probabilidad

El ML se basa en principios estadísticos. El término "Aprendizaje Automático" fue acuñado por **Arthur Samuel** en 1959 mientras trabajaba en IBM.

### 2.2 Modelos Bayesianos

#### Teorema de Bayes:
El Teorema de Bayes permite calcular la probabilidad de una hipótesis basada en la probabilidad previa, los datos observados y la probabilidad de los datos según la hipótesis.

**Fórmula:**  
\[ P(h|D) = \frac{P(D|h) \cdot P(h)}{P(D)} \]  
Donde:  
- \( P(h|D) \): Probabilidad posterior (hipótesis \( h \) dado los datos \( D \)).  
- \( P(D|h) \): Probabilidad de los datos \( D \) dado \( h \).  
- \( P(h) \): Probabilidad previa de \( h \).  
- \( P(D) \): Probabilidad de observar \( D \).

#### Ejemplo de Cálculo:
Supongamos que queremos determinar la probabilidad de que un paciente tenga una enfermedad (\( h \)) dado un resultado positivo en una prueba (\( D \)). Si:  
- \( P(D|h) = 0.95 \) (precisión de la prueba).  
- \( P(h) = 0.01 \) (prevalencia de la enfermedad).  
- \( P(D) = 0.05 \) (tasa total de resultados positivos).  

Usando Bayes:  
\[ P(h|D) = \frac{0.95 \cdot 0.01}{0.05} = 0.19 \]  
Esto significa que hay un 19% de probabilidad de que el paciente tenga la enfermedad.

#### Algoritmos Naive Bayes:
- **Ventajas:** Rápidos y sencillos para clasificar datos.  
- **Desventajas:** Pueden ser malos estimadores en algunos casos.

### 2.3 K-Nearest Neighbors (KNN)

El algoritmo **KNN** es un método de aprendizaje supervisado usado para problemas de clasificación.

- **Cómo funciona:**  
  - Se seleccionan los “k” puntos más cercanos al objetivo usando una métrica de distancia.  
  - Se realiza una votación entre estos puntos para determinar la clasificación.  
- **Ventajas:** Simple y efectivo en muchos casos.
