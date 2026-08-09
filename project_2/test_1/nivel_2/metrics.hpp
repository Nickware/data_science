#pragma once
#include "particle.hpp"
#include <string>

// Resumen agregado de un frame: conteos a cada lado de la compuerta,
// una temperatura "proxy" (<vx^2>) y una entropía de Shannon aproximada
// calculada sobre el histograma de vx.
struct MetricasFrame {
    int frame;
    int n_izq, n_der;
    int n_izq_rapidas, n_der_rapidas;
    float temp_izq, temp_der;
    float entropia_izq, entropia_der;
    float entropia_total;
};

// Reserva en GPU los buffers de acumulación (contadores, sumas, histogramas).
// Llamar una sola vez antes del bucle de frames.
void inicializarMetricas();

// Libera los buffers reservados por inicializarMetricas().
void liberarMetricas();

// Lanza el kernel de reducción sobre el estado actual de las partículas
// en GPU y devuelve las métricas ya calculadas en host.
MetricasFrame calcularMetricas(const Particle* d_particulas, int n, int frame_actual);

// Crea (o sobrescribe) el CSV de métricas con su encabezado.
void crearArchivoMetricas(const std::string& ruta);

// Agrega una fila al CSV de métricas.
void guardarMetricas(const MetricasFrame& m, const std::string& ruta);
