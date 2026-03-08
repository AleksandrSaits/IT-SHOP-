import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8755271111:AAEKcs3D3iqBzO7w1yp6N-JUl0f_1kCZFsE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ----------- ГЛАВНОЕ МЕНЮ -----------

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🤖 AI чат", callback_data="ai")],
        [InlineKeyboardButton(text="🛒 Магазин", callback_data="shop")],
        [InlineKeyboardButton(text="📅 Запись", callback_data="booking")],
        [InlineKeyboardButton(text="💼 Портфолио", callback_data="portfolio")],
        [InlineKeyboardButton(text="📩 Заказать бота", callback_data="order")]
    ]
)

def back_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
        ]
    )

# ----------- START -----------

@dp.message(Command("start"))
async def start(message: types.Message):

    text = """
🤖 *AlexDev Demo Bot*

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
