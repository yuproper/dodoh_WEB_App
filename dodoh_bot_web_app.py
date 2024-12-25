TOKEN = "тут надо вставить ваш токен"

import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    webApp = telebot.types.WebAppInfo("https://6c932e9f-a7a9-4f88-b29a-331314c0f780-00-1cx6cfi3cm5gx.riker.replit.dev/")
    webAppButton = telebot.types.KeyboardButton(text="Открыть менеджер паролей", web_app=webApp)
    markup.add(webAppButton)

    bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы открыть менеджер паролей.", reply_markup=markup)

bot.polling()
