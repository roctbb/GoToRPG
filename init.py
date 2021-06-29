import telebot
import config
import json
import pytz

bot = telebot.TeleBot(token=config.TOKEN)

default_locations = [
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
        "id": "med_house",
        "file": "locations.med_house",
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
        "name": "Дом охотника",
        "inventory": ["ball", "stick", "stick"]
    },
    {
        "id": "admin_house",
        "file": "locations.admin_house",
        "name": "Администрация"
    },
    {
        "id": "forest",
        "file": "locations.forest",
        "name": "Лес"
    },
    {
        "id": "fire",
        "file": "locations.fire",
        "name": "Костер"
    },
    {
        "id": "school",
        "file": "locations.school",
        "name": "Учебка",
        "inventory": ["guitar", "stick"]
    },
    {
        "id": "sports",
        "file": "locations.sports",
        "name": "Волейбольное поле"
    },
]

try:
    with open('users.json', 'r') as file:
        users = json.load(file)
except:
    users = []

try:
    with open('locations.json', 'r') as file:
        locations = json.load(file)
except:
    locations = default_locations

stickers = {
    "nikolay": "CAACAgIAAxkBAAIVGmDYmcLuaWX73R-rLVun5hLgOFKlAAK7AAMTKxwE_BmnnTxRwBwgBA"
}

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
        if user.get('name') == name:
            return user
    return None


def check_params(user):
    if "inventory" not in user:
        user['inventory'] = ["waterball"]
    if "states" not in user:
        user['states'] = []
    if "eat_points" not in user:
        user["eat_points"] = 100
    if "sleep_points" not in user:
        user["sleep_points"] = 192
    if "code_lines" not in user:
        user["code_lines"] = 0
    if "volleyball_points" not in user:
        user["volleyball_points"] = 0


def init(chat_id):
    user = {
        "chat_id": chat_id
    }

    bot.send_message(chat_id, "🙋‍♀️ Добро пожаловать в игру! Напиши свое имя...")

    users.append(user)
    return user


def leaderboard():

    actual_users = list(filter(lambda x: 'code_lines' in x and 'volleyball_points' in x, users))

    top_coders = list(sorted(actual_users, key=lambda x: -x['code_lines']))[:5]
    top_sports = list(sorted(actual_users, key=lambda x: -x['volleyball_points']))[:5]

    return "🏆 Топ программистов:\n\n {}\n\n🏆 Топ спортсменов:\n\n {}".format(
        '\n'.join(map(lambda x: x['name'], top_coders)), '\n'.join(map(lambda x: x['name'], top_sports)))


def location_list():
    descrition = '🗺 Локации:\n'

    for location in locations:
        descrition += '- {}: {}\n'.format(location['id'], location['name'])

    return descrition


def save_name(user, name):
    user["name"] = name
    user["location"] = "street"
    bot.send_message(user["chat_id"], "🤝 Рад познакомиться с тобой, {}! .\n\n{}".format(name, location_list()))
    help(user)


def help(user):
    bot.send_message(user["chat_id"], "Помощь:\n\n"
                                      "* /goto ЛОКАЦИЯ - перейти в локацию;\n"
                                      "* /info - статус персонажа;\n"
                                      "* /leaderboard - топ игроков;\n"
                                      "* /locations - список локаций.")


def change_location_by_id(user, location_id):
    location = find_location(location_id)

    if not location:
        bot.send_message(user["chat_id"], "👀 Такого места нет.")
    else:
        neighbors = find_users_by_location(location_id)

        description = "👫 С вами в одной локации: "
        for neighbor in neighbors:
            if neighbor['chat_id'] != user['chat_id']:
                bot.send_message(neighbor['chat_id'], "{} теперь в {}!".format(user['name'], location["name"]))
                description += neighbor['name'] + " "
        if len(neighbors) < 2:
            description += "только вы."

        user['location'] = location_id
        bot.send_message(user["chat_id"], "ℹ️ Теперь вы находитесь в {}.".format(location['name']))
        bot.send_message(user["chat_id"], description)

    return location


def save():
    with open('users.json', 'w') as file:
        json.dump(users, file)
    with open('locations.json', 'w') as file:
        json.dump(locations, file)
