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

text = """
Паблик не умер.
Отчёт за 2 недели.
Жестко нарешал задачи с литкода получилось примерно 30 штук.
13 средних и 17 легких. Сейчас двигаюсь по роадмапе NeetCode: https://neetcode.io/roadmap и все советую кто хочет начать решать. Из этого списка я решил 21 задачу и остановился на разделе скользящего окна и связанные списки мне не поддаются. Как решу половину из этих трех разделов перейду в деревья. Иногда залетю на соревнования с кодфорса и от литкода, но там мне сложно, но есть какой-то стимул быстро думать.

Ботаю английский язык.
Читаю этот ресурс - http://begin-english.ru/samouchitel
Выписал себе сколько слов я знаю из 1000 самых популярных - https://www.dropbox.com/s/pt7a734rriiocza/1000 most u.. (эксель таблица)
Иногда отдельно смотрю видики по словам, смотрю видосы с субтитрами и еще начал смотреть такой формат: https://www.youtube.com/watch?v=sicBNCh-Yxc&t=3s... Это чота типа разбора диалогов из сериалов с помощью автора, помогает узнать слова которых нет в таблице выше.
Оценивать себя буду уже ближе к экзамену щас я слабый.

Алгоритмы.
Готовлю билеты по алгоритмам, написал Дейкстру, разобрался с представлениями в памяти, написал алгоритмы поиска минимального оставного дерева(Прима, Крускала), написал Recursive Backtracking для построения лабиринта. Муравьев я уже писал. Буду разбираться 59-67 вопросами, особенно интересует паралелизация сортировки.

Итоги: потихоньку помаленьку двигаюсь к цели. У меня там еще в запасе неделя буду активно нагонять.
"""
b = BotMessage()
b.add_media('https://sun9-3.userapi.com/impg/5ksiNEDIA7JAE3ZkAAe51TT_0hZ0gp0uuZzH8w/fZu4O9Zb9rg.jpg?size=1114x824&quality=96&sign=065f49377c4aeedb13a0433a5cc3d6be&type=album', caption=text)
b.add_media('https://sun9-3.userapi.com/impg/5ksiNEDIA7JAE3ZkAAe51TT_0hZ0gp0uuZzH8w/fZu4O9Zb9rg.jpg?size=1114x824&quality=96&sign=065f49377c4aeedb13a0433a5cc3d6be&type=album', caption=text)
b.push()