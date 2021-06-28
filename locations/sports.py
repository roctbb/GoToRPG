import random
import time
from init import *
from datetime import datetime

def welcome(user, location, bot):
    hour = datetime.now().hour
    bot.send_message(user['chat_id'],'Здесь вы можете поиграть в волейбол 🏐')
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
            bot.send_message(user['chat_id'], "Вы заработали очко!".format(user['name']))
            user['volley_points'] += 1

        user['sleep_points'] -= 5