import sys
import json
sys.path.append('home/kelvin/Tago/tago-sdk-python')

from tago import Tago
import os

TOKEN = '72cd18ed-58ba-489b-9ccf-50bcac194fa7'

data = {
    'variable': 'teste',
    'value': 18
}

print "Testing device functions"
print Tago(TOKEN).device.info()
print Tago(TOKEN).device.insert(data)
result = Tago(TOKEN).device.getParams("")
print result
