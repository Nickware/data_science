## Demonio de Maxwell para Runners

Proyecto interdisciplinario que combina física estadística, inteligencia artificial y computación de alto rendimiento para resolver un problema real

### (Fase 1): Demonio de Maxwell Clásico con 50k Partículas
##### Características:
>> 1. Simulación de 50,000 partículas (verdes = "inscritas", rojas = "no inscritas").
> 
>> 2. Salida en formato GNUPLOT (archivo .dat por frame).
> 
>> 3. Generación de vídeo MP4 usando ffmpeg.
>
>> 4. Código comentado para cada componente crítico.

##### Estructura de Archivos

/proyecto_maxwell/
│   ├── simulación.cpp      # Código principal (C++/CUDA)
│   ├── compilar.sh         # Script para compilar
│   ├── generar_video.sh    # Script para crear MP4
│   └── /datos             # Carpeta con frames (.dat)