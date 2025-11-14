from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔑 Clave universal
CLAVE_VALIDA = "A9X4M7K3Z1Q8"

# 🏠 Endpoint raíz (para pruebas rápidas)
@app.route("/", methods=["GET"])
def home():
    return "Servidor activo ✅", 200

# 🔐 Validación de licencia
@app.route("/validate", methods=["POST"])
def validate():
    datos = request.get_json()

    if datos and datos.get("key") == CLAVE_VALIDA:
        return jsonify({"estado": "exito"}), 200
    
    return jsonify({"estado": "fallar"}), 403


# Para correr localmente
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
