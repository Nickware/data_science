

# Detección de fraude en Black Friday vs  fallas incipientes en una vía secundaria

Este proyecto compara dos casos reales de análisis en tiempo real que, pese a pertenecer a sectores distintos (finanzas e infraestructura civil), comparten necesidades técnicas similares y pueden resolverse con enfoques comunes de ciencia de datos e ingeniería de MLOps.

### 1. Detección de fraude en Black Friday en Colombia

- **Contexto:** Gran volumen de transacciones digitales en eventos comerciales especiales.
- **Problema:** Identificar en tiempo real operaciones sospechosas para evitar fraudes como phishing o compras con tarjetas clonadas.
- **Datos en tiempo real:** Monto, ubicación, frecuencia y tipo de compra.
- **Modelos ML aplicables:** LSTM o Random Forest con reentrenamiento frecuente para adaptarse a patrones cambiantes.
- **Infraestructura recomendada:** Kafka (ingestión de eventos) + Kubeflow/KFServing (serving de modelos) + Katib (experimentación automática) + Grafana (monitoreo).


### 2. Detección de fallas incipientes en una vía secundaria (ejemplo: Avenida 68, Metro de Bogotá)

- **Contexto:** Vía sometida a cargas variables y cambios físicos durante grandes obras civiles.
- **Problema:** Detectar con anticipación anomalías estructurales (hundimientos, grietas) que pongan en riesgo la seguridad.
- **Datos en tiempo real:** Sensores IoT de vibración, presión, inclinación distribuidos en la vía.
- **Modelos ML aplicables:** Autoencoders o árboles de decisión sobre series temporales estructurales.
- **Infraestructura recomendada:** MQTT (comunicación IoT) + Kubeflow/KFServing (serving) + Grafana (monitoreo).


### Comparación estructural

| Elemento | Black Friday (Fraude financiero) | Vía Metro de Bogotá (Infraestructura física) |
| :-- | :-- | :-- |
| Contexto | Transacciones comerciales | Obras y cambios físicos |
| Tipo de datos | Transaccionales, digitales | Sensores físicos IoT |
| Riesgo principal | Fraude bancario | Daños/colapsos viales |
| Necesidad operativa | Baja latencia, adaptabilidad | Robustez, acción ante eventos críticos |
| Herramientas comunes | Kubeflow, Kafka/MQTT, Grafana | Kubeflow, MQTT, Grafana |

### Pipeline común con Kubeflow

Ambos casos pueden modelarse como pipelines automáticos:

1. Ingesta en streaming (Kafka o MQTT).
2. Preprocesamiento (limpieza, normalización).
3. Inferencia en tiempo real (serving del modelo entrenado).
4. Nodo de alertas (activaciones automáticas).
5. Registro y almacenamiento para retroalimentación.

### Utilidad del enfoque comparado

- Ilustra cómo el análisis en tiempo real y la ingeniería de datos trascienden sectores.
- Permite mejor transferencia de conocimiento y herramientas (fintech → infraestructura, y viceversa).
- Favorece la construcción de ciudades inteligentes y sinergias entre IA, analítica y sistemas operativos modernos.
- Converge esfuerzos en plataformas modulares (Kubeflow, Kafka, Grafana), optimizando recursos y talento.

*Actualmente, el proyecto se encuentra en fase de desarrollo, avanzando en la implementación de los pipelines de análisis en tiempo real y plataformas de MLOps descritos para ambos casos de uso. Se está trabajando tanto en la integración de fuentes de datos en streaming (financieras y de sensores físicos) como en la puesta en marcha de los modelos de inteligencia artificial y los sistemas de monitoreo automatizado, lo que permitirá validar y ajustar la arquitectura propuesta en entornos reales antes de su despliegue definitivo.

