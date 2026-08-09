"""
Analiza datos/metricas.csv generado por la simulación y produce dos
gráficas: (1) evolución del conteo de partículas a cada lado de la
compuerta, y (2) evolución de la entropía de Shannon por lado y total.

Uso:
    python3 analizar_metricas.py [ruta_csv]

Requiere pandas y matplotlib (pip install pandas matplotlib).
"""
import sys
import pandas as pd
import matplotlib.pyplot as plt

ruta_csv = sys.argv[1] if len(sys.argv) > 1 else "datos/metricas.csv"
df = pd.read_csv(ruta_csv)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

ax1.plot(df["frame"], df["n_izq"], label="Izquierda (x<0.5)")
ax1.plot(df["frame"], df["n_der"], label="Derecha (x>=0.5)")
ax1.plot(df["frame"], df["n_izq_rapidas"], "--", label="Rápidas izquierda")
ax1.plot(df["frame"], df["n_der_rapidas"], "--", label="Rápidas derecha")
ax1.set_ylabel("Número de partículas")
ax1.set_title("Segregación por la compuerta (demonio de Maxwell)")
ax1.legend()
ax1.grid(alpha=0.3)

ax2.plot(df["frame"], df["entropia_izq"], label="Entropía izquierda")
ax2.plot(df["frame"], df["entropia_der"], label="Entropía derecha")
ax2.plot(df["frame"], df["entropia_total"], label="Entropía total", linewidth=2, color="black")
ax2.set_xlabel("Frame")
ax2.set_ylabel("Entropía de Shannon (nats)")
ax2.set_title("Evolución de la entropía de la distribución de vx")
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("datos/metricas.png", dpi=150)
print("Gráfica guardada en datos/metricas.png")

print("\nResumen (primer y último frame):")
print(df.iloc[[0, -1]].to_string(index=False))
