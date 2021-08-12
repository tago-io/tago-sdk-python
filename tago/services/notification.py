import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Notification:
  def __init__(self, analysis_token):
    self.token = analysis_token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': analysis_token}

  def send(self, title, message, ref_id):
    data = {
      'title': title,
      'message': message,
      'ref_id': ref_id
    }
    return requests.post('{api_endpoint}/analysis/services/notification/send'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()
