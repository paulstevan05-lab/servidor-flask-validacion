from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

VALID_KEYS = {
    "A5X4Z7K3Z1T9",
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "active"}), 200

@app.route("/validate", methods=["POST", "GET"])
def validate():
    try:
        # Para POST con JSON
        if request.method == "POST":
            data = request.get_json(force=True, silent=True)
            if not data:
                logger.error("No JSON data received")
                return jsonify({"status": "fail", "error": "No JSON"}), 400
            key = data.get("key")
        # Para GET con query param
        else:
            key = request.args.get("key")
        
        logger.info(f"Validando key: {key}")
        
        if key and key in VALID_KEYS:
            logger.info(f"Key válida: {key}")
            return jsonify({"status": "success"}), 200
        else:
            logger.warning(f"Key inválida: {key}")
            return jsonify({"status": "fail"}), 403
            
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"status": "fail", "error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logger.info(f"Iniciando en puerto: {port}")
    app.run(host="0.0.0.0", port=port, debug=False)












