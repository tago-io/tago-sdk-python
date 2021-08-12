import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Device:
  def __init__(self, token):
    self.token = token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': token}

  def info(self):
    return requests.get('{api_endpoint}/info'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def insert(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/data'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def find(self, query_obj):
    query_obj = query_obj if query_obj else {}
    result = requests.get('{api_endpoint}/data'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=query_obj)

    return result.json()

  def remove(self, args={}):
    queryOrID = args.get('queryOrID')
    if not (len(args)):
      queryOrID = {
        'query': 'last_item'
      }
    query_obj = queryOrID if queryOrID else args
    return requests.delete('{api_endpoint}/data'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=query_obj).json()

  def getParams(self, sent_status):
    return requests.get('{api_endpoint}/device/params'.format(api_endpoint=API_TAGO), params=sent_status, headers=self.default_headers).json()

  def markParam(self, param_id):
    return requests.put('{api_endpoint}/device/params/{param_id}'.format(api_endpoint=API_TAGO, param_id=param_id), headers=self.default_headers).json()
