#include "init.hpp"
#include "config.hpp"
#include <random>
#include <cstring>
#include <cstdio>

std::vector<Particle> inicializarParticulas() {
    std::vector<Particle> particulas(N);

    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> pos_dist(0.0f, 1.0f);
    std::uniform_real_distribution<float> vel_dist(-1.0f, 1.0f);
    std::uniform_int_distribution<int> id_dist(1000, 9999);

    for (int i = 0; i < N; ++i) {
        particulas[i].x = pos_dist(gen);
        particulas[i].y = pos_dist(gen);
        particulas[i].vx = vel_dist(gen);
        particulas[i].vy = vel_dist(gen);
        particulas[i].color = (i < N_VERDES) ? 0 : 1;

        if (particulas[i].color == 0) {
            std::snprintf(particulas[i].numero, sizeof(particulas[i].numero), "%04d", id_dist(gen));
        } else {
            std::strcpy(particulas[i].numero, "NA");
        }
    }
    return particulas;
}
