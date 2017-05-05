import requests
import json
import os

class Geocoding:
	def __init__(self,key):
		self.key = key
		self.default_headers = { 'content-type': 'application/json', 'Device-Token': key }

	def getAddress(self, geolocation):
		if type(geolocation) == str:
			geoplited = geolocation.split(',')

			if len(geoplited) > 1:
				geolocation = [geoplited[0].strip(), geoplited[1].strip()]
			else:
				raise ValueError("Invalid geolocation")
		elif geolocation.coordinates:
			geolocation = geolocation.coordinates
		else:
			raise ValueError("Invalid geolocation")

		geolocation = ','.join([geolocation[0], geolocation[1]])

		url = 'https://maps.googleapis.com/maps/api/geocode/json'
		query = {'latlng': geolocation, 'key': self.key}
		geoloc_response = requests.get(url, params=query, headers=self.default_headers).json()
		return geoloc_response

	def getGeolocation(self, address):
		url = 'https://maps.googleapis.com/maps/api/geocode/json'
		query = { 'address':address, 'key': self.key }
		geoloc_response = requests.get(url, params=query, headers=self.default_headers).json()
		return geoloc_response