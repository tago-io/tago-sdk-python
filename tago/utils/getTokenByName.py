import requests
import json
import os

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

# TODO create this function
def getTokenByName(account, device_id, names = None):
    # tokens = 
