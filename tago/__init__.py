from device import Device
from analysis import Analysis
from services import Services

class Tago:
    def __init__(self, token):
        self.device = Device(token)
        self.analysis = Analysis(analysis, token)
        self.services = Services(token)