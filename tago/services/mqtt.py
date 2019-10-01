import requests
import json
import os

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'


class Mqtt:
  def __init__(self, analysis_token):
    self.analysis_token = analysis_token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': analysis_token}

  # publish MQTT
  # message{string} : Message
  # bucket{string} : Bucket to recive message
  # returns promise

  def publish(self, message, bucket, options):
    if not bucket or not message:
      raise ValueError("Empty or Bad arguments")

    data = {'message': message, 'bucket': bucket}
    url = '{api_endpoint}/analysis/services/mqtt/publish'.format(
      api_endpoint=API_TAGO)
    return requests.post(url, json=data, headers=self.default_headers).json()
