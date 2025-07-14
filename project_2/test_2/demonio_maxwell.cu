#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <cstring>
#include <sys/stat.h> // Para mkdir
#include <cuda_runtime.h>

// Constantes
const int N = 10;                   // 10 partículas (5 verdes, 5 rojas)
const int FRAMES = 500;             // Más frames para ver evolución
const float UMBRAL_VELOCIDAD = 0.7f; // Demonio: solo partículas rojas rápidas pasan

struct Particle {
    float x, y;     // Posición (0 < x < 2, 0 < y < 1)
    float vx, vy;   // Velocidad
    int color;      // 0: verde (no pasa), 1: rojo (puede pasar)
};

__global__ void actualizarParticulas(Particle* particulas, int frame_actual) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= N) return;

    // Mover partícula (dinámica más rápida)
    particulas[idx].x += particulas[idx].vx * 0.02f;
    particulas[idx].y += particulas[idx].vy * 0.02f;

    // Rebote en bordes (caja rectangular: 0 < x < 2, 0 < y < 1)
    if (particulas[idx].x <= 0 || particulas[idx].x >= 2) particulas[idx].vx *= -1;
    if (particulas[idx].y <= 0 || particulas[idx].y >= 1) particulas[idx].vy *= -1;

    // Demonio de Maxwell: compuerta en x=1 (solo rojas rápidas pasan a la derecha)
    if (particulas[idx].x < 1.0f && particulas[idx].vx > UMBRAL_VELOCIDAD && particulas[idx].color == 1) {
        particulas[idx].x += 0.05f;  // Pasar a la derecha
    }
}

void guardarFrame(const Particle* particulas, int frame_id) {
    std::ofstream archivo("datos/frame_" + std::to_string(frame_id) + ".dat");
    // Dibujar compuerta (línea vertical en x=1)
    archivo << "1 0\n1 1\n\n";  // Formato para línea en GNUPLOT
    
    // Guardar partículas (verdes: círculos, rojas: cruces)
    for (int i = 0; i < N; ++i) {
        archivo << particulas[i].x << " " << particulas[i].y << " " << particulas[i].color << "\n";
    }
    archivo.close();
}

int main() {
    // Crear carpeta "datos" si no existe
    mkdir("datos", 0777);

    Particle* d_particulas;
    cudaMalloc(&d_particulas, N * sizeof(Particle));

    Particle particulas[N];
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> pos_x(0.0f, 1.0f);  // Inicialmente todas a la izquierda
    std::uniform_real_distribution<float> pos_y(0.0f, 1.0f);
    std::uniform_real_distribution<float> vel(-1.5f, 1.5f);   // Velocidades más altas

    // Inicializar 5 verdes (no pasan) y 5 rojas (pueden pasar)
    for (int i = 0; i < N; ++i) {
        particulas[i].x = pos_x(gen);
        particulas[i].y = pos_y(gen);
        particulas[i].vx = vel(gen);
        particulas[i].vy = vel(gen);
        particulas[i].color = (i < 5) ? 0 : 1;  // Primeras 5 verdes, resto rojas
    }

    cudaMemcpy(d_particulas, particulas, N * sizeof(Particle), cudaMemcpyHostToDevice);

    for (int frame = 0; frame < FRAMES; ++frame) {
        dim3 blockSize(256);
        dim3 gridSize((N + blockSize.x - 1) / blockSize.x);
        actualizarParticulas<<<gridSize, blockSize>>>(d_particulas, frame);
        cudaMemcpy(particulas, d_particulas, N * sizeof(Particle), cudaMemcpyDeviceToHost);
        guardarFrame(particulas, frame);
    }

    cudaFree(d_particulas);
    std::cout << "Simulación completada. Ejecuta: ./generar_video.sh\n";
    return 0;
}
