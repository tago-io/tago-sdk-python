import requests
import json
import os

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Connector:
    # needs to implement details
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Connector-Token': token }

    # needs to test
    def info(self, data):
        return requests.get('{api_endpoint}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # needs to test
    def resolveToken(self, serie_number, authorization):
        url = '{api_endpoint}/connector/resolve/{serie_number}'
        if authorization:
            url += '{url}/{authorization}'
        return requests.get(url.format(api_endpoint = API_TAGO), headers=self.default_headers).json()
