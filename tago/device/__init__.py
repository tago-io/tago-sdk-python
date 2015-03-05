import requests
import json
import os
from socket import TagoRealTime

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io/v0/'
REALTIME = os.environ.get('TAGO_REALTIME') or 'realtime.tago.io'
REALTIME_PORT = int(os.environ.get('TAGO_REALTIME_PORT') or 80)


class Device:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': token }

    def api_data_post(self, data):
        url = API_TAGO + 'data/'
        return requests.post(url, data=json.dumps(data), headers=self.default_headers).json()

    def api_data_update(self, id, data):
        url = API_TAGO + 'data/' + id
        return requests.put(url, data=json.dumps(data), headers=self.default_headers).json()

    def api_data_delete(self, id):
        url = API_TAGO + 'data/' + id
        return requests.delete(url, headers=self.default_headers).json()

    def insert(self, data):
        return self.api_data_post(data)

    def update(self, id, data):
        return self.api_data_update(id, data)

    def delete(self, id):
        return self.api_data_delete(id)

    def listening(self, callback, wait=False):
        return TagoRealTime(REALTIME, REALTIME_PORT, self.token, callback).listening(wait)
