# Script que emplea PCA para reducir la dimensionalidad de los datos
# Se visualizan los resultados en un gráfico 2D.

# Se parte del supuesto que se tiene múltiples variables termodinámicas (resistividad, calor específico, susceptibilidad).
# El archivo 'datos_superconductor.csv' contiene las columnas 'Temperatura', 'Parametro_Orden', 'Amplitud_Fluctuaciones', 'Potencia_Espectral'.

# Se aplica PCA para reducir la dimensionalidad de los datos.
# Se visualizan los resultados en un gráfico 2D, donde cada punto representa una temperatura y su color indica la temperatura correspondiente.
# Si la Componente 1 captura >80% de la varianza, probablemente está ligada a Tc.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

T = np.linspace(4, 10, 100)  # Temperaturas

# Cargar datos desde el archivo
data = pd.read_csv('datos_superconductor.csv')

# Ejemplo: Usar datos para PCA
X = data[['Temperatura', 'Parametro_Orden', 'Amplitud_Fluctuaciones', 'Potencia_Espectral']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

# Gráfico
plt.scatter(components[:, 0], components[:, 1], c=T, cmap='viridis')
plt.colorbar(label='Temperatura (K)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')
plt.title('PCA: Variables Termodinámicas + FFT')
plt.show()