# Entornos de programación de IA con Python

En esta unidad vamos a analizar varios entornos habitualmente utilizados cuando se programa deep learning con Python.

## 1. Jupyter Notebook y entornos compatibles

El Proyecto Jupyter se creó en 2014, a partir de IPython, que era una consola para programación en Python, por Fernando Pérez, para dar especial protagonismo al lenguaje Notebook, que es agnóstico y permite el desarrollo con un formato muy práctico en otros lenguajes.

### 1.1 Jupyter Notebook

La mayor parte del flujo de trabajo en la ciencia de datos transcurre en Notebooks, pues este formato ha contribuido a agilizar dicho proceso y a poder evaluar resultados y compartirlos con otros de una forma más visual y clara.  
La forma más sencilla de iniciarse en la utilización de esta herramienta es instalar Anaconda y arrancar Jupyter desde el escritorio propio de Anaconda. Lo primero que se muestra es el escritorio con los directorios y notebooks que pueda haber en el directorio principal del entorno.

### 1.2 Google Colab

Google Colab, que inicialmente se conocía como Colaboratory, es un entorno interactivo en el que se pueden generar cuadernos ejecutables en los que se combinan celdas de código con celdas de texto enriquecido, imágenes, HTML, LaTeX, etc.  
Al tratarse de un servicio en la nube, accesible vía web, no hay que instalar ni configurar nada.

### 1.3 Binder

Binder es una web app que proporciona un servidor temporal para ejecutar cuadernos de Jupyter alojados en un repositorio de GitHub. Es gratuito y muy sencillo de utilizar. Es un desarrollo de código abierto, mantenido por la comunidad con el apoyo de empresas como Google, OVH o el Turing Institute.  
Solo es necesario dar acceso al repositorio donde están los notebooks.

### 1.4 Kaggle

La plataforma kaggle.com surgió en 2010, promovida por Anthony Goldbloom y Jeremy Howard, como una comunidad de científicos e ingenieros de datos dispuestos a participar en competiciones de aprendizaje automático a partir de retos que planteaban diferentes empresas.

## 2. IDEs para proyectos

Aunque el proceso de construcción y entrenamiento de un modelo se va a realizar con un entorno de notebooks con bastante probabilidad, cuando ya tenemos el modelo predictivo, su implementación en un proyecto es más común hacerla utilizando un entorno de programación más orientado a desarrollo de aplicaciones.

### 2.1 Visual Studio Code

Visual Studio Code es un IDE, propiedad de Microsoft, que ha ido ganando aceptación en los últimos años. A pesar de que la descarga oficial está bajo software privativo con opciones de suscripción y servicios extra por parte de Microsoft, está disponible de forma gratuita y en código abierto.  
En realidad, está especialmente enfocado en proyectos de .NET y otros lenguajes auspiciados por Microsoft, pero la comunidad de Python lo ha ido adoptando de forma generalizada, y existen un buen número de plugins para Python, integrados en marketplace, que mejoran mucho la experiencia programando en Python.

### 2.2 Pycharm

Pycharm es un IDE enfocado en Python, desarrollado por la empresa JetBrains, que incluye varias funcionalidades muy específicas de ese lenguaje. Cuenta con una versión denominada Community, que es gratuita y se publica bajo la Licencia Apache, que incluye:

- Un entorno virtual para cada proyecto.
- Un editor inteligente que ayuda a detectar errores, verificar sintaxis, completar código y muestra de documentación automática.
- Incluye depurador gráfico, ejecución de tests e inspector de código.
- Como todos los IDE, tiene una terminal incorporada.

### 2.3 Replit

Replit es un IDE online que ejecuta el código desde el propio navegador. La principal ventaja es lo sencillo que es empezar un proyecto y lanzarlo rápidamente. Sus características a destacar son:

- Soporta muchos lenguajes, más de 50, entre los que está Python.
- Es tan versátil que hasta se puede utilizar desde un móvil.
- Permite trabajo colaborativo sobre el mismo proyecto, en tiempo real, aunque es especialmente recomendable hacer la integración con GitHub para una mayor seguridad.
- Las opciones de despliegue son muy simples pero eficaces. Se puede dar acceso al Repl en diferentes formatos y desde el mismo momento de crearlo.
- Cuenta con un catálogo de APIs y plugins muy variado que enriquecen el proyecto adaptándolo a cualquier necesidad extra.

### 2.4 Sublime Text

Sublime Text es un editor de texto y código fuente desarrollado en C++. Es de las opciones más sencillas que vas a ver en cuanto a IDE, aunque admite plugins de terceros que enriquecen la experiencia. Algunas de las funcionalidades que merece la pena destacar son:

- Minimapa con una previsualización de la estructura del código para moverse por éste.
- Tareas múltiples de selección y cursor.
- Autocompletado y marcado de llaves.
- Coloreado de sintaxis.
- Soporte de Snippets y Plugins.
