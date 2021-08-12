import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'


class Sms:
  def __init__(self, analysis_token):
    self.analysis_token = analysis_token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': analysis_token}

  # Send SMS to a number
  # to{string} : Number to send SMS, Example: +554498774411
  # message{string} :
  # Returns Promise
  def send(self, to, message):
    if not to or not message:
      raise ValueError("Empty or Bad arguments")

    data = {'to': to, 'message': message}
    url = '{api_endpoint}/analysis/services/sms/send'.format(
      api_endpoint=API_TAGO)
    return requests.post(url, json=data, headers=self.default_headers).json()
