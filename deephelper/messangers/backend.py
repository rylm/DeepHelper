"""
This  module including backend for Messangers

"""
from telebot import TeleBot


class TelegramAPI(TeleBot):
    def __init__(self, settings):
        self.chat_id = settings["chat_id"]
        super(TelegramAPI, self).__init__(settings["token"])

    def send_message(self, messages):
        for chat_id in self.chat_id:
            super(TelegramAPI, self).send_message(chat_id, messages)
