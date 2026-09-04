# Repositorio de proyectos de ciencia de datos

Este repositorio reúne cuatro proyectos académicos que recorren análisis
científico, simulación GPU, generación de datos sintéticos y arquitectura de
plataformas para análisis en tiempo real. Cada proyecto tiene su propia
documentación detallada; este archivo sirve como índice y guía de entrada.

## Proyectos

### 1. Fluctuaciones térmicas en superconductores

**Ruta:** [project_1](project_1/)

Analiza, con datos sintéticos, el comportamiento del parámetro de orden cerca
de la temperatura crítica `Tc`. El flujo incluye:

- simulación de fluctuaciones con un modelo inspirado en Ginzburg-Landau;
- análisis de frecuencias mediante FFT;
- consolidación de datos en CSV;
- reducción de dimensionalidad con PCA;
- clasificación de los estados superconductor y normal mediante regresión
	logística;
- comparación opcional con Octave.

**Tecnologías:** Python, NumPy, Pandas, SciPy, Matplotlib, scikit-learn y
Octave. Los scripts se ejecutan de forma independiente, por ejemplo:

```bash
cd project_1
python3 01-temperatura.py
python3 02-fluctuaciones.py
python3 04-data1-2.py
python3 05-PCA.py
python3 06-regresion.py
octave comparacion.m  # opcional
```

La precisión indicada en la documentación es una expectativa sobre datos
sintéticos, no una garantía: los scripts usan ruido aleatorio y no fijan una
semilla común.

### 2. Demonio de Maxwell para partículas

**Ruta:** [project_2](project_2/)

Implementa una simulación bidimensional de partículas con una compuerta
selectiva en CUDA. El proyecto contiene dos líneas de trabajo:

- [test_1](project_2/test_1/): versión modular con dos niveles. El [Nivel 1](project_2/test_1/nivel_1/)
	simula 50.000 partículas, guarda frames para GNUPLOT y aplica rebotes y
	control de cruces. El [Nivel 2](project_2/test_1/nivel_2/) añade conteos por
	lado, temperatura como proxy y entropía de Shannon en `metricas.csv`, además
	de un análisis en Python.
- [test_2](project_2/test_2/): simulación reducida y didáctica con 10
	partículas, 500 frames y generación de visualizaciones/video.

**Tecnologías:** C++, CUDA, Python, GNUPLOT, ImageMagick y ffmpeg según el
flujo utilizado. Para compilar el Nivel 2:

```bash
cd project_2/test_1/nivel_2
make
./simulacion_particulas
python3 analizar_metricas.py
```

Se necesita CUDA Toolkit con `nvcc` y una GPU compatible. La entropía del
Nivel 2 es informacional, medida en nats sobre bins de velocidad; funciona
como indicador de tendencia y no como entropía termodinámica absoluta.

### 3. Datos sintéticos para análisis en tiempo real

**Ruta:** [project_3](project_3/)

Propone un pipeline común para dos casos de uso:

- [compras](project_3/compras/): eventos financieros sintéticos para probar
	detección de fraude en transacciones de Black Friday;
- [vias](project_3/vias/): eventos sintéticos de sensores de vibración,
	inclinación y presión para detectar fallas incipientes en una vía.

Ambos generadores usan Faker y producen 10 eventos JSON para pruebas:

```bash
cd project_3/compras
python3 generar_financieros.py

cd ../vias
python3 generar_viales.py
```

La documentación propone integrar Kafka o MQTT, Kubeflow/KFServing y Grafana
para ingestión, inferencia y monitoreo. Las guías de [Grafana](project_3/install/grafana/)
y [Kubeflow](project_3/install/kuberflow/) describen instalaciones de
referencia. Actualmente este proyecto contiene generadores y documentación de
arquitectura; no incluye todavía un pipeline desplegable completo.

### 4. Sitio de documentación con Hugo

**Ruta:** [project_4](project_4/)

Documenta Hugo como generador de sitios estáticos y describe su arquitectura,
estructura de directorios, front matter, taxonomías, temas, comandos,
integraciones y despliegue. También incluye guías separadas de
[configuración](project_4/configuration/) e [instalación](project_4/instalation/).

Este proyecto se encuentra en fase documental: en la ruta actual no hay un
sitio Hugo completo con `config.toml`, `content/`, `layouts/` o `themes/` para
compilar. Para convertirlo en un sitio ejecutable habría que crear esa
estructura y añadir contenido Markdown.

## Mapa rápido

| Proyecto | Área principal | Estado actual |
| --- | --- | --- |
| 1 | Análisis científico y aprendizaje automático | Scripts ejecutables con datos sintéticos |
| 2 | Simulación física en GPU | Implementación CUDA con niveles de simulación y métricas |
| 3 | Datos sintéticos y MLOps | Generadores JSON y arquitectura propuesta |
| 4 | Publicación de documentación | Guías de Hugo, sin sitio generado incluido |

## Requisitos generales

Cada proyecto tiene requisitos distintos. De forma resumida:

- Python 3 y las dependencias científicas indicadas para el Proyecto 1.
- CUDA Toolkit, `nvcc` y una GPU compatible para el Proyecto 2.
- Python 3 y `Faker` para los generadores del Proyecto 3.
- Hugo únicamente si se implementa y compila el sitio descrito en el Proyecto 4.

Consulta el README de cada proyecto antes de instalar herramientas o ejecutar
los comandos de esta página.
