# Paradoja del demonio de Maxwell

La paradoja del demonio de Maxwell es un experimento mental propuesto por James Clerk Maxwell para poner a prueba la segunda ley de la termodinámica. Imagina una caja con gas dividida en dos, y un “ser” que abre una compuerta solo para dejar pasar moléculas rápidas hacia un lado y lentas hacia el otro, creando una diferencia de temperatura sin gastar trabajo aparente. [es.wikipedia](https://es.wikipedia.org/wiki/Demonio_de_Maxwell)

## Planteamiento
La aparente contradicción es que el demonio parecería hacer que el calor fluya de un cuerpo frío a uno caliente, algo que la segunda ley prohíbe en procesos espontáneos. En la versión clásica, el resultado sería una disminución de la entropía del sistema. [espanol.libretexts](https://espanol.libretexts.org/Bookshelves/Fisica/Termodinamica_y_Mecanica_Estadistica/Libro:_Termodin%C3%A1mica_y_Mec%C3%A1nica_Estad%C3%ADstica_(Nair)/10:_Entrop%C3%ADa_e_Informaci%C3%B3n/10.02:_Demonio_de_Maxwell)

## No viola la física
La resolución moderna dice que el demonio no puede actuar gratis: medir, registrar y procesar información tiene un costo termodinámico. Cuando se incluye la información que el demonio obtiene sobre las moléculas, la entropía total no disminuye; en otras palabras, el “orden” local se compensa con un aumento de entropía en otra parte del sistema. [bbc](https://www.bbc.com/mundo/noticias-36500302)

## Importancia científica
Esta paradoja fue clave para conectar termodinámica e información, y ayudó a desarrollar ideas fundamentales sobre física estadística y teoría de la información. Por eso sigue siendo un ejemplo clásico cuando se habla de entropía, computación y límites de los sistemas físicos. [observatoriobioetica](https://www.observatoriobioetica.org/2021/09/el-demonio-de-maxwell-cumple-150-anos-en-plena-forma/36686)

## Idea en una frase
No es que el demonio “rompa” la segunda ley, sino que obliga a reconocer que **la información también tiene costo físico**. [culturacientifica](https://culturacientifica.com/2017/10/24/el-demonio-de-maxwell/)

## Paradoja del Demonio de Maxwell para Runners

Este proyecto interdisciplinario combina física estadística, inteligencia artificial y computación de alto rendimiento para resolver un problema real

### (Fase 1): Demonio de Maxwell Clásico con 50k Partículas
Implementación con C++/CUDA que permite simular 50,000 partículas (con colores y atributos). La rutina guarda los datos en formato compatible con GNUPLOT. La salida del script en GNUPLOT permite generar un vídeo (mp4). Implementación modular. 
##### Características:
>> 1. Simulación de 50,000 partículas (verdes = "inscritas", rojas = "no inscritas").
> 
>> 2. Salida en formato GNUPLOT (archivo .dat por frame).
> 
>> 3. Generación de vídeo MP4 usando ffmpeg.
>
>> 4. Código comentado para cada componente crítico.

##### Estructura de Archivos

> /proyecto_maxwell/
> 
>│   ├── simulación.cpp      # Código principal (C++/CUDA)
> 
>│   ├── compilar.sh         # Script para compilar
> 
>│   ├── generar_video.sh    # Script para crear MP4
> 
>│   └── /datos             # Carpeta con frames (.dat)
