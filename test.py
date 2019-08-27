import sys
import json
import os
# sys.path.append('home/kelvin/Tago/tago-sdk-python')

from tago import Tago

TOKEN = '72cd18ed-58ba-489b-9ccf-50bcac194fa7'

data = {
    'variable': 'teste',
    'value': 18
}

print "Testing device functions"
print Tago(TOKEN).device.info()
print Tago(TOKEN).device.remove({})
# print Tago(TOKEN).device.insert(data)
result = Tago(TOKEN).device.getParams("")
print result
