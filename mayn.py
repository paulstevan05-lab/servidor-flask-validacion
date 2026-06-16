from flask import Flask, request, jsonify
from flask_cors import CORS  # <--- IMPORTANTE PARA EVITAR EL ERROR DE CONEXIÓN
import os

app = Flask(__name__)
CORS(app)  # <--- HABILITA CORS PARA TODA LA APP

# 1. Tu lista de keys individuales (La tuya operativa sigue intacta)
VALID_KEYS = {
    "A5X4Z7K3Z1T9",
}

# 2. Diccionario de Usuarios y Contraseñas
VALID_USERS = {
    "a7f39b2c4e": "@kamikazesupport",
    "tedm4ster": "tedm4ster",
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "active"}), 200

@app.route("/validate", methods=["POST"])
def validate():
    try:
        data = request.get_json()
        
        # --- MÉTODO 1: Validación por Key única ---
        if "key" in data:
            if data.get("key") in VALID_KEYS:
                return jsonify({"status": "success", "login_type": "key"}), 200
                
        # --- MÉTODO 2: Validación por Múltiples User:Pass ---
        elif "user" in data and "pass" in data:
            req_user = data.get("user")
            req_pass = data.get("pass")
            
            if req_user in VALID_USERS and VALID_USERS[req_user] == req_pass:
                return jsonify({"status": "success", "login_type": "userpass"}), 200
                
        # Si fallan ambos métodos
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 403
        
    except Exception as e:
        return jsonify({"status": "fail", "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)















