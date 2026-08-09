#pragma once
#include "particle.hpp"

__global__ void actualizarParticulas(Particle* particulas, int n, int frame_actual);
