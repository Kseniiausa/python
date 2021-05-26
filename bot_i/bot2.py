import telebot
import config
 
bot = telebot.TeleBot(config.TOKEN)

#приветствие

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    


    bot.send_message(message.chat.id, "Приветики, {0.first_name}!\nЯ - <b>{1.first_name}</b>, побалтаем?.".format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
#выполнит нижестоящую функцию, если от Telegram придёт текстовое сообщение
def lalala(message):
    
     bot.send_message(message.chat.id,message.text) #отвечает также


 
# RUN
bot.polling(none_stop=True)

