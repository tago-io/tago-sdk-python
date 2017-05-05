import requests
import json
import os

class Distance:
	def __init__(self, key):
		self.key = key
		self.default_headers = {'Device-Token': key}

	#
	# Find distance between two locations
	# API Documentation : https://developers.google.com/maps/documentation/distance-matrix/intro
	# origin{string}
	# destination{string}
	# language{string}
	# mode{string}
	# example origin : '35.7706256,-78.6952835' 
	# example destination : '35.7728213,-78.6865257'
	#
	
	def measure(self, origin, destination, language, mode):
		if not origin or not destination:
			raise ValueError("Empty or Bad arguments")

		if not mode:
			mode = 'car'

		if not language:
			language = 'en-US'

		url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
		data = {'key':self.key, 'origins': origin, 'destinations': destination,\
				'mode':mode, 'language':language}
		distance = requests.get(url, params=data, headers=self.default_headers).json()
		return distance