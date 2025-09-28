## Análisis de fluctuaciones térmicas en materiales superconductores.

> - **Problema**: Determinar el comportamiento estadístico de fluctuaciones térmicas en un superconductor para predecir transiciones de fase. 
>
> - **Métodos y técnicas**: Regresión logística, Transformada de Fourier, Análisis de Componentes Principales (PCA).
>
> - **Tecnologías usadas**: Python (NumPy, Pandas, SciPy), Octave, Jupyter Notebook.
>
> - **Expectativa**: Se espera un modelo predictivo con una precisión del 92%.
>

## 1. Simulación de Datos Termodinámicos
Como los datos experimentales pueden ser difíciles de obtener, se inicia simulando fluctuaciones térmicas cerca de Tc usando el modelo de Ginzburg-Landau con ruido térmico.

```python
     python 01.temperatura.py
``` 
El parámetro de orden ψ (que marca la transición superconductora) con ruido térmico. Las fluctuaciones son más intensas cerca de Tc (crítica en regímenes tipo II).

## 2. Análisis de Fourier para Fluctuaciones
Se aplica la Transformada Rápida de Fourier (FFT) para analizar las frecuencias dominantes en las fluctuaciones.

```python
     python 02.fluctuaciones.py
``` 
Si el espectro sigue una ley de potencia (1/fα), se sugieren correlaciones críticas (típicas en transiciones de fase).

## 3.  Conexión entre Datos Termodinámicos y el Análisis de Fourier
El Paso 2 toma las fluctuaciones (noise) generadas en el Paso 1 y analiza sus componentes frecuenciales para identificar patrones ocultos.

Flujo de datos:
> Paso 1: Genera psi y noise (ruido térmico): noise es una señal aleatoria en el dominio del tiempo (o temperatura T).

> Paso 2: Se aplica FFT a la ruido para transformarlo al dominio de la frecuencia.
```python
     fft_vals = fft(noise)
```
## 4.  Generación, Análisis y Guardado de Datos

1. Generar datos del Paso 1 (Parámetro de orden y fluctuaciones)
2. Análisis FFT (Paso 2)
3. Crear DataFrame con todas las variables
4. Guardar datos en un archivo CSV

```python
     python 04.data1-2.py
``` 

Explicación de Columnas
- `Temperatura (TT)`: Variable independiente (en Kelvin).
- `Parámetro_Orden (ψ)`: Parámetro de orden superconductivo con fluctuaciones.
- `Amplitud_Fluctuaciones (noise)`: Fluctuaciones térmicas (dependientes de T).
- `Potencia_Espectral`: Resultado del FFT (espectro de potencia de las fluctuaciones).

## 5. PCA para Reducción de Dimensionalidad

Se parte del hecho de que se tienen múltiples variables termodinámicas (resistividad, calor específico, susceptibilidad).

```python
     python 05.PCA.py
``` 
Resultado: Si la componente 1 captura >80% de la varianza, probablemente está ligada a Tc.

## 6. Regresión Logística para Predecir Transiciones

Se clasifican los estados en "superconductor" (1) y "normal" (0) basados en temperatura y fluctuaciones.

```python
     python 06.regresion.py
``` 
Salida esperada

```text
     Precisión del modelo: 92.00%
```

## 7. Datos sintéticos (en caso de que no se tengan datos reales)

Si no se cuenta con datos experimentales, se pueden generar datos sintéticos basados en la teoría BCS:

```python
     python 08.resistividad.py
``` 
## 8. Validación Física con Octave (Opcional)

Para verificar que las fluctuaciones simuladas son físicamente realistas, se debe resolver la ecuación de Ginzburg-Landau estocástica en Octave:

```octave
     octave comparacion.m
``` 
