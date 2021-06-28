import random

import telebot
from datetime import datetime
import time
from random import randint
from init import *
import importlib

def welcome(user, location, bot):
    hour = datetime.now().hour

    if 7 <= hour <= 23:
        bot.send_message(user['chat_id'],
                         '🐕 Добро пожаловать в дом охотника!\n\n'
                         'Здесь можно:\n'
                         '* /waterball - взять капитошку;\n'
                         '* /look - найти монетку;\n'
                         '* /take_ball - взять мяч, если он здесь;\n'
                         '* /give_ball - положить мяч его на место.')
    if 0 <= hour <= 3:
        bot.send_message(user['chat_id'],
                         '🐕 Вы входите в дом охотника!\nСейчас в доме охотника собрание и тут собрались все Орги. Все очень удивились вашему приходу, и Рост проводил вас домой.')

        location = change_location_by_id(user, "home")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)
    if 3 < hour < 7:
        bot.send_message(user['chat_id'],
                         '🐕 Вы пытаетесь зайти в дом охотника, но он закрыт!\nВ задумчивости вы остаетесь на улице.')

        location = change_location_by_id(user, "street")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)

def event(users, location, bot):
    hour = datetime.now().hour
    if 10 < hour < 14 or 14 < hour < 19:
        for user in users:
            x = random.randint(0, 101)
            if x <= 80:
                if 'medical_outlet' in user['inventory']:
                    bot.send_message(user['chat_id'],
                                     "Заходит Николай, но у вас есть разрешение от Лены сидеть дома. Николай отстал от Вас.")
                else:
                    bot.send_message(user['chat_id'],
                                     "Вы не на парах! Вас поймал Николай! Вы наказаны и отправляетесь на пару...")

                    if 'punished' not in user['states']:
                        user['states'].append('punished')

                    location = change_location_by_id(user, "school")
                    try:
                        location_module = importlib.import_module(location['file'])
                        location_module.welcome(user, location, bot)
                    except Exception as e:
                        print(e)
    for user in users:
        if randint(1, 10) == 1:
            bot.send_message(user['chat_id'], '🥪 Света угостила вас бутербродом с колбасой.')
            user['eat_points'] += 40
        if randint(1, 10) == 1:
            bot.send_message(user['chat_id'], '💧 Жамшид незаметно облил вас водой. Вы намокли.')
            if "wet" not in user['states']:
                user['states'].append('wet')




def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/waterball" in msg.text:
        if user['inventory'].count("waterball") > 2:
            bot.send_message(user['chat_id'], '💧 У вас уже 3 капитошки, больше не унести.')
        else:
            user['inventory'].append("waterball")
            for neighbor in neighbors:
                bot.send_message(neighbor['chat_id'], "{} взял капитошку!".format(user['name']))

    elif "/look" in msg.text:
        x = randint(0, 101)
        if x <= 30:
            bot.send_message(user["chat_id"], "Вы нашли монетку!")
            user['inventory'].append("coin")
        if x > 30:
            bot.send_message(user["chat_id"], "👀 Поиски не увенчались успехом...")
    elif "/give_ball" in msg.text:
        if "ball" in user['inventory']:
            location['inventory'].append("ball")
            user['inventory'].remove("ball")

            for neighbor in neighbors:
                bot.send_message(neighbor["chat_id"], "{} вернул мяч...".format(user['name']))
        else:
            bot.send_message(user["chat_id"], "👀 У вас нет мяча...")
    elif "/take_ball" in msg.text:
        if "ball" in location['inventory']:
            user['inventory'].append("ball")
            location['inventory'].remove("ball")

            for neighbor in neighbors:
                bot.send_message(neighbor['chat_id'], "{} забрал мяч!".format(user['name']))
        else:
            owner = users[0]
            for guser in users:
                if "ball" in guser['inventory']:
                    owner = guser
                    break
            bot.send_message(user['chat_id'], "👀  Мяч уже забрал {}.".format(owner['name']))
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))
