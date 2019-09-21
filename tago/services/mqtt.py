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

  def publish(self, topic, message, bucket, options={}):
    url = '{api_endpoint}/analysis/services/mqtt/publish'.format(api_endpoint=API_TAGO)
    data = dict(**{'topic': topic, 'message': message, 'bucket': bucket}, **options)
    return requests.post(url, data=json.dumps(data), headers=self.default_headers).json()
