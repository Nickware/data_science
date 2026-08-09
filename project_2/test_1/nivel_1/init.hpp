#pragma once
#include "particle.hpp"
#include <vector>

// Genera N partículas: la primera mitad verdes (con identificador de 4
// dígitos) y la segunda mitad rojas (identificador "NA"), con posición
// y velocidad iniciales aleatorias.
std::vector<Particle> inicializarParticulas();
