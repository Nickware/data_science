# Este script grafica apartir de la generación de datos conectados
# Se generan datos de fluctuaciones térmicas conectados y se calcula el espectro de potencia.

# (Paso 1) El gráfico del noise en dominio del tiempo 
# (Paso 2) El grafico mediante transformada rápida de Fourier (FFT) las frecuencias dominantes en las fluctuaciones.


import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Generar datos conectados
T = np.linspace(4, 10, 1000)  # Mayor resolución
noise = 0.1 * np.random.normal(size=len(T))

# Gráfico del noise en dominio del tiempo (Paso 1)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(T, noise, 'b-', alpha=0.6)
plt.title("Fluctuaciones térmicas (dominio de T)")
plt.xlabel("Temperatura (K)")
plt.ylabel("Amplitud")

# FFT (Paso 2)
fft_vals = fft(noise)
freqs = np.fft.fftfreq(len(noise), d=(T[1]-T[0]))
power = np.abs(fft_vals)**2

plt.subplot(1, 2, 2)
plt.plot(freqs[freqs > 0], power[freqs > 0], 'r-')
plt.title("Espectro de potencia (dominio de frecuencia)")
plt.xlabel("Frecuencia (1/K)")
plt.ylabel("Potencia")
plt.tight_layout()
plt.show()
