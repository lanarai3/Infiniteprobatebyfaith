from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)

app = Flask(__name__)

dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text("Hello, your probate bot is live!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running!", 200
