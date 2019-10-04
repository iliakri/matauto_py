import requests
import json


class SessionHelper:
    s = requests.session()

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.s.post(self.app.host + '/users/authorization', json=data)

    def logout(self):
        return self.s.delete(self.app.host + '/users/authorization')

    def get_user_if_login(self):
        return self.s.get(self.app.host + '/users/authorization')

    def login_required(self):
        return self.s.put(self.app.host + '/users/authorization')

    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 201:
            print(json.dumps(res.json(), ensure_ascii=False, indent=2))
        return self.s

