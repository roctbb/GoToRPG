from datetime import datetime
import time
import random


audio = ["music/Жуки - Батарейка.mp3", "music/quest-pistols-ty-tak-krasiva.mp3"]

horror_stories = ["""Явь. Девочке 5 лет. У нее 3 сестры, и она больше всех на папу похожа. Отец пропал и 3 дня дома не появляется, мать психует. Под утро 3 дня она просыпается от того, что он её за плечо трогает, и видит его с доской с гвоздями в виске, весь в крови, говорит, что в лесочке возле соседнего дома искать надо. Она маме рассказала, мама бегом к ментам. Нашли. Экспертиза показала, что умер он этим утром, а с этой доской с гвоздями он лежал в этом лесочке и был жив 3 дня. Её мама в дурку хотела сдать…""",
                  "Два пастуха от скуки мастерят пугало, называют его Гарольдом в честь фермера, которого ненавидят, глумятся над ним, вымещают злость, пинают и оскорбляют. А чучело сначала молчит, потом ворчит и в конце концов оживает: сдирает с одного из своих мучителей кожу и вывешивает на солнышке для просушки.",
                  "Один человек заблудился в лесу. Он долго блуждал и, в конце концов, в сумерках натолкнулся на хижину. Внутри никого не было, и он решил лечь спать. Но он долго не мог заснуть, потому что на стенах висели портреты каких-то людей, и ему казалось, что они зловеще смотрят на него. В конце концов он заснул от усталости. Утром его разбудил яркий солнечный свет. На стенах не было никаких картин. Это были окна.",
                  "Двенадцатилетняя девочка жила с отцом. У них были прекрасные отношения. Однажды отец собрался задержаться на работе и сказал, что вернется поздно ночью. Девочка ждала его, ждала и, наконец, легла спать. Ей приснился странный сон: отец стоял на другой стороне оживленного шоссе и что-то ей кричал. Она едва расслышала слова: “Не… открывай… дверь”. И тут девочка проснулась от звонка. Она вскочила с постели, подбежала к двери, посмотрела в глазок и увидела лицо отца. Девочка уже собиралась открыть замок, как вспомнила сон. И лицо отца было каким-то странным. Она остановилась. Снова зазвенел звонок.\n– Папа?\nДзинь, дзинь, дзинь.\n— Папа, ответь мне!\nДзинь, дзинь, дзинь.\n— Там кто-то есть с тобой?\nДзинь, дзинь, дзинь.\n— Папа, почему ты не отвечаешь?\n— девочка едва не плакала.\nДзинь, дзинь, дзинь.\n— Я не открою дверь, пока ты мне не ответишь!\nВ дверь всё звонили и звонили, но отец молчал. Девочка сидела, сжавшись в углу прихожей. Так продолжалось около часа, потом девочка провалилась в забытье. На рассвете она проснулась и поняла, что в дверь больше не звонят. Она подкралась к двери и снова посмотрела в глазок. Ее отец всё ещё стоял там и смотрел прямо на неё. Девочка осторожно открыла дверь и закричала. Отрубленная голова её отца была прибита к двери гвоздем на уровне глазка. На дверной звонок была прикреплена записка, в которой было всего два слова: «Умная девочка».",
                  "Жила была девочка у которой родители часто уезжали на работу на ночь. И чтобы она не боялась, они купили ей собаку. в тот день все было как всегда, родители уехали а девочка закрыла все окна кроме одного маленького на кухне, и пошла спать. ночью она проснулась из-за звука капель падающих в ванной, она по привычке опустила руку под кровать и ее собака как всегда облизала ей руку. она успокоилась и уснула. так повторялось три или четыре раза,но в итоге она не выдержала и пошла в ванную. и там она увидела свою собаку подвешенную за хвост, а с ее горла капала кровь. но самый ужас это зеркало в ванной на котором было написано -""МНЕ ПОНРАВИЛСЯ ВКУС ТВОИХ ПАЛЬЦЕВ""-На следующее утро девочку нашли в запертой ванной, живую но в шоке, так как всю ночь она провела там, вместе со своим псом.",
                  "Когда я был ребёнком, моя семья переехала в большой старый двухэтажный дом с большими пустыми комнатами и скрипящими половицами. Оба родителя работали, поэтому я часто был один, когда возвращался со школы. Однажды вечером, когда я пришел домой, свет не был включен.\nЯ крикнул: «Мама?» И услышал, как ее голос нараспев произнёс: «Дааа?» Я позвонил ей и поднялся по лестнице, чтобы посмотреть, в какой комнате она была, но снова получил тот же ответ: «Дааа?»\nНа тот момент я не знал в идеале планировку дома, но она была в одной из далёких комнат в самом конце коридора. Меня это смутило, но я всё равно пошёл к ней, чтобы увидеть свою маму. Её присутствие избавляет меня от всяких страхов.\nКак только я потянулся к ручке двери, чтобы войти в комнату, я услышал, как входная дверь открывается внизу, и моя мама весёлым голосом зовёт меня: «Милый, ты дома?» Я отпрыгнул, испугавшись, и побежал к ней вниз по лестнице, но, когда я обернулся, дверь в комнату начала медленно открываться. На миг я увидел там что-то странное и не знаю, что это было, но оно смотрел на меня.",
                  """Путник вошел в отель и направился прямиком к ресепшену..
                  Администратор выдал ему ключи и сказал: "чтобы ни случилось, не подходите к двери без номера около вашей комнаты"
                  Путник отправился в свою комнату и лег спать..Всю ночь он не мог сомкнуть глаз. Он постоянно думал о комнате без номера..Он вышел в коридор, подошел к двери и попробовал её открыть, но та оказалась заперта..
                  Он нагнулся и посмотрел в замочную скважину.
                  Он увидел женщину, сидевшую прислонившись к стене. Лица её он не разглядел, так как она смотрела в другую сторону..
                  Мужчина хотел было постучать, но в последний момент передумал..
                  Он решил вернутся в свою комнату..
                  На следующее утро он вновь подошел к двери и посмотрел в замочную скважину..всё что он увидел это только что-то красное
                  "Хм..наверное женщина заметила, как я смотрел в замочную скважину вчера и завесила её красной тряпкой..или что-то в этом роде.."
                  Смущенный и озадаченный он решил выяснить у владельца отеля в чем же все таки дело
                  - Вы смотрели в замочную скважину?
                  - Да..
                  - ..ну значит мне придется рассказать вам все как есть..несколько лет назад мужчина убил свою жену в той комнате, и мне кажется её призрак всё ещё находится там..
                  Наступила небольшая пауза.
                  - Внешне женщина выглядела вполне обычно..но её глаза...были красного цвета...""",
                  """Маленький мальчик спал в своей постели ночью. Вдруг он слышит шаги за дверью и смотрит в глазок, чтобы посмотреть, что происходит. Она распахивается, и заходит убийца, несущий трупы его родителей. После того, как он посадил их на стул, убийца что-то написал кровью мертвецов на стене, а затем спрятался под кроватью ребёнка.

                  Ребёнок был страшно напуган. Он не может прочитать послание на стене и знает, что мужчина лежит под его кроватью. Ребёнок, как и все дети, начал притворяться спящим. Он всё ещё лежит и слышит дыхание убийцы из-под кровати.

                  Проходит час, и его ночное зрение стало лучше. Ребёнок пытается разобрать слова, но это сложно. Следующие слова заставили его дыхание замереть: «Я знаю, что ты проснулся». Он чувствует, что что-то двигается под кроватью.""",
                  """Лет пять назад глубокой ночью раздались 4 коротких звонка в мою дверь. Я проснулся, разозлился и не стал открывать: я никого не ждал. На вторую ночь кто-то снова позвонил 4 раза. Я выглянул в глазок, но за дверью никого не было. Днем я рассказывал эту историю, и пошутил, что, наверное, смерть ошиблась дверью. На третий вечер ко мне зашел знакомый и засиделся допоздна. В дверь снова позвонили, но я сделал вид, что ничего не заметил, чтобы проверить: может, у меня галлюцинации. Но он все прекрасно услышал и, после моей истории, воскликнул: “Ну-ка разберемся с этими шутниками!” и выбежал во двор. В ту ночь я видел его последний раз. Нет, он не исчез. Но по дороге домой его избила пьяная компания, и он скончался в больнице. Звонки прекратились. Я вспомнил об этой истории, потому что вчера ночью услышал три коротких звонка в дверь.""",
]

