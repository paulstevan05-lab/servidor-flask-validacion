from flask import Flask, request, jsonify
import os

app = Flask(name)

VALID_KEYS = {
    "A5X4Z7K3Z1T9",
}

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "active"}), 200

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    if data and data.get("key") in VALID_KEYS:
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 403

if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)













