users=[]
@bot.message_handler(commands=['Vzyat_kapitoshku'])
if "/waterball" in msg.text:
    user['inventory'].append kapitoshka
    for neighbor in neighbors:
        bot.send_message(neighbor['chat_id'], "{} поднял капитошку")