import json

class BaseConfig:
    
    data = {}

    @staticmethod
    def load(filename = None):
        global data
        with open("config.json" if filename is None else filename) as file:
            data = json.load(file)

    @staticmethod
    def get_login(reload = False):
        if reload: 
             load()

        return data["login"]

    @staticmethod
    def is_test(reload = False):
        if reload: 
            load()

        return data["test"] == 1

class BaseActionResult:
    def __init__(self, ok = True, error = "", data = None):
        self.error = error
        self.ok = ok
        self.data = data
