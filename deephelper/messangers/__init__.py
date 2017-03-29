"""
All messanger front- and backend
"""
from .backend import TelegramAPI


class Messangers(object):
    """docstring for Messangers."""

    def __init__(self, settings):
        super(Messangers, self).__init__()

        self._messagers_list = []
        set_keys = list(settings.keys())
        ## Future
        # self._message_template = settings.get("message_template")
        # self._input_data_pattern = settings.get("input_pattern")

        # try:
        #     set_keys.remove("message_template")
        #     set_keys.remove("input_pattern")
        # except Exception:
        #     pass
        ## End future

        for mesanger_name in set_keys:
            mesanger_bot = self._build_messanger(mesanger_name,
                                                    settings[mes_name])
            self._messagers_list.append(mesanger_bot)

    def send_messages(self, message):
        """Send messages to all chats"""
        for messanger in self._messagers_list:
            messanger.send_message(message)

    def _build_messanger(self, messanger, settings):
        if messanger == "telegram":
            return TelegramAPI(settings)
        else:
            er_mes = "Sorry, It's not working now with {}"
            raise NotImplementedError(er_mes.format(messanger))
