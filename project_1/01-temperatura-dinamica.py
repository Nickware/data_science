"""Simulacion temporal simplificada del parametro de orden superconductivo.

La dinamica usa una ecuacion de Langevin adimensional:

    dpsi/dt = -gamma * dF/dpsi + ruido
    F(psi, T) = 0.5 * a(T) * psi**2 + 0.25 * b * psi**4

No representa una simulacion experimental ni una integracion espacial de
Ginzburg-Landau. Sirve para generar un conjunto reproducible de datos
sinteticos con una temperatura que cambia durante la simulacion.
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


DEFAULT_OUTPUT = "datos_temperatura_dinamica.csv"


def simular_dinamica(
    tc=7.2,
    temperatura_inicial=4.0,
    temperatura_final=10.0,
    pasos=1000,
    dt=0.01,
    gamma=1.0,
    ruido=0.08,
    semilla=42,
):
    """Simula la relajacion temporal de psi durante una rampa de temperatura."""
    if pasos < 2:
        raise ValueError("pasos debe ser mayor o igual que 2")
    if dt <= 0 or gamma <= 0 or ruido < 0:
        raise ValueError("dt y gamma deben ser positivos; ruido no puede ser negativo")

    rng = np.random.default_rng(semilla)
    tiempo = np.arange(pasos) * dt
    temperatura = np.linspace(temperatura_inicial, temperatura_final, pasos)
    psi = np.empty(pasos, dtype=float)
    psi[0] = np.sqrt(max(tc - temperatura[0], 0.0))

    # Modelo de potencial doble pozo por debajo de Tc y pozo unico por encima.
    for indice in range(1, pasos):
        a = temperatura[indice] - tc
        fuerza_restauradora = -(a * psi[indice - 1] + psi[indice - 1] ** 3)
        incremento_ruido = ruido * np.sqrt(dt) * rng.normal()
        psi[indice] = psi[indice - 1] + gamma * fuerza_restauradora * dt + incremento_ruido

    psi_equilibrio = np.sqrt(np.maximum(tc - temperatura, 0.0))
    fluctuacion = psi - psi_equilibrio

    return pd.DataFrame(
        {
            "tiempo": tiempo,
            "temperatura": temperatura,
            "psi": psi,
            "psi_equilibrio": psi_equilibrio,
            "fluctuacion": fluctuacion,
        }
    )


def main():
    parser = argparse.ArgumentParser(
        description="Genera una simulacion temporal sintetica de psi(T)."
    )
    parser.add_argument("--salida", default=DEFAULT_OUTPUT, help="CSV de salida")
    parser.add_argument("--pasos", type=int, default=1000, help="Numero de pasos temporales")
    parser.add_argument("--dt", type=float, default=0.01, help="Paso temporal")
    parser.add_argument("--semilla", type=int, default=42, help="Semilla aleatoria")
    parser.add_argument("--sin-grafica", action="store_true", help="No mostrar la grafica")
    args = parser.parse_args()

    datos = simular_dinamica(pasos=args.pasos, dt=args.dt, semilla=args.semilla)
    ruta_salida = Path(args.salida)
    datos.to_csv(ruta_salida, index=False)
    print(f"Datos guardados en '{ruta_salida}'. Filas: {len(datos)}")

    if not args.sin_grafica:
        figura, ejes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
        ejes[0].plot(datos["tiempo"], datos["psi"], label="psi simulado")
        ejes[0].plot(
            datos["tiempo"],
            datos["psi_equilibrio"],
            "--",
            label="psi de referencia",
        )
        ejes[0].set_ylabel("Parametro de orden psi")
        ejes[0].legend()
        ejes[0].grid(alpha=0.3)

        ejes[1].plot(datos["tiempo"], datos["temperatura"], color="tab:red")
        ejes[1].axhline(7.2, color="black", linestyle="--", label="Tc = 7.2 K")
        ejes[1].set_xlabel("Tiempo simulado")
        ejes[1].set_ylabel("Temperatura (K)")
        ejes[1].legend()
        ejes[1].grid(alpha=0.3)

        figura.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
