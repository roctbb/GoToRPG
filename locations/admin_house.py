from datetime import datetime
import random

from init import *

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour
    bot.send_message(user['chat_id'], 'Чтобы купить мороженое, напишите /icecream')
    if "/icecream" in msg.text:
        if 8 < hour < 23:
            if 'coin' in user['inventory']:
                bot.send_message(user["chat_id"], 'Вы купили одно мороженое')
                user['inventory'].remove('coin')
                user['inventory'].append('icecream')
            else:
                bot.send_message(user["chat_id"], 'У вас нет монет, монет')
        else:
            bot.send_message(user["chat_id"], 'Администриция закрыта')

def event(users, location, bot):
    for user in users:
        bot.send_message(user['chat_id'], 'Чтобы купить мороженое, напишите /icecream')
