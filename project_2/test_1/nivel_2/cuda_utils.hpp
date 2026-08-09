#pragma once
#include <cuda_runtime.h>
#include <cstdio>
#include <cstdlib>

// Envuelve cualquier llamada a la API de CUDA y aborta con un mensaje
// claro si falla, en vez de continuar en un estado indefinido.
#define CUDA_CHECK(llamada)                                                        \
    do {                                                                            \
        cudaError_t err = (llamada);                                                \
        if (err != cudaSuccess) {                                                    \
            std::fprintf(stderr, "Error CUDA en %s:%d -> %s\n", __FILE__, __LINE__,   \
                          cudaGetErrorString(err));                                    \
            std::exit(EXIT_FAILURE);                                                   \
        }                                                                               \
    } while (0)
