# KubeStore: High Availability Infrastructure 🛒

Simulación de un entorno de producción para un E-Commerce capaz de soportar picos de tráfico masivos (Black Friday scenario).

🚀 Stack Tecnológico

K8s Core: Deployments, Services (NodePort), ConfigMaps, Secrets.

Automation: Horizontal Pod Autoscaler (HPA).

Health Checks: Liveness & Readiness Probes.

Data Layer: Redis (con inyección segura de credenciales).

⚔️ Desafíos Superados

Auto-Escalado: Implementación de HPA que escala de 1 a 10 réplicas automáticamente bajo estrés de CPU (simulado con Load Generator).

Zero-Downtime Updates: Despliegue de nuevas versiones mediante estrategia Rolling Update sin interrupción de servicio.

Seguridad: Desacoplamiento de configuración y contraseñas usando K8s Secrets.
