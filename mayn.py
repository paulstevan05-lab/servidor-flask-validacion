from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔑 Clave universal
VALID_KEY = "A9X4M7K3Z1Q8"

# 📡 Endpoint raíz (para uptime/probas rápidas)
@app.route("/", methods=["GET"])
def home():
    return "Servidor activo ✅", 200  # Siempre responde 200 OK

# 🔐 Endpoint de validación (POST JSON {"key": "..."} )
@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    if data and data.get("key") == VALID_KEY:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 403

if __name__ == "__main__":
    # Para pruebas locales (en Render se usa gunicorn + Procfile)
    app.run(host="0.0.0.0", port=8080)
