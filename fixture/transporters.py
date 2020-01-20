import requests


class TransportersHelper:

    def __init__(self, app):
        self.app = app

    def get_normative_by_transporter(self, transporter_id: int, cookies=None):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/normative', cookies=cookies)

    def create_normative(self, transporter_id: int, production_id: int, tray_weight: float, productivity_count: float, cookies=None):
        data = {"production_id": production_id, "tray_weight": tray_weight, "productivity_count": productivity_count}
        return requests.put(self.app.host + f'/transporters/{transporter_id}/normative', json=data, cookies=cookies)

    def get_shifts_by_transporter(self, transporter_id: int, start_date, end_date=None, cookies=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/transporters/{transporter_id}/shifts/workers', params=payload, cookies=cookies)

    def get_cameras_by_transporter(self, transporter_id: int, cookies=None):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/cameras', cookies=cookies)

    def get_zones_by_transporter(self, transporter_id: int, cookies=None):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/zones', cookies=cookies)

    def get_zones_status_by_transporter(self, transporter_id: int, cookies=None):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/zones/status', cookies=cookies)

    def get_productions_by_transporter(self, transporter_id: int, cookies=None):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/productions', cookies=cookies)

    def add_production_to_transporter(self, transporter_id: int, production_id: int, cookies=None):
        return requests.post(self.app.host + f'/transporters/{transporter_id}/productions/{production_id}', cookies=cookies)

    def del_production_from_transporter(self, transporter_id: int, production_id: int, cookies=None):
        return requests.delete(self.app.host + f'/transporters/{transporter_id}/productions/{production_id}', cookies=cookies)

    def get_transporters_by_id(self, transporter_id: int, cookies=None):
        return requests.get(self.app.host + f'/transporters/{transporter_id}', cookies=cookies)

    def update_transporters_by_id(self, transporter_id: int, main_production_id: int, extra_production_id: int, cookies=None):
        data = {"main_production_id": main_production_id, "extra_production_id": extra_production_id}
        return requests.get(self.app.host + f'/transporters/{transporter_id}', json=data, cookies=cookies)

    def get_workers_status_by_transporters(self, transporter_id: int, start_date: str, end_date=None, cookies=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/transporters/{transporter_id}/workers/status', params=payload, cookies=cookies)

    def download_report_by_transporter(self, transporter_id: int, start_date, end_date=None, cookies=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/transporters/{transporter_id}/download', params=payload, cookies=cookies)

