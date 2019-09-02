import sys
import os
from tago import Tago

ANALYSYS_TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'a5da3fc5-3cd5-4ee4-9ab4-d781aab65ffd'

def myAnalysis(context, scope):
  print(environment_variables)
  account_token = list(filter(lambda account_token: account_token['key'] == 'account_token', context.environment))
  account_token = account_token[0]{'account_token'}
  account = Tago.account(account_token)
  devices = account.devices.list(1, ['id', 'tags'], {tags: [{
    key: 'analysis', value: 'geotraq',
  }]}, 1000)
  print(devices)
