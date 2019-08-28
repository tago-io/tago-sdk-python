import requests
import requests_mock
import json
import re
from tago.extra.geocoding import Geocoding as geocoding

TOKEN = 'AIzaSyAJSOIe3c2vxYXa0YDtnf15JFkuRK-3tIk'


def mock_callback(request, context):
    schema = {'latlng': 'geolocation', 'key': TOKEN}

    # Dictionary of params for the request
    res_dict = request.qs

    # Check if the request has all the valid keys
    for key, value in schema.iteritems():
        if key not in res_dict:
            return {'result': 'failure'}

    # Check if the request has all the valid params
    for key, value in schema.iteritems():
        if not res_dict[key][0]:
            return {'result': 'failure'}

    # regex for latitute and longitude
    # Check for sanity of latlng
    re_origin = re.match(
        '[\+\-]?\d*\.\d*\,[\+\-]?\d*\.\d*', res_dict['latlng'][0])
    if(re_origin == None):
        return {'result': 'failure'}

    # Check if API_KEY passed matches the header's API_KEY
    res_header = request.headers
    if(res_header['Device-Token'] != schema['key']):
        return {'result': 'failure'}

    # Return if all checks passed
    return {'result': 'success'}


def mock_callback_geo(request, context):
    schema = {'address': 'address', 'key': TOKEN}

    # Dictionary of params for the request
    res_dict = request.qs

    # Check if the request has all the valid keys
    for key, value in schema.iteritems():
        if key not in res_dict:
            return {'result': 'failure'}

    # Check if the request has all the valid params
    for key, value in schema.iteritems():
        if not res_dict[key][0]:
            return {'result': 'failure'}

    # Check if API_KEY passed matches the header's API_KEY
    res_header = request.headers
    if(res_header['Device-Token'] != schema['key']):
        return {'result': 'failure'}

    # Return if all checks passed
    return {'result': 'success'}

#
# Unit test HACK
# Check status of response request
# Json object {'result': 'success/failure'}
# is returned.
#


def check_status(response, exp_status):
    print(response)
    # Check the response status
    if (response['result'] != 'failure'):
        status = True
    else:
        status = False

    # Compare with the expected status and assert
    if (exp_status == status):
        assert True
    else:
        assert False


def test_getAddress():
    with requests_mock.Mocker() as cur_mock:
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        cur_mock.get(url, json=mock_callback)

        # Empty values are not being tested as null error is thrown at geocoding
        # class, so null values are not possible

        # Good case
        result = geocoding(TOKEN).getAddress('23.434213,24.3233323')
        check_status(result, True)

        # Bad case
        result = geocoding('wrong_token').getAddress('23.434213,24.3233323')
        check_status(result, False)

        # Bad case
        result = geocoding(TOKEN).getAddress('ab,ab')
        check_status(result, False)


def test_getGeolocation():
    with requests_mock.Mocker() as cur_mock:
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        cur_mock.get(url, json=mock_callback_geo)

        # Empty values are not being tested as null error is thrown at geocoding
        # class, so null values are not possible

        # Good case
        result = geocoding(TOKEN).getGeolocation(
            'Empire State Building, New York')
        check_status(result, True)

        # Bad case
        result = geocoding('wrong_token').getGeolocation(
            'Empire State Building, New York')
        check_status(result, False)
