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

@app.route("/version")
def version():
    return jsonify({"version": "1.0.1-FinalofFinal"})

@app.route("/update")
defversion():
returnjsonify({"update":"test CICD Docker Container"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
