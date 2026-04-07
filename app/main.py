from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Nathan DevOps lab",
        "env": os.getenv("APP_ENV", "dev")
    })

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
