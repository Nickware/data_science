# Instalar **Grafana** en Linux 

Instalar **Grafana** en Linux es un proceso sencillo y depende de la distribución. A continuación, se muestra cómo instalarlo en las distribuciones más comunes: **Ubuntu/Debian**, **CentOS/RHEL/Fedora**, y también con **Docker** (opcional).

---

## ¿Qué es Grafana?
Grafana es una plataforma de visualización y análisis de métricas que permite crear dashboards interactivos a partir de fuentes de datos como Prometheus, InfluxDB, MySQL, Elasticsearch, y muchas más.

---

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

Abre tu navegador y ve a:

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

Accede desde tu navegador:

```
http://<tu-ip>:3000
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

Luego accede a `http://localhost:3000`.

> 💡 Usar `grafana/grafana-enterprise` si emplea la versión Enterprise.

---

##  Seguridad recomendada

- **Cambiar la contraseña de admin** al primer inicio.
- Considerar usar un **proxy inverso** (como Nginx o Apache) con HTTPS si expones Grafana a internet.
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
