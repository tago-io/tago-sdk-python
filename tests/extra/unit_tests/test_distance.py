import requests
import requests_mock
import json
import re
from tago.extra.distance import Distance as distance

TOKEN = 'AIzaSyAJSOIe3c2vxYXa0YDtnf15JFkuRK-3tIk'

def mock_callback(request, context):
	schema = {'key': TOKEN, 'origins': 'origin', 'destinations': 'destination',\
				'mode':'mode', 'language':'language'}

	# Dictionary of params for the request
	res_dict = request.qs

	# Check if the request has all the valid params
	for key, value in schema.iteritems():
		if not res_dict[key][0]: 
			return {'result': 'failure'}

	# Check if the request has all the valid keys
	for key, value in schema.iteritems():
		if key not in res_dict: 
			return {'result': 'failure' }

	# regex for latitute and longitude
	# Check for sanity of origin
	re_origin = re.match('[\+\-]?\d*\.\d*\,[\+\-]?\d*\.\d*', res_dict['origins'][0])
	if(re_origin == None):
		return {'result': 'failure' }
	
	# Check for sanity of destination
	re_origin = re.match('[\+\-]?\d*\.\d*\,[\+\-]?\d*\.\d*', res_dict['destinations'][0])
	if(re_origin == None):
		return {'result': 'failure' }

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
	print response
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

def test_measure():
	with requests_mock.Mocker() as cur_mock:
		url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
		cur_mock.get(url, json=mock_callback)
		
		# Empty values are not being tested as null error is thrown at distance 
		# class, so null values are not possible

		# Good case
		result = distance(TOKEN).measure('35.7706256,-78.6952835', \
										'35.7728213,-78.6865257', '', '')
		check_status(result, True)

		# Bad case
		result = distance('wrong_token').measure('35.7706256,-78.6952835', \
										'35.7728213,-78.6865257', '', '')
		check_status(result, False)

		# Bad case
		result = distance(TOKEN).measure('ABC', \
										'35.7728213,-78.6865257', '', '')
		check_status(result, False)

		# Bad case
		result = distance(TOKEN).measure('35.7706256,-78.6952835', \
										'XYZ', '', '')
		check_status(result, False)