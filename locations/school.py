from datetime import datetime
import random



from init import check_params


def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour
    minute = datetime.now().minute
    check_params(user)
    # поднятие / оставление гитары
    if "/give_guitar" in msg.text:
        if "guitar" in user['inventory']:
            location['inventory'].append("guitar")
            user['inventory'].remove("guitar")

            for neighbor in neighbors:
                bot.send_message(neighbor["chat_id"], "{} вернул гитару".format(user['name']))
        else:
            bot.send_message(user["chat_id"], "У вас нет гитары")
    elif "/take_guitar" in msg.text:

        user['inventory'].append("guitar")
        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} поднял гитару".format(user['name']))
    if "/code" in msg.text:
        bot.send_message(user['chat_id'], "ты пишешь код, подожди")


        user['code_line' ] +=  random.randint(4,6)
        bot.send_message(user['chat_id'], "вы написали строчки кода,у вас ",user['codeline'],'трочек кода')

        if  "wet" in user["states"] or "derty" in user["states"] or "sick" in user["states"] or "punished"in user["states"] or "ponos" in user["states"]  :
            user['code_line',] += random.randint(2, 4)
            bot.send_message(user['chat_id'], "вы написали строчки кода,у вас ", user['codeline'], 'трочек кода')



        if "toxic" in user["states"]:
            def event(users, location, bot):
                user['code_line',] += random.randint(6, 10)
                bot.send_message(user['chat_id'], "вы написали строчки кода,у вас ", user['codeline'], 'трочек кода')
