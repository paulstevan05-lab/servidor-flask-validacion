from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔑 Claves
VALID_KEYS = {
    "A0X4M7K3Z1Q0",
    "KEYXA4M7K3Z0VIP",
    "A9X4M0K3Z1Q0"
}

@app.route("/", methods=["GET"])
def home():
    return "Servidor activo ✅", 200

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()

    if data and data.get("key") in VALID_KEYS:
        return jsonify({"status": "success"}), 200

    return jsonify({"status": "fail"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)







