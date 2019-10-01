import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class Files:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def list(self, path='/', pagination_token=None, qty=300):
    params = {
      'path': path,
      'pagination_token': pagination_token,
      'qty': qty,
    }
    return requests.get('{api_endpoint}/files/'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=params).json()

  def uploadBase64(self, arrayOfFileObjects):
    return requests.post('{api_endpoint}/files'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(arrayOfFileObjects)).json()

  def move(self, arrayOfFileObjects):
    return requests.put('{api_endpoint}/files'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(arrayOfFileObjects)).json()

  def delete(self, arrayOfFileObjects):
    return requests.delete('{api_endpoint}/files'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(arrayOfFileObjects)).json()

  def checkPermission(self, file):
    return requests.get('{api_endpoint}/files/permission'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=json.dumps(file)).json()

  def changePermission(self, arrayOfFileObjects):
    return requests.put('{api_endpoint}/files/permission'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(arrayOfFileObjects)).json()

  def getFileURLSigned(self, url):
    if '.tago.io/file/' not in url:
      raise ValueError('{url} is not a TagoIO files url'.format(url=url))
    return requests.get(url=url, headers=self.default_headers, params=json.dumps({'noRedirect': True})).json()
