import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Actions:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Account-Token': token }

        return

    def list(self):
        return requests.get('{api_endpoint}/action'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def create(self, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/action'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def edit(self, action_id, data):
    	data = data if data else {}
    	return requests.put('{api_endpoint}/action/{action_id}'.format(api_endpoint=API_TAGO, action_id=action_id), headers=self.default_headers, data=json.dumps(data)).json()

    def delete(self, action_id):
    	return requests.delete('{api_endpoint}/action/{action_id}'.format(api_endpoint=API_TAGO, action_id=action_id), headers=self.default_headers).json()

    def info(self, action_id):
    	if action_id is None or action_id == '':
	    	return self.list()

    	return requests.get('{api_endpoint}/action/{action_id}'.format(api_endpoint=API_TAGO, action_id=action_id), headers=self.default_headers).json()
