import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Загружаем токен из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ТВОЙ ЮЗЕРНЕЙМ
MY_USERNAME = "AlexDev_bot_ai"

# Проверка что токен загрузился
if not BOT_TOKEN:
    raise ValueError("Токен не найден! Создай файл .env с BOT_TOKEN=твой_токен")

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ============ КНОПКИ ============
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💰 Цены"),
            KeyboardButton(text="📁 Примеры")
        ],
        [
            KeyboardButton(text="👤 Обо мне"),
            KeyboardButton(text="📞 Контакты")
        ]
    ],
    resize_keyboard=True
)

# ============ КОМАНДА START ============
@dp.message(Command("start"))
async def start_command(message: Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"👋 Привет, {user_name}!\n\n"
        f"Я Александр Балашов, мне 15 лет.\n"
        f"🤖 Делаю простых ботов под ключ.\n"
        f"🔥 Цена от 2500₽\n\n"
        f"Выбирай функцию ниже 👇",
        reply_markup=main_keyboard
    )

# ============ КНОПКА ЦЕНЫ ============
@dp.message(lambda message: message.text == "💰 Цены")
async def prices(message: Message):
    await message.answer(
        "💰 **МОИ ЦЕНЫ:**\n\n"
        "▫️ Простой бот — **2500₽**\n"
        "▫️ Бот с каталогом — **3500₽**\n"
        "▫️ Бот с админкой — **5000₽**\n\n"
        "✅ Всё включено"
    )

# ============ КНОПКА ПРИМЕРЫ ============
@dp.message(lambda message: message.text == "📁 Примеры")
async def examples(message: Message):
    await message.answer(
        "📁 **ЧТО ДЕЛАЛ:**\n\n"
        "🔹 Бот для записи\n"
        "🔹 Бот-магазин\n"
        "🔹 Бот для отзывов\n"
        "🔹 Бот-анкета\n\n"
        "Хочешь так же? Пиши!"
    )

# ============ КНОПКА ОБО МНЕ ============
@dp.message(lambda message: message.text == "👤 Обо мне")
async def about(message: Message):
    await message.answer(
        "👤 **ОБО МНЕ:**\n\n"
        "🔸 Имя: Александр Балашов\n"
        "🔸 Возраст: 15 лет\n\n"
        "🚀 Делаю ботов через нейросети"
    )

# ============ КНОПКА КОНТАКТЫ ============
@dp.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: Message):
    contact_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Написать", url=f"https://t.me/{MY_USERNAME}")]
        ]
    )
    
    await message.answer(
        f"📞 **КОНТАКТЫ:**\n\n"
        f"👤 Telegram: @{MY_USERNAME}\n"
        f"👇 Жми кнопку:",
        reply_markup=contact_button
    )

# ============ ЗАПУСК ============
async def main():
    print("✅ Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())            KeyboardButton(text="📞 Контакты")
        ]
    ],
    resize_keyboard=True
)

# ============ КОМАНДА START ============
@dp.message(Command("start"))
async def start_command(message: Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"👋 Привет, {user_name}!\n\n"
        f"Я Александр Балашов, мне 15 лет.\n"
        f"🤖 Делаю простых ботов под ключ.\n"
        f"🔥 Цена от 2500₽\n\n"
        f"Выбирай функцию ниже 👇",
        reply_markup=main_keyboard
    )

# ============ КНОПКА ЦЕНЫ ============
@dp.message(lambda message: message.text == "💰 Цены")
async def prices(message: Message):
    await message.answer(
        "💰 **МОИ ЦЕНЫ:**\n\n"
        "▫️ Простой бот (заявки, приветствие) — **2500₽**\n"
        "▫️ Бот с каталогом товаров — **3500₽**\n"
        "▫️ Бот с админ-панелью — **5000₽**\n\n"
        "✅ Всё включено: код, настройка, поддержка"
    )

# ============ КНОПКА ПРИМЕРЫ ============
@dp.message(lambda message: message.text == "📁 Примеры")
async def examples(message: Message):
    await message.answer(
        "📁 **ЧТО Я УЖЕ ДЕЛАЛ:**\n\n"
        "🔹 Бот для записи к парикмахеру\n"
        "🔹 Бот-магазин одежды\n"
        "🔹 Бот для сбора отзывов\n"
        "🔹 Бот-анкета знакомств\n\n"
        "🔥 Хочешь так же? Жми /start и пиши в личку!"
    )

# ============ КНОПКА ОБО МНЕ ============
@dp.message(lambda message: message.text == "👤 Обо мне")
async def about(message: Message):
    await message.answer(
        "👤 **ОБО МНЕ:**\n\n"
        "🔸 Имя: Александр Балашов\n"
        "🔸 Возраст: 15 лет\n"
        "🔸 Город: РФ\n\n"
        "🚀 Делаю ботов с помощью нейросетей (Quinn, DeepSeek)\n"
        "💡 Беру простые заказы, делаю быстро и недорого\n"
        "🎯 Цель: чтобы каждый мог позволить себе бота"
    )

# ============ КНОПКА КОНТАКТЫ ============
@dp.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: Message):
    contact_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Написать автору", url=f"https://t.me/{MY_USERNAME}")]
        ]
    )
    
    await message.answer(
        f"📞 **КОНТАКТЫ:**\n\n"
        f"👤 Telegram: @{MY_USERNAME}\n"
        f"⏰ Отвечаю с 10:00 до 22:00\n\n"
        f"👇 Жми кнопку ниже, чтобы написать мне:",
        reply_markup=contact_button
    )

