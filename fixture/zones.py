import requests


class ZonesHelper:

    def __init__(self, app):
        self.app = app

    def get_zones(self):
        return requests.get(self.app.host + '/workshops/transporters/zones')

    def get_zones_for_conveyor(self, uid: int):
        return requests.get(self.app.host + f'/workshops/transporters/{uid}/zones')