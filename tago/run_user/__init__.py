import requests
import json
import os
from socket import TagoRealTime

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class RunUser:
    # needs to implement details
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': token }

    # TODO: test it
    def info(self, tagoRunURL):
        return requests.get('{api_endpoint}/run/{tagoRunURL}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: create this function
    def editInfo(self, tagoRunURL, changes):
        return requests.put('{api_endpoint}/run/{tagoRunURL}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: create this function
    def create(self, tagoRunURL, newUserObj):
        @staticmethod
        # return requests.post(self.handle_url(id=False), data=json.dumps(data), headers=self.default_headers).json()

    # email and password should be in a object?
    def login(self, tagoRunURL, email, password):
        @staticmethod

    # TODO: test it
    def confirmUser(self, tagoRunURL, token):
        @staticmethod
        return requests.get('{api_endpoint}/run/{tagoRunURL}/confirm/{token}'.format(api_endpoint = API_TAGO), headers = self.default_headers).json()
    
    # TODO: test it
    def passwordRecover(self, tagoRunURL, email):
        @staticmethod
        return requests.get('{api_endpoint}/run/{tagoRunURL}/passwordreset/{email}'.format(api_endpoint = API_TAGO), headers = self.default_headers).json()

    # TODO: test it
    def passwordChange(self, tagoRunURL, password):
        @staticmethod
        return requests.post('{api_endpoint}/run/{tagoRunURL}/passwordreset/{email}'.format(api_endpoint = API_TAGO), data=json.dumps(password), headers = self.default_headers).json()

    # TODO: test it
    def notificationList(self, tagoRunURL):
        return requests.get('{api_endpoint}/run/{tagoRunURL}/notification'.format(api_endpoint = API_TAGO), headers = self.default_headers).json()

    # TODO: create this function
    def notificationMarkRead(tagoRunURL, notifications):

    # TODO: test it
    def notificationButton(tagoRunURL, notification_id, btn_id):
        return requests.put('{api_endpoint}/run/{tagoRunURL}/notification/{notification_id}/{btn_id}'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: create this function
    def notificationDelete(tagoRunURL, notification_id):

