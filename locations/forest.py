from datetime import datetime
import time
from random import randint

def welcome(user, location, bot):
    bot.send_message(user['chat_id'], "В лесу есть много ягод🍓 и грибов🍄. Можешь их поискать🔎\n"
                                      "Чтобы собирать и есть ягоды используй /berries 🍒\n"
                                      "Чтобы собирать и есть грибы используй /mushroom 🍄 ")

def message(msg, user, location, neighbors, bot):
    if "/berries" in msg.text:
        berrychance = randint(1, 4)
        if berrychance == 2:
            user["eat_points"] += 10
            bot.send_message(user["chat_id"], "Вы cъели ягодки!🍇\n"
                                              "Ваше уровень питание: {}".format(user['eat_points']))
        else:
            bot.send_message(user['chat_id'], "Увы ягод ты не нашёл. Поищи ещё 😱")

    if "/mushroom" in msg.text:
        berrychance = randint(1, 6)
        if berrychance[user] == 1:
            user["eat_points"] += 12
            bot.send_message(user["chat_id"], "Вы cъели грибы!🍄\n"
                                              "Теперь ваще состояние токсичное. 🦠\n"
                                              "Ваше уровень питание: {}".format(user['eat_points']) )
            user['states'].append('toxic')
        else:
            bot.send_message(user['chat_id'], "Ты не нашёл грибочков 😢")



    # TODO: можно поесть ягод (user['eat_points'] + N) / грибов (добавляет состояние "toxic")

def event(neighbors, location, bot):
    hour = datetime.now().hour
    for user in neighbors:
        if "dirty" not in user['states']:
            user['states'].append('dirty')
            bot.send_message(user['chat_id'], "В лесу грязно. Вы испачкались💩")

    if 0 < hour < 10:
        if randint(1, 7) == 1:
            for user in neighbors:
                bot.send_message(user['chat_id'], "Появляется маньяк🔪💉.")

            if len(neighbors) > 3:
                strong = 0
                sticks = 0
                for user in neighbors:
                    # TODO + еда и сон
                    if "sick" not in user['states'] and "punished" not in user['states']:
                        strong += 1

                    if "stick" in user['inventory']:
                        sticks += 1

                if strong > 3 and sticks > 3:
                    bot.send_message(user['chat_id'],"Общими усилиями вы смогли победить маньяка!🥳🤩")
                    for user in neighbors:
                        user['sleep_points'] += 100
                        user['eat_points'] += 100
                        user['inventory'].append(waterball)
                        for i in range(20):
                            user['inventory'].append("waterball")
                        for i in range(5):
                            user['inventory'].append("icecream")
                        for i in range(10):
                            user['inventory'].append("coin")
                        for i in range(5):
                            user['inventory'].append("frog")
                        user['inventory'].append("sword")


                        bot.send_message(user['chat_id'], "За победу вы получили:🎁\n"
                                                          "20 капитошек💣\n"
                                                          "5 мороженных🍦\n"
                                                          "10 монет💰\n"
                                                          "5 лягушек🐸\n"
                                                          "1  меч🗡")


                    return
                else:
                    bot.send_message(user['chat_id'], "Маньяк побеждает! Вы умерли!🩸")

            else:
                for user in neighbors:
                    bot.send_message(user['chat_id'], " Слишком мало людей👤 чтобы победить его.\n Вы возращаетесь обратно🔙.")

            for user in users:
                bot.send_message(user['chat_id'],"Маньяк убил {}🩸".format(user['name']))


        else:
            bot.send_message(user['chat_id'], "Сейчас позднее время🕰. Не время ходить по лесу🌌")
            #TODO: if проиграли - for user in users отправить уведомление о смерти, users.remove(user)




















































































































































