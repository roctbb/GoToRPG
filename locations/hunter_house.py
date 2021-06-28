from datetime import datetime
import time
from random import randint

users[hunterhouse].append(0)
def welcome(user, location, bot):
    if users[hunterhouse]==0:
        bot.send_message(user,'Добро пожаловать в дом охотника.Здесь ты можешь получить капитошку(/waterball),найти монетку(/look),взять мяч(/take_ball),положить мяч(/give_ball)')

def event(users, location, bot):
    for user in users:
        bot.send_sticker(user['chat_id'], stickers['nikolay'])
        bot.send_message(user['chat_id'], 'В доме охотника появился Николай. Вы отвлекаете его от работы! Вы наказаны!')
        user['states'].append('punishment')

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/waterball" in msg.text:
        if user['inventory'].count("waterball") > 2:
            pass
        else:
            user['inventory'].append("waterball")
            for neighbor in neighbors:
                bot.send_message(neighbor['chat_id'], "{} поднял капитошку".format(user['name']))


    elif "/look" in msg.text:
        x = randint(0, 101)
        if x <= 30:
            bot.send_message(user["chat_id"], "Вы нашли монетку!")
            user['inventory'].append("coin")
        if x > 30:
            bot.send_message(user["chat_id"], "Поиски не увенчались успехом...")
    elif "/give_ball" in msg.text:
        if "ball" in user['inventory']:
            location['inventory'].append("ball")
            user['inventory'].remove("ball")

            for neighbor in neighbors:
                bot.send_message(neighbor["chat_id"], "{} вернул мяч...".format(user['name']))
        else:
            bot.send_message(user["chat_id"], "У вас нет мяча...")
    elif "/take_ball" in msg.text:
        # TODO
        user['inventory'].append("ball")
        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} поднял мяч".format(user['name']))
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))
