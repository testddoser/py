import telebot
import time

print("!BOT STARTED!")

# Создаем объект бота
bot = telebot.TeleBot('6305832366:AAE7bDANfSymlLY9R5Wb8ypbQMH3pHP3QRs')
bot.send_message(1199404728, "!BOT STARTED!")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Я отсылаю сообщение каждые 20 секнуд")

while True:
    time.sleep(20)
    bot.send_message(1199404728, "Прошло 20 секунд")

# Запускаем бота
bot.infinity_polling()
