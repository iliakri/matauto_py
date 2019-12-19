import requests
import json
import allure


class UsersHelper:
    s = requests.session()

    def __init__(self, app):
        self.app = app

    def get_user_by_id(self, user_id: int):
        return requests.get(self.app.host + f'/users/{user_id}')

    def create_user(self, user):
        return requests.post(self.app.host + '/users', json=user)

    def get_user_if_login(self):
        return self.s.get(self.app.host + '/users/authorization')

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self.s.post(self.app.host + '/users/authorization', json=data)

    def logout(self):
        return self.s.delete(self.app.host + '/users/authorization')

    @allure.step("Авторизация")
    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 201:
            allure.attach(json.dumps(res.json(), ensure_ascii=False, indent=2), "Response", "application/json")
        return self.s

57