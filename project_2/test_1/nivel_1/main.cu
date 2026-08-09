#include <iostream>
#include <string>
#include "config.hpp"
#include "particle.hpp"
#include "init.hpp"
#include "io.hpp"
#include "kernel.cuh"
#include "metrics.hpp"
#include "cuda_utils.hpp"

int main() {
    const std::string carpeta_salida = "datos";
    const std::string ruta_metricas = carpeta_salida + "/metricas.csv";
    crearDirectorioSalida(carpeta_salida);
    crearArchivoMetricas(ruta_metricas);

    std::vector<Particle> particulas = inicializarParticulas();

    Particle* d_particulas = nullptr;
    CUDA_CHECK(cudaMalloc(&d_particulas, N * sizeof(Particle)));
    CUDA_CHECK(cudaMemcpy(d_particulas, particulas.data(), N * sizeof(Particle), cudaMemcpyHostToDevice));

    inicializarMetricas();

    dim3 blockSize(HILOS_POR_BLOQUE);
    dim3 gridSize((N + blockSize.x - 1) / blockSize.x);

    for (int frame = 0; frame < FRAMES; ++frame) {
        actualizarParticulas<<<gridSize, blockSize>>>(d_particulas, N, frame);
        CUDA_CHECK(cudaGetLastError());

        // Las métricas se calculan directamente sobre el buffer en GPU,
        // sin esperar a la copia a host que usa guardarFrame.
        MetricasFrame m = calcularMetricas(d_particulas, N, frame);
        guardarMetricas(m, ruta_metricas);

        CUDA_CHECK(cudaMemcpy(particulas.data(), d_particulas, N * sizeof(Particle), cudaMemcpyDeviceToHost));
        guardarFrame(particulas.data(), N, frame, carpeta_salida);

        if (frame % 10 == 0) {
            std::cout << "Frame " << frame << " / " << FRAMES
                      << " | izq=" << m.n_izq << " der=" << m.n_der
                      << " | S_total=" << m.entropia_total << "\n";
        }
    }

    liberarMetricas();
    cudaFree(d_particulas);
    std::cout << "Simulacion completada. " << FRAMES << " frames guardados en " << carpeta_salida << "/\n";
    std::cout << "Metricas termodinamicas en " << ruta_metricas << "\n";
    return 0;
}
