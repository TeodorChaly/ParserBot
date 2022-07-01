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
num = 0


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
    if language == "LV":
        latvian_list = ["Darbs un bizness", "Transports", "Nekustamie īpašumi", "Celtniecība", "Elektrotehnika",
                        "Drēbes, apavi", "Mājai", "Ražošana", "Bērniem", "Dzīvnieki", "Lauksaimniecība",
                        "Atpūta, hobiji"]
        big_category_name(message, latvian_list)
    elif language == "RU":
        russian_list = ["Работа и бизнес", "Транспорт", "Недвижимость", "Строительство", "Электротехника",
                        "Одежда, обувь",
                        "Для дома", "Производство", "Для детей", "Животные", "Сельское хозяйство", "Отдых, увлечения"]
        big_category_name(message, russian_list)
    else:
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


@bot.message_handler(commands=['filter', "filtering"])
def filter_menu(message):
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
                                          "(Example: '1) TEXT : TEXT_TWO')"
                                          "\nIf you want min and max (write 'min'-'max')")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        b1 = types.KeyboardButton("Filter one")
        b2 = types.KeyboardButton("Filter two")
        b3 = types.KeyboardButton("Filter tree")
        b4 = types.KeyboardButton("Without filter")
        markup.add(b1, b2, b3, b4)
        bot.send_message(message.chat.id, "Now, please enter big category, where are yours element:"
                                          "\nIf you want change language enter /lan", reply_markup=markup)

    print(language, big_category, medium_category, small_category, extra_category)


def filter_check(message):
    global filter_element_one, filter_element_two, filter_element_three
    if "one" in message.text:
        return 1
    elif "two" in message.text:
        return 2
    elif "tree" in message.text:
        return 3
    else:
        return 4


def filter_element(message, number):
    global filter_element_one, filter_element_two, filter_element_three
    element_one = message.text.partition(':')[0].strip()
    element_two = message.text.partition(':')[2].strip()
    if "-" in element_two:
        minimum = element_two.partition('-')[0].strip()
        maximum = element_two.partition('-')[2].strip()
        if number == 1:
            filter_element_one[element_one] = minimum, maximum
        elif number == 2:
            filter_element_two[element_one] = minimum, maximum
        elif number == 3:
            filter_element_three[element_one] = minimum, maximum
    else:
        if number == 1:
            filter_element_one[element_one] = element_two
        elif number == 2:
            filter_element_two[element_one] = element_two
        elif number == 3:
            filter_element_three[element_one] = element_two
        else:
            print("404")


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
        choose_category_1(message)
    filter_menu(message)


def choose_category_1(message):
    bot.send_message(message.chat.id, "Pelease, enter all cotegory to element, using slash /"
                                      " (example Vieglie auto/Audi):")


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        global language, big_category, num
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
                             "Currently category: " + message.text, reply_markup=ReplyKeyboardRemove())
            choose_category_1(message)
        if "/" in message.text and language != "" and big_category != "":
            path = message.text
            contruating_path(message, path)
        if ":" in message.text and num != 0:
            filter_element(message, num)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            b1 = types.KeyboardButton("Filter one")
            b2 = types.KeyboardButton("Filter two")
            b3 = types.KeyboardButton("Filter tree")
            b4 = types.KeyboardButton("Done")
            markup.add(b1, b2, b3, b4)
            bot.send_message(message.chat.id, "Dededed", reply_markup=markup)
            print(filter_element_one, filter_element_two, filter_element_three)
        if message.text in ["Filter one", "Filter two", "Filter tree", "Without filter", "Done"] and language != "" and big_category != "":
            if message.text == "Done" or message.text == "Without filter":
                bot.send_message(message.chat.id, "Ok", reply_markup=ReplyKeyboardRemove())
                print(filter_element_one, filter_element_two, filter_element_three)
            else:
                bot.send_message(message.chat.id, "Now write filter (Example: TEXT:TEXT_TWO): ", reply_markup=ReplyKeyboardRemove())
                num = filter_check(message)


bot.infinity_polling()
