"""
This  module including backend for Messangers

"""
from telebot import TeleBot


class TelegramAPI(TeleBot, object):
    def __init__(self, settings):
        self.chat_id = settings["chat_id"]
        super(TelegramAPI, self).__init__(settings["token"])

    def send_message(self, messages):
        for chat_id in self.chat_id:
            super(TelegramAPI, self).send_message(chat_id, messages)

def template_settings(base_template=None, settings=None):
    template = {}
    if base_template:

        template["standart"] = base_template
        base_pattern = base_template["input_pattern"]
    if settings:
        for key in settings.keys():
            if isinstance(settings[key], str):
                template[key]

