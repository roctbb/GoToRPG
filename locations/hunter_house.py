from datetime import datetime
import time
from random import randint


@bot.message_handler(commands=['Vzyat_kapitoshku'])
def huntho(message):
    if "/waterballup" in msg.text:
        user['inventory'].append(kapitoshka)
        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} поднял капитошку")

def event(users, location, bot):
    for user in users:
        bot.send_sticker(user['chat_id'], stickers['nikolay'])
        bot.send_message(user['chat_id'], 'На улице появился Николай. Вы отвлекаете его от работы! Вы наказаны!')
        user['states'].append('punishment')

coin = 0

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/look" in msg.text:
        x = randint(0,101)
        if x <= 30:
            bot.send_message(user["chat_id"], "Вы нашли монетку!")
            user['inventory']
        if x > 30:
            bot.send_message(user["chat_id"], "Поиски не увенчались успехом...")
    if "/talk" in msg.txt:
        bot.send_message(user['chat_id'],)

@bot.message_handler(commands=['ballup'])
def ball(message):
    if "/ballup" in msg.text:
        user['inventory'].append(ball)
        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} поднял мяч")