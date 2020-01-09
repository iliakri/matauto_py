import requests


class WorkshopsHelper:

    def __init__(self, app):
        self.app = app

    def get_workshops(self):
        return requests.get(self.app.host + '/workshops')

    def get_workshop_by_id(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}')

    def get_transporters_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/transporters')

    def get_workers_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers')

    def create_worker_by_workshop(self, workshop_id: int, worker):
        return requests.post(self.app.host + f'/workshops/{workshop_id}/workers', json=worker)

    def get_worker_by_workshop(self, workshop_id: int, worker_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}')

    def put_worker_by_workshop(self, workshop_id: int, worker_id: int, name: str, clock_num: str):
        data = {"name": name, "clock_num": clock_num}
        return requests.put(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}', json=data)

    def delete_worker_by_workshop(self, workshop_id: int, worker_id: int):
        return requests.delete(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}')

    def get_workers_with_paginated(self, workshop_id: int, page: int, per_page: int, field: str, direction: str, search: str):
        payload = {'page': page, 'per_page': per_page, 'field': field, 'direction': direction, 'search': search}
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers/pages', params=payload)

    def get_hats_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats')

    def download_hats_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats/download')

    def get_shift_by_id(self, shift_id: int):
        return requests.get(self.app.host + f'/shifts/{shift_id}')




