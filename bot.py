import telebot
import config
import importlib

bot = telebot.TeleBot(token=config.TOKEN)

users = []
locations = [
    {
        "id": "street",
        "file": "locations.street",
        "name": "Улица"
    },
    {
        "id": "home",
        "file": "locations.home",
        "name": "Домик"
    },
    {
        "id": "med",
        "file": "locations.med",
        "name": "Медпункт"
    },
    {
        "id": "korostel",
        "file": "locations.korostel",
        "name": "Коростель"
    },
    {
        "id": "hunter_house",
        "file": "locations.hunter_house",
        "name": "Дом охотника"
    }
]

def find_users_by_location(location_id):
    users_in_location = []

    for user in users:
        if 'location' in user and user['location'] == location_id:
            users_in_location.append(user)

    return users_in_location

def find_location(location_id):
    for location in locations:
        if location['id'] == location_id:
            return location
    return None

def find_user(chat_id):
    for user in users:
        if user['chat_id'] == chat_id:
            return user
    return None

def init(chat_id):
    user = {
        "chat_id": chat_id
    }

    bot.send_message(chat_id, "Добро пожаловать в игру! Напиши свое имя...")

    users.append(user)
    return user

def location_list():
    descrition = 'Локации:\n'

    for location in locations:
        descrition += '- {}: {}'.format(location['id'], location['name'])

def save_name(user, name):
    user["name"] = name
    user["location"] = "street"
    bot.send_message(user["chat_id"], """Рад познакомиться с тобой, {}! Чтобы перейти в локацию, напиши /goto ЛОКАЦИЯ.
    
    """.format(location_list(), name))

def change_location_by_id(user, location_id):
    location = find_location(location_id)

    if not location:
        bot.send_message(user["chat_id"], "Такого места нет.")
    else:
        neighbors = find_users_by_location(location_id)

        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} теперь в {}!".format(user['name'], location["name"]))

        user['location'] = location_id
        bot.send_message(user["chat_id"], "Теперь вы находись в {}.".format(location['name']))


@bot.message_handler(content_types=['text'])
def process_message(message):
    user = find_user(message.chat.id)

    if not user:
        init(message.chat.id)
        return

    if "name" not in user:
        save_name(user, message.text)
        return

    if "/goto" in message.text:
        try:
            cmd, location_id = message.text.split(' ')
            change_location_by_id(user, location_id)
            return
        except Exception as e:
            print(e)
            bot.send_message(user["chat_id"], "Укажите название локации.")
            return

    location = find_location(user['location'])
    users = find_users_by_location(user['location'])

    try:
        location_module = importlib.import_module(location['file'])
        location_module.message(message, user, location, users, bot)
    except Exception as e:
        print(e)

bot.polling()
#Aboba