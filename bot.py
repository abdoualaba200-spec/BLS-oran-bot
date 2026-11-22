

import os
import requests
from flask import Flask, request

TOKEN = os.environ["BOT_TOKEN"]
URL = f"https://api.telegram.org/bot{TOKEN}/"

app = Flask(__name__)

def send_message(chat_id, text):
    requests.post(
        URL + "sendMessage",
        json={"chat_id": chat_id, "text": text},
        timeout=15
    )

@app.route("/")
def home():
    return "BLS Oran Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if chat_id and text == "/start":
        send_message(
            chat_id,
            "مرحبا بك! 🤖\nبوت BLS Oran راه يخدم بنجاح!\nسنضيف مراقبة المواعيد لاحقاً."
        )

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
