from datetime import datetime
import time
from random import randint

def welcome(user, location, bot):
    if user['chat_id'] in location:
        bot.send_message(user['chat_id'],"Вы зашли на локацию Дом")

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/look" in msg.text:
        x = randint(0,101)
        if x <= 30:
            bot.send_message(user["chat_id"], "Вы нашли монетку!")
            user['inventory'].append("coin")
        if x > 30:
            bot.send_message(user["chat_id"], "Поиски не увенчались успехом...")
    if "/sleep" in msg.text:
        if 10 < hour < 15:
            bot.send_message(user["chat_id"], "Вы спите в доме днём. Повышение выносливости снижено на 30%." )
            user['sleep_points'] += 100
        elif 0 < hour < 7:
            bot.send_message(user["chat_id"], "Вы спите.")
            user['sleep_points'] = 192
        else:
            bot.send_message(user["chat_id"], "Вы прилегли отдохнуть. Повышение выносливости снижено на 30%.")
            user['sleep_points'] += 20
        return
    if "/shower" in msg.text:
        bot.send_message(user["chat_id"], "Вы пошли в душ")
        time.sleep(10)
        bot.send_message(user['chat_id'], "Вы стали чише! Теперь на Вас 99 клопов вместо 100")

        if "wet" in user['states']:
            user['states'].remove("wet")

        if "dirty" in user['states']:
            user['states'].remove("dirty")

        return

def event(users, location, bot):
    hour = datetime.now().hour
    minute = datetime.now().minute

    if 10 < hour < 11.30 or 12 < hour < 14 or 15 < hour < 16.30 or 17 < hour < 19:
        for user in users:
            x = randint(0,101)
            if x <= 80:
                if 'medical_outlet' in user['inventory']:
                    bot.send_message(user['chat_id'], "У вас есть разрешение от Лены сидеть дома. Николай отстал от Вас.")
                else:
                    bot.send_message(user['chat_id'], "Вы не на парах! Вас поймал Николай! Вы наказаны!")
                    user['states'].append('punished')