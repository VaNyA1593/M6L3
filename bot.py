import telebot
import time
import threading
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

def start_timer(chat_id, seconds):

    time.sleep(seconds)
    bot.send_message(chat_id, f"Время вышло! Прошло {seconds} секунд.")

@bot.message_handler(commands=['timer'])
def set_timer(message):
    
    parts = message.text.split()
    
    if len(parts) != 2:
        bot.reply_to(message, "Введите время в секундах после команды /timer.")
        return
    
    if not parts[1].isdigit():
        bot.reply_to(message, "Пожалуйста, введите число.")
        return
    
    seconds = int(parts[1])
    bot.reply_to(message, f"Таймер на {seconds} секунд запущен.")
    
    
    thread = threading.Thread(target=start_timer, args=(message.chat.id, seconds))
    thread.start()

bot.polling()
