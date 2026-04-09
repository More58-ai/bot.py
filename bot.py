import asyncio
from flask import Flask, request, jsonify
from flask_cors import CORS
from aiogram import Bot
from datetime import datetime

# Конфігурація
TOKEN = "8796172625:AAEk2jRV4OY65elspv1qLeAeAEPC4YEay4o"
GROUP_ID = --1003782583708  # <-- ID вашої групи

app = Flask(__name__)
CORS(app)
bot = Bot(token=TOKEN)

def get_now():
    return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

@app.route('/send-order', methods=['POST'])
def send_order():
    data = request.json

    message = (
        f"🆕 НОВЕ ЗАМОВЛЕННЯ\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📦 Товар: {data.get('product')}\n"
        f"👤 Нік: {data.get('nickname')}\n"
        f"📱 Discord: {data.get('discord')}\n"
        f"📧 Email: {data.get('email')}\n"
        f"💰 Ціна: {data.get('price')} ₴\n"
        f"💳 Метод: {data.get('paymentMethod')}\n"
        f"⏳ Термін: {data.get('duration')}\n"
        f"🆔 ID: {data.get('id')}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📅 {get_now()}"
    )

    # Створюємо новий цикл подій для кожного запиту
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Змінено ADMIN_ID на GROUP_ID
        loop.run_until_complete(
            bot.send_message(chat_id=GROUP_ID, text=message)
        )
        return jsonify({"success": True})
    except Exception as e:
        print(f"Помилка: {e}")
        return jsonify({"success": False, "error": str(e)})
    finally:
        loop.close()

if __name__ == '__main__':
    print("🚀 Сервер запущено на http://localhost:5000")
    app.run(port=5000)
