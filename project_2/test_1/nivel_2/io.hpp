#pragma once
#include "particle.hpp"
#include <string>

// Crea el directorio de salida (y sus padres) si no existe.
void crearDirectorioSalida(const std::string& ruta);

// Guarda un frame completo en un único archivo de texto, en formato
// compatible con GNUPLOT: "x y color numero" por línea.
void guardarFrame(const Particle* particulas, int n, int frame_id, const std::string& carpeta);
