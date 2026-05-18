# Generación de datos sintéticos de resistividad para un superconductor
# Este código simula la resistividad de un material superconductor cerca de su temperatura crítica (Tc).
# La resistividad es cero en la fase superconductora (T < Tc) y aumenta linealmente en la fase normal (T > Tc), con un pequeño ruido añadido para simular datos experimentales reales.
# El resultado se guarda en un archivo CSV para su posterior análisis o visualización.
# Nota: Este código es solo un ejemplo y puede ser modificado para ajustarse a diferentes materiales o condiciones experimentales.
# Importar las bibliotecas necesarias
# numpy para cálculos numéricos y pandas para manejo de datos
# Asegúrate de tener estas bibliotecas instaladas en tu entorno de Python para ejecutar este código correctamente.
# Puedes instalar estas bibliotecas usando pip si no las tienes:
# pip install numpy pandas
# El código a continuación genera un conjunto de datos sintéticos de resistividad en función de la temperatura, simula el comportamiento típico de un superconductor y guarda los datos en un archivo CSV para su análisis posterior.
# Importar las bibliotecas necesarias

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