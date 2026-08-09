# Genera una imagen PNG por cada frame guardado en datos/
# Uso: gnuplot visualizar.gnu
# (luego se pueden unir en un gif con, por ejemplo, ImageMagick: convert -delay 5 datos/frame_*.png animacion.gif)

set terminal pngcairo size 800,800
set xrange [0:1]
set yrange [0:1]
set xlabel "x"
set ylabel "y"
unset key

# Debe coincidir con FRAMES en config.hpp
n_frames = 100

do for [i=0:n_frames-1] {
    set output sprintf("datos/frame_%d.png", i)
    set title sprintf("Frame %d", i)
    set arrow 1 from 0.5,0 to 0.5,1 nohead lc rgb "black" dt 2
    plot sprintf("datos/frame_%d.dat", i) using 1:2:3 with points pt 7 ps 0.3 lc variable
}
