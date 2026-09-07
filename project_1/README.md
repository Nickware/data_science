# Análisis de fluctuaciones térmicas en superconductores

Este proyecto es un prototipo educativo para explorar, con datos sintéticos,
algunas técnicas de análisis asociadas al estudio de transiciones entre los
estados superconductor y normal. El código utiliza un modelo simplificado del
parámetro de orden, ruido aleatorio, análisis espectral, PCA y regresión
logística.

> **Alcance:** los scripts no trabajan con mediciones experimentales y no
> implementan una simulación numérica completa de la ecuación de Ginzburg-
> Landau. Las fórmulas utilizadas son aproximaciones didácticas para generar
> datos y visualizar conceptos.

## Objetivos

- Representar de forma simplificada un parámetro de orden `psi` cerca de una
     temperatura crítica `Tc`.
- Generar fluctuaciones aleatorias dependientes de la temperatura.
- Observar un espectro de potencia mediante la Transformada Rápida de Fourier
     (FFT).
- Consolidar variables sintéticas en un archivo CSV.
- Aplicar PCA para reducir la dimensionalidad.
- Probar una clasificación binaria mediante regresión logística.
- Generar, de manera independiente, un ejemplo sintético de resistividad.

## Requisitos

Se necesita Python 3 y las siguientes bibliotecas:

```bash
pip install numpy pandas scipy matplotlib scikit-learn
```

Para ejecutar la comparación opcional se requiere GNU Octave:

```bash
sudo apt install octave
```

## Archivos y comportamiento

### `01-temperatura.py`

Genera temperaturas entre 4 K y 10 K, calcula un parámetro de orden
simplificado y añade ruido gaussiano. Muestra el resultado junto con
`Tc = 7.2 K`.

```bash
python3 01-temperatura.py
```

El script no guarda datos ni implementa una dinámica temporal o espacial.

### `02-fluctuaciones.py`

Genera ruido gaussiano independiente, calcula su FFT y muestra el espectro de
potencia para frecuencias positivas.

```bash
python3 02-fluctuaciones.py
```

### `03-fluctuaciones-espectro.py`

Es una variante visual del análisis anterior: muestra en una misma figura el
ruido en función de la temperatura y su espectro de potencia.

```bash
python3 03-fluctuaciones-espectro.py
```

Los scripts 02 y 03 no leen la salida de `01-temperatura.py` ni prueban por sí
solos una ley de potencia `1/f`. Para estudiar correlaciones críticas habría
que generar una señal correlacionada y ajustar explícitamente el espectro.

### `04-data1-2.py`

Genera nuevamente datos sintéticos de temperatura, parámetro de orden,
fluctuaciones y potencia espectral. Guarda el resultado en
`datos_superconductor.csv`.

```bash
python3 04-data1-2.py
```

Este es el primer paso del flujo de datos que sí está conectado con otro
script del proyecto.

### `05-PCA.py`

Lee `datos_superconductor.csv`, estandariza sus cuatro columnas y calcula dos
componentes principales. Finalmente muestra una gráfica coloreada por
temperatura.

```bash
python3 05-PCA.py
```

Debe ejecutarse después de `04-data1-2.py`. El script no comprueba que la
primera componente explique un porcentaje específico de la varianza; esa
interpretación debe hacerse consultando `pca.explained_variance_ratio_`.

### `06-regresion.py`

Genera sus propios datos sintéticos y entrena una regresión logística para
clasificar `1` cuando `T < Tc` (superconductor) y `0` en caso contrario
(normal).

```bash
python3 06-regresion.py
```

Este script es independiente de `datos_superconductor.csv`. La precisión se
calcula sobre una división aleatoria y puede cambiar entre ejecuciones porque
no se fija una semilla para la generación del ruido. No debe presentarse como
una precisión garantizada ni como validación experimental.

### `08-resistividad.py`

Genera una tabla independiente de resistividad sintética y la guarda como
`resistividad_sintetica.csv`.

```bash
python3 08-resistividad.py
```

Usa `Tc = 9.2 K`, diferente de los `7.2 K` empleados en otros scripts. La
resistividad se define como cero por debajo de `Tc` y aumenta linealmente por
encima, con ruido añadido. No alimenta el flujo de PCA o regresión.

### `comparacion.m`

Contiene la comparación opcional en Octave. Debe ejecutarse desde esta
carpeta:

```bash
octave comparacion.m
```

Su relación con los scripts de Python es complementaria; no forma parte de un
pipeline automático entre archivos.

## Flujo de datos real

El único flujo explícito entre scripts es:

```text
04-data1-2.py
                    |
                    v
datos_superconductor.csv
                    |
                    v
05-PCA.py
```

Los demás scripts generan y analizan sus propios datos. Para ejecutar el flujo
principal:

```bash
cd project_1
python3 04-data1-2.py
python3 05-PCA.py
```

## Interpretación y limitaciones

- Los datos son sintéticos y contienen ruido aleatorio.
- `01-temperatura.py` y `04-data1-2.py` usan una expresión algebraica para
     `psi`; no resuelven la ecuación estocástica de Ginzburg-Landau.
- La FFT muestra contenido frecuencial, pero el código no ajusta una ley
     `1/f` ni demuestra correlaciones críticas.
- La regresión logística clasifica una etiqueta construida directamente a
     partir de `T < Tc`; esto sirve como demostración, no como descubrimiento de
     una transición a partir de datos independientes.
- La PCA reduce la representación de las variables, pero el código no prueba
     que una componente esté físicamente ligada a `Tc`.
- La resistividad sintética es un modelo lineal simplificado y utiliza una
     temperatura crítica diferente.

## Posibles extensiones

1. Centralizar `Tc`, el rango de temperaturas y la semilla aleatoria.
2. Hacer que los scripts compartan archivos de entrada y salida definidos.
3. Generar señales correlacionadas y ajustar el espectro en escala log-log.
4. Separar entrenamiento, validación y prueba en la clasificación.
5. Reportar matriz de confusión, `F1` y otras métricas.
6. Implementar y validar una discretización de la ecuación de Ginzburg-Landau
     si se requiere una simulación física.
