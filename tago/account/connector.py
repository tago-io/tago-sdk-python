import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'


class Connector:
    def __init__(self, acc_token):
        self.token = acc_token
        self.default_headers = {
            'content-type': 'application/json', 'Account-Token': acc_token}

        return

    # TODO: need review
    def list(self, page=1, fields=['id', 'name'], filter={}, amount=20, orderBy='name,asc'):
        params = {
            'page': page,
            'fields': fields,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
        }
        return requests.get('{api_endpoint}/connector'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(params)).json()

        # TODO need review
    def info(self, connector_id, no_parent=False):
        if connector_id is None or connector_id == '':
            return self.list()
        return requests.get('{api_endpoint}/connector/{connector_id}'.format(api_endpoint=API_TAGO, connector_id=connector_id), headers=self.default_headers).json()

        # TODO test it
    def create(self, data):
        data = data if data else {}
        return requests.post('{api_endpoint}/connector'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def edit(self, connector_id, data):
        data = data if data else {}
        return requests.put('{api_endpoint}/connector/{connector_id}'.format(api_endpoint=API_TAGO, connector_id=connector_id), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def delete(self, connector_id):
        return requests.delete('{api_endpoint}/connector/{connector_id}'.format(api_endpoint=API_TAGO, connector_id=connector_id), headers=self.default_headers).json()

    # TODO review it
    def tokenList(self, connector_id, page=1, amount=20, filter={}, fields=['name', 'token', 'created_at'], orderBy='created_at,desc'):
        params = {
            'page': page,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
            'fields': fields,
        }
        return requests.get('{api_endpoint}/connector/token/{connector_id}'.format(api_endpoint=API_TAGO, connector_id=connector_id), headers=self.default_headers, params=json.dumps(params)).json()

        # TODO need review
    def tokenCreate(self, connector_id, data):
        data = data if data else {}
        data['connector'] = connector_id
        return requests.post('{api_endpoint}/connector/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

        # TODO test it
    def tokenDelete(self, token):
        return requests.delete('{api_endpoint}/connector/token/{token}'.format(api_endpoint=API_TAGO, token=token), headers=self.default_headers).json()
