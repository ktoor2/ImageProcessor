import json


class Configs:
    __instance = None

    @staticmethod
    def getInstance():
        if not Configs.__instance:
            Configs()
        return Configs.__instance

    def __init__(self):
        if Configs.__instance:
            raise Exception("This class is a singleton!")
        else:
            self.config = load_configs()
            Configs.__instance = self


def load_configs():
    """
    load config.json and return dictionary
    :return: dictionary
    """
    with open('config/config.json', 'r') as f:
        return json.load(f)