def welcome(user, location, bot):
    #hour = datetime.now().hour
    hour = 22

    if 0 <= hour <= 6:
        bot.send_message(user["chat_id"], "Вы подходите к кострищу, но все уже разошлись и костер потух. Приходите завтра.")
    elif 6 < hour < 22:
        bot.send_message(user["chat_id"], "С 22 часов ночи начинаются посиделки у костра. Сейчас костер не горит.")
    else:
        bot.send_message(user['chat_id'], "Вы подходите к кострищу, садитесь на свободное место.\n"
                             "*🌭 /fry_sausage\n"
                             "*💬 /talk\n"
                             "*⭐ /star\n"
                             "*🎸 /play\n"
                             "*👻 /horror")

def message(msg, user, location, neighbors, bot):
    hour = datetime.now().hour

    if 1 < hour < 22:
        bot.send_message(user["chat_id"], "С 22 часов ночи начинаются посиделки у костра. Сейчас костер не горит.")
        return

    if "/fry_sausage" in msg.text:
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

             bot.send_message(user["chat_id"], "Вы играете на гитаре и все подпевают...")
             for neighbor in neighbors:
                 if user["chat_id"] != neighbor["chat_id"]:
                     bot.send_message(neighbor["chat_id"], "{} играет на гитаре.".format(user['name']))
                 # отправлять в чат случайную песню
                 bot.send_audio(neighbor["chat_id"], open(random.choice(audio), 'rb').read())
         else:
             bot.send_message(user["chat_id"], "Вам нужна гитара. Гитару, кажется, видели в учебке.")


    if "/horror" in msg.text:
        # найти в интернете несколько страшилок
        for neighbor in neighbors:
            bot.send_message(neighbor["chat_id"], "{} рассказывает страшную историю.")
            bot.send_message(neighbor["chat_id"], random.choice(horror_stories))
            time.sleep(20)
            bot.send_message(neighbor["chat_id"], "В процессе рассказа страшной истории все услышали шорох в лесу...")
