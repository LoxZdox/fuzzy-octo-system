import telebot
import webbrowser
import sqlite3
from telebot import types


bot = telebot.TeleBot('6381271276:AAE7xQ_DVI9PVsXVhYxvMldJnveQkry8P3U')


@bot.message_handler(commands=['start', 'help', 'menu'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('/hello')
    markup.row(btn1)
    btn2 = types.KeyboardButton('/new')
    btn3 = types.KeyboardButton('/show')
    markup.row(btn2, btn3)
    btn4 = types.KeyboardButton('/edit')
    btn5 = types.KeyboardButton('/delete')
    markup.row(btn4, btn5)
    btn6 = types.KeyboardButton('/github')
    markup.row(btn6)
    bot.send_message(message.chat.id, '\
Привет, я классический TODO бот, ты можешь \
создавать здесь задачи и производить с ними \
стандартные операции типа изменения, вывода \
и удаления задач. Для этого ты можешь \
использовать кнопки, либо команды /new, /show, \
/edit и /delete', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.first_name} {message.chat.last_name}!')


@bot.message_handler(commands=['new'])
def main(message):
    bot.send_message(message.chat.id, 'Введите название вашей задачи')


@bot.message_handler(commands=['show'])
def main(message):
    bot.send_message(message.chat.id, 'Ваш список задач: \n')


@bot.message_handler(commands=['edit'])
def main(message):
    bot.send_message(message.chat.id, 'Введите номер задачи, \
которую вы хотите отредактировать')


@bot.message_handler(commands=['delete'])
def main(message):
    bot.send_message(message.chat.id, 'Введите номер задачи, \
которую вы хотите удалить')
    

@bot.message_handler(commands=['github', 'guthib'])
def site(message):
    webbrowser.open('https://github.com/LoxZdox')


@bot.message_handler()
def main(message):
    if message:
        bot.reply_to(message, f'Привет, {message.chat.first_name} {message.chat.last_name}!')
        bot.register_next_step_handler(message, complex_message(message))

def complex_message(message):
    bot.send_message(message.chat.id, "Я бы хотел тебе помочь, но не могу, у меня лапки")
    

bot.polling(non_stop=True)