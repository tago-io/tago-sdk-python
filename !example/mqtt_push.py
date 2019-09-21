# To run it, you should have inside the example folder

import sys
sys.path.append('..')

import tago
from tago import Services
import json

ANALYSYS_TOKEN = 'a5da3fc5-3cd5-4ee4-9ab4-d781aab65ffd'

# Snippet to push data to MQTT. Follow this pattern within your application
# If you want more details about MQTT, search "MQTT" in TagoIO help center.
# You can find plenty of documentation about this topic.
# TagoIO Team.
def mqtt_push(context, scope):
  if not scope:
    return print('No data')

  # Searching for push_payload in scope, if there isn't push_payload variable, my_data = None
  my_data = next((x for x in scope if x['variable'] == 'push_payload'), None)

  if not my_data:
    return print('No data')

  # Create your data object to push to MQTT
  my_data_object = {
    'variable': 'temperature_celsius',
    'value': (my_data['value'] - 32) * (5 / 9),
    'unit': 'C',
  }

  # Create a object with the options you choosed
  options = {
    'retain': False,
    'qos': 0,
  }

  # Getting MQTT object
  mqtt = Services(ANALYSYS_TOKEN).MQTT

  # Publishing to MQTT
  print(mqtt.publish('tago/my_topic', json.dumps(my_data_object, separators=(',', ':')), my_data['bucket'], options))

tago.Analysis(ANALYSYS_TOKEN).init(mqtt_push)
