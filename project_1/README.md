# Física de las fluctuaciones térmicas en superconductores

## 1. Las Fluctuaciones Térmicas en Superconductores

Las **fluctuaciones térmicas** son desviaciones aleatorias del estado de equilibrio de un sistema debido a la **energía térmica** (\( k_B T \)). En superconductores, estas fluctuaciones afectan al **parámetro de orden superconductivo** (\( \psi \)), que describe la densidad de pares de Cooper.

### **Visualización Física**:
Imagínese el parámetro de orden como un "campo" que tiene un valor promedio \( \langle \psi \rangle \). Las fluctuaciones térmicas hacen que este campo oscile espacial y temporalmente alrededor de su valor medio, especialmente cerca de la temperatura crítica (\( T_c \)).

## 2. Origen Físico.

### **A. Termodinámica Estadística**
- A \( T > 0 \), los sistemas están en constante agitación térmica.  
- Los pares de Cooper (responsables de la superconductividad) pueden romperse y recombinarse debido a la energía térmica.  
- La **amplitud de las fluctuaciones** es proporcional a \( k_B T / \xi^d \), donde \( \xi \) es la longitud de coherencia y \( d \) la dimensionalidad del sistema.

### **B. Cerca de \( T_c \) (Región Crítica)**
- La longitud de coherencia \( \xi \) diverge como \( \xi \propto |T - T_c|^{-1/2} \).  
- Esto **amplifica las fluctuaciones** porque la energía necesaria para crear una excitación se vuelve muy pequeña.  
- El sistema exhibe **fluctuaciones críticas** que pueden dominar el comportamiento físico.

## **3. Tipos de Fluctuaciones Térmicas**

| **Tipo** | **Descripción** | **Efecto Observado** |
|----------|-----------------|----------------------|
| **Fluctuaciones Gaussianas** | Pequeñas desviaciones alrededor del valor medio (válidas lejos de \( T_c \)). | Contribuciones aditivas a la resistividad (\( \Delta \rho \propto T \)). |
| **Fluctuaciones Críticas** | Grandes desviaciones cerca de \( T_c \), con escalado no lineal. | Picos en calor específico, resistividad no lineal, formación de vórtices. |
| **Fluctuaciones de Fase** | Variaciones en la fase del parámetro de orden (importantes en superconductores 2D como cupratos). | Transición de Berezinskii-Kosterlitz-Thouless (BKT) en sistemas 2D. |

## **4. Consecuencias Observables**

### **A. Resistividad Eléctrica**
- Por encima de \( T_c \), las fluctuaciones producen una **resistividad residual** que sigue una ley de potencia:  
  \[
  \rho(T) \propto (T - T_c)^{-1} \quad \text{(fluctuaciones de Aslamazov-Larkin)}
  \]
- En la práctica, esto significa que la transición no es abrupta (como en la teoría BCS clásica), sino que hay una **cola de fluctuaciones** en la resistividad.

### **B. Calor Específico**
- Cerca de \( T_c \), el calor específico muestra **divergencias críticas** debido a las fluctuaciones.  
- En superconductores tipo II (ej: YBa₂Cu₃O₇), se observan picos asimétricos en \( C_p(T) \).

### **C. Formación de Vórtices**
- En superconductores tipo II, las fluctuaciones térmicas pueden **nuclean vórtices magnéticos** incluso sin campo aplicado.  
- Esto es crítico en aplicaciones (ej: imanes de MRI), donde los vórtices causan pérdidas por resistencia.

## **5. Modelos Teóricos para Fluctuaciones**

### **A. Teoría de Ginzburg-Landau (GL) con Ruido Térmico**
- La ecuación de GL estocástica describe la dinámica del parámetro de orden:
  \[
  \Gamma \frac{\partial \psi}{\partial t} = -\frac{\delta F}{\delta \psi^*} + \eta(\mathbf{r}, t)
  \]
  - \( F \): Energía libre de GL.  
  - \( \eta(\mathbf{r}, t) \): Ruido térmico blanco (correlacionado con \( \langle \eta^*(\mathbf{r}, t) \eta(\mathbf{r}', t') \rangle \propto k_B T \delta(\mathbf{r} - \mathbf{r}') \delta(t - t') \)).

