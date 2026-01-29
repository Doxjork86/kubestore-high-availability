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
![HPA Scaling]
<img width="760" height="122" alt="hpa" src="https://github.com/user-attachments/assets/6948857e-90cc-4297-a743-340b5afa0e57" />


### Actualización sin Cortes (v1 -> v2)
*El cliente recibe la nueva versión sin interrupción del servicio.*
![Rolling Update]
<img width="655" height="208" alt="rolling1" src="https://github.com/user-attachments/assets/959a19e1-2ee6-4780-9bd7-271a1ab17d68" />
<img width="652" height="261" alt="rolling2" src="https://github.com/user-attachments/assets/3b3079a1-77f7-48d0-a4bf-d360cfa81750" />
<img width="759" height="41" alt="image" src="https://github.com/user-attachments/assets/0b62af33-ed37-4f1c-8d93-033c9b27bd23" />


### Observabilidad
*Dashboard de Grafana mostrando el consumo de recursos del clúster.*
![Grafana Dashboard]
<img width="1603" height="265" alt="grafana" src="https://github.com/user-attachments/assets/1f16e657-4350-47bb-94cf-3af189effb67" />

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
