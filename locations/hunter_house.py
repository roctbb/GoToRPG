@bot.message_handler(commands=['Vzyat_kapitoshku'])
def huntho(message):
    if "/waterballгз" in msg.text:
        user['inventory'].append(kapitoshka)
        for neighbor in neighbors:
            bot.send_message(neighbor['chat_id'], "{} поднял капитошку")

def event(users, location, bot):
    for user in users:
        bot.send_sticker(user['chat_id'], stickers['nikolay'])
        bot.send_message(user['chat_id'], 'На улице появился Николай. Вы отвлекаете его от работы! Вы наказаны!')
        user['states'].append('punishment')