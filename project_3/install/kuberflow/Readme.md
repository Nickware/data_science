# Instalación Kubeflow en Linux

Guía paso a paso para instalar Kubeflow en Linux, usando **MicroK8s** (una distribución ligera de Kubernetes ideal para desarrollo local). Este enfoque es recomendado oficialmente por el equipo de Kubeflow para entornos de prueba o desarrollo.

---

## Requisitos previos

- Sistema: **Linux (Ubuntu 20.04/22.04 recomendado)**
- Al menos **8 GB de RAM** (16 GB recomendados)
- Al menos **4 CPUs**
- Espacio en disco: **50 GB+**
- Acceso a internet

---

## Paso 1: Instalar MicroK8s

MicroK8s es una versión ligera y fácil de usar de Kubernetes mantenida por Canonical.

```bash
# Actualizar sistema
sudo apt update

# Instalar snap (si no se tiene instalado)
sudo apt install snapd -y

# Instalar MicroK8s
sudo snap install microk8s --classic

# Añadir usuario al grupo microk8s (evita usar sudo)
sudo usermod -a -G microk8s $USER
newgrp microk8s  # Aplicar el cambio de grupo en la sesión actual
```

> Cerrar y volver abrir la terminal o ejecutar `newgrp microk8s` para aplicar los permisos.

---

## Paso 2: Configurar MicroK8s

Habilitar los addons necesarios:

```bash
# Habilitar DNS, almacenamiento y dashboard (opcional)
microk8s enable dns storage

# Verificar que el clúster esté listo
microk8s status --wait-ready
```

---

## Paso 3: Instalar `kubectl` (si no está disponible)

MicroK8s incluir su propia versión de `kubectl`:

```bash
# Crear alias para usar kubectl sin prefijo
sudo snap alias microk8s.kubectl kubectl

# Verifica
kubectl get nodes
```

---

## Paso 4: Instalar Kubeflow con el operador de MicroK8s (método más sencillo)

MicroK8s incluir un **addon de Kubeflow** que automatiza toda la instalación:

```bash
# Habilitar el addon de Kubeflow (¡esto puede tardar 10-30 minutos!)
microk8s enable kubeflow
```

Durante la instalación, se pedirá:

- Una contraseña para el usuario **admin**.
- Una IP o nombre de host para acceder a la interfaz web (por defecto usar `10.64.140.43.xip.io`, pero se puede usar `localhost` si accede desde la misma máquina).

>  **Nota**: Si está en una máquina local, puede aceptar los valores por defecto.

Una vez finalizado, verá un mensaje como:

```
Kubeflow is available at http://<IP>.xip.io
Username: admin
Password: <la que eligio>
```

---

## Paso 5: Acceder a la interfaz web de Kubeflow

Abrir un navegador y ver a la URL que mostró el instalador, por ejemplo:

```
http://10.64.140.43.xip.io
```

O si esta en la misma máquina, puede usar **port-forwarding** para acceder vía `localhost`:

```bash
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```

Luego acceder a:  
 **http://localhost:8080**

Iniciar sesión con:
- **Usuario**: `admin`
- **Contraseña**: la que se definio durante la instalación

---

## (Opcional) Verificar los pods

Puede verificar que todos los componentes se hayan desplegado correctamente:

```bash
kubectl get pods -n kubeflow
```

Se debería ver varios pods en estado `Running`.

---

## Limpieza (si desea desinstalar)

```bash
# Deshabilitar Kubeflow
microk8s disable kubeflow

# O eliminar todo MicroK8s
sudo snap remove microk8s
```

---

## Notas importantes

- **Kubeflow es complejo**: está diseñado para entornos de producción con múltiples usuarios, pipelines, notebooks, etc.
- **No use esta instalación en producción**: el addon de MicroK8s es solo para desarrollo/local.
- Para producción, considerar usar **Kubeflow en un clúster Kubernetes gestionado** (como EKS, GKE o AKS) con herramientas como **kfctl** o **manifests de GitHub**.
---

## Recursos oficiales

- [Kubeflow en MicroK8s](https://ubuntu.com/kubeflow/install)
- [Documentación oficial de Kubeflow](https://www.kubeflow.org/)

