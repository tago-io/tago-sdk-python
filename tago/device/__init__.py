import requests
import json
import os

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Device:
    # needs to implement details
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': token }

    # tested
    def info(self):
        return requests.get('{api_endpoint}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # tested
    def insert(self, data):
        data = data if data else {}
        return requests.post('{api_endpoint}/data'.format(api_endpoint = API_TAGO), headers = self.default_headers, data=json.dumps(data)).json()

    # tested
    def find(self, query_obj):
        query_obj = query_obj if query_obj else {}
        return requests.get('{api_endpoint}/data'.format(api_endpoint = API_TAGO), headers=self.default_headers, params = json.dumps(query_obj)).json()

    # to do
    def remove(self, args):
        return self.api_data_delete(query)
    
    # need testing
    def getParams(self, sent_status):
        return requests.get('{api_endpoint}/device/params'.format(api_endpoint=API_TAGO), params=json.dumps(sent_status), headers=self.default_headers).json()
    
    # need testing
    def markParam(self, param_id):
        return requests.put('{api_endpoint}/device/params/{param_id}'.format(api_endpoint=API_TAGO,param_id=param_id), headers=self.default_headers).json()
