import requests


class WorkshopsHelper:

    def __init__(self, app):
        self.app = app

    def get_workshops(self):
        return requests.get(self.app.host + '/workshops/')

    def get_workshop_by_id(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}')

    def get_transporters_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/transporters')

    def get_workers_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers')

    def get_worker_by_workshop(self, workshop_id: int, worker_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}')

    def get_hats_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats')

    def get_zones(self):
        return requests.get(self.app.host + '/workshops/transporters/zones')


