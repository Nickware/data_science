# Se aplica la Transformada Rápida de Fourier (FFT) para analizar las frecuencias dominantes en las fluctuaciones.
# Se generan datos de fluctuaciones térmicas conectados y se calcula el espectro de potencia.
# Se generan datos de fluctuaciones térmicas conectados

# Se sugiere que el espectro de potencia sigue una ley de potencia (1/fα1/fα).
# Se utiliza la FFT para identificar las frecuencias dominantes en las fluctuaciones térmicas.
# Se calcula el espectro de potencia utilizando la FFT
# Se sugiere correlaciones críticas (típico en transiciones de fase).


from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

# Generar datos conectados
T = np.linspace(4, 10, 1000)  # Mayor resolución
noise = 0.1 * np.random.normal(size=len(T))

# FFT de las fluctuaciones
fft_vals = fft(noise)
freqs = np.fft.fftfreq(len(noise), d=(T[1]-T[0]))  # Frecuencias

# Espectro de potencia
power = np.abs(fft_vals)**2

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(freqs[freqs > 0], power[freqs > 0], label='Espectro de potencia')
plt.xlabel('Frecuencia (1/K)')
plt.ylabel('Potencia')
plt.title('Análisis de Fourier de Fluctuaciones Térmicas')
plt.grid()
plt.show()
