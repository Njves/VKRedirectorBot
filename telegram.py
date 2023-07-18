"""
Module that implements Telegram bot api
"""
import telebot
from telebot.types import InputMediaPhoto
from config import TOKEN_TG

bot = telebot.TeleBot(TOKEN_TG)
chat_id = "@iwced"


class BotMessage:
    """
    Collects media files and sends them to the chat
    """

    def __init__(self):
        self.media = []
        self.overflowed_part = ''

    def add_media(self, url, caption=None):
        """
        Collects media to the list
        :param url: media url
        :param caption: caption
        """
        if self.media:
            self.media.append(InputMediaPhoto(media=url))
        else:
            if len(caption) <= 1024:
                self.media.append(InputMediaPhoto(media=url, caption=caption))
            else:
                new_text = ''
                end = ''
                for t in caption.splitlines():
                    if len(new_text + (t + '\n')) <= 1024:
                        new_text += (t + '\n')
                    else:
                        end += (t + '\n')
                self.media.append(InputMediaPhoto(media=url, caption=new_text))
                self.overflowed_part = end

    def push(self):
        """
        Sends message to chat
        :return:
        """
        bot.send_media_group(chat_id, self.media)
        if self.overflowed_part:
            bot.send_message(chat_id, self.overflowed_part)
