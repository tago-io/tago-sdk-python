import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Plan:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def setPlanParameters(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/account/plan'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def getPriceToUpdate(self, data):
    return requests.get('{api_endpoint}/account/plan_value'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=json.dumps(data)).json()

  def getActivePlan(self):
    return requests.get('{api_endpoint}/account/plan'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def getCurrentPrices(self):
    return requests.get('{api_endpoint}/pricing'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def summary(self):
    return requests.get('{api_endpoint}/billing'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()
