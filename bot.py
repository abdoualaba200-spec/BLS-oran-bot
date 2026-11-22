
import os
import requests
import time

TOKEN = os.environ.get("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

offset = 0

print("BLS Bot is running!")

while True:
    try:
        response = requests.get(
            URL + "getUpdates",
            params={"offset": offset, "timeout": 30},
            timeout=35
        ).json()

        for update in response.get("result", []):
            offset = update["update_id"] + 1
            message = update.get("message", {})
            chat_id = message.get("chat", {}).get("id")
            text = message.get("text", "")

            if chat_id and text == "/start":
                requests.post(
                    URL + "sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": "مرحبا! 🤖 بوت BLS Oran راه يخدم بنجاح!"
                    }
                )

    except Exception as error:
        print(error)
        time.sleep(5)
