from fixture.assertion import AssertionHelper
from fixture.hats import HatsHelper
from fixture.schemas import SchemasHelper
from fixture.workers import WorkersHelper
from fixture.workshops import WorkshopsHelper
from fixture.zones import ZonesHelper
from fixture.users import UsersHelper
from fixture.sender import SenderHelper


class Application:

    def __init__(self, host):
        self.host = host
        self.hats = HatsHelper(self)
        self.schemas = SchemasHelper(self)
        self.workers = WorkersHelper(self)
        self.zones = ZonesHelper(self)
        self.workshops = WorkshopsHelper(self)
        self.users = UsersHelper(self)
        self.sender = SenderHelper(self)
        self.assertion = AssertionHelper(self)



