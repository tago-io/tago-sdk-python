import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class PaymentMethods:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def create(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/account/payment_method'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def list(self):
    return requests.get('{api_endpoint}/account/payment_method'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def setDefaultPaymentMethod(self, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/account/payment_method'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def deletePaymentMethod(self, data):
    data = data if data else {}
    return requests.delete('{api_endpoint}/account/payment_method'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()
