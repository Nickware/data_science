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

>> 01.temperatura.py
>
> El parámetro de orden ψ (que marca la transición superconductora) con ruido térmico.
>
> Las fluctuaciones son más intensas cerca de Tc (crítica en regímenes tipo II).

## 2. Análisis de Fourier para Fluctuaciones
Se aplica la Transformada Rápida de Fourier (FFT) para analizar las frecuencias dominantes en las fluctuaciones.

>> 02.fluctuaciones.py
>
> Si el espectro sigue una ley de potencia (1/fα), se sugiere correlaciones críticas (típico en transiciones de fase).
