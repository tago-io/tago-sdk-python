import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Notifications:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def list(self, params):
    return requests.get('{api_endpoint}/notification'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=params).json()

  def markAsRead(self, notifications):
    if not isinstance(notifications, list):
      try:
        notifications = list(notifications)
      except TypeError:
        raise ValueError('Parameter should be iterable')
    else:
      data = {'notification_ids': notifications}
    return requests.put('{api_endpoint}/notification/read'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def accept(self, notification_id):
    return requests.post('{api_endpoint}/notification/accept/{notification_id}'.format(api_endpoint=API_TAGO, notification_id=notification_id), headers=self.default_headers).json()

  def refuse(self, notification_id):
    return requests.post('{api_endpoint}/notification/refuse/{notification_id}'.format(api_endpoint=API_TAGO, notification_id=notification_id), headers=self.default_headers).json()

  def remove(self, notification_id):
    return requests.delete('{api_endpoint}/notification/{notification_id}'.format(api_endpoint=API_TAGO, notification_id=notification_id), headers=self.default_headers).json()

  def registerDevice(self, device_token, platform):
    data = {
      'device_token': device_token,
      'platform': platform,
    }
    return requests.post('{api_endpoint}/notification/push/register'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def unRegisterDevice(self, device_token):
    data = {
      'device_token': device_token,
    }
    return requests.post('{api_endpoint}/notification/push/unregister'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()
