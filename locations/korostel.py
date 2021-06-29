from datetime import datetime
import random
from init import *
import importlib
import pytz


def welcome(user, location, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    if "dirty" in user['states']:
        bot.send_message(user["chat_id"], "Вы испачкались, в таком виде вас не пускают. Вы перемещаетесь на улицу.")

        location = change_location_by_id(user, "street")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)
        return

    if hour == 10:
        welcome_text = "🍱 Добро пожаловать в Коростель! Сейчас завтрак и вы можете позавтракать. Аккуратнее с перееданием!\n\n" \
                       "* /breakfast - позавтракать;\n" \
                       "* /bread - купить хлеб."
    elif 11 <= hour <= 13 or 14 < hour <= 18:
        welcome_text = "🍱 Добро пожаловать в Коростель!\n\n" \
                       "* /bread - купить хлеб."
    elif hour == 14:
        welcome_text = "🍱 Добро пожаловать в Коростель! Сейчас обед. Аккуратнее с перееданием!\n\n" \
                       "* /lunch - пообедать;\n" \
                       "* /bread - купить хлеб."
    elif hour == 19:
        welcome_text = "🍱 Добро пожаловать в Коростель! Сейчас ужин. Аккуратнее с перееданием!\n\n" \
                       "* /dinner - пообедать;\n" \
                       "* /bread - купить хлеб."
    else:
        bot.send_message(user["chat_id"], "🕜 Ресторан закрыт. Вы перемещаетесь на улицу.")

        location = change_location_by_id(user, "street")
        try:
            location_module = importlib.import_module(location['file'])
            location_module.welcome(user, location, bot)
        except Exception as e:
            print(e)
        return
    bot.send_message(user["chat_id"], welcome_text)


def message(msg, user, location, neighbors, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    if "/breakfast" in msg.text:
        if hour == 10:
            bulochka = random.randint(1, 2)
            bot.send_message(user["chat_id"], "Вы завтракаете...")
            user["eat_points"] += 50
            bot.send_message(user["chat_id"], "Ваше уровень питание: {}".format(user['eat_points']))

            if bulochka == 1:
                bot.send_message(user["chat_id"], "вы получили булочку чтобы сьесть ее напишите /eat_bulochka")
                user['inventory'].append('bulochka')

            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "Вы переели, теперь у вас понос.")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], "Вы сейчас не можете позавтракать.")

    elif "/lunch" in msg.text:
        if hour == 14:
            bot.send_message(user["chat_id"], "Вы обедаете.")
            user["eat_points"] += 50
            bot.send_message(user["chat_id"], "Ваше уровень сытости: {}".format(user['eat_points']))

            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "Вы переели, теперь у вас понос.")

                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], "Вы сейчас не можете пообедать.")
    elif "/dinner" in msg.text:
        if hour == 19:
            bot.send_message(user["chat_id"], "Вы ужинаете...")
            user["eat_points"] += 50
            bot.send_message(user["chat_id"], "Ваше уровень сытости: {}".format(user['eat_points']))

            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "Вы переели, теперь у вас понос.")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], "Вы сейчас не можете поужинать.")

    elif "/bread" in msg.text:
        if 'coin' in user['inventory']:
            bot.send_message(user["chat_id"], 'Вы купили один хлеб чтобы сьесть напишите /eat_bread')
            user['inventory'].remove('coin')
            user['inventory'].append('bread')

        else:
            bot.send_message(user["chat_id"], "У вас нет денег.")

    elif "/eat_bread" in msg.text:
        if 'bread' in user['inventory']:
            bot.send_message(user["chat_id"], 'Вы сьели хлеб')
            user["eat_points"] += 15
            user['inventory'].remove('bread')
            bot.send_message(user["chat_id"], "Ваш уровень сытости: {}".format(user['eat_points']))

            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "Вы переели, теперь у вас понос.")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], 'У вас нет хлеба.')

    elif "/eat_bulochka" in msg.text:
        if 'bulochka' in user['inventory']:
            bot.send_message(user["chat_id"], 'Вы сьели булочку')
            user["eat_points"] += 15
            user['inventory'].remove('bulochka')
            bot.send_message(user["chat_id"], "Ваш уровень сытости: {}".format(user['eat_points']))
        else:
            bot.send_message(user["chat_id"], 'У вас нет булочки.')
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))

def event(users, location, bot):
    hour = datetime.now(pytz.timezone('Europe/Moscow')).hour

    if hour > 20:
        for user in users:
            bot.send_message(user['chat_id'], "🕜 Коростель закрывается, вас попросили выйти на улицу.")

            location = change_location_by_id(user, "street")
            try:
                location_module = importlib.import_module(location['file'])
                location_module.welcome(user, location, bot)
            except Exception as e:
                print(e)
