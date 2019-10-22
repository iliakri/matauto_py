from fixture.hats import HatsHelper
from fixture.schemas import SchemasHelper
from fixture.workers import WorkersHelper
from fixture.workshops import WorkshopsHelper
from fixture.zones import ZonesHelper
from fixture.session import SessionHelper
from fixture.sender import SenderHelper


class Application:

    def __init__(self, host):
        self.host = host
        self.hats = HatsHelper(self)
        self.schemas = SchemasHelper(self)
        self.workers = WorkersHelper(self)
        self.zones = ZonesHelper(self)
        self.workshops = WorkshopsHelper(self)
        self.session = SessionHelper(self)
        self.sender = SenderHelper(self)



