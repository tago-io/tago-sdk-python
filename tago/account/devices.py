import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Devices:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': token }

        return

    def list(self):
        return requests.get('{api_endpoint}/device'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()
