from datetime import datetime
import time
from random import randint
from init import *
import importlib

def welcome(user, location, bot):
    bot.send_message(user['chat_id'], "Вы выходите за калитку и попадаете в лес. В лесу много ягод 🍓 и грибов 🍄. Можешь их поискать, но ночью тут опасно...\n\n"
                                      "🍒 /berries \n"
                                      "🍄 /mushroom")

def message(msg, user, location, neighbors, bot):
    if "/berries" in msg.text:
        berrychance = randint(1, 4)
        if berrychance == 2:
            user["eat_points"] += 7
            bot.send_message(user["chat_id"], "🍇 Вы cъели ягоду!")

            if user["eat_points"] > 120:
                bot.send_message(user["chat_id"], "Вы явно переели, теперь у вас понос.")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")
        else:
            bot.send_message(user['chat_id'], "Увы ягод ты не нашёл. Поищи ещё 😱")

    elif "/mushroom" in msg.text:
        mushroomchance = randint(1, 6)

        if mushroomchance == 1:
            user["eat_points"] += 10
            bot.send_message(user["chat_id"], "🍄 Вы cъели гриб!\n"
                                              "Вы ощущаете тяжесть в конечностях, голоса в голове нашептывают вам код на Brainfuck. 🦠" )
            if user["eat_points"] > 120:
                bot.send_message(user["chat_id"], "Вы явно переели, теперь у вас понос.")
                if "ponos" not in user['states']:
                    user['states'].append("ponos")

            if "toxic" not in user['states']:
                user['states'].append('toxic')
        else:
            bot.send_message(user['chat_id'], "Ты не нашёл грибочков 😢")

def event(neighbors, location, bot):
    hour = datetime.now().hour

    for user in neighbors:
        if "dirty" not in user['states']:
            user['states'].append('dirty')
            bot.send_message(user['chat_id'], "💩 В лесу грязно. Вы испачкались.")

    if 0 < hour < 5:
        if randint(1, 7) == 1:
            for user in neighbors:
                bot.send_message(user['chat_id'], "👹 !!! Появляется маньяк !!! 🔪💉.")

            if len(neighbors) > 2:
                strong = 0
                sticks = 0
                for user in neighbors:
                    if "sick" not in user['states'] and "punished" not in user['states'] and "toxic" not in user['states']:
                        strong += 1

                    if "stick" in user['inventory']:
                        sticks += 1

                if strong > 2 and sticks > 2:
                    for user in neighbors:
                        bot.send_message(user['chat_id'], "Вы отчаянно набрасываетесь на маньяка с дубинками...")
                        bot.send_message(user['chat_id'], "и общими усилиями побеждаете маньяка! 🥳🤩")

                        user['sleep_points'] += 100
                        user['eat_points'] += 100
                        for i in range(20):
                            user['inventory'].append("waterball")
                        for i in range(5):
                            user['inventory'].append("icecream")
                        for i in range(10):
                            user['inventory'].append("coin")
                        for i in range(5):
                            user['inventory'].append("frog")

                        user['inventory'].append("coffee")


                        bot.send_message(user['chat_id'], "За победу вы получили:🎁\n"
                                                          "* 20 капитошек💣\n"
                                                          "* 5 мороженных🍦\n"
                                                          "* 10 монет💰\n"
                                                          "* 5 лягушек🐸\n"
                                                          "* кофе!!! ☕️")
                        bot.send_message(user['chat_id'],
                                         "Вы гордо возвращаетесь в лагерь и заходите в домик.🔙")

                        location = change_location_by_id(user, "home")
                        try:
                            location_module = importlib.import_module(location['file'])
                            location_module.welcome(user, location, bot)
                        except Exception as e:
                            print(e)

                    return
                else:
                    for user in neighbors:
                        bot.send_message(user['chat_id'], "Вы отчаянно набрасываетесь на маньяка...")
                        bot.send_message(user['chat_id'], "Но у вас не хватает сил, и маньяк побеждает! Вы умерли! 🩸")

                        if "guitar" in user['inventory']:
                            location = find_location("hunter_house")
                            location['inventory'].append("guitar")
                        if "stick" in user['inventory']:
                            location = find_location("hunter_house")
                            location['inventory'].append("stick")

                        users.remove(user)

                        for guser in users:
                            if guser not in neighbors:
                                bot.send_message(guser['chat_id'], "Маньяк убил {}🩸".format(user['name']))

            else:
                for user in neighbors:
                    bot.send_message(user['chat_id'], "👤 В лесу слишком мало людей чтобы победить маньяка.\n Вы убегаете в лагерь и оказываетесь на улице.🔙")

                    location = change_location_by_id(user, "street")
                    try:
                        location_module = importlib.import_module(location['file'])
                        location_module.welcome(user, location, bot)
                    except Exception as e:
                        print(e)

        else:
            bot.send_message(user['chat_id'], "Сейчас позднее время 🕰. Не время ходить по лесу! 🌌")





















































































































































