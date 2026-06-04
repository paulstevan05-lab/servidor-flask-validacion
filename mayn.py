from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 1. Tu lista de keys individuales (La tuya operativa sigue intacta)
VALID_KEYS = {
    "A5X4Z7K3Z1T9",
    # Para crear más keys, solo agregalas aquí abajo:
    # "NUEVA_KEY_1234",
    # "OTRA_KEY_5678",
}

# 2. Diccionario de Usuarios y Contraseñas (Puedes crear todos los que quieras)
# El formato es "usuario": "contraseña"
VALID_USERS = {
    "a7f39b2c4e": "@kamikazesupport",
    # Para crear más usuarios, solo agregalos aquí abajo siguiendo el formato:
    # "cliente1": "mipassword123",
    # "pedro": "clave456",
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
            
            # Verificamos si el usuario existe en la lista y si su contraseña es correcta
            if req_user in VALID_USERS and VALID_USERS[req_user] == req_pass:
                return jsonify({"status": "success", "login_type": "userpass"}), 200
                
        # Si fallan ambos métodos
        return jsonify({"status": "fail", "message": "Credenciales o Key inválidas"}), 403
        
    except Exception as e:
        return jsonify({"status": "fail", "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)















