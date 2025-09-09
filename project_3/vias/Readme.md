# Generador de eventos viales simulados para análisis y pruebas.

Este script genera eventos viales simulados, produciendo un archivo JSON con datos ficticios para analizar y probar sistemas relacionados con el tránsito urbano.

## Descripción general

El script utiliza la librería **Faker** para crear direcciones realistas y combina valores aleatorios de vibración, inclinación y presión, ajustados según el nivel de tránsito simulado en horas pico y horas valle. El resultado es una lista de eventos en formato JSON, ideal para pruebas de sistemas de monitoreo vial, algoritmos de alerta y plataformas de análisis de datos urbanos.

## Estructura y funcionalidad

- **Simulación de condiciones viales**: Cada evento contiene una marca de tiempo, un identificador único de sensor, ubicación (dirección y coordenadas aleatorias dentro de un rango de Bogotá), fabricante y tipo de sensor.
- **Variables físicas**: Vibración (RMS), inclinación (en grados) y presión (en kPa) se generan aleatoriamente y ajustan según el volumen de tránsito estimado.
- **Sistema de alerta**: El nivel de alerta depende de si los valores de vibración o presión sobrepasan ciertos límites, ayudando a probar algoritmos de detección automatizada de incidentes o anomalías.
- **Output**: Genera 10 eventos consecutivos y los guarda en el archivo **eventos_viales.json**, apto para usar en pruebas de procesamiento de datos o visualizaciones.

## Aplicaciones comunes

- **Pruebas de software urbano**: Permite validar sistemas de alerta sin depender de datos reales.
- **Entrenamiento de algoritmos**: Utiliza datos sintéticos para ajustar y calibrar modelos de detección.
- **Visualización y depuración**: Facilita la creación rápida de escenarios urbanos para desarrollo y demostraciones.

## Ejemplo de salida

Cada evento tiene una estructura como la siguiente:

```json
{
  "timestamp": "2025-09-08T01:02:03.456Z",
  "sensor_id": "SENS_251",
  "ubicacion": {
    "direccion": "Calle Ficticia #123",
    "coordenadas": {
      "lat": 4.658947,
      "lon": -74.111236
    }
  },
  "fabricante_sensor": "Bosch",
  "tipo_sensor": "acelerómetro",
  "vibracion_rms": 2.7,
  "inclinacion_deg": 1.9,
  "presion_kPa": 120.3,
  "transito_est_medio": 145,
  "alerta": 1
}
```


## Observaciones técnicas

- **Fácil adaptación**: Se puede modificar el número de eventos, el rango de coordenadas, o los fabricantes y tipos de sensores según los requisitos del proyecto.
- **Enfoque en realismo**: Aunque los datos son sintéticos, la combinación de Faker y variables escaladas por tránsito mejora la verosimilitud.

Este script es útil para ingenieros, analistas urbanos y desarrolladores que necesitan simular tráfico y condiciones viales en entornos controlados.
