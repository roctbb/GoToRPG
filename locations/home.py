from datetime import datetime
import time
from random import randint
stamina = 0
clean = 0
wet = False
coin = 0

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
    pass
    # если ты в домике во время пар - может прийти Николай и дать punished