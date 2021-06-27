import config
import importlib
from init import *


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

    with open('users.json', 'w') as file:
        json.dump(users, file)
    with open('locations.json', 'w') as file:
        json.dump(locations, file)

bot.polling()