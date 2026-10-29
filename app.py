import os
import telebot
from flask import Flask
import threading

# توکن از تنظیمات Render خونده میشه
TOKEN = os.environ.get('TELEGRAM_TOKEN', '949689925:eapHLLUVNw5X8iFstGdx2JKgui5RsHBCUgA')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! من بات جدیدم و حالا کاملاً مال خودت هستم. 😎")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "تو گفتی: " + message.text)

@app.route('/')
def home():
    return "Bot is running"

def run_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    # اجرای بات در یک ترد جداگانه
    threading.Thread(target=run_bot).start()
    # اجرای وب‌سرور برای اینکه Render فکر نکنه برنامه خوابیده
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
