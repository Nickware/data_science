#!/bin/bash

# Configuración de GNUPLOT
for (( i=0; i<500; i++ )); do
    # Separar datos: compuerta (línea) y partículas (puntos)
    awk 'NR <= 3 {print $1, $2}' "datos/frame_${i}.dat" > "datos/compuerta_${i}.dat"
    awk 'NR > 3 {print $1, $2, $3}' "datos/frame_${i}.dat" > "datos/particulas_${i}.dat"

    # Generar gráfico con GNUPLOT
    gnuplot <<- EOF
        set terminal png size 800,400
        set output "datos/plot_${i}.png"
        set xrange [0:2]
        set yrange [0:1]
        set title "Demonio de Maxwell - Frame ${i}"
        
        # Dibujar compuerta (línea negra)
        plot "datos/compuerta_${i}.dat" with lines lc "black" title "Compuerta", \
             "datos/particulas_${i}.dat" using 1:2:(\$3 == 0 ? 0x0000FF : 0xFF0000) \
             with points pt (\$3 == 0 ? 7 : 2) ps 2 lc rgb variable notitle
EOF
done

# Crear vídeo con ffmpeg
ffmpeg -framerate 30 -i "datos/plot_%d.png" -c:v libx264 -r 30 -pix_fmt yuv420p demonio_maxwell.mp4 -y

echo "✅ Vídeo generado: demonio_maxwell.mp4"