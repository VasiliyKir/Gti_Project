#здесь идёт код
import telebot

bot = telebot.TeleBot("751363980:AAHYtCJmmUmmKCl_F7Swwo6zfrgLIA2xKno")

# bot.send_message(404488278, "")

# upd = bot.get_updates()
# print(upd)

# last_upd = upd[-1]
# message_from_user = last_upd.message
# print(message_from_user)
@bot.message_handler(commands=["help"])
def handle_command(message):
    bot.send_message(message.chat.id, """Список команд:
/start - начать
/stopBot - завершить
/events - категории
/mysubs - мои подписки
/back - назад""")
@bot.message_handler(commands=["stopBot"])
def handle_command(message):
    bot.send_message(message.chat.id, """Жаль, увидимся позже!""")
@bot.message_handler(commands=["start"])
def handle_command(message):
    bot.send_message(message.chat.id, """Добро пожаловать, выберете дальнейшие действия.""")
@bot.message_handler(commands=["events"])
def handle_command(message):
    bot.send_message(message.chat.id, """Фильтр""")
    bot.send_message(message.chat.id,  """Все мероприятия:
    /1 - мероприятие 1
    /2 - мероприятие 2
    /3 - мероприятие 3
    /4 - мероприятие 4
    /5 - мероприятие 5
    /6 - мероприятие 6
    /7 - мероприятие 7
    /8 - мероприятие 8""")
@bot.message_handler(commands=["1"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 1
Дата
Время
Ссылка""")
@bot.message_handler(commands=["2"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 2
Дата
Время
Ссылка""")
@bot.message_handler(commands=["3"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 3
Дата
Время
Ссылка""")
@bot.message_handler(commands=["4"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 4
Дата
Время
Ссылка""")
@bot.message_handler(commands=["5"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 5
Дата
Время
Ссылка""")
@bot.message_handler(commands=["6"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 6
Дата
Время
Ссылка""")
@bot.message_handler(commands=["7"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 7
Дата
Время
Ссылка""")
@bot.message_handler(commands=["8"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мероприятие 8
Дата
Время
Ссылка""")
@bot.message_handler(commands=["mysubs"])
def handle_command(message):
    bot.send_message(message.chat.id, """Мои подписки:""")
@bot.message_handler(commands=["back"])
def handle_command(message):
    bot.send_message(message.chat.id, """Вы шагнули назад.
Бот возвращается к предыдущему сообщение.""")
bot.polling(none_stop=True, interval=0)
