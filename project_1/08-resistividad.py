# Generación de datos sintéticos de resistividad para un superconductor

import numpy as np
import pandas as pd

# Generar datos sintéticos de resistividad cerca de Tc
Tc = 9.2  # Ejemplo: Nb3Sn
T = np.linspace(5, 15, 100)
resistividad = np.where(
    T < Tc, 
    0,  # Resistividad cero en fase superconductora
    1e-3 + 2e-3 * (T - Tc)  # Resistividad lineal en fase normal
) + 0.1e-3 * np.random.normal(size=len(T))  # Ruido experimental

df = pd.DataFrame({
    'Temperatura': T,
    'Resistividad': resistividad,
    'Fase': np.where(T < Tc, 'Superconductor', 'Normal')
})

# Guardar datos generados (para uso futuro)
df.to_csv('resistividad_sintetica.csv', index=False)