import importlib
from datetime import datetime
import random
import pytz

from init import *

def welcome(user, location, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    if 0 < hour < 7:
        bot.send_message(user['chat_id'], "🌚 Вы вышли прогуляться на улицу. Сейчас ночь и находиться вне домика нельзя, остерегайтесь Николая! Если вас поймают, то вас накажут и вы расстроитесь.\n\n"
                                          "* /waterball ПОЛЬЗОВАТЕЛЬ - бросить капитошку;\n"
                                          "* /sleep - спать.")
    else:
        bot.send_message(user['chat_id'],
                         "🌞 Вы вышли прогуляться на улицу.\n\n"
                         "* /waterball ПОЛЬЗОВАТЕЛЬ - бросить капитошку;\n"
                         "* /sleep - спать.")

def message(msg, user, location, neighbors, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    if "/waterball" in msg.text:
        try:
            cmd, name = msg.text.split()
            target = find_user_by_name(name)

            if not target or target['location'] != user['location']:
                bot.send_message(user['chat_id'], "👀 Нет такого пользователя!")
                return

            if user['eat_points'] < 20:
                bot.send_message(user['chat_id'], "👀 Вы слишком голодны для этого!")
                return

            if "waterball" not in user['inventory']:
                bot.send_message(user['chat_id'], "👀 У вас нет капитошки!")
                return

            border = 4
            if "sick" in user['states']:
                border += 2
            if "punished" in user['states']:
                border += 2
            if "toxic" in user['states']:
                border += 2
            if "ponos" in user['states']:
                border += 2

            if random.randint(1, 10) > border:
                for neighbor in neighbors:
                    bot.send_message(neighbor['chat_id'], "🎯 {} кидает капитошку в {} и попадает!".format(user['name'], target['name']))
                bot.send_message(target['chat_id'], "💦 В вас попали капитошкой и вы намокли!")

                if "wet" not in target['states']:
                    target['states'].append('wet')
            else:
                for neighbor in neighbors:
                    bot.send_message(neighbor['chat_id'], "👀 {} кидает капитошку в {}, но промахивается!".format(user['name'], target['name']))

            user['inventory'].remove('waterball')

        except Exception as e:
            print(e)
            bot.send_message(user['chat_id'], "👀 Укажите цель!")
        return

    if "/sleep" in msg.text:
        if 10 < hour < 15:
            bot.send_message(user["chat_id"], "🥵 Сейчас слишком жарко уснуть не выходит. Вы лежите на солнце и получаете солнчный удар.")
            if "sick" not in user['states']:
                user['states'].append('sick')
        elif 0 < hour < 7:
            if "sick" not in user['states']:
                bot.send_message(user["chat_id"], "💤 Вы спите на улице.")
                user['sleep_points'] += 20

                if random.randint(1,3) == 1:
                    bot.send_message(user["chat_id"], "🤒 Тут холодно, вы простудились.")
                    user['states'].append('sick')
            else:
                bot.send_message(user["chat_id"], "🤒 Вы простужены и не можете спать на улице.")
        else:
            bot.send_message(user["chat_id"], "💤 Вы прилегли отдохнуть.")
            user['sleep_points'] += 5

    for neighbor in neighbors:
        if neighbor["chat_id"] != user["chat_id"]:
            bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))

def event(users, location, bot):
    # дождь
    if random.randint(1,10) == 1:
        for user in users:
            bot.send_message(user['chat_id'], '☔️ Пошел дождь.')
            if 'wet' not in user['states']:
                user['states'].append('wet')
                bot.send_message(user['chat_id'], '💦 Вы намокли. Чтобы просохнуть, примите душ.')

    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    # пояление Николая
    if 0 < hour < 7:
        if random.randint(1, 3) == 1:
            for user in users:
                bot.send_sticker(user['chat_id'], stickers['nikolay'])
                bot.send_message(user['chat_id'], '👺 В темноте появляется Николай, кажется он расстроен встречей с вами. Вы нарушаете правила и отвлекаете его от работы.\n😔 Вас отругали и вы расстроились. Вы возвращаетесь домой.')

                location = change_location_by_id(user, "home")
                try:
                    location_module = importlib.import_module(location['file'])
                    location_module.welcome(user, location, bot)
                except Exception as e:
                    print(e)
                if "punished" not in user['states']:
                    user['states'].append('punishment')


