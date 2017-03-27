import requests
import json
import os
from socket import TagoRealTime

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Device:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': token }

    def handle_url(self, id):
        if id:
            url = '{api_endpoint}/data/{id}'.format(api_endpoint=API_TAGO,id=id)
        else:
            url = '{api_endpoint}/data'.format(api_endpoint=API_TAGO,id=id)
        return url

    def api_data_post(self, data):
        return requests.post(self.handle_url(id=False), data=json.dumps(data), headers=self.default_headers).json()

    def api_data_get(self, query):
        return requests.get(self.handle_url(id=False), params=query, headers=self.default_headers).json()

    def api_data_delete(self, id):
        return requests.delete(self.handle_url(id=id), headers=self.default_headers).json()

    def info(self, data):
        return requests.get('{api_endpoint}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def insert(self, data):
        return self.api_data_post(data)

    def find(self, query):
        return self.api_data_get(query)

    def remove(self, id=False):
        return self.api_data_delete(id)

    def getParams(self, sent_status):
        return requests.get('{api_endpoint}/device/params'.format(api_endpoint=API_TAGO), params=sent_status, headers=self.default_headers).json()

    def markParam(self, param_id):
        return requests.put('{api_endpoint}/device/params/{id}'.format(api_endpoint=API_TAGO,id=param_id), headers=self.default_headers).json()

    def listening(self, callback, wait=False):
        return TagoRealTime(REALTIME, self.token, callback).listening(wait)
