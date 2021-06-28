import random

import config
import importlib
from init import *
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
                bot.send_message(user['chat_id'], "Вы очень хотите есть...")

            if user['sleep_points'] != 0:
                user['sleep_points'] -= 1
            else:
                bot.send_message(user['chat_id'], "Вы очень хотите спать...")

            # заболевание
            if "wet" in user['states'] and "sick" not in user['states'] and random.randint(1, 20) == 1:
                bot.send_message(user['chat_id'], "Вы простудились...")
                user['states'].append('sick')

        for location in locations:
            try:
                location_module = importlib.import_module(location['file'])
                location_module.event(users, location, bot)
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

    if "/goto" in message.text:
        try:
            cmd, location_id = message.text.split(' ')
            change_location_by_id(user, location_id)
            return
        except Exception as e:
            print(e)
            bot.send_message(user["chat_id"], "Укажите название локации.")
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