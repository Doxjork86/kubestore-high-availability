# 🛒 KubeStore: High Availability E-Commerce Infrastructure

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

**KubeStore** es una simulación de infraestructura de comercio electrónico resiliente, diseñada para soportar cargas de tráfico masivo y garantizar cero tiempo de inactividad (Zero-Downtime) durante despliegues.

Este proyecto demuestra la implementación de patrones avanzados de **Cloud-Native** y orquestación con Kubernetes.

## 🏗️ Arquitectura

El sistema está desacoplado en microservicios y componentes de infraestructura:

* **Store API:** Backend en Python (Flask) que sirve el catálogo y gestiona transacciones.
* **Data Layer:** Redis persistente para gestión de sesiones y carritos de compra.
* **Orchestration:** Kubernetes (Minikube) gestionando el ciclo de vida de los pods.
* **Security:** Gestión de secretos (`Secret`) y configuraciones (`ConfigMap`) desacopladas del código.

## 🚀 Características Clave (Key Features)

### 1. Auto-Escalado Inteligente (HPA)
El sistema implementa **Horizontal Pod Autoscaler**.
- **Comportamiento:** Monitorea el uso de CPU en tiempo real.
- **Acción:** Escala horizontalmente de **1 a 10 réplicas** cuando la carga supera el 50%.
- **Resultado:** Capacidad elástica para soportar picos de tráfico (ej: Black Friday).

### 2. Zero-Downtime Deployments
Actualizaciones de versión utilizando la estrategia **Rolling Update**.
- Garantiza que siempre haya pods disponibles durante la transición v1 -> v2.
- Los usuarios nunca experimentan errores de conexión durante el despliegue.

### 3. Self-Healing & Probes
- **Liveness Probes:** Reinicia automáticamente contenedores bloqueados.
- **Readiness Probes:** Evita enviar tráfico a pods que aún están cargando datos críticos, previniendo errores 500 en el arranque.

## 📸 Evidencia de Ejecución

### Auto-Escalado bajo Ataque
*El HPA detecta un pico de CPU del 118% y escala las réplicas automáticamente.*
![HPA Scaling](LINK_A_TU_FOTO_HPA_AQUI)

### Actualización sin Cortes (v1 -> v2)
*El cliente recibe la nueva versión sin interrupción del servicio.*
![Rolling Update](LINK_A_TU_FOTO_CURL_V2_AQUI)

### Observabilidad
*Dashboard de Grafana mostrando el consumo de recursos del clúster.*
![Grafana Dashboard](LINK_A_TU_FOTO_GRAFANA_AQUI)

## 🛠️ Cómo ejecutar este proyecto

### Prerrequisitos
- Docker & Minikube
- kubectl

### Despliegue
```bash
# 1. Iniciar Minikube
minikube start

# 2. Crear Namespace
kubectl create namespace kubestore

# 3. Desplegar Base de Datos y Secretos
kubectl apply -f k8s/redis-secret.yaml
kubectl apply -f k8s/redis-config.yaml
kubectl apply -f k8s/redis.yaml

# 4. Desplegar API
kubectl apply -f k8s/api.yaml

# 5. Activar Auto-Escalado
kubectl apply -f k8s/hpa.yaml
