# Clasificacion de los estados en "superconductor" (1) 
# y "normal" (0) basado en la temperatura y fluctuaciones.

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generar datos del Paso 1 (Parámetro de orden y fluctuaciones)
Tc = 7.2  # Temperatura crítica (K)
T = np.linspace(4, 10, 100)  # Temperaturas
delta_T = T - Tc
psi = np.sqrt(np.maximum(-delta_T, 0)) + 0.1 * np.random.normal(size=len(T))  # Parámetro de orden con ruido
noise = (0.1 / (np.abs(delta_T) + 0.01)) * np.random.normal(size=len(T))  # Ruido dependiente de T

# Datos sinteticos: X = temperatura,fluctuaciones], y = [Fase]
x = np.column_stack((T,noise))
y = (T < Tc).astype(int)  # 1 si T < Tc (superconductor)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modelo de regresión logística
model = LogisticRegression()
model.fit(X_train, y_train)

# Predicciones
accuracy = model.score(X_test, y_test)
print(f"Precisión del modelo: {accuracy:.2%}")
# Predicciones de la fase
predictions = model.predict(X_test)
print("Predicciones de la fase (0: normal, 1: superconductor):")
print(predictions)