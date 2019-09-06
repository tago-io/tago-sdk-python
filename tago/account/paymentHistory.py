import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class PaymentHistory:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def getHistory(self):
    return requests.get('{api_endpoint}/account/payment_history'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()
