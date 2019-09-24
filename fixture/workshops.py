import requests


class WorkshopsHelper:

    def __init__(self, app):
        self.app = app

    def get_workshops(self):
        return requests.get(self.app.host + '/workshops/')

    def get_workshop_by_id(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}')

    def get_normative(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/normative')

    def create_normative(self, transporter_id: int, production_id: int, tray_weight: float, productivity_count: float):
        data = {"production_id": production_id, "tray_weight": tray_weight, "productivity_count": productivity_count}
        return requests.put(self.app.host + f'/workshops/transporters/{transporter_id}/normative', json=data)

    def get_shift_by_transporter(self, transporter_id: int, start_date, end_date=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/shifts/workers', params=payload)

    def get_shift_by_id(self, shift_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/shifts/{shift_id}')

    def get_cameras_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/cameras')

    def get_zones_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/zones')

    def get_status_of_zones_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/zones/status')

    def get_productions_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/productions')

    def get_transporters_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/transporters')

    def get_transporters_by_id(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}')

    def get_workers_status_by_workshop(self, transporter_id: int, start_date: str, end_date=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/workers/status', params=payload)

    def get_workers_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers')

    def create_worker_by_workshop(self, workshop_id: int, worker):
        # data = {"name": name, "clock_num": clock_num}
        return requests.post(self.app.host + f'/workshops/{workshop_id}/workers', json=worker)

    def get_worker_by_workshop(self, workshop_id: int, worker_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}')

    def put_worker_by_workshop(self, workshop_id: int, worker_id: int, name: str, clock_num: str):
        data = {"name": name, "clock_num": clock_num}
        return requests.put(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}', json=data)

    def delete_worker_by_workshop(self, workshop_id: int, worker_id: int):
        return requests.delete(self.app.host + f'/workshops/{workshop_id}/workers/{worker_id}')

    def get_workers_with_paginated(self, workshop_id: int, page: int, per_page: int, field: str, direction: str,
                                   search: str):
        payload = {'page': page, 'per_page': per_page, 'field': field, 'direction': direction, 'search': search}
        return requests.get(self.app.host + f'/workshops/{workshop_id}/workers/pages', params=payload)

    def get_hats_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats')

    def download_hats_by_workshop(self, workshop_id: int):
        return requests.get(self.app.host + f'/workshops/{workshop_id}/hats/download')

    def download_report_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/workshops/transporters/{transporter_id}/download')