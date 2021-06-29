from datetime import datetime
import random
from init import *
import importlib
import pytz

def welcome(user, location, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    if "dirty" in user['states']:
        bot.send_message(user["chat_id"], "Вы испачкались, в таком виде вас не пускают. Вы перемещаетесь на улицу.")

        location = change_location_by_id(user, "street")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)
    else:
        bot.send_message(user['chat_id'], "🏫 Вы в учебке. Находясь здесь вы постепенно учитесь писать код.\n\n"
                                          "* /give_guitar - положить гитару;\n"
                                          "* /take_guitar - взять гитару.\n")


def message(msg, user, location, neighbors, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour
    minute = datetime.now(pytz.timezone('Europe/Moscow')).minute
    # поднятие / оставление гитары
    if "/give_guitar" in msg.text:
        if "guitar" in user['inventory']:
            location['inventory'].append("guitar")
            user['inventory'].remove("guitar")

            for neighbor in neighbors:
                bot.send_message(neighbor["chat_id"], "{} вернул гитару".format(user['name']))
        else:
            bot.send_message(user["chat_id"], "У вас нет гитары.")
    elif "/take_guitar" in msg.text:
        if "guitar" not in location['inventory']:
            bot.send_message(user["chat_id"], "Гитару уже кто-то взял.")
        else:
            location['inventory'].remove("guitar")
            user['inventory'].append("guitar")
            for neighbor in neighbors:
                bot.send_message(neighbor['chat_id'], "{} поднял гитару".format(user['name']))


def event(users, location, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    # пояление Николая
    if 0 < hour < 8:
        if random.randint(1, 3) == 1:
            for user in users:
                bot.send_message(user['chat_id'],
                                 '👺 В учебку заходит Николай, кажется он расстроен встречей с вами. Вы нарушаете правила и отвлекаете его от работы.\n😔 Вас отругали и вы расстроились. Вы возвращаетесь домой.')

                location = change_location_by_id(user, "home")
                try:
                    location_module = importlib.import_module(location['file'])
                    location_module.welcome(user, location, bot)
                except Exception as e:
                    print(e)
                if "punished" not in user['states']:
                    user['states'].append('punishment')

    else:
        for user in users:
            border = 4

            if "sick" in user['states']:
                border += 2
            if "punished" in user['states']:
                border += 2
            if "ponos" in user['states']:
                border += 2
            if "toxic" in user['states']:
                border -= 4
            if "coffee" in user['inventory']:
                border -= 4

            if random.randint(1, 10) > border:
                bot.send_message(user['chat_id'], "Вы написали строчку кода.")
                user['code_lines'] += 1
