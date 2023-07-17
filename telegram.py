import telebot
from telebot.types import InputMediaPhoto
from config import TOKEN_TG

bot = telebot.TeleBot(TOKEN_TG)
chat_id = "@iwced"


class BotMessage:
    def __init__(self):
        self.media = []

    def add_media(self, url, caption=None):
        if self.media:
            self.media.append(InputMediaPhoto(media=url))
        else:
            self.media.append(InputMediaPhoto(media=url, caption=caption))

    def push(self):
        bot.send_media_group(chat_id, self.media)
