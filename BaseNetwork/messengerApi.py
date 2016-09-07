import telebot


class BotAPI:
    def __init__(self, api_token):
        self.telegram_token = api_token
        self.telegram = telebot.TeleBot(self.telegram_token)
        self.chats_id = [145718567]

    def send_messages(self, message):
        self.telegram.send_message(self.chats_id[0], message)
        print(message)
