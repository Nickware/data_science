#include "io.hpp"
#include <filesystem>
#include <fstream>
#include <sstream>

void crearDirectorioSalida(const std::string& ruta) {
    std::filesystem::create_directories(ruta);
}

void guardarFrame(const Particle* particulas, int n, int frame_id, const std::string& carpeta) {
    // Se arma todo el contenido en memoria y se escribe de una sola vez:
    // con decenas de miles de líneas por frame, muchas llamadas pequeñas
    // a operator<< sobre el ofstream son notablemente más lentas.
    std::ostringstream buffer;
    for (int i = 0; i < n; ++i) {
        buffer << particulas[i].x << ' ' << particulas[i].y << ' '
               << particulas[i].color << ' ' << particulas[i].numero << '\n';
    }
    std::ofstream archivo(carpeta + "/frame_" + std::to_string(frame_id) + ".dat");
    archivo << buffer.str();
}
