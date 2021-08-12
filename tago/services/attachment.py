import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'


class Attachment:
  def __init__(self, analysis_token):
    self.token = analysis_token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': analysis_token}

  # TODO: test it
  def upload(self, archive, filename, type):
    data = {
      'archive': archive,
      'filename': filename,
      'type': type,
    }
    return requests.post('{api_endpoint}/analysis/services/attachment/upload'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()
