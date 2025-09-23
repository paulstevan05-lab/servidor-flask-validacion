from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔑 Clave universal
VALID_KEY = "A9X4M7K3Z1Q8"

# 🟢 Endpoint raíz (para UptimeRobot o pruebas rápidas)
@app.route("/", methods=["GET"])
def home():
    return "Servidor activo ✅", 200

# 🔐 Endpoint de validación tolerante
@app.route("/validate", methods=["GET", "POST"])
def validate():
    key = None

    # 1) JSON: {"key": "..."}
    if request.is_json:
        data = request.get_json(silent=True) or {}
        if isinstance(data, dict):
            key = data.get("key")

    # 2) form-data
    if not key:
        key = request.form.get("key")

    # 3) querystring: /validate?key=...
    if not key:
        key = request.args.get("key")

    # 4) texto plano en el body
    if not key:
        raw = (request.get_data(as_text=True) or "").strip()
        if raw.startswith("key="):
            raw = raw.split("=", 1)[1]
        if raw:
            key = raw

    ok = (key == VALID_KEY)
    return jsonify({"status": "success" if ok else "fail"}), (200 if ok else 403)

# 🛟 Alias por compatibilidad (/try_once redirige a la misma validación)
@app.route("/try_once", methods=["GET", "POST"])
def try_once():
    return validate()

# 🧪 (Opcional) Endpoint para depuración: ver qué manda tu APK
@app.route("/echo", methods=["GET", "POST"])
def echo():
    return jsonify({
        "method": request.method,
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": (request.get_json(silent=True) if request.is_json else None),
        "data": request.get_data(as_text=True),
        "headers": dict(request.headers),
    }), 200

if __name__ == "__main__":
    # Solo para pruebas locales. En Render se usa gunicorn (Procfile)
    app.run(host="0.0.0.0", port=8080)
