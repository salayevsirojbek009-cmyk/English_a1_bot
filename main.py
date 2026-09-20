import telebot

TOKEN = "8855246500:AAEgDH7x_kTVBjhar0TPIF9N52Xo0V8YW20"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, "Xush kelibsiz! Bu English A1 boti.\n\n/help - Yordam")

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.reply_to(message, "Bot buyruqlari:\n/start - Ishga tushirish")

bot.infinity_polling()
