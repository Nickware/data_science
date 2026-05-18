# Clasificacion de los estados en "superconductor" (1) 
# y "normal" (0) basado en la temperatura y fluctuaciones.
# Se utiliza regresión logística para modelar la probabilidad de que un material
# esté en estado superconductor en función de la temperatura y las fluctuaciones.
# Se generan datos sintéticos para entrenar el modelo, y luego se evalúa su precisión.
# El modelo se entrena con un conjunto de datos que incluye la temperatura y las fluctuaciones,
# y se prueba con un conjunto de datos separado para evaluar su rendimiento.
# El resultado final es la precisión del modelo y las predicciones de la fase para el conjunto de prueba.
# Se espera que el modelo tenga una alta precisión, especialmente cerca de la temperatura crítica,
# donde la transición de fase ocurre.
# Este enfoque permite entender cómo la temperatura y las fluctuaciones afectan la probabilidad de que un material sea superconductor, y puede ser útil para identificar materiales con propiedades superconductoras en función de sus características térmicas y de fluctuación.
# Importar las bibliotecas necesarias
# Se utiliza numpy para generar datos sintéticos, sklearn para la regresión logística y la división de datos.
# Se generan datos sintéticos para la temperatura, el parámetro de orden y las fluctuaciones, y luego se entrena un modelo de regresión logística para clasificar los estados de superconductor y normal.
# El modelo se evalúa utilizando la precisión en un conjunto de prueba, y se muestran las predicciones de la fase para ese conjunto.
# El código es un ejemplo de cómo se puede aplicar la regresión logística para clasificar estados en función de características térmicas y de fluctuación, lo que es relevante en el estudio de materiales superconductores.
# El código se puede adaptar para incluir más características o para utilizar otros modelos de clasificación si se desea mejorar la precisión o explorar diferentes enfoques.
# En resumen, este código es un ejemplo de cómo se puede utilizar la regresión logística para clasificar estados de superconductor y normal en función de la temperatura y las fluctuaciones, utilizando datos sintéticos para entrenar y evaluar el modelo.
# Se espera que el modelo tenga una alta precisión, especialmente cerca de la temperatura crítica, donde la transición de fase ocurre, lo que puede proporcionar información valiosa sobre las propiedades superconductoras de los materiales en función de sus características térmicas y de fluctuación.
# El código se puede adaptar para incluir más características o para utilizar otros modelos de clasificación si se desea mejorar la precisión o explorar diferentes enfoques.

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generar datos del paso anterior (Parámetro de orden y fluctuaciones)
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
