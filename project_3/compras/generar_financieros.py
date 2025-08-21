# Generador de eventos financieros simulados para análisis y pruebas.
# Este script crea eventos financieros ficticios con datos variados para simular transacciones.
# Los datos incluyen información del usuario, tipo de compra, dispositivo y probabilidad de fraude.
# Requiere la librería Faker para generar datos realistas.

from datetime import datetime
import random
import json
from faker import Faker

fake = Faker()

def generar_evento_financiero():
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=75)
    edad = int((datetime.utcnow().date() - fecha_nacimiento).days / 365.25)
    hora_actual = datetime.utcnow().hour
    transaccion = {
        "timestamp": datetime.utcnow().isoformat(),
        "monto": round(random.uniform(10000, 3000000), 2),
        "ubicacion": fake.city(),
        "ip": fake.ipv4_public(),
        "frecuencia_24h": random.randint(1, 15),
        "tipo_compra": random.choice(["ecommerce", "restaurante", "retail", "suscripciones", "servicios"]),
        "dispositivo": {
            "tipo": random.choice(["móvil", "PC", "POS"]),
            "sistema_operativo": random.choice(["Android", "iOS", "Windows 10", "Linux", "macOS"]),
            "navegador": random.choice(["Chrome", "Safari", "Firefox", "Edge"])
        },
        "usuario": {
            "id_usuario": f"usr_{random.randint(1000, 9999)}",
            "edad": edad,
            "cliente_vip": random.choice([True, False])
        },
        "fraude": random.choices([0, 1], weights=[0.95, 0.05])[0]
    }
    return transaccion

if __name__ == "__main__":
    eventos = [generar_evento_financiero() for _ in range(10)]
    with open("eventos_financieros.json", "w") as f:
        json.dump(eventos, f, indent=2)
