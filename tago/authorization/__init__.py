import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Authorization:
  def __init__(self, token):
    self.token = token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': token}

  def info(self):
    return requests.get('{api_endpoint}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def createDevice(self, data):
    return requests.post('{api_endpoint}/device'.format(api_endpoint=API_TAGO), json=data, headers=self.default_headers).json()
