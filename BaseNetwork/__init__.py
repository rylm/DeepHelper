from .messengerApi import BotAPI


class BaseNetwork(object):
    def __init__(self, **kwargs):
        self.telegram_api = kwargs.get("BotAPI", BotAPI)(kwargs.get("messengers_token", None))

        if "training_messages_template" in kwargs.keys():
            self.training_messages_template = kwargs["training_messages_template"]

            if "output_pattern" not in kwargs.keys():
                raise KeyError("Not output pattern in settings for {}".format(self.training_messages_template))
            self.output_pattern = kwargs["output_pattern"]

        else:
            self.training_messages_template = '{}'

    def send_messages(self, *message):
        out_message = {}
        for key, value in zip(self.output_pattern, message):
            out_message.update({key: value})

        message = self.training_messages_template.format(*message, **out_message)
        
        self.telegram_api.send_messages(message)
