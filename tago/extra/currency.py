import requests
import json
import os

class Currency:
	def __init__(self, key):
		self.key = key
		self.default_headers = { 'content-type': 'application/json', 'Device-Token': key }

	#
	# Find conversion rates for currency
	# API Documentation : https://currencylayer.com
	# c_from{string} : Currency for which conversion rate is to be found
	# c_to{string} : Currency to which c_from is to be converted
	# for multiple conversions c_to should be comma separated currencies.
	# example for single conversion : "convert('USD', 'EUR')"
	# example for multiple conversion : "convert('USD', 'EUR,GBP')"
	#
	
	def convert(self, c_from, c_to):
		if not c_from or not c_to:
			raise ValueError("Empty or Bad arguments")

		url = 'http://apilayer.net/api/live'
		data = {'access_key':self.key, 'source': c_from, 'currencies': c_to, 'format': 1}
		convert_cur = requests.get(url, params=data, headers=self.default_headers).json()
		convert_cur_json = {'from': convert_cur['source'], 'result': convert_cur['quotes']}
		return convert_cur_json
