# Optional: Add the Telegram bot to the previous exercise. 
# Ask the user to enter a search word in the Telegram interface and get a gif image as a result.

# token - 6429077230:AAHmDsR9QJQAhaP0-vKgAV2yKjAoY0rBaI0
# bot's name - giphy_tpy_bot
# pip install pyTelegramBotAPI


import telebot
from giphy_search import giphy_search_2 as gs
bot = telebot.TeleBot('6429077230:AAHmDsR9QJQAhaP0-vKgAV2yKjAoY0rBaI0')

@bot.message_handler(commands=["start"])
def start(message):
    if message.from_user.last_name != None:
        mess1 = f"Привіт, {message.from_user.first_name} {message.from_user.last_name}. Я з сімейства Автоботів, вкажи слово і я дещо тобі покажу"
    else:
        mess1 = f"Привіт, {message.from_user.first_name}. Я з сімейства Автоботів, вкажи слово і я дещо тобі покажу"
    bot.send_message(message.chat.id, mess1)


@bot.message_handler()
def get_user_text(message):
    url = "".join(gs(message.text, 1))
    bot.send_animation(message.chat.id, animation=url)

bot.polling(non_stop=True)


