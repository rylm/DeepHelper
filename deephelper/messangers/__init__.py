"""
All messanger front- and backend
"""
from .backend import TelegramAPI


class Messangers(object):
    """docstring for Messangers."""

    def __init__(self, settings):
        super(Messangers, self).__init__()

        self._messagers_list = []
        self._message_template = settings.get("message_template")
        self._input_data_pattern = settings.get("input_pattern")
        set_keys = list(settings.keys())

        try:
            set_keys.remove("message_template")
            set_keys.remove("input_pattern")
        except Exception:
            pass

        for mes_name in set_keys:
            mes_bot = self._build_messanger(mes_name, settings[mes_name])
            self._messagers_list.append(mes_bot)

    def send_messages(self, *argv):
        """Send messages to all chats"""
        if self._message_template:

            if self._input_data_pattern:
                message_data = {}
                for key, arg in zip(self._input_data_pattern, argv):
                    message_data[key] = arg

                message = self._message_template.format(**message_data)
            else:
                message = self._message_template.format(*argv)

        else:
            message = str(argv[0])

        for messanger in self._messagers_list:
            messanger.send_message(message)

    def _build_messanger(self, messanger, settings):
        if messanger == "telegram":
            return TelegramAPI(settings)
        else:
            er_mes = "Sorry, It's not working with {}"
            raise NotImplementedError(er_mes.format(messanger))
