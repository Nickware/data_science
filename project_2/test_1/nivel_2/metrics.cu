#include "metrics.hpp"
#include "config.hpp"
#include "cuda_utils.hpp"
#include <fstream>
#include <cmath>
#include <vector>

namespace {
    int*   d_conteos  = nullptr; // [n_izq, n_der, n_izq_rapidas, n_der_rapidas]
    float* d_suma_vx2 = nullptr; // [izq, der]
    int*   d_hist_izq = nullptr; // NUM_BINS
    int*   d_hist_der = nullptr; // NUM_BINS
}

// Kernel de reducción: cada hilo clasifica su partícula (lado de la
// compuerta, si es "rápida", y el bin de vx al que pertenece) y acumula
// con atomicAdd. Con decenas de miles de partículas y solo unos pocos
// destinos posibles (2 lados x 20 bins), la contención de los atomics
// es manejable y evita una reducción en dos pasadas.
__global__ void kernelMetricas(const Particle* particulas, int n,
                                int* conteos, float* suma_vx2,
                                int* hist_izq, int* hist_der) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx >= n) return;

    Particle p = particulas[idx];
    bool izquierda = p.x < X_COMPUERTA;

    atomicAdd(&conteos[izquierda ? 0 : 1], 1);
    if (fabsf(p.vx) > UMBRAL_VELOCIDAD) {
        atomicAdd(&conteos[izquierda ? 2 : 3], 1);
    }
    atomicAdd(&suma_vx2[izquierda ? 0 : 1], p.vx * p.vx);

    float vx_recortado = fminf(fmaxf(p.vx, VX_MIN), VX_MAX);
    int bin = static_cast<int>((vx_recortado - VX_MIN) / (VX_MAX - VX_MIN) * NUM_BINS);
    if (bin >= NUM_BINS) bin = NUM_BINS - 1;
    if (bin < 0) bin = 0;

    atomicAdd(&(izquierda ? hist_izq : hist_der)[bin], 1);
}

void inicializarMetricas() {
    CUDA_CHECK(cudaMalloc(&d_conteos, 4 * sizeof(int)));
    CUDA_CHECK(cudaMalloc(&d_suma_vx2, 2 * sizeof(float)));
    CUDA_CHECK(cudaMalloc(&d_hist_izq, NUM_BINS * sizeof(int)));
    CUDA_CHECK(cudaMalloc(&d_hist_der, NUM_BINS * sizeof(int)));
}

void liberarMetricas() {
    cudaFree(d_conteos);
    cudaFree(d_suma_vx2);
    cudaFree(d_hist_izq);
    cudaFree(d_hist_der);
}

namespace {
    // Entropía de Shannon S = -Sum p_i ln(p_i) sobre un histograma
    // normalizado. Es una entropía "informacional" en nats, no la
    // entropía termodinámica en J/K: sirve como proxy relativo del
    // desorden de la distribución de velocidades, no como su valor
    // físico absoluto (ver la nota en el README sobre esta limitación).
    float entropiaShannon(const std::vector<int>& hist, int total) {
        if (total <= 0) return 0.0f;
        float s = 0.0f;
        for (int h : hist) {
            if (h <= 0) continue;
            float p_i = static_cast<float>(h) / static_cast<float>(total);
            s -= p_i * std::log(p_i);
        }
        return s;
    }
}

MetricasFrame calcularMetricas(const Particle* d_particulas, int n, int frame_actual) {
    CUDA_CHECK(cudaMemset(d_conteos, 0, 4 * sizeof(int)));
    CUDA_CHECK(cudaMemset(d_suma_vx2, 0, 2 * sizeof(float)));
    CUDA_CHECK(cudaMemset(d_hist_izq, 0, NUM_BINS * sizeof(int)));
    CUDA_CHECK(cudaMemset(d_hist_der, 0, NUM_BINS * sizeof(int)));

    dim3 blockSize(HILOS_POR_BLOQUE);
    dim3 gridSize((n + blockSize.x - 1) / blockSize.x);
    kernelMetricas<<<gridSize, blockSize>>>(d_particulas, n, d_conteos, d_suma_vx2, d_hist_izq, d_hist_der);
    CUDA_CHECK(cudaGetLastError());

    int conteos[4];
    float suma_vx2[2];
    std::vector<int> hist_izq(NUM_BINS), hist_der(NUM_BINS);

    CUDA_CHECK(cudaMemcpy(conteos, d_conteos, 4 * sizeof(int), cudaMemcpyDeviceToHost));
    CUDA_CHECK(cudaMemcpy(suma_vx2, d_suma_vx2, 2 * sizeof(float), cudaMemcpyDeviceToHost));
    CUDA_CHECK(cudaMemcpy(hist_izq.data(), d_hist_izq, NUM_BINS * sizeof(int), cudaMemcpyDeviceToHost));
    CUDA_CHECK(cudaMemcpy(hist_der.data(), d_hist_der, NUM_BINS * sizeof(int), cudaMemcpyDeviceToHost));

    MetricasFrame m;
    m.frame = frame_actual;
    m.n_izq = conteos[0];
    m.n_der = conteos[1];
    m.n_izq_rapidas = conteos[2];
    m.n_der_rapidas = conteos[3];
    m.temp_izq = m.n_izq > 0 ? suma_vx2[0] / m.n_izq : 0.0f;
    m.temp_der = m.n_der > 0 ? suma_vx2[1] / m.n_der : 0.0f;
    m.entropia_izq = entropiaShannon(hist_izq, m.n_izq);
    m.entropia_der = entropiaShannon(hist_der, m.n_der);

    std::vector<int> hist_total(NUM_BINS);
    for (int i = 0; i < NUM_BINS; ++i) hist_total[i] = hist_izq[i] + hist_der[i];
    m.entropia_total = entropiaShannon(hist_total, m.n_izq + m.n_der);

    return m;
}

void crearArchivoMetricas(const std::string& ruta) {
    std::ofstream archivo(ruta);
    archivo << "frame,n_izq,n_der,n_izq_rapidas,n_der_rapidas,"
               "temp_izq,temp_der,entropia_izq,entropia_der,entropia_total\n";
}

void guardarMetricas(const MetricasFrame& m, const std::string& ruta) {
    std::ofstream archivo(ruta, std::ios::app);
    archivo << m.frame << ',' << m.n_izq << ',' << m.n_der << ','
            << m.n_izq_rapidas << ',' << m.n_der_rapidas << ','
            << m.temp_izq << ',' << m.temp_der << ','
            << m.entropia_izq << ',' << m.entropia_der << ',' << m.entropia_total << '\n';
}
