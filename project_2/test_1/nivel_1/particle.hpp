#pragma once

// Longitud del buffer de identificador: 4 dígitos + terminador nulo.
constexpr int LONGITUD_ID = 5;

// Se usa tanto en host como en device, por lo que debe ser un tipo
// simple (POD) sin constructores ni miembros no triviales.
struct Particle {
    float x, y;                 // Posición en la caja [0,1] x [0,1]
    float vx, vy;                // Velocidad
    int color;                    // 0 = verde (inscrito), 1 = rojo (no inscrito)
    char numero[LONGITUD_ID];    // "1234" para verdes, "NA" para rojas
};
