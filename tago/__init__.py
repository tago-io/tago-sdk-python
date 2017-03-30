from device import Device
from analysis import Analysis

class Tago:
    def __init__(self, token):
        self.device = Device(token)
        self.analysis = Analysis(analysis, token)
