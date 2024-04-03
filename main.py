import telebot

print("!BOT STARTED!")

# Создаем объект бота
bot = telebot.TeleBot('6305832366:AAE7bDANfSymlLY9R5Wb8ypbQMH3pHP3QRs')
bot.send_message(1199404728, "!BOT STARTED!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a simple bot. Type something and I will try to answer.")

@bot.message_handler(content_types=['text'])
def handle_message(message):
    # Отвечаем на сообщение пользователя
    bot.reply_to(message, message.text)

# Запускаем бота
bot.infinity_polling()
