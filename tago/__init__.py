from device import Device
from analysis import Analysis
from account import Account
from services import Services
from extra import Extra
from connector import Connector

class Tago:
    def __init__(self, token):
        # Pending functions
        self.device = Device(token)
        self.connector = Connector(token)

        self.analysis = Analysis(analysis, token)
        self.account = Account(token)
        self.services = Services(token)
        # Token here corresponds to Third Party API_KEY
        self.extra = Extra(token)
