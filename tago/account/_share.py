import requests # Used to make HTTP requests
import os

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

def invite(type, ref_id, data, default_options):
    data = data if data else {}
    if ref_id is None or ref_id == '':
        return None # Type ID parameter is obligatory
    elif data['email'] is None or data['email'] == '':
        return None # data email parameter is obligatory.
    return requests.post('{api_endpoint}/share/{type}/{ref_id}'.format(api_endpoint=API_TAGO,type=type,ref_id=ref_id), headers=default_options, data=json.dumps(data)).json()

def edit(type, share_id, data, default_options):
    data = data if data else {}
    if share_id is None or share_id == '':
        return None # Share ID parameter is obligatory
    return requests.put('{api_endpoint}/share/{share_id}'.format(api_endpoint=API_TAGO,share_id=share_id), headers=default_options, data=json.dumps(data)).json()

def list(type, ref_id, default_options):
    data = data if data else {}
    if ref_id is None or ref_id == '':
        return None # Type ID parameter is obligatory
    return requests.get('{api_endpoint}/share/{type}/ref_id'.format(api_endpoint=API_TAGO,type=type), headers=default_options).json()

def remove(type, share_id, default_options):
    if share_id is None or share_id == '':
        return None # Share ID parameter is obligatory
    return requests.delete('{api_endpoint}/share/{type}?id={share_id}'.format(api_endpoint=API_TAGO,type=type,share_id=share_id), headers=default_options).json()

# Not sure what exports do...
