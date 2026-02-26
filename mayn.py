from flask import Flask, request, jsonify
import os

app = Flask(__name__)

VALID_KEYS = {
    "A5X4Z7K3Z1T2",
    "K3Y1A4T9K1Z3VIP",
    "K3Y1A4T2K1Z1VIP",
    "K3Y1V4T3K1Z1VIP",
    "K3YXT1M7K3Z9VIP",
    "K3YXT9M7K9Z9VIX",
    "K3YXA1M7K3Z7VIP",
    "AX4M0K3Z1VIX",
    "A3X4M0K3Z1Q7"
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)










