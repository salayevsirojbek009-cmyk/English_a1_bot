import telebot
from telebot import types

BOT_TOKEN = "8855246500:AAG-bJUZR5VvVpBpOe0D1d7PnOO_4PgxWuo"
bot = telebot.TeleBot(BOT_TOKEN)

# KATEGORIYALAR
categories = {
    "mevalar": {
        "title": "🍎 MEVALAR",
        "words": [
            {"en": "APPLE", "uz": "olma", "example": "I like apple."},
            {"en": "BANANA", "uz": "banan", "example": "The banana is yellow."},
            {"en": "ORANGE", "uz": "apelsin", "example": "I eat orange."},
        ]
    },
    "speaking": {
        "title": "💬 SPEAKING",
        "words": [
            {"en": "HELLO", "uz": "salom", "example": "Hello, my name is Ali."},
            {"en": "GOODBYE", "uz": "xayr", "example": "Goodbye, see you!"},
            {"en": "HOW ARE YOU?", "uz": "siz qanday?", "example": "How are you today?"},
        ]
    },
    "uylar": {
        "title": "🏠 UYLAR",
        "words": [
            {"en": "HOUSE", "uz": "uy", "example": "This is my house."},
            {"en": "ROOM", "uz": "xona", "example": "My room is big."},
            {"en": "DOOR", "uz": "eshik", "example": "The door is open."},
        ]
    },
}

def main_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📚 Bugungi So'z", callback_data="today"))
    markup.add(types.InlineKeyboardButton("❓ Quiz", callback_data="quiz"))
    markup.add(types.InlineKeyboardButton("👥 Guruh", callback_data="group"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    text = "📚 **MAVZULAR TANLANG:**\n\n"
    
    markup = types.InlineKeyboardMarkup()
    for cat_key, cat_data in categories.items():
        text += f"{cat_data['title']}\n"
        markup.add(types.InlineKeyboardButton(
            cat_data['title'], 
            callback_data=f"cat_{cat_key}"
        ))
    
    bot.send_message(message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("cat_"))
def show_category(call):
    cat_key = call.data.split("_")[1]
    cat = categories[cat_key]
    
    text = f"{cat['title']}\n\n"
    for i, w in enumerate(cat['words'], 1):
        text += f"{i}️⃣ **{w['en']}** ({w['uz']})\n💬 {w['example']}\n\n"
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("◀️ Orqaga", callback_data="back"))
    markup.add(types.InlineKeyboardButton("📚 Bugungi", callback_data="today"))
    markup.add(types.InlineKeyboardButton("👥 Guruh", callback_data="group"))
    
    bot.send_message(call.message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    text = "📚 **MAVZULAR TANLANG:**\n\n"
    
    markup = types.InlineKeyboardMarkup()
    for cat_key, cat_data in categories.items():
        text += f"{cat_data['title']}\n"
        markup.add(types.InlineKeyboardButton(
            cat_data['title'], 
            callback_data=f"cat_{cat_key}"
        ))
    
    bot.send_message(call.message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "today")
def today(call):
    cat = list(categories.values())[0]
    w = cat['words'][0]
    text = f"🔤 **{w['en']}** ({w['uz']})\n💬 {w['example']}"
    bot.send_message(call.message.chat.id, text, reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "quiz")
def quiz(call):
    text = "❓ **QUIZ**\n\nAPPLE nima degan ma'noni ko'z tuta?"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🍎 Olma", callback_data="correct"))
    markup.add(types.InlineKeyboardButton("❌ Kitob", callback_data="wrong"))
    markup.add(types.InlineKeyboardButton("❌ Mushuk", callback_data="wrong"))
    bot.send_message(call.message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "correct")
def correct(call):
    bot.send_message(call.message.chat.id, "✅ **TO'G'RI!** Zo'r! 🎉", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "wrong")
def wrong(call):
    bot.send_message(call.message.chat.id, "❌ **NOTO'G'RI!** Apple = Olma 🍎", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: call.data == "group")
def group(call):
    text = "👥 **BIZNING GURUH:**\n\nt.me/english_a1_group\n\nQo'shil va o'zingni tanitish!"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🏠 Asosiy", callback_data="main"))
    bot.send_message(call.message.chat.id, text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "main")
def back_to_main(call):
    text = "📚 **MAVZULAR TANLANG:**\n\n"
    
    markup = types.InlineKeyboardMarkup()
    for cat_key, cat_data in categories.items():
        text += f"{cat_data['title']}\n"
        markup.add(types.InlineKeyboardButton(
            cat_data['title'], 
            callback_data=f"cat_{cat_key}"
        ))
    
    bot.send_message(call.message.chat.id, text, reply_markup=markup)

bot.infinity_polling()
