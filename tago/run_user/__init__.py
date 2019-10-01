import requests
import json
import os

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class RunUser:
  def __init__(self, token):
    self.token = token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': token}

  def info(self, tagoRunURL):
    return requests.get('{api_endpoint}/run/{tagoRunURL}/info'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), headers=self.default_headers).json()

  def editInfo(self, tagoRunURL, changes={}):
    data = changes
    return requests.put('{api_endpoint}/run/{tagoRunURL}/info'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), headers=self.default_headers, json=data).json()

  @staticmethod
  def create(self, tagoRunURL, newUserObj):
    return requests.post('{api_endpoint}/run/{tagoRunURL}/signup'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), headers=self.default_headers, data=json.dumps(newUserObj)).json()

  # email and password should be in a object?
  @staticmethod
  def login(self, tagoRunURL, emailAndPasswordObject):
    data = {
      'email': emailAndPasswordObject.email,
      'password': emailAndPasswordObject.password
    }
    return requests.post('{api_endpoint}/run/{tagoRunURL}/login'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), headers=self.default_headers, json=data).json()

  @staticmethod
  def confirmUser(self, tagoRunURL, token):
    return requests.get('{api_endpoint}/run/{tagoRunURL}/confirm/{token}'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL, token=token), headers=self.default_headers).json()

  @staticmethod
  def passwordRecover(self, tagoRunURL, email):
    return requests.get('{api_endpoint}/run/{tagoRunURL}/passwordreset/{email}'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL, email=email), headers=self.default_headers).json()

  @staticmethod
  def passwordChange(self, tagoRunURL, password):
    return requests.post('{api_endpoint}/run/{tagoRunURL}/passwordreset/{email}'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), data=json.dumps(password), headers=self.default_headers).json()

  def notificationList(self, tagoRunURL):
    return requests.get('{api_endpoint}/run/{tagoRunURL}/notification'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), headers=self.default_headers).json()

  def notificationMarkRead(self, tagoRunURL, notifications):
    if not isinstance(notifications, list):
      raise ValueError('Notifications parameter must be a list')
    data = {'notification_ids': notifications}
    return requests.put('{api_endpoint}/run/{tagoRunURL}/notification'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL), headers=self.default_headers, json=data).json()

  def notificationButton(self, tagoRunURL, notification_id, btn_id):
    return requests.put('{api_endpoint}/run/{tagoRunURL}/notification/{notification_id}/{btn_id}'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL, notification_id=notification_id, btn_id=btn_id), headers=self.default_headers).json()

  def notificationDelete(self, tagoRunURL, notification_id):
    return requests.delete('{api_endpoint}/run/{tagoRunURL}/notification/{notification_id}'.format(api_endpoint=API_TAGO, tagoRunURL=tagoRunURL, notification_id=notification_id), headers=self.default_headers).json()
