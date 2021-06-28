from datetime import datetime
hour = datetime.now().hour



def welcome (user,location,bot):
    hour = datetime.now().hour
    if 10 < hour < 11:
        welcome_text = """Это коростель здесь вы можете покушать.
        /breakfast-позавтракать
    Eли ваша шкала еды больше 100 то у вас понос.
    """
    if 11 < hour < 13:
        welcome_text = "Сейчас нельзя покушать"
    if 13 < hour < 14:
        welcome_text = """Это коростель здесь вы можете покушать.
            /lunch-пообедать
        Eли ваша шкала еды больше 100 то у вас понос.
        """
    if 14 < hour > 19:
        welcome_text = "Сейчас нельзя покушать"
    if 19 < hour < 20:
        welcome_text = """Это коростель здесь вы можете покушать.
              /dinner-поожинать
          Eли ваша шкала еды больше 100 то у вас понос.
          """
    bot.send_message(user["chat_id"], welcome_text)

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/breakfast" in msg.text:
        if 10 < hour < 11:
          bot.send_message(user["chat_id"], "Вы завтракаете...")
          user["eat_points"] += 80
          if user["eat_points"] > 100:
              bot.send_message(user["chat_id"], "У вас понос")
              if "ponos" not in user['states']:
                  user['states'].append("ponos")
        else:
          bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/lunch" in msg.text:
        if 13 < hour < 14:
            bot.send_message(user["chat_id"], "Вы обедаете ")
            user["eat_points"] += 80
            if user["eat_points"] > 100:
                bot.send_message(user["chat_id"], "У вас понос")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/dinner" in msg.text:
            if 19 < hour < 20:
                bot.send_message(user["chat_id"], "Вы ужинаете ")
                user["eat_points"] += 80
                if user["eat_points"] > 100:
                    bot.send_message(user["chat_id"], "У вас понос")
                    if "ponos" not in user['states']:
                        user['states'].append("ponos")
            else:
                bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    else:
        for neighbor in neighbors:
          if neighbor["chat_id"] != user["chat_id"]:
            bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))


