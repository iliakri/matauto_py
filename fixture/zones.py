import requests


class ZonesHelper:

    def __init__(self, app):
        self.app = app

    def get_zones(self):
        return requests.get(self.app.host + '/workshops/transporters/zones')