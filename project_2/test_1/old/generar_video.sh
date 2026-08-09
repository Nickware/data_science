#!/bin/bash
# Convertir frames .dat a imágenes PNG con GNUPLOT
for (( i=0; i<100; i++ )); do
    gnuplot <<- EOF
        set terminal png size 800,400
        set output "datos/frame_${i}.png"
        set xrange [0:1]
        set yrange [0:1]
        set title "Demonio de Maxwell - Frame ${i}"
        plot "datos/frame_${i}.dat" using 1:2:3 with points lc variable notitle
EOF
done

# Crear vídeo MP4 con ffmpeg
ffmpeg -framerate 30 -i datos/frame_%d.png -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4
echo "Vídeo generado: output.mp4"