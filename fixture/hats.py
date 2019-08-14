
class HatsHelper:

    def __init__(self, app):
        self.app = app

    def get_hats(self):
        return self.app.s.get(self.app.host + '/hats')

    def get_hats_by_workshop(self, uid: int):
        return self.app.s.get(self.app.host + f'/hats/workshops/{uid}')
