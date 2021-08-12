import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Tags:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def getTagKeys(self, type):
    return requests.get('{api_endpoint}/tags/keys/{type}'.format(api_endpoint=API_TAGO, type=type), headers=self.default_headers).json()
