from datetime import datetime

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if "/sleep" in msg.text:
        if 10 < hour < 15:
            bot.send_message(user["chat_id"], "Вы загораете.")
        elif 0 < hour < 7:
            bot.send_message(user["chat_id"], "Вы спите на улице.")
        else:
            bot.send_message(user["chat_id"], "Вы прилегли отдохнуть.")
    else:
        for neighbor in neighbors:
            if neighbor["chat_id"] != user["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{}: {}".format(user["name"], msg.text))



def event(location, users, bot):
    pass