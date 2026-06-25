# ¿Qué es Grafana?

**Grafana** es una de las plataformas de código abierto más populares del mundo para la **visualización y el análisis de datos métricos**.

En palabras sencillas: es la herramienta por excelencia para crear **tableros (dashboards) interactivos, visualmente espectaculares y en tiempo real**. No importa dónde estén guardados tus datos, Grafana te permite conectarte a ellos, hacerles consultas y transformarlos en gráficos de líneas, mapas de calor, barras, indicadores o mapas geográficos.

Para entender su éxito en el mundo del desarrollo, la infraestructura y la ciencia de datos, hay que mirar sus pilares fundamentales:

### 1. El principio del "Panel de Control Único"

Grafana no almacena tus datos de forma nativa. Su filosofía es conectarse a bases de datos existentes. Tiene soporte para decenas de **fuentes de datos (Data Sources)** mediante plugins, incluyendo:

* **Bases de datos de series temporales (TSDB):** Prometheus, InfluxDB, Graphite (ideales para infraestructura y monitoreo).
* **Bases de datos relacionales y NoSQL:** PostgreSQL, MySQL, Elasticsearch, MongoDB.
* **Servicios en la nube:** Amazon CloudWatch, Google Cloud Monitoring, Azure Monitor.

Esto significa que puedes cruzar datos de tu servidor Linux, de tu base de datos SQL y de tu nube en un mismo tablero gráfico.

### 2. ¿Para qué se utiliza principalmente?

* **Monitoreo de Infraestructura y Observabilidad (DevOps):** Ver en tiempo real el consumo de CPU, memoria RAM, tráfico de red, temperatura o almacenamiento de servidores, contenedores (Docker/Podman) o clústeres.
* **Seguimiento de Aplicaciones (APM):** Analizar cuántas peticiones por segundo recibe una API, el tiempo de respuesta de los endpoints o la tasa de errores (por ejemplo, errores 500).
* **Internet de las Cosas (IoT) y Sensores:** Graficar variables físicas en tiempo real (calidad del aire, humedad, vibración de maquinaria) capturadas por sensores remotos.
* **Métricas de Negocio:** Visualizar conversiones de usuarios, ventas por hora o usuarios activos en una plataforma.

### 3. Alertas Inteligentes

Grafana no solo sirve para mirar pantallas. Puedes configurar sistemas de **alertas**. Si la temperatura de un nodo sube de cierto umbral o si el almacenamiento se llena al **90%**, Grafana puede enviar automáticamente una notificación detallada a Discord, Slack, Telegram, correo electrónico o PagerDuty para que actúes de inmediato.

---

### La combinación ganadora: El "Stack LG" o "Prometheus + Grafana"

En el ecosistema tecnológico actual, Grafana casi nunca trabaja solo. Es sumamente común verlo emparejado con **Prometheus**.

* **Prometheus** se encarga de ir a buscar, recolectar y almacenar las métricas crudas en formato de texto.
* **Grafana** se conecta a Prometheus para leer esos datos masivos y darles un formato visual comprensible, limpio y analizable para los seres humanos.

Instalar **Grafana** en Linux es un proceso sencillo y depende de la distribución. A continuación, se muestra cómo instalarlo en las distribuciones más comunes: **Ubuntu/Debian**, **CentOS/RHEL/Fedora**, y también con **Docker** (opcional).

## Método 1: Instalación en Ubuntu / Debian

### 1. Agregar el repositorio oficial de Grafana

```bash
# Instalar dependencias
sudo apt install -y software-properties-common apt-transport-https wget

# Importar la clave GPG
wget -q -O - https://apt.grafana.com/gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/grafana.gpg

# Agregar el repositorio (versión OSS - Open Source)
echo "deb [signed-by=/usr/share/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
```

### 2. Instalar Grafana

```bash
sudo apt update
sudo apt install grafana -y
```

### 3. Iniciar y habilitar el servicio

```bash
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
sudo systemctl status grafana-server
```

> Por defecto, Grafana escucha en el puerto **3000**.

### 4. Acceder desde el navegador

Abrir navegador, se deberá observar:

```
http://localhost:3000
```

- Usuario por defecto: `admin`
- Contraseña por defecto: `admin` (regularmente pedirá cambiarla al primer inicio)

---

## Método 2: Instalación en CentOS / RHEL / Rocky Linux / AlmaLinux

### 1. Agregar el repositorio oficial

```bash
# Para RHEL/CentOS 7/8/9 o derivados
sudo tee /etc/yum.repos.d/grafana.repo <<EOF
[grafana]
name=grafana
baseurl=https://rpm.grafana.com
repo_gpgcheck=1
enabled=1
gpgcheck=1
gpgkey=https://rpm.grafana.com/gpg.key
sslverify=1
sslcacert=/etc/pki/tls/certs/ca-bundle.crt
EOF
```

### 2. Instalar Grafana

```bash
# En sistemas con dnf (RHEL 8/9, Fedora, Rocky, Alma)
sudo dnf install grafana -y

# O en sistemas con yum (CentOS 7)
sudo yum install grafana -y
```

### 3. Iniciar el servicio

```bash
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
sudo systemctl status grafana-server
```

### 4. Abrir el puerto en el firewall (si es necesario)

```bash
# Con firewalld
sudo firewall-cmd --permanent --add-port=3000/tcp
sudo firewall-cmd --reload
```

Acceder desde el navegador:

```
http://<la-ip>:3000
```

---

## Método 3: Instalación con Docker (opcional)

Si prefiere usar contenedores:

```bash
# Crear red (opcional, útil si usas Prometheus, etc.)
docker network create grafana-net

# Ejecutar Grafana
docker run -d \
  --name=grafana \
  --network=grafana-net \
  -p 3000:3000 \
  grafana/grafana-oss
```

Luego acceder a `http://localhost:3000`.

> Usar `grafana/grafana-enterprise` si emplea la versión Enterprise.

---

##  Seguridad recomendada

- **Cambiar la contraseña de admin** al primer inicio.
- Considerar usar un **proxy inverso** (como Nginx o Apache) con HTTPS si expone Grafana a internet.
- Desactivar el registro de usuarios si no es necesario: edita `/etc/grafana/grafana.ini` y pon:
  ```ini
  [users]
  allow_sign_up = false
  ```

Luego reiniciar:
```bash
sudo systemctl restart grafana-server
```

---

##  Archivos importantes

- Configuración: `/etc/grafana/grafana.ini`
- Logs: `/var/log/grafana/grafana.log`
- Plugins: `/var/lib/grafana/plugins/`

---

##  Verificar instalación

```bash
systemctl is-active grafana-server  # Debe decir "active"
ss -tuln | grep 3000               # Verificar que escucha en el puerto 3000
```
