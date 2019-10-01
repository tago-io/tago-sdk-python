import time
import requests
import json
import os

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'

class Console:
  def __init__(self, analysis_token):
    self.analysis_token = analysis_token
    self.default_headers = { 'content-type': 'application/json', 'Device-Token': analysis_token}

  def log(self, message, timestamp = None):
    if not message:
      raise ValueError("Empty or Bad arguments")

    if not timestamp:
      timestamp = time.time() * 1000  # Time from epoch in sec*1000

    data = {'message': message, 'timestamp': timestamp}
    url = '{api_endpoint}/analysis/services/console/send'.format(api_endpoint=API_TAGO)
    return requests.post(url, json=data, headers=self.default_headers).json()
