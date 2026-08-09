#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <cstring>  // Para strcpy
#include <cuda_runtime.h>

// Constantes
const int N = 50;              // 50,000 partículas
const int FRAMES = 1;           // 100 frames de simulación
const float UMBRAL_VELOCIDAD = 0.5f; // Demonio: solo partículas rápidas pasan

// Estructura de una partícula (CPU y GPU)
struct Particle {
    float x, y;     // Posición
    float vx, vy;   // Velocidad
    int color;      // 0: verde (inscrito), 1: rojo (no inscrito)
    char numero[5]; // Número de identificación (ej: "1234")
};

// Kernel CUDA: actualizar posiciones y aplicar "demonio"
__global__ void actualizarParticulas(Particle* particulas, int frame_actual) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= N) return;

    // Mover partícula (dinámica simplificada)
    particulas[idx].x += particulas[idx].vx * 0.001f;
    particulas[idx].y += particulas[idx].vy * 0.001f;

    // Rebote en bordes de la caja (0 < x < 1, 0 < y < 1)
    if (particulas[idx].x <= 0 || particulas[idx].x >= 1) particulas[idx].vx *= -1;
    if (particulas[idx].y <= 0 || particulas[idx].y >= 1) particulas[idx].vy *= -1;

    // Demonio de Maxwell: compuerta en x=0.5
    if (particulas[idx].x < 0.5f && particulas[idx].vx > UMBRAL_VELOCIDAD) {
        particulas[idx].x += 0.01f;  // Permitir paso a la derecha
    }
}

// Función para guardar un frame en formato GNUPLOT
void guardarFrame(const Particle* particulas, int frame_id) {
    std::ofstream archivo("datos/frame_" + std::to_string(frame_id) + ".dat");
    for (int i = 0; i < N; ++i) {
        archivo << particulas[i].x << " " << particulas[i].y << " " 
                << particulas[i].color << " " << particulas[i].numero << "\n";
    }
    archivo.close();
}

int main() {
    // Reservar memoria en GPU
    Particle* d_particulas;
    cudaMalloc(&d_particulas, N * sizeof(Particle));

    // Inicializar partículas en CPU (50% verdes "inscritas", 50% rojas)
    Particle* particulas = new Particle[N];
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> pos_dist(0.0f, 1.0f);
    std::uniform_real_distribution<float> vel_dist(-1.0f, 1.0f);

    for (int i = 0; i < N; ++i) {
        particulas[i].x = pos_dist(gen);
        particulas[i].y = pos_dist(gen);
        particulas[i].vx = vel_dist(gen);
        particulas[i].vy = vel_dist(gen);
        particulas[i].color = (i < N/2) ? 0 : 1;  // Primeras 25k verdes, resto rojas
        
        // Asignar número aleatorio de 4 dígitos a las verdes
        if (particulas[i].color == 0) {
            snprintf(particulas[i].numero, 5, "%04d", std::uniform_int_distribution<int>(1000, 9999)(gen));
        } else {
            strcpy(particulas[i].numero, "NA");
        }
    }

    // Copiar datos a GPU
    cudaMemcpy(d_particulas, particulas, N * sizeof(Particle), cudaMemcpyHostToDevice);

    // Simular y guardar frames
    for (int frame = 0; frame < FRAMES; ++frame) {
        // Lanzar kernel en GPU (256 hilos por bloque)
        dim3 blockSize(256);
        dim3 gridSize((N + blockSize.x - 1) / blockSize.x);
        actualizarParticulas<<<gridSize, blockSize>>>(d_particulas, frame);
        
        // Copiar datos de vuelta a CPU para guardar
        cudaMemcpy(particulas, d_particulas, N * sizeof(Particle), cudaMemcpyDeviceToHost);
        
        // Guardar frame actual
        guardarFrame(particulas, frame);
    }

    // Liberar memoria
    delete[] particulas;
    cudaFree(d_particulas);

    std::cout << "Simulación completada. Datos guardados en /datos/\n";
    return 0;
}