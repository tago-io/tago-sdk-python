import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class Devices:
    def __init__(self, acc_token):
        self.token = acc_token
        self.default_headers = {
            'content-type': 'application/json', 'Account-Token': acc_token}

        return

    # TODO: need review
    def list(self, page=1, fields=['id', 'name'], filter={}, amount=20, orderBy='name,asc', resolveBucketName=False):
        params = {
            'page': page,
            'filter': filter,
            'fields': fields,
            'amount': amount,
            'orderBy': orderBy,
            'resolveBucketName': resolveBucketName
        }
        return requests.get('{api_endpoint}/device'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=json.dumps(params)).json()

        # TODO test it
    def create(self, data):
        data = data if data else {}
        return requests.post('{api_endpoint}/device'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def edit(self, device_id, data):
        data = data if data else {}
        return requests.put('{api_endpoint}/device/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def delete(self, device_id):
        return requests.delete('{api_endpoint}/device/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers).json()

    # TODO: need review

    def tokenList(self, device_id, page=1, amount=20, filter={}, fields=['name', 'token', 'permission'], orderBy='created_at,desc', resolveBucketName=False):
        params = {
            'page': page,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
            'fields': fields,
        }
        return requests.get('{api_endpoint}/device/token/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, params=json.dumps(params)).json()

        # TODO test it
    def tokenCreate(self, device_id, data):
        data = data if data else {}
        data['device'] = device_id

        return requests.post('{api_endpoint}/device/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def tokenDelete(self, token_id):
        return requests.delete('{api_endpoint}/device/token/{token_id}'.format(api_endpoint=API_TAGO, token_id=token_id), headers=self.default_headers).json()

        # TODO test it
    def info(self, device_id):
        # if device id is null, then call list
        if device_id is None or device_id == '':
            return self.list()

        return requests.get('{api_endpoint}/device/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers).json()

        # TODO test it
    def paramSet(self, device_id, data):
        return requests.post('{api_endpoint}/device/{device_id}/params'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO test it
    def paramCreate(self, device_id, data):
        return requests.post('{api_endpoint}/device/{device_id}/params'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO test it
    def paramEdit(self, device_id, param_id, data):
        return requests.put('{api_endpoint}/device/{device_id}/params/{param_id}'.format(api_endpoint=API_TAGO, device_id=device_id, param_id=param_id), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def paramList(self, device_id, sent_status):
        params = {
            'sent_status': sent_status,
        }
        return requests.get('{api_endpoint}/device/{device_id}/params'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, params=json.dumps(params)).json()

    def paramRemove(self, device_id, param_id):
        return requests.delete('{api_endpoint}/device/{device_id}/params/{param_id}'.format(api_endpoint=API_TAGO, device_id=device_id, param_id=param_id), headers=self.default_headers).json()
