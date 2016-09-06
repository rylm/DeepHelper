import time
from BaseNetwork import BaseNetwork


class Net(BaseNetwork):
    def __init__(self, name, **kwargs):
        self.name = name
        super(Net, self).__init__(**kwargs)

    def train(self):
        for i in range(10):
            self.send_messages(time.ctime())
