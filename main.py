import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import telebot

# Render uchun port serveri
class HealthCheck(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheck)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()

# Telegram Bot kodi
TOKEN = "8855246500:AAEgDH7x_kTVBjhar0TPIF9N52Xo0V8YW20"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, "Xush kelibsiz! Bu English A1 boti.\n\n/help - Yordam")

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.reply_to(message, "Bot buyruqlari:\n/start - Ishga tushirish")

bot.infinity_polling()
