import sys
import json
sys.path.append('../..')

from tago import Tago
import os

TOKEN = '72cd18ed-58ba-489b-9ccf-50bcac194fa7'

result = Tago(TOKEN).device.getParams("")
print result
