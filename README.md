## Tago - Python Lib

Official Python lib for Tago

## Code Status

[![wercker status](https://app.wercker.com/status/16919e20780e3441fc3eb4c744e7bad3/m "wercker status")](https://app.wercker.com/project/bykey/16919e20780e3441fc3eb4c744e7bad3)

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
    print 'Data added'
else:
    print result['message']

```

##### Find Data
**.find(OBJECT)**
``` python
result = my_device.find({'query': 'last_value'})
if result['status']:
    print result['message'] # Array with data
else:
    print result['message'] # Error (if status is False)

```

##### Delete Data
**.delete(/ID/)**
``` python

my_device.delete('Data_ID') # Without response
# or
result = my_device.delete('Data_ID') # With response
if result['status']:
    print 'Data Removed'
else:
    print result['message']

```

##### Update Data
**.update(DATA, /ID/)**
``` python

data_to_update = {
    'value' : 32
}

my_device.update(data_to_update, 'Data_ID') # Without response
# or
result = my_device.update(data_to_update, 'Data_ID') # With response
if result['status']:
    print 'Data updated'
else:
    print result['message']

```

##### Listening new data by Socket
**.listening(CALLBACK)**

When new data arrives into Tago.io for you, it will be sent it to your device if you configure for this in the ‘Action’ (Left Menu in Admin). For this purpose, you need to create a new action and select the option ‘Send to Device’. All devices using the token associated with the bucket will receive the data.

``` python

def func_callback_data(data):
    print data

my_device.listening(func_callback_data)

```

## License

Tago lib client for Python is released under the [Copyright License](https://github.com/tago-io/tago-python/blob/master/LICENSE).
