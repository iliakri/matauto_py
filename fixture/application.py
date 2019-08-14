import requests
from fixture.hats import HatsHelper


class Application:
    s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host
        self.hats = HatsHelper(self)

