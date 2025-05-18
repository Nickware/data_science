# Simulación de fluctuaciones térmicas en el parámetro de orden ψ (que marca la transición superconductor)
# Este script simula el comportamiento del parámetro de orden en un superconductor en función de la temperatura, incluyendo fluctuaciones térmicas.
# El modelo de Ginzburg-Landau describe cómo el parámetro de orden ψ varía con la temperatura y el campo magnético.

# El parámetro de orden ψ (que marca la transición superconductora) con ruido térmico con el modelo de Ginzburg-Landau.
# El parámetro de orden ψ es una medida de la densidad de pares de Cooper en un superconductor.
# El parámetro de orden ψ se comporta como una función de la temperatura, 
# # El parámetro de orden ψ cerca de Tc, muestra fluctuaciones térmicas.
# La temperatura crítica Tc es el punto donde el material se vuelve superconductor.
# Las fluctuaciones son más intensas cerca de Tc (crítica en regímenes tipo II).
# Se emplean datos experimentales dummy

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del superconductor (ej: NbSe2)
Tc = 7.2  # Temperatura crítica (K)
T = np.linspace(4, 10, 100)  # Rango de temperatura (K)
delta_T = T - Tc  # Distancia a Tc

# Parámetro de orden (ψ) con fluctuaciones térmicas (ruido gaussiano)
psi_mean = np.sqrt(np.maximum(-delta_T, 0))  # Teoría GL pura
noise = 0.1 * np.random.normal(size=len(T))  # Fluctuaciones térmicas
psi = psi_mean + noise

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(T, psi, 'o', label='Parámetro de orden con fluctuaciones')
plt.axvline(Tc, color='r', linestyle='--', label=f'Tc = {Tc} K')
plt.xlabel('Temperatura (K)')
plt.ylabel('ψ (Parámetro de orden)')
plt.legend()
plt.grid()
plt.show()
