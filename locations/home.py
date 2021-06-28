import random
from datetime import datetime
import time
from random import randint
from init import *


def welcome(user, location, bot):
    bot.send_message(user['chat_id'], "Вы зашли на локацию Дом")
    bot.send_message(user['chat_id'], "/waterball - бросить капитошку "
                                      "/sleep - Сон "
                                      "/shower - принять душ "
                                      "/look - поискать монетки")


def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/look" in msg.text:
        x = randint(0, 101)
        if x <= 30 and "coin" not in user['inventory']:
            bot.send_message(user["chat_id"], "Вы нашли монетку!")
            user['inventory'].append("coin")
        if x > 30:
            bot.send_message(user["chat_id"], "Поиски не увенчались успехом...")
    if "/sleep" in msg.text:
        if 10 < hour < 15:
            bot.send_message(user["chat_id"], "Вы спите в доме днём. Повышение выносливости снижено на 30%.")
            user['sleep_points'] += 100
        elif 0 < hour < 7:
            bot.send_message(user["chat_id"], "Вы спите.")
            user['sleep_points'] = 192
        else:
            bot.send_message(user["chat_id"], "Вы прилегли отдохнуть. Повышение выносливости снижено на 30%.")
            user['sleep_points'] += 20
        return
    if "/shower" in msg.text:
        bot.send_message(user["chat_id"], "Вы пошли в душ.")
        time.sleep(10)
        bot.send_message(user['chat_id'], "Вы стали чише! Теперь на Вас 99 клопов вместо 100")

        if "wet" in user['states']:
            user['states'].remove("wet")

        if "dirty" in user['states']:
            user['states'].remove("dirty")

    if "/waterball" in msg.text:
        try:
            cmd, name = msg.text.split()
            target = find_user_by_name(name)

            if not target:
                bot.send_message(user['chat_id'], "👀 Нет такого пользователя!")
                return
            if user['eat_points'] < 20:
                bot.send_message(user['chat_id'], "👀 Вы слишком голодны для этого!")
                return

            if "punished" in user['states']:
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
                    bot.send_message(neighbor['chat_id'],
                                     "🎯 {} кидает капитошку в {} и попадает!".format(user['name'], target['name']))
                bot.send_message(target['chat_id'], "💦 В вас попали капитошкой и вы намокли!")

                if "wet" not in target['states']:
                    target['states'].append('wet')
            else:
                for neighbor in neighbors:
                    bot.send_message(neighbor['chat_id'],
                                     "👀 {} кидает капитошку в {}, но промахивается!".format(user['name'],
                                                                                             target['name']))
            x = randint(1, 101)
            if x <= 90:
                bot.send_message(user['chat_id'], "Вы разлили воду! Николай пришёл и наказал вас!")
                if 'punished' not in user['states']:
                    user['states'].append('punished')
            else:
                bot.send_message(user['chat_id'], "Вы разлили воду, но этого никто не заметил!")

            user['inventory'].remove('waterball')

        except Exception as e:
            print(e)
            bot.send_message(user['chat_id'], "👀 Укажите цель!")
        return

    return


def event(users, location, bot):
    hour = datetime.now().hour
    minute = datetime.now().minute

    if 10 < hour < 11.30 or 12 < hour < 14 or 15 < hour < 16.30 or 17 < hour < 19:
        for user in users:
            x = randint(0, 101)
            if x <= 80:
                if 'medical_outlet' in user['inventory']:
                    bot.send_message(user['chat_id'],
                                     "У вас есть разрешение от Лены сидеть дома. Николай отстал от Вас.")
                else:
                    bot.send_message(user['chat_id'], "Вы не на парах! Вас поймал Николай! Вы наказаны!")
                    user['states'].append('punished')
