from datetime import datetime
import random
def welcome (user, location,bot):
    bot.send_message(user["chat_id"], """🏥Добро пожаловать в медпункт! 
    🙃напишите /medical_outlet, чтобы получить медотвод
    😏напишите /skiplessons, чтобы прогулять пару
    ✨напишите /nightwalk, чтобы пойти гулять ночью
    💚напишите /heal, чтобы подлечиться""")

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour
    minute = datetime.now().minute

    # TODO медотвод - medical_outlet
    if "/medical_outlet" in msg.text:
        y = random.randint(0, 101)
        if y <= 12:
            bot.send_message(user["chat_id"], "Вам дали медотвод и теперь вы свободны от пар.😏")
        if y > 12:
            bot.send_message(user["chat_id"], "Вам не дали медотвод.😔")

    if "/skiplesson" in msg.text:
        if 10 < hour < 11:
            z = random.randint(1,10)
            if z <= 6:
                bot.send_message(user["chat_id"], """Вы пожаловались на плохое самочувствие, но Лена отправила 
                вас на пары.🙁""")
            else:
                bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувсвие и остались у Лены.👀")
        elif 12 < hour < 14:
            z = random.randint(1, 10)
            if z <= 6:
                bot.send_message(user["chat_id"], """Вы пожаловались на плохое самочувствие, но Лена отправила 
                        вас на пары.🙁""")
            else:
                bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувсвие и остались у Лены.👀")
        elif 15 < hour < 16:
            z = random.randint(1, 10)
            if z <= 6:
                bot.send_message(user["chat_id"], """Вы пожаловались на плохое самочувствие, но Лена отправила 
                        вас на пары.🙁""")
            else:
                bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувсвие и остались у Лены.👀")
        elif 17 < hour < 19:
            z = random.randint(1, 10)
            if z <= 6:
                bot.send_message(user["chat_id"], """Вы пожаловались на плохое самочувствие, но Лена отправила 
                        вас на пары.🙁""")
            else:
                bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувсвие и остались у Лены.👀")
        else:
            bot.send_message(user["chat_id"], "Пар нету, а значит и прогуливать нечего)")
    elif "/nightwalk" in msg.text:
        if 0 < hour < 4:
            bot.send_message(user["chat_id"], """Вы пожаловались на плохое самочувствие
             и по обратной дороге навернули пару лишних кругов🌿""")
        else:
            bot.send_message(user["chat_id"], "Сейчас можно гулять и без этого)")
    elif "/heal" in msg.text:
        bot.send_message(user["chat_id"], "Лена подлечила вас💚")
        if "sick" in user['states']:
            user["states"].remove("sick")
        elif "ponos" in user["states"]:
            user["states"].remove('ponos')
            user["eat_points"]=0
        else:
            bot.send_message(user["chat_id"], "Вы здоровы💚")
    elif "/coin" in msg.text:
        x = random.randint(0, 31)
        if x <= 10:
            bot.send_message(user["chat_id"], "Вы нашли монетку)💲")
            user['inventory'].append("coin")
        if x > 10:
            bot.send_message(user["chat_id"], "Поиски не увенчались успехом.😔")
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))



def event(location, users, bot):
    pass