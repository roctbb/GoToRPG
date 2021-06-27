
@bot.message_handler(commands=['Vzyat_kapitoshku'])
if "/waterballгз" in msg.text:
    user['inventory'].append(kapitoshka)
    for neighbor in neighbors:
        bot.send_message(neighbor['chat_id'], "{} поднял капитошку")

def event(users, location, bot):

    hour = datetime.now().hour

    # пояление Николая
    if 0 < hour < 7:
        if random.randint(1, 3) == 1:
            for user in users:
                bot.send_sticker(user['chat_id'], stickers['nikolay'])
                bot.send_message(user['chat_id'], 'В доме охотника появился Николай. Вы отвлекаете его от работы! Вы наказаны!')
                user['states'].append('punishment')
