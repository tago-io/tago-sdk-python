import requests
import json
import os

API_TAGO=os.environ.get('TAGO_API') or 'https://api.tago.io'

def version():
  return requests.get('{api_endpoint}/status'.format(api_endpoint=API_TAGO)).json()
