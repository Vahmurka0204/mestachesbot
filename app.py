import telebot
import os
from chore import Chore

API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)
chores = []


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
@bot.message_handler(commands=['new'])
def send_welcome(message):
    bot.reply_to(message, "Добавляем новое дело. Формат: \n1. Название \n2.Дата следующей уборки \n3. Периодичность")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text_task = message.text
    task_split = text_task.split("\n")
    chore = Chore(len(chores), task_split[0],task_split[1], task_split[2])
    chores.append(chore)
    bot.reply_to(message, f"Добавлено новое дело: {chore.name}")
    

bot.infinity_polling()