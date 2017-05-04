import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables
from socket import TagoRealTime
from actions import Actions
from analysis import Analysis
from dashboards import Dashboards
from devices import Devices
from buckets import Buckets

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Account:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Account-Token': token }
	
    def info(self):
        return requests.get('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def statistics(self, params):
        return requests.get('{api_endpoint}/statistics'.format(api_endpoint=API_TAGO), params=params, headers=self.default_headers).json()
    
    def edit(self, data):
        return requests.put('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def delete(self):
        return requests.delete('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def profileList(self):
        return requests.get('{api_endpoint}/account/profile'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()
    
    def profileCreate(self, data):
        return requests.post('{api_endpoint}/account/profile'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def profileDelete(self, profile_id):
        return requests.delete('{api_endpoint}/account/profile/{profile_id}'.format(api_endpoint=API_TAGO, profile_id=profile_id), headers=self.default_headers).json()

    def tokenList(self):
        return requests.get('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def tokenCreate(self, data):
        return requests.post('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def tokenDelete(self):
        return requests.delete('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def login(self, data):
        return requests.post('{api_endpoint}/account/profile/login'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def getActions(self):
        return Actions(self.token)
    def getAnalysis(self):
        return Analysis(self.token)
    def getDashboards(self):
        return Dashboards(self.token)
    def getDevices(self):
        return Devices(self.token)
