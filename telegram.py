import telebot
import parsing
from telebot import types
from my_token import TOKEN

# создаём телеграм бота
bot=telebot.TeleBot(TOKEN)

# функция обработки ввода команды "/start" в бота 
@bot.message_handler(commands=['start'])
def start_message(message):
    # создании клавиатуры
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_start_parsing = types.KeyboardButton("Start collection data")
    markup.add(btn_start_parsing)

    # отправка сообщения пользователю
    bot.send_message(message.chat.id,'Please, click the button!',reply_markup=markup)

# функция обработки ввода в бота текста
@bot.message_handler(content_types='text')
def message_reply(message):
    # проверка, на команду сбора данных
    if message.text=="Start collection data":
        # парсинг и сохранение данных
        parsing.main()
        # отправляем результат
        with open('result.xlsx', 'r', encoding="utf-8") as file:
            bot.send_message(message.chat.id, file)
    else:
        bot.send_message(message.chat.id,'Please, click the button!')

# бесконечная работа бота
bot.infinity_polling()