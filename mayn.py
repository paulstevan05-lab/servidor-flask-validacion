from flask import Flask, request, jsonify
import os

app = Flask(__name__)

VALID_KEYS = {
    "A5X4Z7K3Z1T9",
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "active"}), 200

@app.route("/validate", methods=["POST"])
def validate():
    try:
        data = request.get_json()
        if data and data.get("key") in VALID_KEYS:
            return jsonify({"status": "success"}), 200
        return jsonify({"status": "fail"}), 403
    except Exception as e:
        return jsonify({"status": "fail", "error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)















