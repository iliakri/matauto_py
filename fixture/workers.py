import requests


class WorkersHelper:

    def __init__(self, app):
        self.app = app

    def get_worker(self, uid: int):
        return requests.get(self.app.host + f'/workshops/workers/{uid}')

    def get_worker_by_workshop(self, uid: int):
        return requests.get(self.app.host + f'/workshops/{uid}/workers')