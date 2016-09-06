import importlib
import json


def train_network(settings):
    v = importlib.import_module(settings["network_file"])
    net = getattr(v, settings["network_class"])

    n = net("ufuuubu", **settings)
    n.train()


if __name__ == "__main__":
    import argparse

    pars = argparse.ArgumentParser()
    pars.add_argument("-s", "--settings_file", nargs="?", default=None)

    arg = pars.parse_args()
    if not (arg.settings_file is None):
        settings = json.load(open(arg.settings_file))
    else:
        raise pars.error("Don't using with 0 arguments")

    train_network(settings)
