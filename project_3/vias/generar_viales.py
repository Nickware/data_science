# Generador de eventos viales simulados para análisis y pruebas.
# Este script crea eventos viales ficticios con datos variados para simular condiciones de tránsito.
# Los datos incluyen información del sensor, ubicación, vibración, inclinación y presión.
# Requiere la librería Faker para generar datos realistas.

from datetime import datetime
import random
import json
from faker import Faker

fake = Faker()

def generar_evento_vial():
    hora_actual = datetime.utcnow().hour
    en_hora_pico = hora_actual in range(6, 9) or hora_actual in range(16, 19)
    transito_estimado = random.randint(80, 200) if en_hora_pico else random.randint(30, 80)
    vibracion_base = random.uniform(0.5, 1.5)
    presion_base = random.uniform(70, 90)
    inclinacion_base = random.uniform(0.5, 2.5)
    vibracion = vibracion_base * (1 + transito_estimado / 200)
    presion = presion_base * (1 + transito_estimado / 300)
    inclinacion = inclinacion_base * (1 + transito_estimado / 250)
    alerta = 2 if vibracion > 3 or presion > 130 else 1 if vibracion > 2 or presion > 110 else 0

    evento = {
        "timestamp": datetime.utcnow().isoformat(),
        "sensor_id": f"SENS_{random.randint(100, 999)}",
        "ubicacion": {
            "direccion": fake.street_address(),
            "coordenadas": {
                "lat": round(random.uniform(4.60, 4.70), 6),
                "lon": round(random.uniform(-74.15, -74.05), 6)
            }
        },
        "fabricante_sensor": random.choice(["HBM", "Bosch", "National Instruments", "Honeywell"]),
        "tipo_sensor": random.choice(["acelerómetro", "strain gauge", "sensor piezoeléctrico"]),
        "vibracion_rms": round(vibracion, 2),
        "inclinacion_deg": round(inclinacion, 2),
        "presion_kPa": round(presion, 2),
        "transito_est_medio": transito_estimado,
        "alerta": alerta
    }
    return evento

if __name__ == "__main__":
    eventos = [generar_evento_vial() for _ in range(10)]
    with open("eventos_viales.json", "w") as f:
        json.dump(eventos, f, indent=2)
