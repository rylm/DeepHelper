class BotAPI:
    def __init__(self, api_token):
        self.api_token = api_token

    @staticmethod
    def send_messages(message):
        print(message)
