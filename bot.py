import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

# --- Настройка логирования для Render ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# --- Получение токена ---
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ ОШИБКА: Токен не найден! Добавьте BOT_TOKEN в переменные окружения Render")
    sys.exit(1)

# --- Инициализация ---
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- Клавиатура ---
def get_main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 Цены"), KeyboardButton(text="📁 Примеры")],
            [KeyboardButton(text="👤 Обо мне"), KeyboardButton(text="📞 Контакты")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню..."
    )

# --- Хендлеры ---

@dp.message(Command("start"))
async def start_command(message: Message):
    logger.info(f"Команда /start от пользователя {message.from_user.id}")
    try:
        await message.answer(
            f"👋 Привет, {message.from_user.first_name}!\n\n"
            f"Я Александр, делаю ботов от 2500₽.\n"
            f"Выбирай раздел 👇",
            reply_markup=get_main_keyboard()
        )
    except Exception as e:
        logger.error(f"Ошибка в start_command: {e}")

@dp.message(Text("💰 Цены"))
async def prices(message: Message):
    try:
        await message.answer(
            "💰 **Прайс-лист:**\n"
            "• Простой бот — 2500₽\n"
            "• Бот с каталогом — 3500₽\n"
            "• Бот с админкой — 5000₽\n\n"
            "📞 Для заказа пишите в контакты.",
            parse_mode="Markdown"
        )
    except Exception as e:
        logger.error(f"Ошибка в prices: {e}")

@dp.message(Text("📁 Примеры"))
async def examples(message: Message):
    try:
        await message.answer(
            "📁 **Мои работы:**\n"
            "• Бот для записи клиентов\n"
            "• Интернет-магазин в Telegram\n"
            "• Бот для сбора отзывов"
        )
    except Exception as e:
        logger.error(f"Ошибка в examples: {e}")

@dp.message(Text("👤 Обо мне"))
async def about(message: Message):
    try:
        await message.answer(
            "👤 **Обо мне:**\n"
            "Александр, 15 лет.\n"
            "Разрабатываю Telegram-ботов с использованием современных технологий и AI."
        )
    except Exception as e:
        logger.error(f"Ошибка в about: {e}")

@dp.message(Text("📞 Контакты"))
async def contacts(message: Message):
    try:
        await message.answer(
            "📞 **Связь со мной:**\n"
            "Telegram: @AlexDev_bot_ai\n"
            "Пишите в любое время!"
        )
    except Exception as e:
        logger.error(f"Ошибка в contacts: {e}")

# --- Фолбэк хендлер (на любые другие сообщения) ---
@dp.message()
async def unknown_message(message: Message):
    if not message.text:
        return
    try:
        await message.answer(
            "Я вас не понял. Пожалуйста, используйте кнопки меню 👇",
            reply_markup=get_main_keyboard()
        )
    except Exception as e:
        logger.error(f"Ошибка в unknown_message: {e}")

# --- Запуск ---
async def main():
    logger.info("✅ Бот запускается...")
    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен пользователем")
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)
    finally:
        await bot.session_close()
        logger.info("✅ Сессия бота закрыта")

if __name__ == "__main__":
    asyncio.run(main())
