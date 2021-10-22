import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'


class Mqtt:
    def __init__(self, analysis_token):
        self.analysis_token = analysis_token
        self.default_headers = {
            'content-type': 'application/json', 'Device-Token': analysis_token}

    # publish MQTT
    # message{string} : Message
    # bucket{string} : Bucket to recive message
    # returns promise

    def publish(self, message, bucket, topic, retain, qos):
        if not bucket or not message:
            raise ValueError("Empty or Bad arguments")

        data = dict({'topic': topic, 'message': message,
                    'bucket': bucket, 'retain': retain, 'qos': qos})
        url = '{api_endpoint}/analysis/services/mqtt/publish'.format(
            api_endpoint=API_TAGO)
        return requests.post(url, data=json.dumps(data), headers=self.default_headers).json()
