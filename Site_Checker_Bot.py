import telebot
from telebot import types
bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to site parser!")
    bot.register_next_step_handler(message, choose_language)


def choose_language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lat_lan = types.KeyboardButton("Latvian (LV)")
    rus_lan = types.KeyboardButton("Russian (RU)")


    markup.add(rus_lan, lat_lan)

    bot.reply_to(message.chat.id, "Choose language (LV or RU)?")


bot.polling()
