import requests  # Used to make HTTP requests
import os
import json

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'

def invite(type, ref_id, data, default_options):
  data = data if data else {}
  if ref_id is None or ref_id == '':
    raise ValueError('ref_id must be set')
  elif data['email'] is None or data['email'] == '':
    raise ValueError('email must be set in data')
  return requests.post('{api_endpoint}/share/{type}/{ref_id}'.format(api_endpoint=API_TAGO, type=type, ref_id=ref_id), headers=default_options, json=data).json()

def edit(share_id, data, default_options):
  data = data if data else {}
  if share_id is None or share_id == '':
    raise ValueError('share_id must be set')
  return requests.put('{api_endpoint}/share/{share_id}'.format(api_endpoint=API_TAGO, share_id=share_id), headers=default_options, json=data).json()

def list(type, ref_id, default_options):
  if ref_id is None or ref_id == '':
    raise ValueError('ref_id must be set')
  return requests.get('{api_endpoint}/share/{type}/{ref_id}'.format(api_endpoint=API_TAGO, type=type, ref_id=ref_id), headers=default_options).json()

def remove(share_id, default_options):
  if share_id is None or share_id == '':
    raise ValueError('share_id must be set')
  return requests.delete('{api_endpoint}/share/{share_id}'.format(api_endpoint=API_TAGO, share_id=share_id), headers=default_options).json()