### **B. Teoría de Fluctuaciones de Aslamazov-Larkin (AL)**
- Predice la conductividad adicional por fluctuaciones (\( \sigma' \propto (T - T_c)^{-1} \) en 3D).

### **C. Modelo de Langevin para Vórtices**
- Describe el movimiento de vórtices bajo fluctuaciones térmicas (útil para transporte).

## **6. Importancia en Materiales Reales**

| **Material** | **Característica** | **Efecto de Fluctuaciones** |
|--------------|-------------------|-----------------------------|
| **Cupratos (ej: YBCO)** | Superconductores 2D, alta \( T_c \). | Fluctuaciones muy fuertes (región crítica amplia). |
| **Superconductores convencionales (Nb, Pb)** | 3D, baja \( T_c \). | Fluctuaciones débiles (transición abrupta). |
| **Películas delgadas** | Dimensionalidad reducida. | Fluctuaciones dominantes (transiciones BKT). |

## **7. Conexión con tu Proyecto**

### **¿Cómo analizar estas fluctuaciones numéricamente?**
1. **Simular fluctuaciones**: Usar el modelo GL estocástico (como en tu script).  
2. **Detectar transiciones de fase**: La regresión logística clasifica estados basados en \( \psi \) y su variación.  
3. **Analizar espectros**: La FFT identifica si las fluctuaciones tienen componentes críticas (ej: \( 1/f \) ruido).  
4. **Reducir dimensionalidad**: El PCA encuentra combinaciones de variables (temperatura, amplitud de fluctuaciones) que explican la transición.

## **8. Ejemplo Numérico: Simulación Avanzada**

```python
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
Tc = 7.2
T = np.linspace(6, 8, 200)
tau = (T - Tc) / Tc  # Temperatura reducida

# Modelo GL con fluctuaciones
psi_mean = np.sqrt(np.maximum(-tau, 0))  # Valor medio
fluctuaciones = (0.5 / (np.abs(tau) + 0.001)) * np.random.normal(size=len(T))  # Ruido crítico
psi = psi_mean + fluctuaciones

# Calcular resistividad fluctuante (modelo AL)
rho = 1e-3 * np.where(T > Tc, tau**-1, 0) + 0.1e-3 * np.random.normal(size=len(T))

# Gráfico
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(T, psi, 'o', markersize=3)
ax1.axvline(Tc, color='r', linestyle='--', label=f'Tc = {Tc} K')
ax1.set_ylabel('ψ (Parámetro de orden)')
ax1.legend()

ax2.plot(T, rho, 's', markersize=3)
ax2.axvline(Tc, color='r', linestyle='--')
ax2.set_xlabel('Temperatura (K)')
ax2.set_ylabel('Resistividad (Ω·m)')
plt.tight_layout()
plt.show()
```

## **9. Desafíos Experimentales**

- **Ruido externo**: Diferenciar fluctuaciones térmicas de ruido instrumental.  
- **Efectos de tamaño finito**: En muestras pequeñas, las fluctuaciones son más intensas.  
- **Anisotropía**: En materiales como cupratos, las fluctuaciones son direccionales.

## **10. Aplicaciones Tecnológicas**

- **Diseño de imanes superconductores**: Entender fluctuaciones ayuda a evitar "quenches" (pérdidas repentinas de superconductividad).  
- **Computación cuántica**: Las fluctuaciones limitan la coherencia de qubits superconductores.  
- **Sensores**: Fluctuaciones térmicas pueden ser usadas como termómetros ultrasensibles.

## **Conclusión**

Las fluctuaciones térmicas en superconductores son un **fenómeno central** que:  
1. **Revela la naturaleza cuántica** del estado superconductor.  
2. **Limita aplicaciones tecnológicas** en altas temperaturas.  
3. **Provee información valiosa** sobre transiciones de fase y dimensionalidad del sistema.

Este proyecto combina herramientas estadísticas y computacionales para **cuantificar y predecir** estas fluctuaciones, un enfoque de vanguardia en física de materiales.


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
