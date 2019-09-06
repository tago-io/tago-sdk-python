import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class Explore:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def addExplore(self, explore_id):
    return requests.post('{api_endpoint}/explore/{explore_id}'.format(api_endpoint=API_TAGO, explore_id=explore_id), headers=self.default_headers).json()

  def list(self):
    return requests.get('{api_endpoint}/explore'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()
