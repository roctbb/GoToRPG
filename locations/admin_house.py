from datetime import datetime
import random
import importlib
from init import *


def welcome(user, location, bot):
    hour = datetime.now().hour
    if hour > 20 or hour < 8:
        bot.send_message(user["chat_id"], "Администрация закрыта, приходите завтра. Вы перемещаетесь на улицу.")

        location = change_location_by_id(user, "street")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)
    elif "dirty" in user['states']:
        bot.send_message(user["chat_id"], "Вы испачкались, в таком виде вас не пускают. Вы перемещаетесь на улицу.")

        location = change_location_by_id(user, "street")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)
    else:
        bot.send_message(user['chat_id'], "👩‍💼 Вы в здании администрации.\n\n"
                                          "* /icecream - купить мороженое.")


def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/icecream" in msg.text:
        if 'coin' in user['inventory']:
            bot.send_message(user["chat_id"], '🍦 В инвентарь добавлено одно мороженое.')
            user['inventory'].remove('coin')
            user['inventory'].append('icecream')
        else:
            bot.send_message(user["chat_id"], '👀 У вас нет монет, монет...')
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))


def event(users, location, bot):
    hour = datetime.now().hour

    if hour > 20 or hour < 8:
        for user in users:
            bot.send_message(user['chat_id'], "🕜 Администрация закрывается, вас попросили выйти на улицу.")

            location = change_location_by_id(user, "street")
            try:
                location_module = importlib.import_module(location['file'])
                location_module.welcome(user, location, bot)
            except Exception as e:
                print(e)
