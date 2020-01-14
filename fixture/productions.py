import requests


class ProductionsHelper:

    def __init__(self, app):
        self.app = app

    def get_all_productions(self, cookies=None):
        return requests.get(self.app.host + '/productions', cookies=cookies)

    def get_production_by_id(self, production_id: int, cookies=None):
        return requests.get(self.app.host + f'/productions/{production_id}', cookies=cookies)

    def update_production_by_id(self, production_id: int, cookies=None):
        data = {"name": "string", "id": 1}
        return requests.patch(self.app.host + f'/productions/{production_id}', cookies=cookies, json=data)
