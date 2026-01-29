import os
import time
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# Simulación de carga pesada al inicio (Ej: conectando a DBs, cargando IA...)
print("⏳ Iniciando carga de catálogo...", flush=True)
time.sleep(10)  # La app tardará 10s en estar lista
print("✅ Catálogo cargado. Tienda lista.", flush=True)

# Conexión a Redis usando las variables de K8s
redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_pass = os.environ.get('REDIS_PASSWORD', None)
r = redis.Redis(host=redis_host, port=6379, password=redis_pass, decode_responses=True)

@app.route('/')
def home():
    try:
        # Intentamos contar una visita en Redis
        visits = r.incr('counter')
    except Exception as e:
        visits = "Error conectando a Redis"
    return jsonify({"store": "KubeStore v2 🚀 (Black Friday)", "visits": visits, "status": "Online"})

@app.route('/health')
def health():
    # K8s llamará aquí para saber si estamos vivos
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
