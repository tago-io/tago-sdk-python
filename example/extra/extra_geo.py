import os
import sys
from tago import Tago
sys.path.append('../..')


TOKEN = 'AIzaSyAXC9hGh4hdrFNWkLk8N-u2ewO_TvEbTCE'


def print_result(result):
    for key, value in result.iteritems():
        print(key + " : ", value)


def test_getAddress():
    result = Tago(TOKEN).extra.geocoding().getAddress('23.434213,24.3233323')
    print("Get Address test")
    print_result(result)


def test_getGeolocation():
    result = Tago(TOKEN).extra.geocoding().getGeolocation(
        'Empire State Building, New York')
    print("Get Geolocation test")
    print_result(result)


test_getGeolocation()
test_getAddress()
