from datetime import datetime
import random
hour = datetime.now().hour



def welcome (user,location,bot):
    hour = datetime.now().hour
    if 10 <= hour <= 11:
        welcome_text = """Это коростель здесь вы можете покушать.
/breakfast-позавтракать.
Напишите /bread чтобы  купить хлеб.
Аккуратнее с перееданием!"""
    if 11 <= hour <= 13:
        welcome_text = "Сейчас нельзя покушать,можете купить хлеб, напишите /bread чтобы купить хлеб."
    if 13 <= hour <= 14:
        welcome_text = """Это коростель здесь вы можете покушать.
    /lunch-пообедать.
    Напишите /bread чтобы  купить хлеб.
    Аккуратнее с перееданием!"""


    if 14 <= hour <= 19:
        welcome_text = "Сейчас нельзя покушать, можете купить хлеб, напишите /bread чтобы купить хлеб."
    if 19 <= hour <= 20:
        welcome_text = """Это коростель здесь вы можете покушать.
    /dinner-поожинать.
    Напишите /bread чтобы  купить хлеб.
    Аккуратнее с перееданием!"""
    if 20 <= hour <= 10:
        welcome_text = "Сейчас нельзя покушать, можете купить хлеб, напишите /bread чтобы купить хлеб."
    bot.send_message(user["chat_id"], welcome_text)

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/breakfast" in msg.text:
        if 10 <= hour <= 11:
          bulochka=random.randint(1,2)
          bot.send_message(user["chat_id"], "Вы завтракаете...")
          user["eat_points"] += 80
          if bulochka == 1:
              bot.send_message(user["chat_id"], "вы получили булочку чтобы сьесть ее напишите /eat_bulochka")
              user['inventory'].append('bulochka')

          if user["eat_points"] > 100:
              bot.send_message(user["chat_id"], "У вас понос")
              if "ponos" not in user['states']:
                  user['states'].append("ponos")
        else:
          bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/lunch" in msg.text:
        if 13 <= hour <=14:
            bot.send_message(user["chat_id"], "Вы обедаете ")
            user["eat_points"] += 80
            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "У вас понос")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/dinner" in msg.text:
            if 19 <= hour <= 20:
                bot.send_message(user["chat_id"], "Вы ужинаете ")
                user["eat_points"] += 80
                if user["eat_points"] > 100:
                    bot.send_message(user["chat_id"], "У вас понос")
                    if "ponos" not in user['states']:
                        user['states'].append("ponos")
            else:
                bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/bread" in msg.text:
        if 'coin' in user['inventory']:
            bot.send_message(user["chat_id"], 'Вы купили один хлеб тобы сьесть напишите /eat_bread')
            user['inventory'].remove('coin')
            user['inventory'].append('bread')
            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "У вас понос")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], "У вас нет coin")

    if "/eat_bread" in msg.text:
        if 'bread' in user ['inventory']:
            bot.send_message(user["chat_id"], 'Вы сьели хлеб')
            user['inventory'].remove('bread')
        else:
            bot.send_message(user["chat_id"], 'У вас нет хлеба')
    if "/eat_bulochka" in msg.text:
        if 'bulochka' in user ['inventory']:
            bot.send_message(user["chat_id"], 'Вы сьели булочку')
            user['inventory'].remove('bulochka')
        else:
            bot.send_message(user["chat_id"], 'У вас нет булочки')




    else:
        for neighbor in neighbors:
          if neighbor["chat_id"] != user["chat_id"]:
            bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))



