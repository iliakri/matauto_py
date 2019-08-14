from fixture.hats import HatsHelper
from fixture.schemas import SchemasHelper


class Application:

    def __init__(self, host):
        self.host = host
        self.hats = HatsHelper(self)
        self.schemas = SchemasHelper(self)


