import sys
sys.path.append('..')

from tago import Device

MY_DEVICE_TOKEN = 'add your device token here'
my_device = Device(MY_DEVICE_TOKEN)

data_to_insert = {
    'variable': 'temperature',
    'location': {'lat': 42.2974279, 'lng': -85.628292},
    'time': '2014-01-20 03:43:59',
    'unit': 'C',
    'value': 63
}

# my_device.insert(data_to_insert)  # Without response

result = my_device.insert(data_to_insert)  # With response
if result['status']:
    print(result['result'])
else:
    print(result['message'])


findData = my_device.find({'query': 'last_value'})
if findData['status'] is True:
  print(findData['result']) # Array with data
else:
  print(findData['message']) # Error (if status is False)
