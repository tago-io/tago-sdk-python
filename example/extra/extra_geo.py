import sys
sys.path.append('../..')

from tago import Tago
import os

TOKEN = 'AIzaSyAXC9hGh4hdrFNWkLk8N-u2ewO_TvEbTCE'

def test_getAddress():
	result = Tago(TOKEN).extra.geocoding().getAddress('23.434213,24.3233323')
	print "Get Address test"
	print result

def test_getGeolocation():
	result = Tago(TOKEN).extra.geocoding().getGeolocation('Empire State Building, New York')
	print "Get Geolocation test"
	print result

test_getGeolocation()
test_getAddress()