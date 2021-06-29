from datetime import datetime
import random
import importlib
from init import *
import pytz

def welcome (user, location,bot):
    bot.send_message(user["chat_id"], """🏥 Добро пожаловать в медпункт!\n\n 
    🙃 напишите /medical_outlet, чтобы получить медотвод; \n
    😏 напишите /skiplessons, чтобы прогулять пару; \n
    ✨ напишите /nightwalk, чтобы пойти гулять ночью; \n
    💚 напишите /heal, чтобы подлечиться""")

def message(msg, user, location, neighbors, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour



    # TODO медотвод - medical_outlet
    if "/medical_outlet" in msg.text:
        y = random.randint(0, 101)
        if y <= 12:
            if 'medical_outlet' not in user['inventory']:
                user['inventory'].append('medical_outlet')
            bot.send_message(user["chat_id"], "😏 Вам дали медотвод и теперь вы свободны от пар.")
        if y > 12:
            bot.send_message(user["chat_id"], "😔 Вам не дали медотвод.")

    if "/skiplesson" in msg.text:
        if 10 < hour <= 11:
            z = random.randint(1,10)
            if z <= 6:
                bot.send_message(user["chat_id"], """🙁 Вы пожаловались на плохое самочувствие, но Лена отправила 
                вас на пары.""")
            else:
                bot.send_message(user["chat_id"], "👀 Вы пожаловались на плохое самочувсвие и остались у Лены.")
        elif 12 < hour < 14:
            z = random.randint(1, 10)
            if z <= 6:
                bot.send_message(user["chat_id"], """🙁 Вы пожаловались на плохое самочувствие, но Лена отправила 
                        вас на пары.""")
            else:
                bot.send_message(user["chat_id"], "👀 Вы пожаловались на плохое самочувсвие и остались у Лены.")
        elif 15 < hour < 16:
            z = random.randint(1, 10)
            if z <= 6:
                bot.send_message(user["chat_id"], """🙁 Вы пожаловались на плохое самочувствие, но Лена отправила 
                        вас на пары.""")
            else:
                bot.send_message(user["chat_id"], "👀 Вы пожаловались на плохое самочувсвие и остались у Лены.")
        elif 17 < hour < 19:
            z = random.randint(1, 10)
            if z <= 6:
                bot.send_message(user["chat_id"], """🙁 Вы пожаловались на плохое самочувствие, но Лена отправила 
                        вас на пары.""")
            else:
                bot.send_message(user["chat_id"], "👀 Вы пожаловались на плохое самочувсвие и остались у Лены.")
        else:
            bot.send_message(user["chat_id"], "Пар нету, а значит и прогуливать нечего)")
    elif "/nightwalk" in msg.text:
        if 0 < hour < 4:
            bot.send_message(user["chat_id"], """🌿 Вы пожаловались на плохое самочувствие
             и по обратной дороге навернули пару лишних кругов""")
        else:
            bot.send_message(user["chat_id"], "Сейчас можно гулять и без этого)")
    elif "/heal" in msg.text:
        if "sick" in user['states']:
            bot.send_message(user["chat_id"], "💚 Лена подлечила вас, теперь вы здоровы.")
            user["states"].remove("sick")
        elif "ponos" in user["states"]:
            user["states"].remove('ponos')
            user["eat_points"] = 0
            bot.send_message(user["chat_id"], "🍕 Вам сделали колоноскопию. Вы здоровы, но очень голодны.")
        else:
            bot.send_message(user["chat_id"], "😜 У вас ипохондрия)")


    elif "/coin" in msg.text:
        x = random.randint(0, 31)
        if x <= 10 and 'coin' not in user['inventory']:
            bot.send_message(user["chat_id"], "💲 Вы нашли монетку)")
            user['inventory'].append("coin")
        if x > 10:
            bot.send_message(user["chat_id"], "😔 Поиски не увенчались успехом.")
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))

def event(users, location, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour
    minute = datetime.now(pytz.timezone('Europe/Moscow')).minute

    if 10 < hour < 14 or 14 < hour < 19:
        for user in users:
            x = random.randint(0, 101)
            if x <= 80:
                if 'medical_outlet' in user['inventory']:
                    bot.send_message(user['chat_id'],
                                     "У вас есть разрешение от Лены сидеть дома. Николай отстал от Вас.")
                else:
                    bot.send_message(user['chat_id'], "Вы не на парах! Вас поймал Николай! Вы наказаны и отправляетесь на пару...")

                    if 'punished' not in user['states']:
                        user['states'].append('punished')

                    location = change_location_by_id(user, "school")
                    try:
                        location_module = importlib.import_module(location['file'])
                        location_module.welcome(user, location, bot)
                    except Exception as e:
                        print(e)