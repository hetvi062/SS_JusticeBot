from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    response = requests.post(rasa_url, json={"message": user_input})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5000)
