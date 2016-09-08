import telebot


class BotAPI:
    def __init__(self, api_token):
        self.telegram_token = api_token
        self.telegram = telebot.TeleBot(self.telegram_token)
        self.chats_id = []

    def send_messages(self, message):
        for chat_id in self.chats_id:
            self.telegram.send_message(chat_id, message)
        print(message)
