import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables
from ..internal import fixFilter

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'


class Analysis:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def list(self, page=1, fields=['id', 'name'], filter={}, amount=20, orderBy='name,asc'):
    params = {
      'page': page,
      'fields': fields,
      'filter': filter,
      'amount': amount,
      'orderBy': orderBy,
    }
    params = fixFilter(params, filter)

    return requests.get('{api_endpoint}/analysis'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=params).json()

  def create(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/analysis'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def edit(self, analyze_id, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/analysis/{analyze_id}'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers, json=data).json()

  def delete(self, analyze_id):
    return requests.delete('{api_endpoint}/analysis/{analyze_id}'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()

  def info(self, analyze_id):
    # if analyze_id is null, then call list
    if analyze_id is None or analyze_id == '':
      return self.list()

    return requests.get('{api_endpoint}/analysis/{analyze_id}'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()

  def run(self, analyze_id, scope):
    return requests.post('{api_endpoint}/analysis/{analyze_id}/run'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers, data=scope).json()

  def tokenGenerate(self, analyze_id):
    return requests.get('{api_endpoint}/analysis/{analyze_id}/token'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()

  def uploadScript(self, analyze_id, file_name, file):
    data = {
      'file': file,
      'file_name': file_name,
    }
    return requests.post('{api_endpoint}/analysis/{analyze_id}/upload'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers, json=data).json()

  def downloadScript(self, analyze_id):
    return requests.get('{api_endpoint}/analysis/{analyze_id}/download'.format(api_endpoint=API_TAGO, analyze_id=analyze_id), headers=self.default_headers).json()
