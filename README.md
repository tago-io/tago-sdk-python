## Tago - Python Lib

Official Python lib for Tago

<!-- ## Code Status

[![wercker status](https://app.wercker.com/status/7eba1fa5503f7f5ad61a15a0a6e63234/m "wercker status")](https://app.wercker.com/project/bykey/7eba1fa5503f7f5ad61a15a0a6e63234) -->

## Documentation

#### Installation

```
$ sudo pip install -U tago
```
#### Usage
##### Insert Data
**.insert(OBJECT);**
``` python
from tago import Tago

MY_DEVICE_TOKEN = 'add your device token here'
my_device = Tago(MY_DEVICE_TOKEN).device

data_to_insert = {
    'variable' : 'temperature',
    'location' : '42.2974279,-85.628292',
    'time'     : '2014-01-20 03:43:59',
    'unit'     : 'C',
    'value'    : 63
};

my_device.insert(data_to_insert) // Without response
# or
result = my_device.insert(data_to_insert) // With response
if result['status']:
    print 'Data added'
else:
    print result['result']

```

##### Delete Data
**.delete(/ID/);**
``` python

my_device.delete('Data_ID') // Without response
# or
result = my_device.delete('Data_ID') // With response
if result['status']:
    print 'Data Removed'
else:
    print result['result']

```

##### Update Data
**.update(DATA, /ID/);**
``` python

data_to_update = {
    'value' : 32
};

my_device.update(data_to_update, 'Data_ID') // Without response
# or
result = my_device.update(data_to_update, 'Data_ID') // With response
if result['status']:
    print 'Data updated'
else:
    print result['result']

```

##### Listening new data by Socket
**.listening(CALLBACK);**

When arrive new data in Tago.io we will send to your device, so you need configure this in **Action** (Menu on Admin) create a new **action** and select the option **Send to Device**. All device using the token with bucket associated will receive the data.

``` python

def func_callback_data(data):
    print data

my_device.listening(func_callback_data)

```

## License

Tago lib client for Python is released under the [Copyright License](https://github.com/tago-io/tago-python/blob/master/LICENSE).
