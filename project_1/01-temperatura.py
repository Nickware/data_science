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
