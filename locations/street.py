from datetime import datetime
import random

from init import *

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

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
                bot.send_message(user['chat_id'], "👀 Вы деморализованы и не можете бросить капитошку...")
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
                    bot.send_message(neighbor['chat_id'], "{} кидает капитошку в {} и попадает!".format(user['name'], target['name']))
                bot.send_message(target['chat_id'], "Вы намокли!")

                if "wet" not in target['states']:
                    target['states'].append('wet')
            else:
                for neighbor in neighbors:
                    bot.send_message(neighbor['chat_id'], "{} кидает капитошку в {}, но промахивается!".format(user['name'], target['name']))

            user['inventory'].remove('waterball')

        except Exception as e:
            print(e)
            bot.send_message(user['chat_id'], "👀 Укажите цель!")
        return

    if "/sleep" in msg.text:
        if 10 < hour < 15:
            bot.send_message(user["chat_id"], "Вы загораете.")
        elif 0 < hour < 7:
            bot.send_message(user["chat_id"], "Вы спите на улице.")
            user['sleep_points'] += 20

            if ""
        else:
            bot.send_message(user["chat_id"], "Вы прилегли отдохнуть.")
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))
        return

    for neighbor in neighbors:
        if neighbor["chat_id"] != user["chat_id"]:
            bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))



def event(users, location, bot):
    if random.randint(1,10) == 1:
        for user in users:
            bot.send_message(user['chat_id'], 'Пошел дождь')
            if 'wet' not in user['states']:
                user['states'].append('wet')

    hour = datetime.now().hour

    # пояление Николая
    if 0 < hour < 7:
        if random.randint(1, 3) == 1:
            for user in users:
                bot.send_sticker(user['chat_id'], stickers['nikolay'])
                bot.send_message(user['chat_id'], 'На улице появился Николай. Вы отвлекаете его от работы! Вы наказаны!')
                user['states'].append('punishment')


