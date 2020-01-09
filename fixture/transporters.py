import requests


class TransportersHelper:

    def __init__(self, app):
        self.app = app

    def get_normative_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/normative')

    def create_normative(self, transporter_id: int, production_id: int, tray_weight: float, productivity_count: float):
        data = {"production_id": production_id, "tray_weight": tray_weight, "productivity_count": productivity_count}
        return requests.put(self.app.host + f'/transporters/{transporter_id}/normative', json=data)

    def get_shifts_by_transporter(self, transporter_id: int, start_date, end_date=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/transporters/{transporter_id}/shifts/workers', params=payload)

    def get_cameras_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/cameras')

    def get_zones_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/zones')

    def get_zones_status_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/zones/status')

    def get_productions_by_transporter(self, transporter_id: int):
        return requests.get(self.app.host + f'/transporters/{transporter_id}/productions')

    def get_transporters_by_id(self, transporter_id: int):
        return requests.get(self.app.host + f'/transporters/{transporter_id}')

    def update_transporters_by_id(self, transporter_id: int, main_production_id: int, extra_production_id: int):
        data = {"main_production_id": main_production_id, "extra_production_id": extra_production_id}
        return requests.get(self.app.host + f'/transporters/{transporter_id}', json=data)

    def get_workers_status_by_transporters(self, transporter_id: int, start_date: str, end_date=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/transporters/{transporter_id}/workers/status', params=payload)

    def download_report_by_transporter(self, transporter_id: int, start_date, end_date=None):
        payload = {'start_date': start_date, 'end_date': end_date}
        return requests.get(self.app.host + f'/transporters/{transporter_id}/download', params=payload)

