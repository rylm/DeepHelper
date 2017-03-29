#!/bin/python3

import json
from .messangers import Messangers
import dropbox

class DeepHelper(object):
    """Main DeepHelper class"""
    def __init__(self, settings=None):
        """ settings: dict or json-filename """
        super(DeepHelper, self).__init__()
        if isinstance(settings, str):
            with open(settings) as fp:
                settings = json.load(fp)

        if settings:
            if settings.get("messangers"):
                self.messangers = Messangers(settings["messangers"])
            else:
                self.messangers = None

            if settings.get("dropbox"):
                token = settings["dropbox"]["token"]
                self.dropbox = dropbox.client.DropboxClient(token)
            else:
                self.dropbox = None


    def prints(self, message):
        assert self.messangers, "Not setting messangers"
        self.messangers.send_messages(message)

    def send_messages(self, message):
        assert self.messangers, "Not setting messangers"
        self.messangers.send_messages(message)

    def to_dropbox(self, filename):
        assert self.dropbox, "Not setting dropbox"
        with open(filename, "rb") as fp:
            return self.dropbox.put_file('/' + filename, fp.read())
