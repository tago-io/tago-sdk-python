from .device import Device
from .analysis import Analysis
from .account import Account
from .services import Services
from .extra import Extra
from .connector import Connector
from .authorization import Authorization
from .run_user import RunUser

class Tago:
    def __init__(self, token):
        # Pending functions
        self.account = Account(token)
        # self.analysis = Analysis(analysis, token)
        self.authorization = Authorization(token)
        self.connector = Connector(token)
        self.device = Device(token)
        self.extra = Extra(token)
        self.run_user = RunUser(token)
        self.services = Services(token)
