from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
API_KEY = os.getenv("OPENROUTER_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    prompt = request.json.get("prompt")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openrouter/mistral",
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
    return jsonify(r.json())

@app.route("/", methods=["GET"])
def home():
    return "✅ سرور OpenRouter روی Railway فعاله!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
