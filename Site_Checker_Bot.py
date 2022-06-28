import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove

bot = telebot.TeleBot("TOKEN")

language = ""
big_category = ""
medium_category = ""
small_category = ""
extra_category = ""
filter_element_one = {}
filter_element_two = {}
filter_element_three = {}
list_of_category1 = []


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
        latvian_list = ["Darbs un bizness", "Transports", "Nekustamie īpašumi", "Celtniecība", "Elektrotehnika",
                        "Drēbes, apavi", "Mājai", "Ražošana", "Bērniem", "Dzīvnieki", "Lauksaimniecība",
                        "Atpūta, hobiji"]
        big_category_name(message, latvian_list)
        print("LV+")
    elif language == "RU":
        russian_list = ["Работа и бизнес", "Транспорт", "Недвижимость", "Строительство", "Электротехника",
                        "Одежда, обувь",
                        "Для дома", "Производство", "Для детей", "Животные", "Сельское хозяйство", "Отдых, увлечения"]
        big_category_name(message, russian_list)
        print("RU+")
    else:
        print("Difrent")
        bot.send_message(message.chat.id, "You didn't have chosen language")
        choose_language(message)


@bot.message_handler(commands=['test'])
def big_category_name(message, list_of_category):
    global list_of_category1
    list_of_category1 = list_of_category
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    c1 = types.KeyboardButton(list_of_category[0])
    c2 = types.KeyboardButton(list_of_category[1])
    c3 = types.KeyboardButton(list_of_category[2])
    c4 = types.KeyboardButton(list_of_category[3])
    c5 = types.KeyboardButton(list_of_category[4])
    c6 = types.KeyboardButton(list_of_category[5])
    c7 = types.KeyboardButton(list_of_category[6])
    c8 = types.KeyboardButton(list_of_category[7])
    c9 = types.KeyboardButton(list_of_category[8])
    c10 = types.KeyboardButton(list_of_category[9])
    c11 = types.KeyboardButton(list_of_category[10])
    c12 = types.KeyboardButton(list_of_category[1])
    markup.add(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12)
    bot.send_message(message.chat.id, "Now, please enter big category, where are yours element:"
                                      "\nIf you want change language enter /lan", reply_markup=markup)
    for i in list_of_category:
        print(i)
    print(message.text)


@bot.message_handler(commands=['filter', "filtering"])
def filter_menu(message):
    global filter_element_one, filter_element_two, filter_element_three
    if language == "":
        bot.send_message(message.chat.id, "You didn't have chosen language")
        choose_language(message)
    elif big_category == "":
        bot.send_message(message.chat.id, "You didn't have chosen category")
        big_category_choose(message)
    if language != "" and big_category != "":
        bot.send_message(message.chat.id, "You can choose maximum three filtering elements "
                                          "(or you may without filtering)"
                                          "\nWrite text and filter you want "
                                          "(Example: 'Meklējamais vārds vai frāze: Liela')"
                                          "\nIf you want min and max (write 'min'-'max')")
    print(language, big_category, medium_category, small_category, extra_category)


def contruating_path(message, path):
    path_list = path.split("/")
    global medium_category, small_category, extra_category
    if len(path_list) == 1:
        medium_category = path_list[0].strip().capitalize()
    elif len(path_list) == 2:
        medium_category = path_list[0].strip().capitalize()
        small_category = path_list[1].strip().capitalize()
    elif len(path_list) == 3:
        medium_category = path_list[0].strip().capitalize()
        small_category = path_list[1].strip().capitalize()
        extra_category = path_list[2].strip().capitalize()
    else:
        print(len(path_list))
        choose_category_1(message)
    filter_menu(message)


def choose_category_1(message):
    bot.send_message(message.chat.id, "Pelease, enter all cotegory to element, using slash /"
                                      " (example Vieglie auto/Audi):")


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        global language, big_category
        print(message.text)
        if message.text == "Latvian (LV)" or message.text == "Russian (RU)":
            language = str(message.text)[-3:-1]
            bot.send_message(message.chat.id, "Ok, language will be " + message.text.lower() + ".",
                             reply_markup=ReplyKeyboardRemove())
            big_category_choose(message)
        if message.text in list_of_category1:
            big_category = message.text
            bot.send_message(message.chat.id,
                             "Big category are selected(if you want to change = /category )\n"
                             "Currently category: " + message.text,   reply_markup=ReplyKeyboardRemove())
            choose_category_1(message)
        if "/" in message.text and language != "" and big_category != "":
            print(1111)
            path = message.text
            contruating_path(message, path)
        if ":" in message.text:
            print(2222)


bot.infinity_polling()
