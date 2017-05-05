from device import Device
from analysis import Analysis
from account import Account
from services import Services
from extra import Extra

class Tago:
    def __init__(self, token):
        self.device = Device(token)
        self.analysis = Analysis(analysis, token)
        self.account = Account(token)
        self.services = Services(token)
        # Token here corresponds to Third Party API_KEY
        self.extra = Extra(token)
