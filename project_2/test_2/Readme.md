# Simulación simplificada del movimiento de partículas

Este script en C++ con CUDA realiza una simulación simplificada del movimiento de partículas en una caja bidimensional, aplicando un filtro selectivo basado en velocidad y color, inspirado en el concepto de "demonio de Maxwell". A diferencia del script anterior, este maneja menos partículas (10 en total: 5 verdes y 5 rojas) pero más frames (500), con una configuración distinta de caja y compuerta.

***

### Descripción y Funcionalidad

- **Número de partículas:** 10 (5 verdes y 5 rojas).
- **Caja de simulación:** Dimensiones rectangulares 2 unidades en x (0 a 2) y 1 unidad en y (0 a 1).
- **Movimiento:** Cada partícula se mueve actualizando su posición según su velocidad con paso temporal 0.02f, y rebota en los bordes de la caja.
- **Demonio de Maxwell:**  
   - La "compuerta" está ubicada en $$ x = 1 $$.  
   - Solo partículas rojas que estén a la izquierda de la compuerta y tengan velocidad $$ v_x > 0.7 $$ pueden "cruzar" la compuerta hacia la derecha (incrementan su posición en $$ x $$ en 0.05).
- **Colores y significado:**  
   - Verdes (color=0): no pueden cruzar la compuerta.  
   - Rojas (color=1): pueden cruzar bajo condiciones de velocidad.

***

### Estructura clave

- **Particle struct:** Posición, velocidad y color.
- **Kernel CUDA `actualizarParticulas`:**  
  - Calculo paralelo para todas las partículas.  
  - Actualización de posición, rebote y aplicación del demonio de Maxwell.
- **Función `guardarFrame`:**  
  - Guarda la posición de las partículas en archivos para cada frame, con la línea vertical de la compuerta para visualización en GNUPLOT.
- **Inicialización:**  
  - Partículas se posicionan inicialmente solo en la mitad izquierda (0 a 1 en x).  
  - Velocidades se generan en rango $$[-1.5, 1.5]$$.

***

### Proceso de simulación

1. Reservar memoria GPU.
2. Inicializar partículas en CPU.
3. Copiar datos a GPU.
4. Ejecutar kernel CUDA para cada frame, actuando en paralelo.
5. Copiar resultados a CPU y guardar el estado en archivo.
6. Repetir 500 veces para ver evolución.
7. Liberar recursos.

***

### Objetivos y usos potenciales

Este script es ideal para simular dinámicas simples de partículas con una condición de paso selectivo que modela conceptos de termodinámica computacional, complejidad y procesos no equilibrados aplicables en física estadística y ciencia de materiales.

Permite visualizar cómo se comportan partículas con diferentes propiedades (color/velocidad) y el impacto de puntos de control tipo "demonio de Maxwell" en la evolución del sistema.
