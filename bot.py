import random
from init import *
import config
import importlib
import time
import threading


def life_support():
    while True:
        for user in users:
            check_params(user)

            # еда
            if user['eat_points'] != 0:
                user['eat_points'] -= 1
            else:
                bot.send_message(user['chat_id'], "☹️ Вы очень хотите есть...")

            if user['sleep_points'] != 0:
                user['sleep_points'] -= 1
            else:
                bot.send_message(user['chat_id'], "😴 Вы очень хотите спать...")

            # заболевание
            if "wet" in user['states'] and "sick" not in user['states'] and random.randint(1, 20) == 1:
                bot.send_message(user['chat_id'],
                                 "🤧 Вы слишком долго ходили мокрым и простудились. Чтобы подлечиться попробуйте зайти в медпункт.")
                user['states'].append('sick')

        for location in locations:
            try:
                location_module = importlib.import_module(location['file'])
                location_module.event(find_users_by_location(location['id']), location, bot)
            except Exception as e:
                print(e)

        save()
        time.sleep(5 * 60)





@bot.message_handler(content_types=['sticker'])
def print_sticker(message):
    print(message.sticker.file_id)


@bot.message_handler(content_types=['text'])
def process_message(message):
    user = find_user(message.chat.id)

    if not user:
        init(message.chat.id)
        return

    if "name" not in user:
        save_name(user, message.text)
        return

    check_params(user)

    if "/info" in message.text:
        description = "ℹ️ Информация об игроке.\n" \
                      "\n" \
                      "Имя игрока: {}\n" \
                      "Локация: {}\n" \
                      "Сытость: {}\n" \
                      "Бодрость: {}\n" \
                      "Рюкзак: {}\n" \
                      "Состояния: {}\n".format(user['name'], user['location'], user['eat_points'], user['sleep_points'],
                                             ' / '.join(user['inventory']), ' / '.join(user['states']))
        bot.send_message(user['chat_id'], description)
        return

    if "/locations" in message.text:
        bot.send_message(user['chat_id'], location_list())

    if "/goto" in message.text:
        try:
            cmd, location_id = message.text.split(' ')
            location = change_location_by_id(user, location_id)

            try:
                location_module = importlib.import_module(location['file'])
                location_module.welcome(user, location, bot)
            except Exception as e:
                print(e)

            return
        except Exception as e:
            print(e)
            bot.send_message(user["chat_id"], "👀 Укажите название локации.")
            return

    location = find_location(user['location'])
    users = find_users_by_location(user['location'])

    try:
        location_module = importlib.import_module(location['file'])
        location_module.message(message, user, location, users, bot)
    except Exception as e:
        print(e)

    save()


life_thread = threading.Thread(target=life_support)
life_thread.start()

bot.polling()
