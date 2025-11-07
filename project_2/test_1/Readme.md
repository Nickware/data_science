# Simulación de partículas 2D acelerada por GPU

Este script en C++/CUDA implementa una **simulación de partículas 2D** acelerada por GPU, usando técnicas de computación paralela para mostrar dinámica, clasificación y control de partículas en una caja, con interacción analógica al "demonio de Maxwell".

------

## **Descripción General**

- **Propósito**: Simular el movimiento de *N* partículas (25,000 verdes y 25,000 rojas) dentro de un área bidimensional, registrando sus posiciones para cada frame, y aplicar una compuerta selectiva (demonio de Maxwell) en tiempo real, exportando los datos para visualización con GNUPLOT.
- **Tecnología**: Uso de CUDA para paralelización en GPU, permitiendo simulaciones con alta eficiencia computacional.

------

## **Principales Componentes y Lógica**

## **Estructura Particle**

- Guarda posición ($x, y$), velocidad ($v_x, v_y$), color (clasificación) y un número identificador, útil para análisis de seguimiento y clasificación en simulaciones físicas.
- Partículas "verdes" reciben un identificador aleatorio de 4 dígitos; "rojas" reciben "NA".

## **Kernel CUDA:**

- Actualiza la posición de cada partícula usando su velocidad, con corrección por rebote en los límites ($0 < x < 1$, $0 < y < 1$).
- Implementa el demonio de Maxwell en $x = 0.5$: sólo partículas "rápidas" ($v_x > 0.5$) a la izquierda pueden cruzar hacia la derecha.

## **Inicialización:**

- Las partículas se inicializan aleatoriamente en posiciones/velocidades, con 50% de cada tipo.

## **Simulación y Almacenamiento:**

- Para cada frame, el script lanza el kernel en GPU, copia los datos a CPU y guarda el resultado en archivos para visualización posterior.

## **Visualización:**

- Los archivos generados pueden ser graficados con GNUPLOT, permitiendo analizar la evolución espacial y la acción del "demonio".

------

## **Fundamentos Físicos**

- **Demonio de Maxwell**: Analiza cómo fluctuaciones aleatorias y selección controlada alteran el estado de las partículas, analogía con procesos no espontáneos y entropía en sistemas termodinámicos.
- **Rebote en bordes**: Conserva partículas dentro de la caja, condición de frontera frecuente en simulaciones de gases y sistemas cerrados.
- **Clasificación dinámica**: Paralelepípedo entre microscopía de partículas y algoritmos de clasificación en ciencia de datos.

------

## **Extensiones y Aplicaciones**

Este enfoque puede extenderse a:

- Estudios de difusión, simulación molecular y física estadística.
- Implementación de modelos de fluctuaciones térmicas, cruciales en el análisis de materiales superconductores y otros sistemas complejos similares a lo discutido anteriormente.
- Pruebas de hipótesis sobre segregación y selección dinámica en sistemas fuera del equilibrio, incluyendo termodinámica computacional y mecánica estadística moderna.
