# Generador de eventos financieros simulados para análisis y pruebas.

Este script crea eventos simulados de **transacciones financieras** para apoyar análisis, entrenar modelos y realizar pruebas en sistemas de prevención de fraude.

## Descripción general

El script usa la librería **Faker** para generar datos ficticios y realistas sobre transacciones financieras, incluyendo detalles del usuario, monto, tipo de compra, dispositivo utilizado y una estimación probabilística de fraude. El resultado es un archivo JSON con 10 eventos listos para ser procesados por sistemas analíticos o de machine learning.

## Estructura y funcionalidad

- **Datos generados**: Cada transacción incluye marca de tiempo, monto aleatorio (rango amplio), ubicación (ciudad ficticia), dirección IP pública, frecuencia de transacciones en 24h y tipo de compra.
- **Usuario**: El script calcula la edad en función de la fecha de nacimiento simulada, incluye un identificador de usuario y si es cliente VIP.
- **Dispositivo**: Tipo (móvil, PC, POS), sistema operativo y navegador del usuario se seleccionan aleatoriamente para mejorar el realismo y permitir pruebas multiplataforma.
- **Fraude**: El campo "fraude" utiliza una probabilidad del 5% para simular intentos de fraude financiero, útil para calibrar y evaluar mecanismos de detección de anomalías.
- **Output**: Genera y guarda los eventos en **eventos_financieros.json** para facilitar integración en flujos de análisis y entrenamiento.

## Aplicaciones prácticas

- **Entrenamiento de modelos**: Datos ficticios permiten entrenar algoritmos de detección de fraude sin exponer información real.
- **Pruebas de software bancario**: Útil para simular flujos de transacciones en sistemas de monitoreo y respuesta.
- **Validación de dashboards**: Facilita la inspección visual y funcional en interfaces financieras antes de trabajar con datos sensibles.

## Ejemplo de evento

```json
{
  "timestamp": "2025-09-08T01:10:15.123Z",
  "monto": 2541342.67,
  "ubicacion": "Medellín",
  "ip": "187.201.32.45",
  "frecuencia_24h": 7,
  "tipo_compra": "retail",
  "dispositivo": {
    "tipo": "móvil",
    "sistema_operativo": "Android",
    "navegador": "Chrome"
  },
  "usuario": {
    "id_usuario": "usr_4587",
    "edad": 34,
    "cliente_vip": true
  },
  "fraude": 0
}
```


## Observaciones técnicas

- El script es **flexible y adaptable**, permitiendo modificar rangos de edad, montos o dispositivos para distintos escenarios.
- La función de fraude simple es útil para balancear muestras en casos de prueba, aunque no modela patrones complejos de fraude real.
- Fácil de integrar en pipelines de análisis, APIs, o entornos de desarrollo de software financiero.

Este generador facilita la simulación de transacciones financieras en entornos seguros y controlados, ideal para desarrolladores, analistas de riesgo y científicos de datos orientados al sector financiero.
