import numpy as np
import pandas as pd
from scipy.fft import fft

# 1. Generar datos del Paso 1 (Parámetro de orden y fluctuaciones)
Tc = 7.2  # Temperatura crítica (K)
T = np.linspace(4, 10, 100)  # Temperaturas
delta_T = T - Tc
psi = np.sqrt(np.maximum(-delta_T, 0)) + 0.1 * np.random.normal(size=len(T))  # Parámetro de orden con ruido
noise = (0.1 / (np.abs(delta_T) + 0.01)) * np.random.normal(size=len(T))  # Ruido dependiente de T

# 2. Análisis FFT (Paso 2)
fft_vals = fft(noise)
power_spectrum = np.abs(fft_vals)**2  # Espectro de potencia

# 3. Crear DataFrame con todas las variables
data = pd.DataFrame({
    'Temperatura': T,
    'Parametro_Orden': psi,
    'Amplitud_Fluctuaciones': noise,
    'Potencia_Espectral': power_spectrum,
})

# 4. Guardar datos en un archivo CSV
data.to_csv('datos_superconductor.csv', index=False)
print("¡Datos guardados en 'datos_superconductor.csv'!")
