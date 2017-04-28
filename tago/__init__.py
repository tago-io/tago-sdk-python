from device import Device
from analysis import Analysis
from account import Account
class Tago:
    def __init__(self, token):
        self.device = Device(token)
        self.analysis = Analysis(analysis, token)
        self.account = Account(token)
