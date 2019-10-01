import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables
from ..internal import fixFilter

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class AccessManagement:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def list(self, page=1, fields=['id', 'name', 'tags'], filter={}, amount=20, orderBy='name,asc'):
    params = {
      'page': page,
      'fields': fields,
      'filter': filter,
      'amount': amount,
      'orderBy': orderBy,
    }
    params = fixFilter(params, filter)

    return requests.get('{api_endpoint}/am'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=params).json()

  def create(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/am'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def edit(self, am_id, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/am/{am_id}'.format(api_endpoint=API_TAGO, am_id=am_id), headers=self.default_headers, json=data).json()

  def delete(self, am_id):
    return requests.delete('{api_endpoint}/am/{am_id}'.format(api_endpoint=API_TAGO, am_id=am_id), headers=self.default_headers).json()

  def info(self, am_id):
    if am_id is None or am_id == '':
      raise ValueError('Access Management ID parameter is obrigatory.')
    return requests.get('{api_endpoint}/am/{am_id}'.format(api_endpoint=API_TAGO, am_id=am_id), headers=self.default_headers).json()
