import requests


class GroupsHelper:
    s = requests.session()

    def __init__(self, app):
        self.app = app

    def get_all_groups(self):
        return self.s.get(self.app.host + '/groups')

    def get_group(self, group_id: int):
        return self.s.get(self.app.host + f'/groups/{group_id}')