import requests


class GroupsHelper:

    def __init__(self, app):
        self.app = app

    def get_all_groups(self, cookies=None):
        return requests.get(self.app.host + '/groups', cookies=cookies)

    def get_group_by_id(self, group_id: int, cookies=None):
        return requests.get(self.app.host + f'/groups/{group_id}', cookies=cookies)