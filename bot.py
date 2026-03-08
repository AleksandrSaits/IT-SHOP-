import asyncio
import threading
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from flask import Flask
import os

TOKEN = "8755271111:AAEFdfPoJCGYJcRmykDCPGoCZ6pLbm_Fj5w"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ---- Telegram bot ----

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Привет! Я бот портфолио 🤖")

async def run_bot():
    await dp.start_polling(bot)

# ---- Flask server ----

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ---- Run both ----

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())
