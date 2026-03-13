import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# Загружаем токен
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Токен не найден! Проверь .env файл")

# Создаем бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Клавиатура
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Цены"), KeyboardButton(text="📁 Примеры")],
        [KeyboardButton(text="👤 Обо мне"), KeyboardButton(text="📞 Контакты")]
    ],
    resize_keyboard=True
)

# Старт
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"Я Александр, делаю ботов от 2500₽.\n"
        f"Выбирай 👇",
        reply_markup=main_keyboard
    )

# Цены
@dp.message(lambda message: message.text == "💰 Цены")
async def prices(message: Message):
    await message.answer(
        "💰 Цены:\n"
        "• Простой бот — 2500₽\n"
        "• Бот с каталогом — 3500₽\n"
        "• Бот с админкой — 5000₽"
    )

# Примеры
@dp.message(lambda message: message.text == "📁 Примеры")
async def examples(message: Message):
    await message.answer(
        "📁 Примеры:\n"
        "• Бот для записи\n"
        "• Бот-магазин\n"
        "• Бот для отзывов"
    )

# Обо мне
@dp.message(lambda message: message.text == "👤 Обо мне")
async def about(message: Message):
    await message.answer("👤 Александр, 15 лет. Делаю ботов через нейросети.")

# Контакты
@dp.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer("📞 Пиши: @AlexDev_bot_ai")

# Запуск
async def main():
    print("✅ Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())