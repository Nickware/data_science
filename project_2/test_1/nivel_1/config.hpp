#pragma once

// Centralizar estos valores evita que main.cu y kernel.cu queden
// desincronizados si alguno cambia un parámetro.

constexpr int N_VERDES = 25000;
constexpr int N_ROJAS  = 25000;
constexpr int N = N_VERDES + N_ROJAS;

constexpr int FRAMES = 100;
constexpr float DT = 0.001f;              // Paso de integración temporal

constexpr float UMBRAL_VELOCIDAD = 0.5f;   // Rapidez mínima para cruzar la compuerta
constexpr float X_COMPUERTA = 0.5f;        // Posición de la compuerta (demonio de Maxwell)

constexpr int HILOS_POR_BLOQUE = 256;

// Parámetros del histograma de vx usado para la entropía de Shannon (Nivel 2).
// La magnitud de vx nunca crece más allá del rango inicial porque las
// colisiones (con la compuerta o con los bordes) solo invierten el signo,
// así que [-1,1] es un rango válido durante toda la simulación.
constexpr int NUM_BINS = 20;
constexpr float VX_MIN = -1.0f;
constexpr float VX_MAX = 1.0f;
