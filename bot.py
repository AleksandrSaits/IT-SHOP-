import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8755271111:AAEFdfPoJCGYJcRmykDCPGoCZ6pLbm_Fj5w"
ADMIN_ID = 8559107011

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ---------------- DATABASE ----------------

db = sqlite3.connect("bot.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
text TEXT
)
""")

db.commit()

def add_user(user_id):
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        db.commit()

# ---------------- MENU ----------------

main_menu = InlineKeyboardMarkup(
inline_keyboard=[
[InlineKeyboardButton(text="🤖 AI чат", callback_data="ai")],
[InlineKeyboardButton(text="🛒 Магазин", callback_data="shop")],
[InlineKeyboardButton(text="📅 Запись", callback_data="booking")],
[InlineKeyboardButton(text="💼 Портфолио", callback_data="portfolio")],
[InlineKeyboardButton(text="📩 Заказать бота", callback_data="order")]
]
)

# ---------------- START ----------------

@dp.message(Command("start"))
async def start(message: types.Message):

    add_user(message.from_user.id)

    text = """
🤖 *AlexDev Demo Bot*

Этот бот демонстрирует возможности Telegram ботов.

Выберите функцию ниже 👇
"""

    await message.answer(text, reply_markup=main_menu, parse_mode="Markdown")

# ---------------- AI CHAT ----------------

@dp.callback_query(lambda c: c.data == "ai")
async def ai_menu(call: types.CallbackQuery):

    text = """
🤖 *AI Демонстрация*

Напишите любой вопрос и бот ответит.

(В демо версии используется простой ответ)
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

@dp.message()
async def fake_ai(message: types.Message):

    if message.text.startswith("/"):
        return

    await message.answer(f"🤖 AI ответ:\n\nЯ получил ваш вопрос:\n*{message.text}*", parse_mode="Markdown")

# ---------------- SHOP ----------------

def shop_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📱 Телефоны", callback_data="phones")],
            [InlineKeyboardButton(text="💻 Ноутбуки", callback_data="laptops")],
            [InlineKeyboardButton(text="🎧 Аксессуары", callback_data="access")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
        ]
    )

@dp.callback_query(lambda c: c.data == "shop")
async def shop(call: types.CallbackQuery):

    text = """
🛒 *Демо магазин*

Выберите категорию товаров.
"""

    await call.message.edit_text(text, reply_markup=shop_keyboard(), parse_mode="Markdown")

@dp.callback_query(lambda c: c.data == "phones")
async def phones(call: types.CallbackQuery):

    text = """
📱 *iPhone 15*

Цена: 999$

Это демонстрация магазина Telegram бота.
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

@dp.callback_query(lambda c: c.data == "laptops")
async def laptops(call: types.CallbackQuery):

    text = """
💻 *MacBook Pro*

Цена: 1999$

Демонстрационный товар.
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

@dp.callback_query(lambda c: c.data == "access")
async def access(call: types.CallbackQuery):

    text = """
🎧 *AirPods Pro*

Цена: 249$

Демонстрационный товар.
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

# ---------------- BOOKING ----------------

@dp.callback_query(lambda c: c.data == "booking")
async def booking(call: types.CallbackQuery):

    text = """
📅 *Демо записи*

Введите ваше имя для записи.
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

# ---------------- PORTFOLIO ----------------

@dp.callback_query(lambda c: c.data == "portfolio")
async def portfolio(call: types.CallbackQuery):

    text = """
💼 *Портфолио*

Я разрабатываю:

🤖 AI боты  
🛒 магазины  
📅 системы записи  
📊 автоматизацию бизнеса

Технологии:

Python • AI • Telegram API
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

# ---------------- ORDER ----------------

@dp.callback_query(lambda c: c.data == "order")
async def order(call: types.CallbackQuery):

    text = """
📩 *Заказать бота*

Напишите описание вашего проекта.

Я свяжусь с вами.
"""

    await call.message.edit_text(text, reply_markup=back_button(), parse_mode="Markdown")

# ---------------- BACK BUTTON ----------------

def back_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅ Главное меню", callback_data="back")]
        ]
    )

@dp.callback_query(lambda c: c.data == "back")
async def back(call: types.CallbackQuery):

    await call.message.edit_text("Главное меню:", reply_markup=main_menu)

# ---------------- ADMIN ----------------

@dp.message(Command("admin"))
async def admin(message: types.Message):

    if message.from_user.id != ADMIN_ID:
        return

    cursor.execute("SELECT COUNT(*) FROM users")
    users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM orders")
    orders = cursor.fetchone()[0]

    text = f"""
📊 Статистика

Пользователей: {users}
Заявок: {orders}
"""

    await message.answer(text)

# ---------------- RUN ----------------

async def main():
    print("Bot started")
    await dp.start_polling(bot)

asyncio.run(main())
