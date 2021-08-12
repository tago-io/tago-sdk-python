import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables
from ..internal import fixFilter

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class ServiceAuth:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def tokenList(self, page=1, amount=20, filter={}, fields=['name', 'token', 'created_at'], orderBy='created_at,desc'):
    params = {
      'page': page,
      'filter': filter,
      'amount': amount,
      'orderBy': orderBy,
      'fields': fields,
    }
    params = fixFilter(params, filter)

    return requests.get('{api_endpoint}/serviceauth'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=params).json()

  def tokenCreate(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/serviceauth'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def tokenDelete(self, token):
    return requests.delete('{api_endpoint}/serviceauth/{token}'.format(api_endpoint=API_TAGO, token=token), headers=self.default_headers).json()

  def tokenEdit(self, token, verification_code):
    data = {'verification_code': verification_code}
    return requests.put('{api_endpoint}/serviceauth/{token}'.format(api_endpoint=API_TAGO, token=token), headers=self.default_headers, json=data).json()
