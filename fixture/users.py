import requests
from allure import step


class UsersHelper:
    s = requests.session()

    def __init__(self, app):
        self.app = app

    @step("Authorize")
    def authorize(self, username, password):
        data = {"username": username, "password": password}
        res = self.s.post(self.app.host + '/users/authorization', json=data)
        self.app.assertion.status_code(res, [201])
        return self.s

    def get_all_users(self, cookies=None):
        return requests.get(self.app.host + '/users', cookies=cookies)

    def create_user(self, user, cookies=None):
        return requests.post(self.app.host + '/users', json=user, cookies=cookies)

    def get_user_by_id(self, user_id: int, cookies=None):
        return requests.get(self.app.host + f'/users/{user_id}', cookies=cookies)

    def update_user(self, user_id: int, user, cookies=None):
        return requests.put(self.app.host + f'/users/{user_id}', json=user, cookies=cookies)

    def delete_user(self, user_id: int, cookies=None):
        return requests.delete(self.app.host + f'/users/{user_id}', cookies=cookies)

    def get_user_if_login(self, cookies=None):
        return requests.get(self.app.host + '/users/authorization', cookies=cookies)

    def login(self, username, password):
        data = {"username": username, "password": password}
        return requests.post(self.app.host + '/users/authorization', json=data)

    def logout(self, cookies=None):
        return requests.delete(self.app.host + '/users/authorization', cookies=cookies)



