import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'

def getTokenByName(account, device_id, names=None):
  tokens = account.devices.tokenList(device_id)
  if not tokens['status']: return None

  if names:
    names = [names] if isinstance(names, str) else names
    for name in names:
      try:
        token = tokens.name.index(name)
      except ValueError:
        token = None
      if token:
        break
  else:
    token = tokens['result'][0]['token']

  if not token:
    raise 'Cannot find Token for {device_id} in {names}'.format(device_id=device_id, names=names)
  return token
