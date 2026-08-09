#include "kernel.cuh"
#include "config.hpp"
#include <math.h>

__global__ void actualizarParticulas(Particle* particulas, int n, int frame_actual) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= n) return;

    Particle p = particulas[idx];

    // Posición propuesta tras el paso de integración
    float nuevo_x = p.x + p.vx * DT;
    float nuevo_y = p.y + p.vy * DT;

    // Demonio de Maxwell: x = X_COMPUERTA actúa como una pared virtual.
    // Solo las partículas cuya rapidez horizontal supera el umbral logran
    // atravesarla; el resto rebota como si chocara contra una pared física.
    bool intenta_cruzar = (p.x < X_COMPUERTA && nuevo_x >= X_COMPUERTA) ||
                           (p.x >= X_COMPUERTA && nuevo_x < X_COMPUERTA);

    if (intenta_cruzar && fabsf(p.vx) <= UMBRAL_VELOCIDAD) {
        p.vx *= -1.0f;
        nuevo_x = p.x + p.vx * DT;
    }

    p.x = nuevo_x;
    p.y = nuevo_y;

    // Rebote en los bordes de la caja, con recorte de posición para evitar
    // que la partícula quede oscilando fuera de [0,1] sin desplazarse.
    if (p.x <= 0.0f) { p.x = 0.0f; p.vx = fabsf(p.vx); }
    if (p.x >= 1.0f) { p.x = 1.0f; p.vx = -fabsf(p.vx); }
    if (p.y <= 0.0f) { p.y = 0.0f; p.vy = fabsf(p.vy); }
    if (p.y >= 1.0f) { p.y = 1.0f; p.vy = -fabsf(p.vy); }

    particulas[idx] = p;
}
