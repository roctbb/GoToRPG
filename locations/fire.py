from datetime import datetime
import time

horror_stories = ["Явь. Девочке 5 лет. У нее 3 сестры, и она больше всех на папу похожа. Отец пропал и 3 дня дома не появляется, мать психует. Под утро 3 дня она просыпается от того, что он её за плечо трогает, она просыпается и видит его с доской с гвоздями в виске, весь в крови, говорит, что в лесочке возле соседнего дома искать надо. Она маме рассказала, мама бегом к ментам. Нашли. Экспертиза показала, что умер он этим утром, а с этой доской с гвоздями он лежал в этом лесочке и был жив 3 дня. Её мама в дурку хотела сдать…",
                  "Два пастуха от скуки мастерят пугало, называют его Гарольдом в честь фермера, которого ненавидят, глумятся над ним, вымещают злость, пинают и оскорбляют. А чучело сначала молчит, потом ворчит и в конце концов оживает: сдирает с одного из своих мучителей кожу и вывешивает на солнышке для просушки.",
                  ""]

def welcome(user, location, bot):
    hour = datetime.now().hour

    if 1 < hour < 22:
        bot.send_message(user["chat_id"], "С 22 часов ночи начинаются посиделки у костра. Сейчас костер не горит.")
    else:
        pass
        # отправить инструкцию

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if 1 < hour < 22:
        bot.send_message(user["chat_id"], "С 22 часов ночи начинаются посиделки у костра. Сейчас костер не горит.")
        return

    if "/fry-sausage" in msg.text:
        if "sausage" not in user['inventory']:
            user['inventory'].append("sausage")
            bot.send_message(user["chat_id"], "Вы жарите сосиску.")
        else:
            bot.send_message(user["chat_id"], "У вас уже есть сосиска.")

    if "/talk" in msg.text:
        bot.send_message(user["chat_id"], "Вы делитесь своими впечатлениями о прошедшем дне.")

        for neighbor in neighbors:
            if user["chat_id"] != neighbor["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{} делится впечатлениями о прошедшем дне.".format(user['name']))

    if "/star" in msg.text:
        bot.send_message(user["chat_id"], "Небо было чистым и все рассматривали полярную звезду.")
        for neighbor in neighbors:
            if user["chat_id"] != neighbor["chat_id"]:
                bot.send_message(neighbor["chat_id"], "{} смотрит на звезды.".format(user['name']))

    if "/play" in msg.text:
        if "guitar" in user['inventory']:
            bot.send_message(user["chat_id"], "Вы играете на гитаре и все подпевают песню.")

            for neighbor in neighbors:
                if user["chat_id"] != neighbor["chat_id"]:
                    bot.send_message(neighbor["chat_id"], "{} играет на гитаре.".format(user['name']))
                # отправлять в чат случайную песню
                # bot.send_audio(neighbor["chat_id"], open('audio.mp3', 'rb').read())
        else:
            bot.send_message(user["chat_id"], "Вам нужна гитара.")

    if "/horror" in msg.text:
        # найти в интернете несколько страшилок
        if 1 < hour < 12:
            bot.send_message(user["chat_id"], "Все по очереди рассказывают страшные истории.")
            time.sleep(10)
            bot.send_message(user["chat_id"], "В процессе рассказа страшной истории все услышали шорох в лесу.")
