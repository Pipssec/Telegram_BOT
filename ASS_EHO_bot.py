import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('5094470494:AAEpxDdWQhfs0mJ4vVvsLxA6gbbUgH_hYXU')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)

# Запускаем бота
bot.polling(none_stop=False, interval=0)
