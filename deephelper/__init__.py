#!/bin/python3

import json
import importlib
from messanger import Messangers


class DeepHelper(object):
    """Main DeepHelper class"""
    def __init__(self, settings=None):
        """ settings: dict or filename """
        super(DeepHelper, self).__init__()
        if isinstance(settings, str):
            with open(settings) as fp:
                settings = json.load(fp)

        if settings:
            if settings.get("messangers"):
                self.messangers = Messangers(settings["messangers"])
            if settings.get("dropbox"):
                import dropbox
                token = settings["dropbox"]["token"]
                self.dropbox = dropbox.client.DropboxClient(token)


    def prints(self, *argv):
        self.messangers.send_messages(*argv)

    def to_dropbox(self, filename):
        with open(filename, "rb") as fp:
            return self.dropbox.put_file('/' + filename, fp)
