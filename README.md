## TagoIO - Python Lib

Official Python lib for TagoIO

## Documentation

#### Installation

```
$ sudo pip install -U tago
```
#### Usage
##### Insert Data
**.insert(OBJECT)**
``` python
from tago import Tago

MY_DEVICE_TOKEN = 'add your device token here'
my_device = Tago(MY_DEVICE_TOKEN).device

data_to_insert = {
    'variable' : 'temperature',
    'location' : {'lat': 42.2974279, 'lng': -85.628292},
    'time'     : '2014-01-20 03:43:59',
    'unit'     : 'C',
    'value'    : 63
}

my_device.insert(data_to_insert) # Without response
# or
result = my_device.insert(data_to_insert) # With response
if result['status']:
    print('Data added')
else:
    print(result['message'])

```

##### Find Data
**.find(OBJECT)**
``` python
result = my_device.find({'query': 'last_value'})
if result['status']:
    print(result['message'] # Array with data)
else:
    print(result['message'] # Error (if status is False))

```

##### Delete Data
**.delete(/ID/)**
``` python

my_device.delete('Data_ID') # Without response
# or
result = my_device.delete('Data_ID') # With response
if result['status']:
    print('Data Removed')
else:
    print(result['message'])

```

## License

TagoIO SDK for Python is released under the [Apache-2.0 License](https://github.com/tago-io/tago-sdk-python/blob/master/LICENSE.md).
