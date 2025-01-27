# Redes Neuronales y Deep Learning

A lo largo de esta unidad se explora el funcionamiento general de las redes neuronales y se profundiza en las técnicas y algoritmos más utilizados en el Aprendizaje Profundo (Deep Learning).

## 1. Definición y Esquema General de una Red Neuronal

### Algoritmos de Redes Neuronales
Las redes neuronales están inspiradas en el funcionamiento de las redes neuronales biológicas. Funcionan como procesadores distribuidos en paralelo que adquieren conocimiento mediante aprendizaje y lo almacenan en las **ponderaciones sinápticas**. Simulan el cerebro en dos aspectos:
- El conocimiento se adquiere a través de un proceso de aprendizaje.
- Las conexiones interneuronales almacenan dicho conocimiento.

Las redes convolucionales (ConvNets o CNNs) destacan por su capacidad para encontrar características locales en pequeños grupos de entradas y son útiles en tareas como:
- Reconocimiento de voz.
- Procesamiento de imágenes.

## 2. Deep Learning y Arquitectura por Capas

El **Deep Learning** es una tecnología de aprendizaje automático que se aplica tanto en entrenamientos supervisados como no supervisados.

### Perceptrón
El perceptrón es una unidad básica de una red neuronal que realiza cálculos para detectar patrones en los datos de entrada.

### 2.1. Topologías de Redes Neuronales

#### a) Red Neuronal de Avance (Feed Forward - FF)
- No hay ciclos en la red.
- Se organiza en capas: entrada, ocultas y salida.
- **Aplicaciones**:
  - Compresión de datos.
  - Reconocimiento de patrones, voz y caracteres manuscritos.

#### b) Red de Base Radial (Radial Basis Network - RBN)
- Se utiliza para problemas de aproximación de funciones.
- **Aplicaciones**:
  - Aproximación de funciones.
  - Clasificación y predicción de series temporales.

#### c) Red de Alimentación Directa Profunda (Deep Feed Forward - DFF)
- Utiliza múltiples capas ocultas para mayor capacidad de representación.

#### d) Red Neuronal Recurrente (Recurrent Neural Network - RNN)
- Procesa datos secuenciales considerando dependencias temporales.
- **Aplicaciones**:
  - Traducción automática.
  - Reconocimiento de voz.
  - Predicción de series temporales.

#### e) LSTM y GRU
- **LSTM**: Introduce una celda de memoria para procesar dependencias a largo plazo.
- **GRU**: Variante simplificada de LSTM con menos puertas.

#### f) Redes Neuronales de Codificadores Automáticos
- **Autoencoder (AE)**: Reduce la dimensionalidad de los datos.
- **Variational Autoencoder (VAE)**: Utiliza probabilidades para representar características.
- **Denoising Autoencoder (DAE)**: Reduce el ruido en los datos.
- **Sparse Autoencoder (SAE)**: Penaliza activaciones para obtener representaciones más compactas.

#### g) Otras Redes Notables
- **Red de Hopfield**: Utilizada para almacenar patrones y recuerdos.
- **Red de Máquinas Boltzmann (BM)**: Aprende distribuciones de probabilidad de datos originales.
- **Deep Belief Network (DBN)**: Detecta características en datos mediante aprendizaje no supervisado.
- **Generative Adversarial Network (GAN)**: Genera datos nuevos basados en los datos de entrenamiento.
- **Deep Residual Network (DRN)**: Evita la degradación del rendimiento en redes profundas.
- **Kohonen Network (KN)**: Útil para reducir dimensionalidad y visualizar datos.

## 3. Proceso de Entrenamiento de una Red Neuronal Profunda

El entrenamiento de una red neuronal profunda consiste en ajustar parámetros para obtener resultados precisos a partir de datos de entrada. A diferencia del aprendizaje automático convencional, el **Deep Learning** sigue aprendiendo y mejorando con el uso continuo.

### Fases del Entrenamiento
1. **Forward Pass**: Procesa la información de entrada para generar un resultado.
2. **Función de Coste**: Compara los resultados con los valores reales y detecta errores.
3. **Backward Pass**: Retropropaga los errores para ajustar parámetros.
4. **Descenso del Gradiente**: Optimiza los parámetros para reducir errores.

### Parámetros de la Red Neuronal Profunda
Durante el entrenamiento, se ajustan los parámetros clave que definen el comportamiento de la red. Por ejemplo, al clasificar plantas, podrían determinarse como parámetros relevantes la longitud y ancho de los pétalos.

