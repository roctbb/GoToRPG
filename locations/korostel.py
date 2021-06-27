from datetime import datetime

def message(msg, user, location, neighbors, bot):

    hour = datetime.now().hour
    if "/breakfast" in msg.text:
        if 9 < hour < 11:
          bot.send_message(user["chat_id"], "Вы завтракаете ")
        else:
         bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/lunch" in msg.text:
            if 14 < hour < 15:
                bot.send_message(user["chat_id"], "Вы обедаете ")
            else:
                bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    if "/dinner" in msg.text:
            if 19 < hour < 20:
                bot.send_message(user["chat_id"], "Вы ужинаете ")
            else:
                bot.send_message(user["chat_id"], "Вы сейчас не можете кушац")
    else:
        for neighbor in neighbors:
          if neighbor["chat_id"] != user["chat_id"]:
            bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))