import random
import time
from init import *
from datetime import datetime
import importlib

def welcome(user, location, bot):
    hour = datetime.now().hour
    bot.send_message(user['chat_id'],'Здесь вы можете поиграть в волейбол 🏐. Но будте аккуратнее, физическая активность требует энергии.')
def message(msg, user, location, neighbors, bot):
    user['inventory'].append('ball')
    hour = datetime.now().hour
    if 'ball' in user['inventory']:
        if len(neighbors) >0:
            bot.send_message(user["chat_id"], 'Вы решили поиграть')
        else:
            bot.send_message(user["chat_id"], 'К сожалению, вам не с кем поиграть')
    else:
        bot.send_message(user["chat_id"], 'К сожалению, у вас нет мяча, поищите его на территории')



def event(users, location, bot):
    for user in users:
        if random.randint(1, 2) == 1:
            for player in users:
                if player['chat_id'] != user['chat_id']:
                    bot.send_message(player['chat_id'], "{} зарабатывает очко!".format(user['name']))
            bot.send_message(user['chat_id'], "Вы заработали очко!")
            user['volleyball_points'] += 1
        else:
            bot.send_message(user['chat_id'], "Вы подаете мяч, но промахиваетесь.")

        user['sleep_points'] -= 5

    # пояление Николая
    hour = datetime.now().hour
    if 0 < hour < 7:
        if random.randint(1, 3) == 1:
            for user in users:
                bot.send_sticker(user['chat_id'], stickers['nikolay'])
                bot.send_message(user['chat_id'],
                                 '👺 В темноте появляется Николай, кажется он расстроен встречей с вами. Вы нарушаете правила и отвлекаете его от работы.\n😔 Вас отругали и вы расстроились. Вы возвращаетесь домой.')

                location = change_location_by_id(user, "home")
                try:
                    location_module = importlib.import_module(location['file'])
                    location_module.welcome(user, location, bot)
                except Exception as e:
                    print(e)
                if "punished" not in user['states']:
                    user['states'].append('punishment')