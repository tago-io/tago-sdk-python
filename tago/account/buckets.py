import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables
import _share # Used in share methods

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Buckets:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Account-Token': token }

        return

    def list(self, devices = False):
    	return requests.get('{api_endpoint}/bucket?devices={devices}'.format(api_endpoint=API_TAGO, devices=devices), headers=self.default_headers).json()

    def create(self, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/bucket'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def edit(self, bkt_id, data):
    	data = data if data else {}
    	return requests.put('{api_endpoint}/bucket/{bkt_id}'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers, data=json.dumps(data)).json()

    def delete(self, bkt_id):
    	return requests.delete('{api_endpoint}/bucket/{bkt_id}'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers).json()

    def info(self, bkt_id):
    	# if bkt_id is null, then call list
    	if bkt_id is None or bkt_id == '':
            return self.list()

    	return requests.get('{api_endpoint}/bucket/{bkt_id}'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers).json()

    def backupInfo(self, backup_id):
    	# if backup_id is null, then error!
    	if backup_id is None or backup_id == '':
            raise ValueError('backup_id must be set')

    	return requests.get('{api_endpoint}/backup/{backup_id}'.format(api_endpoint=API_TAGO, backup_id=backup_id), headers=self.default_headers).json()

    def backupList(self):
    	return requests.get('{api_endpoint}/backup'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    def backupDelete(self, backup_id):
    	# if bkt_id is null, then error!
    	if backup_id is None or backup_id == '':
            raise ValueError('backup_id must be set')

    	return requests.delete('{api_endpoint}/backup/{backup_id}'.format(api_endpoint=API_TAGO, backup_id=backup_id), headers=self.default_headers).json()

    def backupRecover(self, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/backup/recover'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    def shareList(self, bucket_id):
    	# if bucket_id is null, then ERROR
    	if bucket_id is None or bucket_id == '':
            raise ValueError('bucket_id must be set')

        return _share.list('bucket', bucket_id, self.default_headers)

    def shareSendInvite(self, bucket_id, data):
    	data = data if data else {}

    	# if bucket_id is null, then ERROR
    	if bucket_id is None or bucket_id == '':
            raise ValueError('bucket ID must be set')

        if data['email'] is None or data['email'] == '':
            raise ValueError('email must be set')

    	return _share.invite('bucket', bucket_id, data, self.default_headers)

    def shareEdit(self, share_id, data):
    	data = data if data else {}

    	# if share_id is null, then ERROR
    	if share_id is None or share_id == '':
            raise ValueError('share_id must be set')

        if data['email'] is None or data['email'] == '':
            raise ValueError('email must be set')

    	return _share.edit('bucket', share_id, data, self.default_headers)

    def shareDelete(self, share_id):
    	# if share_id is null, then ERROR
    	if share_id is None or share_id == '':
            raise ValueError('share_id must be set')

    	return _share.remove('bucket', share_id, self.default_headers)

    def exportData(self, output, buckets, options):
    	if output is None or output == '':
            raise ValueError('output must be set')
        elif buckets is None or buckets[0] is None:
            raise ValueError('bucket must be set')

        data = {}
        data['buckets'] = buckets
        data['start_date'] = options['start_date']
        data['end_date'] = options['end_date']

    	return requests.post('{api_endpoint}/data/export?output={output}'.format(api_endpoint=API_TAGO, output=output), headers=self.default_headers, data=json.dumps(data)).json()








