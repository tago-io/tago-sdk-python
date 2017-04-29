from tago import Tago
import os
from geocoding import Geocoding
from promise import Promise


TOKEN = 'AIzaSyAXC9hGh4hdrFNWkLk8N-u2ewO_TvEbTCE'

def test_getAddress():
	result = Geocoding(TOKEN).getAddress('23.434213,24.3233323')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False

def test_getGeolocation():
	result = Geocoding(TOKEN).getGeolocation('Empire State Building, New York')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False
