from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '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'  # 🔁 اینجا کلید خودتو بذار

@app.route('/ask', methods=['POST'])
def ask_openrouter():
    prompt = request.json.get('prompt')
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openrouter/mistral",  # یا هر مدل دیگه
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "سرور OpenRouter فعاله 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
