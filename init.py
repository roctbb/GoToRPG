import telebot
import config
import json

bot = telebot.TeleBot(token=config.TOKEN)

try:
    with open('users.json', 'r') as file:
        users = json.load(file)
except:
    users = []

try:
    with open('locations.json', 'r') as file:
        locations = json.load(file)
except:
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

def find_user_by_name(name):
    for user in users:
        if user['name'] == name:
            return user
    return None


def check_params(user):
    if "inventory" not in user:
        user['inventory'] = ["waterball"]
    if "states" not in user:
        user['states'] = []


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
        descrition += '- {}: {}\n'.format(location['id'], location['name'])

    return descrition

def save_name(user, name):
    user["name"] = name
    user["location"] = "street"
    bot.send_message(user["chat_id"], "Рад познакомиться с тобой, {}! Чтобы перейти в локацию, напиши /goto ЛОКАЦИЯ.\n\n{}".format(name, location_list()))


def change_location_by_id(user, location_id):
    location = find_location(location_id)

    if not location:
        bot.send_message(user["chat_id"], "Такого места нет.")
    else:
        neighbors = find_users_by_location(location_id)

        description = "С вами в одной локации: "
        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} теперь в {}!".format(user['name'], location["name"]))
            description += neighbor['name'] + " "

        user['location'] = location_id
        bot.send_message(user["chat_id"], "Теперь вы находитесь в {}.".format(location['name']))
        bot.send_message(user["chat_id"], description)



