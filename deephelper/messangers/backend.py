"""
This  module including backend for Messangers

"""
import telebot


class TelegramAPI(telebot.TeleBot):
    def __init__(self, settings):
        self.chat_ids = settings["chat_id"]
        super(TelegramAPI, self).__init__(settings["token"])

    def send_messages(self, messages):
        for chat_id in self.chat_id:
            super(self, TelegramAPI).send_messages(chat_id, messages)
