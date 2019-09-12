## TagoIO - Python Lib

Official Python lib for TagoIO

## Documentation

#### Installation

```
$ sudo pip3 install -U tago
```

#### Usage
##### Insert Data
**.insert(OBJECT)**
``` python
import tago

MY_DEVICE_TOKEN = 'add your device token here'
my_device = tago.Device(MY_DEVICE_TOKEN)

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
```

##### Find Data
**.find(OBJECT)**
``` python
import tago

MY_DEVICE_TOKEN = 'add your device token here'
my_device = tago.Device(MY_DEVICE_TOKEN)

findData = my_device.find({'query': 'last_value'})
if findData['status'] is True:
  print(findData['result']) # Array with data
else:
  print(findData['message']) # Error (if status is False)
```

## License

TagoIO SDK for Python is released under the [Apache-2.0 License](https://github.com/tago-io/tago-sdk-python/blob/master/LICENSE.md).
