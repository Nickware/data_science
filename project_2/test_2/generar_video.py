import matplotlib.pyplot as plt
import os
from tqdm import tqdm

os.makedirs("datos/plots", exist_ok=True)

for i in tqdm(range(500)):
    with open(f"datos/frame_{i}.dat") as f:
        data = f.readlines()
    
    # Extraer compuerta y partículas
    compuerta = [list(map(float, line.split())) for line in data[:3]]
    particulas = [list(map(float, line.split())) for line in data[3:]]
    
    # Graficar
    plt.figure(figsize=(8, 4))
    plt.plot([1, 1], [0, 1], 'k-', label="Compuerta")
    for x, y, color in particulas:
        if color == 0:
            plt.plot(x, y, 'bo', markersize=8)  # Verdes
        else:
            plt.plot(x, y, 'rx', markersize=8)  # Rojas
    plt.xlim(0, 2)
    plt.ylim(0, 1)
    plt.title(f"Frame {i}")
    plt.savefig(f"datos/plots/plot_{i}.png")
    plt.close()

# Crear vídeo
os.system("ffmpeg -framerate 30 -i datos/plots/plot_%d.png -c:v libx264 demonio_maxwell.mp4 -y")