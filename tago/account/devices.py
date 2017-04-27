import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Devices:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Account-Token': token }

        return

    def list(self):
        return requests.get('{api_endpoint}/device'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def create(self, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/device'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def edit(self, device_id, data):
    	data = data if data else {}
    	return requests.put('{api_endpoint}/device/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, data=json.dumps(data)).json()

    def delete(self, device_id):
    	return requests.delete('{api_endpoint}/device/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers).json()

    def tokenList(self, device_id):
    	return requests.get('{api_endpoint}/device/token/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers).json()

    def tokenCreate(self, device_id, data):
    	data = data if data else {}
    	data['device'] = device_id

    	return requests.post('{api_endpoint}/device/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def tokenDelete(self, token_id):
    	return requests.delete('{api_endpoint}/device/token/{token_id}'.format(api_endpoint=API_TAGO, token_id=token_id), headers=self.default_headers).json()

    def info(self, device_id):
    	# if device id is null, then call list
    	if device_id is None or device_id == '':
	    return self.list()

    	return requests.get('{api_endpoint}/device/{device_id}'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers).json()

    def paramSet(self, device_id, data):
        return requests.post('{api_endpoint}/device/{device_id}/params'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, data=json.dumps(data)).json()

    def paramList(self, device_id, sent_status):
    	# not sure what the key should be b/c they do not put a key in JS method, but i tried this for now
    	# params = {}
    	# params['sent_status'] = sent_status

    	# looking at the device/__init__.py they just pass sent_status as the params in the request...
    	return requests.get('{api_endpoint}/device/{device_id}/params'.format(api_endpoint=API_TAGO, device_id=device_id), headers=self.default_headers, params=sent_status).json()


    def paramRemove(self, device_id, param_id):
    	return requests.delete('{api_endpoint}/device/{device_id}/params/{param_id}'.format(api_endpoint=API_TAGO, device_id=device_id, param_id=param_id), headers=self.default_headers).json()

    def factory(self):
        return self.create({'name': 'TestDeviceName'})

