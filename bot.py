import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

bot = Bot(token="8755271111:AAEFdfPoJCGYJcRmykDCPGoCZ6pLbm_Fj5w")
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤖 AI чат бот")],
        [KeyboardButton(text="📦 Каталог")],
        [KeyboardButton(text="📅 Запись")],
        [KeyboardButton(text="📩 Связаться")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Добро пожаловать в демо бота.\nВыберите функцию:", reply_markup=menu)

@dp.message(lambda m: m.text == "🤖 AI чат бот")
async def ai_demo(msg: types.Message):
    await msg.answer("Напишите любой вопрос.")

@dp.message(lambda m: m.text == "📦 Каталог")
async def catalog(msg: types.Message):
    await msg.answer("📱 Телефоны\n💻 Ноутбуки\n🎧 Аксессуары")

@dp.message(lambda m: m.text == "📅 Запись")
async def booking(msg: types.Message):
    await msg.answer("Напишите ваше имя для записи.")

@dp.message(lambda m: m.text == "📩 Связаться")
async def contact(msg: types.Message):
    await msg.answer("Напишите разработчику: @твойник")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
