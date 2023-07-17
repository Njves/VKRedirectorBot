import telebot
from telebot.types import InputMediaPhoto
from config import TOKEN_TG

bot = telebot.TeleBot(TOKEN_TG)
chat_id = "@iwced"


class BotMessage:
    def __init__(self):
        self.media = []

    def add_media(self, url):
        self.media.append(InputMediaPhoto(media=url))

    def push(self):
        bot.send_media_group(chat_id, self.media)
