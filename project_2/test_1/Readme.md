# Simulación 2D de partículas con demonio de Maxwell (C++/CUDA)

Simulación de N partículas (por defecto 25.000 "verdes" + 25.000 "rojas")
que se mueven en una caja `[0,1] x [0,1]`, con una compuerta selectiva en
`x = 0.5` que solo deja pasar partículas cuya rapidez horizontal supera un
umbral — la analogía computacional del demonio de Maxwell. La posición de
cada partícula se guarda por frame para graficar con GNUPLOT, y desde el
Nivel 2 también se guardan métricas termodinámicas agregadas por frame.

## Estructura del proyecto

```
particle.hpp        Struct Particle (compartido host/device)
config.hpp           Parámetros de la simulación (N, FRAMES, umbrales, bins)
kernel.cuh/.cu        Kernel de movimiento + compuerta + rebote en bordes
metrics.hpp/.cu       Nivel 2: kernel de reducción y entropía por frame
init.hpp/.cpp         Inicialización aleatoria de partículas en CPU
io.hpp/.cpp           Escritura de frames en formato GNUPLOT
cuda_utils.hpp        Macro CUDA_CHECK para verificación de errores
main.cu                Orquestación: bucle de simulación
Makefile                Compilación con nvcc
visualizar.gnu          Genera un PNG por frame con GNUPLOT
analizar_metricas.py    Grafica datos/metricas.csv (conteos y entropía)
```

## Nivel 1 — Correcciones sobre la versión original

La versión original tenía la estructura correcta pero varios problemas que
impedían que realmente funcionara como demonio de Maxwell o que corriera a
la escala descrita. Ver la tabla comparativa al final de este documento
para el detalle línea por línea; en resumen:

- La compuerta en `x=0.5` no bloqueaba nada: solo sumaba un empujón extra
  a partículas que ya cruzaban libremente por su propia dinámica.
- El rebote en los bordes invertía la velocidad pero no recortaba la
  posición, lo que podía dejar partículas oscilando sin desplazarse.
- El directorio `datos/` nunca se creaba, así que la escritura de frames
  fallaba en silencio.
- No había verificación de errores CUDA.
- `N=50` y `FRAMES=1` eran valores de prueba, no los 25.000+25.000 y 100
  frames descritos.
- La escritura de cada frame usaba muchas llamadas pequeñas a `operator<<`
  en vez de un buffer, lo cual es notablemente más lento a esta escala.

## Nivel 2 — Métricas termodinámicas por frame

El Nivel 1 mueve partículas pero no calculaba ninguna cantidad que conecte
la simulación con el análisis termodinámico que motiva el proyecto. El
Nivel 2 agrega un kernel de reducción (`metrics.cu`) que, para cada frame,
recorre las partículas ya actualizadas y con `atomicAdd` acumula:

- `n_izq`, `n_der`: número de partículas a cada lado de la compuerta.
- `n_izq_rapidas`, `n_der_rapidas`: cuántas de ellas superan el umbral de
  velocidad (candidatas a cruzar la compuerta).
- `temp_izq`, `temp_der`: `<vx²>` por lado, usado como *proxy* de
  temperatura (con masa unitaria y sin factor de `k_B`, no es una
  temperatura en Kelvin real).
- `entropia_izq`, `entropia_der`, `entropia_total`: entropía de Shannon
  `S = -Σ p_i ln(p_i)` calculada sobre un histograma de 20 bins de `vx` en
  `[-1,1]`, por lado y para el sistema completo.

Estas métricas se escriben en `datos/metricas.csv`, un archivo aparte de
los `frame_*.dat` de posiciones, para poder analizarlas sin tener que
volver a parsear todas las posiciones.

**Limitación explícita:** esta entropía es una entropía de Shannon
*informacional* (en nats) sobre la distribución de velocidades muestreada
en bins, no la entropía termodinámica de Gibbs/Boltzmann en J/K de un gas
real. Es un proxy útil para ver tendencias (¿el sistema se ordena o se
desordena?), pero no debe citarse como un valor físico absoluto. Ver el
análisis físico entregado junto con este README.

## Cómo construir, ejecutar y analizar

### 1. Requisitos

- `nvcc` (CUDA Toolkit) y una GPU compatible.
- `gnuplot` si se quiere generar las imágenes por frame.
- Python 3 con `pandas` y `matplotlib` si se quiere graficar `metricas.csv`
  (`pip install pandas matplotlib`).

### 2. Construir

```bash
make
```

