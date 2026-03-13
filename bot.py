import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv

# --- Настройка логирования ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# --- Загрузка конфигурации ---
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ Токен не найден! Проверь .env файл")
    sys.exit(1)

# --- Инициализация бота ---
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- Клавиатуры ---
def get_main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="💰 Цены"), KeyboardButton(text="📁 Примеры")],
            [KeyboardButton(text="👤 Обо мне"), KeyboardButton(text="📞 Контакты")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите пункт меню..."
    )

# --- Хендлеры (Обработчики) ---

@dp.message(Command("start"))
async def start_command(message: Message):
    logger.info(f"Команда /start от пользователя {message.from_user.id}")
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        f"Я Александр, делаю ботов от 2500₽.\n"
        f"Выбирай раздел 👇",
        reply_markup=get_main_keyboard()
    )

@dp.message(Text("💰 Цены"))
async def prices(message: Message):
    await message.answer(
        "💰 **Прайс-лист:**\n"
        "• Простой бот — 2500₽\n"
        "• Бот с каталогом — 3500₽\n"
        "• Бот с админкой — 5000₽\n\n"
        "📞 Для заказа пишите в контакты.",
        parse_mode="Markdown"
    )

@dp.message(Text("📁 Примеры"))
async def examples(message: Message):
    await message.answer(
        "📁 **Мои работы:**\n"
        "• Бот для записи клиентов\n"
        "• Интернет-магазин в Telegram\n"
        "• Бот для сбора отзывов"
    )

@dp.message(Text("👤 Обо мне"))
async def about(message: Message):
    await message.answer(
        "👤 **Обо мне:**\n"
        "Александр, 15 лет.\n"
        "Разрабатываю Telegram-ботов с использованием современных технологий и AI."
    )

@dp.message(Text("📞 Контакты"))
async def contacts(message: Message):
    await message.answer(
        "📞 **Связь со мной:**\n"
        "Telegram: @AlexDev_bot_ai\n"
        "Пишите в любое время!"
    )

# --- Фолбэк хендлер (на любые другие сообщения) ---
@dp.message()
async def unknown_message(message: Message):
    # Игнорируем, если это не текст (например, фото или стикер)
    if not message.text:
        return
    
    await message.answer(
        "Я вас не понял. Пожалуйста, используйте кнопки меню 👇",
        reply_markup=get_main_keyboard()
    )

# --- Запуск ---
async def main():
    logger.info("✅ Бот запускается...")
    try:
        # allowed_updates=dp.resolve_used_update_types() пропускает только нужные обновления
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except KeyboardInterrupt:
        logger.info("🛑 Бот остановлен пользователем")
    finally:
        await bot.session.close()
        logger.info("✅ Сессия бота закрыта")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}", exc_info=True)
        
