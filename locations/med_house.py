from datetime import datetime

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/skiplesson" in msg.text:
        if 10 < hour < 11.30:
            bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувсвие и остались у Лены")
        elif 12 < hour < 14:
            bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувствие и остались у Лены.")
        elif 15 < hour < 16.30:
            bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувствие и остались у Лены.")
        elif 17 < hour < 19:
            bot.send_message(user["chat_id"], "Вы пожаловались на плохое самочувствие и остались у Лены.")
        else:
            bot.send_message(user["chat_id"], "Пар нету, а значит и прогуливать нечего)")
    if "/nightwalk" in msg.text:
        if 0 < hour < 4:
            bot.send_message(user["chat_id"], """Вы пожаловались на плохое самочувствие
             и по обратной дороге навернули пару лишних кругов""")
        else:
            bot.send_message(user["chat_id"], "Сейчас можно гулять и без этого)")
    if "/heal" in msg.text:
        bot.send_message(user["chat_id"], "Лена подлечила вас")
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))



def event(location, users, bot):
    pass