Esto compila `main.cu kernel.cu metrics.cu init.cpp io.cpp` y genera el
binario `simulacion_particulas`. `make clean` borra el binario y la
carpeta `datos/`.

### 3. Ejecutar

```bash
./simulacion_particulas
```

Con los valores por defecto (`N=50000`, `FRAMES=100`) esto genera:

- `datos/frame_0.dat` ... `datos/frame_99.dat`: posición, color e
  identificador de cada partícula por frame.
- `datos/metricas.csv`: una fila por frame con las métricas del Nivel 2.

La consola imprime cada 10 frames un resumen (`izq`, `der`, `S_total`)
para verificar que la simulación avanza sin necesidad de abrir los
archivos.

### 4. Analizar los resultados

Para las posiciones (visual, requiere GNUPLOT):

```bash
gnuplot visualizar.gnu
# genera datos/frame_0.png ... datos/frame_99.png
# opcional, para animar con ImageMagick:
convert -delay 5 datos/frame_*.png animacion.gif
```

Para las métricas termodinámicas:

```bash
python3 analizar_metricas.py
# genera datos/metricas.png con dos paneles:
#   1) n_izq/n_der/n_izq_rapidas/n_der_rapidas vs frame
#   2) entropia_izq/entropia_der/entropia_total vs frame
# y además imprime en consola la primera y última fila del CSV
```

Si `N` o `FRAMES` se cambian en `config.hpp`, hay que recompilar
(`make`) y, si se usó `visualizar.gnu`, actualizar `n_frames` en ese
script para que coincida.

## Nivel 1 — fallas y soluciones

| # | Falla (versión original) | Solución (Nivel 1) |
|---|---------------------------|----------------------|
| 1 | `N=50`, `FRAMES=1`: no correspondían a los 25.000+25.000 partículas y 100 frames descritos | `config.hpp` centraliza `N_VERDES=25000`, `N_ROJAS=25000`, `FRAMES=100` |
| 2 | La compuerta en `x=0.5` no bloqueaba nada; solo añadía un empujón a partículas que ya cruzaban libremente | El kernel detecta el intento de cruce (`x` antes/después de `0.5`) y solo deja pasar a las partículas rápidas; el resto rebota |
| 3 | El rebote en bordes invertía `vx`/`vy` sin recortar la posición, permitiendo oscilaciones sin desplazamiento real | Se recorta `x,y` exactamente a `0` o `1` además de invertir la velocidad con el signo correcto (`fabsf`) |
| 4 | El directorio `datos/` nunca se creaba; la escritura fallaba en silencio | `crearDirectorioSalida()` usa `std::filesystem::create_directories` antes de simular |
| 5 | Sin verificación de errores en `cudaMalloc`/kernel/`cudaMemcpy` | Macro `CUDA_CHECK` envuelve toda llamada CUDA y aborta con mensaje claro si falla |
| 6 | Cada frame se escribía con miles de llamadas pequeñas a `operator<<` sobre el `ofstream` | `guardarFrame` arma el contenido en un `ostringstream` y hace un único volcado a disco |
| 7 | Todo el código en un solo archivo monolítico | Separación en `particle.hpp`, `config.hpp`, `kernel.*`, `init.*`, `io.*`, `cuda_utils.hpp`, `main.cu` |

## Nivel 2 — mejoras respecto al Nivel 1

| # | Nivel 1 | Mejora en Nivel 2 |
|---|----------|----------------------|
| 1 | Guarda posiciones por frame, pero ninguna cantidad agregada | Kernel de reducción (`metrics.cu`) calcula conteos, temperatura proxy y entropía por frame |
| 2 | No hay forma de saber si la compuerta está segregando partículas sin inspeccionar manualmente los `.dat` | `n_izq`/`n_der`/`n_izq_rapidas`/`n_der_rapidas` en `metricas.csv` cuantifican la segregación directamente |
| 3 | No hay ninguna cantidad que conecte con el análisis termodinámico mencionado en la descripción del proyecto | `temp_izq`/`temp_der` (proxy de temperatura) y `entropia_*` (Shannon) dan una primera aproximación cuantitativa |
| 4 | El análisis requeriría escribir un script de cero para parsear 100 archivos `.dat` de 50.000 líneas cada uno | `metricas.csv` es un solo archivo compacto (una fila por frame), y `analizar_metricas.py` lo grafica directamente |
| 5 | Ninguna advertencia sobre qué representa (o no) una "entropía" calculada así | El README y los comentarios en `metrics.cu` aclaran que es entropía de Shannon informacional, no entropía termodinámica en J/K |
