import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables
from ..internal import fixFilter

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'


class Network:
    def __init__(self, acc_token):
        self.token = acc_token
        self.default_headers = {
            'content-type': 'application/json', 'Account-Token': acc_token}
        return

    def list(self, page=1, fields=['id', 'name'], filter={}, amount=20, orderBy='name,asc'):
        params = {
            'page': page,
            'fields': fields,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
        }
        params = fixFilter(params, filter)
        return requests.get('{api_endpoint}/integration/network'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=params).json()

    def info(self, network_id, fields=['id', 'name']):
        if network_id is None or network_id == '':
            return self.list()
        params = {'fields': fields}
        return requests.get('{api_endpoint}/integration/network/{network_id}'.format(api_endpoint=API_TAGO), params=params, headers=self.default_headers).json()

    def create(self, data):
        data = data if data else {}
        return requests.post('{api_endpoint}/integration/network'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

    def edit(self, network_id, data):
        data = data if data else {}
        return requests.put('{api_endpoint}/integration/network/{network_id}'.format(api_endpoint=API_TAGO, network_id=network_id), headers=self.default_headers, json=data).json()

    def delete(self, network_id):
        return requests.delete('{api_endpoint}/integration/network/{network_id}'.format(api_endpoint=API_TAGO, network_id=network_id), headers=self.default_headers).json()

    def tokenList(self, network_id, page=1, amount=20, filter={}, fields=['name', 'token', 'created_at'], orderBy='created_at,desc'):
        params = {
            'page': page,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
            'fields': fields,
        }
        params = fixFilter(params, filter)

        return requests.get('{api_endpoint}/integration/network/token/{network_id}'.format(api_endpoint=API_TAGO, network_id=network_id), headers=self.default_headers, params=params).json()

    def tokenCreate(self, network_id, data):
        data = data if data else {}
        data['network'] = network_id
        return requests.post('{api_endpoint}/integration/network/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

    def tokenDelete(self, token):
        return requests.delete('{api_endpoint}/integration/network/token/{token}'.format(api_endpoint=API_TAGO, token=token), headers=self.default_headers).json()
