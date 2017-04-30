import requests
import json
import os

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

class Socket:
	def __init__(self, analysis_token):
		self.analysis_token = analysis_token
		self.default_headers = { 'content-type': 'application/json', 'Device-Token': analysis_token }

	# Send a Socket message to tago
	# bucket_id{string} : Bucket to recive message 
	# data{json_string} : data to be sent
	# returns promise

	def send(self, bucket_id, data_entry):
		if not bucket_id or not data_entry:
			raise ValueError("Empty or Bad arguments")

		try:
			json.loads(data_entry)
		except ValueError:
			print("data_entry is not a valid JSON")

		data = {'bucket_id': bucket_id, 'data': data_entry}
		url = '{api_endpoint}/analysis/services/socket/send'.format(api_endpoint=API_TAGO)
		return requests.post(url, data=json.dumps(data), headers=self.default_headers).json()
