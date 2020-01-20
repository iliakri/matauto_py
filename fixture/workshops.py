import requests


class WorkshopsHelper:

    def __init__(self, app):
        self.app = app

    def get_workshops(self, cookies=None):
        return requests.get(self.app.host + '/workshops', cookies=cookies)

    def get_workshop_by_id(self, workshop_id: int, cookies=None):
        return requests.get(self.app.host + f'/workshops/{workshop_id}', cookies=cookies)

    def get_transporters_by_workshop(self, workshop_id: int, cookies=None):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/transporters', cookies=cookies)

    def get_workers_by_workshop(self, workshop_id: int, cookies=None):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers', cookies=cookies)

    def create_worker_by_workshop(self, workshop_id: int, worker, cookies=None):
        return requests.post(self.app.host + f'/workshops/{workshop_id}/workers', json=worker, cookies=cookies)

    def get_worker_by_workshop(self, workshop_id: int, worker_id: int, cookies=None):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}', cookies=cookies)

    def put_worker_by_workshop(self, workshop_id: int, worker_id: int, name: str, clock_num: str, cookies=None):
        data = {"name": name, "clock_num": clock_num}
        return requests.put(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}', json=data, cookies=cookies)

    def delete_worker_by_workshop(self, workshop_id: int, worker_id: int, cookies=None):
        return requests.delete(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}', cookies=cookies)

    def get_workers_with_paginated(self, workshop_id: int, page: int, page_size: int, direction: str, field: str, search: str, cookies=None):
        payload = {'page': page, 'page_size': page_size, 'direction': direction, 'field': field, 'search': search}
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers', params=payload, cookies=cookies)

    def get_hats_by_workshop(self, workshop_id: int, cookies=None):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats', cookies=cookies)

    def download_hats_by_workshop(self, workshop_id: int, cookies=None):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats/download', cookies=cookies)

    #################
    # Shift         #
    #################
    def get_shift_by_id(self, shift_id: int, cookies=None):
        return requests.get(self.app.host + f'/shifts/{shift_id}', cookies=cookies)




