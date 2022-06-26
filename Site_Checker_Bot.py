import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot("TOKEN")

language = ""
big_category = ""


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Welcome to site parser!")

    choose_language(message)


@bot.message_handler(commands=['lan', 'language'])
def choose_language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lat_lan = types.KeyboardButton("Latvian (LV)")
    rus_lan = types.KeyboardButton("Russian (RU)")

    markup.add(rus_lan, lat_lan)

    bot.send_message(message.chat.id, "Choose language (LV or RU)?", reply_markup=markup)


@bot.message_handler(commands=['category'])
def big_category_choose(message):
    print(language)
    if language == "LV":
        print("LV")
    elif language == "RU":
        print("RU")
    else:
        print("Difrent")
        bot.send_message(message.chat.id, "You didn't have chosen language")
        choose_language(message)


@bot.message_handler(content_types=['text'])
def latvian_names(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    c1 = types.KeyboardButton("Darbs un bizness")
    c2 = types.KeyboardButton("Transports")
    c3 = types.KeyboardButton("Nekustamie īpašumi")
    c4 = types.KeyboardButton("Celtniecība")
    c5 = types.KeyboardButton("Elektrotehnika")
    c6 = types.KeyboardButton("Drēbes, apavi")
    c7 = types.KeyboardButton("Mājai")
    c8 = types.KeyboardButton("Ražošana")
    c9 = types.KeyboardButton("Bērniem")
    c10 = types.KeyboardButton("Dzīvnieki")
    c11 = types.KeyboardButton("Lauksaimniecība")
    c12 = types.KeyboardButton("Atpūta, hobiji")
    print(message)
    markup.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12)
    bot.send_message(message.chat.id, "Choose category:", reply_markup=markup)
    if message.text in ["Darbs un bizness", "Transports", "Nekustamie īpašumi", "Celtniecība", "Elektrotehnika", "Drēbes, apavi", "Mājai", "Ražošana", "Bērniem", "Dzīvnieki", "Lauksaimniecība", "Atpūta, hobiji"]:
        print(message.text)
        bot.send_message(message.chat.id, "Big category are selected(if you want to change = /category ) " + message.text, reply_markup=ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Latvian (LV)" or message.text == "Russian (RU)":
            global language
            language = str(message.text)[-3:-1]
            bot.send_message(message.chat.id, "Ok, language will be " + message.text.lower(), reply_markup=ReplyKeyboardRemove())
            big_category_choose(message)



bot.infinity_polling()
