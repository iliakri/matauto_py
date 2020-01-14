from fixture.assertion import AssertionHelper
from fixture.groups import GroupsHelper
from fixture.productions import ProductionsHelper
from fixture.schemas import SchemasHelper
from fixture.workshops import WorkshopsHelper
from fixture.users import UsersHelper
from fixture.sender import SenderHelper
from fixture.transporters import TransportersHelper


class Application:

    def __init__(self, host):
        self.host = host
        self.schemas = SchemasHelper(self)
        self.workshops = WorkshopsHelper(self)
        self.users = UsersHelper(self)
        self.sender = SenderHelper(self)
        self.assertion = AssertionHelper(self)
        self.groups = GroupsHelper(self)
        self.transporters = TransportersHelper(self)
        self.productions = ProductionsHelper(self)

