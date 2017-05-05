import requests
import requests_mock
import json
from tago.extra.geocoding import Geocoding as geocoding
from promise import Promise

TOKEN = 'AIzaSyAXC9hGh4hdrFNWkLk8N-u2ewO_TvEbTCE'

def test_getAddress():
	result = geocoding(TOKEN).getAddress('23.434213,24.3233323')
	print result
	if result['status'] == 'OK':
		assert True
	else:
		assert False

def test_getGeolocation():
	result = geocoding(TOKEN).getGeolocation('Empire State Building, New York')
	print result
	if result['status'] == 'OK':
		assert True
	else:
		assert False
