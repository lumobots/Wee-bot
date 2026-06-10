import requests
import schedule
import time

BOT_TOKEN = "8680118124:AAGRus8swMAa3T7g4z-w5y9QPC4wHcJoPL0"
CHAT_ID = "7862654660"

def send_wee_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "Let's WEE together 🎉"
    }
    response = requests.post(url, json=payload)
    if response.ok:
        print("✅ Message sent!")
    else:
        print(f"❌ Failed: {response.text}")

send_wee_message()
schedule.every(1).hours.do(send_wee_message)

print("🤖 Bot is running...")
while True:
    schedule.run_pending()
    time.sleep(30)
