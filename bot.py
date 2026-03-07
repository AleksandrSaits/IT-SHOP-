import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from flask import Flask
import threading

# Твой токен
TOKEN = "8762519077:AAF719ES-Tq2t42CJN5iusSwR7kLc8zR87k"

# Создаем Flask приложение (чтобы Render думал, что это веб-сервер)
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Товары
products = [
    {"id": 1, "name": "Товар 1", "price": 100, "desc": "Описание товара 1"},
    {"id": 2, "name": "Товар 2", "price": 200, "desc": "Описание товара 2"},
    {"id": 3, "name": "Товар 3", "price": 300, "desc": "Описание товара 3"},
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📦 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("🛒 Корзина", callback_data="cart")],
        [InlineKeyboardButton("📞 Контакты", callback_data="contacts")]
    ]
    
    await update.message.reply_text(
        "👋 Добро пожаловать в магазин!\nВыберите действие:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    keyboard = []
    for product in products:
        keyboard.append([
            InlineKeyboardButton(
                f"{product['name']} - {product['price']}₽", 
                callback_data=f"product_{product['id']}"
            )
        ])
    keyboard.append([InlineKeyboardButton("◀️ Назад", callback_data="back")])
    
    await query.edit_message_text(
        "📋 Наш каталог:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    product_id = int(query.data.split('_')[1])
    product = products[product_id - 1]
    
    keyboard = [
        [InlineKeyboardButton("✅ Добавить в корзину", callback_data=f"add_{product_id}")],
        [InlineKeyboardButton("◀️ Назад", callback_data="catalog")]
    ]
    
    await query.edit_message_text(
        f"📦 {product['name']}\n💰 Цена: {product['price']}₽\n\n{product['desc']}",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def add_to_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    product_id = int(query.data.split('_')[1])
    product = products[product_id - 1]
    
    if 'cart' not in context.user_data:
        context.user_data['cart'] = []
    context.user_data['cart'].append(product)
    
    keyboard = [
        [InlineKeyboardButton("📋 Продолжить", callback_data="catalog")],
        [InlineKeyboardButton("🛒 Корзина", callback_data="cart")]
    ]
    
    await query.edit_message_text(
        f"✅ {product['name']} добавлен!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    cart = context.user_data.get('cart', [])
    
    if not cart:
        text = "🛒 Корзина пуста"
    else:
        text = "🛒 Ваша корзина:\n\n"
        total = 0
        for item in cart:
            text += f"• {item['name']} - {item['price']}₽\n"
            total += item['price']
        text += f"\n💰 Итого: {total}₽"
    
    keyboard = [
        [InlineKeyboardButton("✅ Оформить", callback_data="checkout")],
        [InlineKeyboardButton("🗑 Очистить", callback_data="clear")],
        [InlineKeyboardButton("◀️ Назад", callback_data="back")]
    ]
    
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

async def checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    cart = context.user_data.get('cart', [])
    if not cart:
        await query.edit_message_text("Корзина пуста!")
        return
    
    await query.edit_message_text(
        "✅ Заказ оформлен!\nСкоро с вами свяжутся!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏠 Главное меню", callback_data="back")]
        ])
    )
    context.user_data['cart'] = []

async def clear_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['cart'] = []
    await query.edit_message_text("🗑 Корзина очищена")

async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    await query.edit_message_text(
        "📞 Наши контакты:\n\nТелефон: +7 (999) 123-45-67\nEmail: shop@example.com",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("◀️ Назад", callback_data="back")]
        ])
    )

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(query, context)

def run_bot():
    """Запуск бота в отдельном потоке"""
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(catalog, pattern="^catalog$"))
    application.add_handler(CallbackQueryHandler(show_product, pattern="^product_"))
    application.add_handler(CallbackQueryHandler(add_to_cart, pattern="^add_"))
    application.add_handler(CallbackQueryHandler(show_cart, pattern="^cart$"))
    application.add_handler(CallbackQueryHandler(checkout, pattern="^checkout$"))
    application.add_handler(CallbackQueryHandler(clear_cart, pattern="^clear$"))
    application.add_handler(CallbackQueryHandler(contacts, pattern="^contacts$"))
    application.add_handler(CallbackQueryHandler(back, pattern="^back$"))
    
    print("Бот запущен!")
    application.run_polling()

if __name__ == "__main__":
    # Запускаем бота в фоне
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    # Запускаем Flask (для Render)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)