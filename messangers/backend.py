

class Messangers(object):
    """docstring for Messangers."""
    def __init__(self, messangers_settings={}):
        super(Messangers, self).__init__()
        self._messagers_list = []

        if len(messangers_settings.keys()) > 0:
            for messanger in messangers_settings.keys():
                self._messagers_list.append(
                            build_messanger(messanger,
                                            messangers_settings[messanger]))

    def send_messages(self, messages):
        for messanger in self._messagers_list:
            messanger.send_messages(messages)


def build_messanger(messanger, settings):
    raise NotImplementedError("Sorry, It's not ready for use")
