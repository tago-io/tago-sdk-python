import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class Middlewares:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def list(self, owner):
    url = '{api_endpoint}/middleware'
    if owner:
      url += '?owner=true'
    return requests.get(url.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def genToken(self, middleware_name):
    return requests.put('{api_endpoint}/middleware/gen_token/{middleware_name}'.format(api_endpoint=API_TAGO, middleware_name=middleware_name), headers=self.default_headers).json()