# ============ ЗАПУСК ============
async def main():
    print("✅ Бот запущен! Заходи в Telegram и проверяй @AlexDev_bot_ai")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())# ============ КОМАНДА START ============
@dp.message(Command("start"))
async def start_command(message: Message):
    user_name = message.from_user.first_name
    await message.answer(
        f"👋 Привет, {user_name}!\n\n"
        f"Я Александр Балашов, мне 15 лет.\n"
        f"🤖 Делаю простых ботов под ключ.\n"
        f"🔥 Цена от 2500₽\n\n"
        f"Выбирай 👇",
        reply_markup=main_keyboard
    )

# ============ КНОПКА ЦЕНЫ ============
@dp.message(lambda message: message.text == "💰 Цены")
async def prices(message: Message):
    await message.answer(
        "💰 **ЦЕНЫ:**\n\n"
        "▫️ Простой бот — **2500₽**\n"
        "▫️ Бот с каталогом — **3500₽**\n"
        "▫️ Бот с админкой — **5000₽**\n\n"
        "✅ Всё включено"
    )

# ============ КНОПКА ПРИМЕРЫ ============
@dp.message(lambda message: message.text == "📁 Примеры")
async def examples(message: Message):
    await message.answer(
        "📁 **ЧТО ДЕЛАЛ:**\n\n"
        "🔹 Бот для записи\n"
        "🔹 Бот-магазин\n"
        "🔹 Бот для отзывов\n"
        "🔹 Бот-анкета\n\n"
        "Хочешь так же? Пиши!"
    )

# ============ КНОПКА ОБО МНЕ ============
@dp.message(lambda message: message.text == "👤 Обо мне")
async def about(message: Message):
    await message.answer(
        "👤 **ОБО МНЕ:**\n\n"
        "🔸 Имя: Александр Балашов\n"
        "🔸 Возраст: 15 лет\n\n"
        "🚀 Делаю ботов через нейросети\n"
        "💡 Просто и недорого"
    )

# ============ КНОПКА КОНТАКТЫ ============
@dp.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: Message):
    contact_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Написать", url=f"https://t.me/{MY_USERNAME}")]
        ]
    )
    
    await message.answer(
        f"📞 **КОНТАКТЫ:**\n\n"
        f"👤 Telegram: @{MY_USERNAME}\n"
        f"👇 Жми кнопку:",
        reply_markup=contact_button
    )

# ============ ЗАПУСК ============
async def main():
    print("✅ Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
Это демонстрационный бот разработчика.

Выберите функцию ниже 👇
"""

    await message.answer(
        text,
        parse_mode="Markdown",
        reply_markup=main_menu
    )

# ----------- AI ЧАТ -----------

@dp.callback_query(lambda c: c.data == "ai")
async def ai_menu(callback: types.CallbackQuery):

    text = """
🤖 *AI Демонстрация*

Напишите любой вопрос.
Бот ответит (демо версия).
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

# ----------- МАГАЗИН -----------

shop_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📱 Телефоны", callback_data="phones")],
        [InlineKeyboardButton(text="💻 Ноутбуки", callback_data="laptops")],
        [InlineKeyboardButton(text="🎧 Аксессуары", callback_data="access")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
    ]
)

@dp.callback_query(lambda c: c.data == "shop")
async def shop(callback: types.CallbackQuery):

    text = """
🛒 *Демо магазин*

Выберите категорию товаров.
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=shop_menu
    )

# ----------- ТОВАРЫ -----------

@dp.callback_query(lambda c: c.data == "phones")
async def phones(callback: types.CallbackQuery):

    text = """
📱 *iPhone 15*

Цена: 999$

Демонстрационный товар.
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

@dp.callback_query(lambda c: c.data == "laptops")
async def laptops(callback: types.CallbackQuery):

    text = """
💻 *MacBook Pro*

Цена: 1999$

Демонстрационный товар.
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

@dp.callback_query(lambda c: c.data == "access")
async def access(callback: types.CallbackQuery):

    text = """
🎧 *AirPods Pro*

Цена: 249$

Демонстрационный товар.
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

# ----------- ЗАПИСЬ -----------

@dp.callback_query(lambda c: c.data == "booking")
async def booking(callback: types.CallbackQuery):

    text = """
📅 *Система записи*

Введите ваше имя для записи.
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

# ----------- ПОРТФОЛИО -----------

@dp.callback_query(lambda c: c.data == "portfolio")
async def portfolio(callback: types.CallbackQuery):

    text = """
💼 *Портфолио*

Я разрабатываю:

🤖 AI боты  
🛒 боты магазины  
📅 системы записи  
📊 автоматизацию бизнеса

Стек:

Python • AI • Telegram API
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

# ----------- ЗАКАЗ БОТА -----------

@dp.callback_query(lambda c: c.data == "order")
async def order(callback: types.CallbackQuery):

    text = """
📩 *Заказать бота*

Напишите разработчику:

@Aleks_ai_de
"""

    await callback.message.edit_text(
        text,
        parse_mode="Markdown",
        reply_markup=back_button()
    )

# ----------- НАЗАД -----------

@dp.callback_query(lambda c: c.data == "back")
async def back(callback: types.CallbackQuery):

    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=main_menu
    )

# ----------- ЗАПУСК -----------

async def main():
    print("Bot started")
    await dp.start_polling(bot)

asyncio.run(main())
