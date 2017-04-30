import requests
import requests_mock
import json
import re
import os
from tago.services.mqtt import MQTT as mqtt

TOKEN = 'test_token'

def mock_callback(request, context):
	schema = {'message':'message', 'bucket': 'bucket'}

	# Dictionary of params for the request
	res_dict = json.loads(request.body)

	# Check if the request has all the valid params
	for key, value in schema.iteritems():
		if not res_dict[key]: 
			return {'result': 'failure'}

	# Check if the request has all the valid keys
	for key, value in schema.iteritems():
		if key not in res_dict: 
			return {'result': 'failure' }

	# Check if TOKEN passed matches the header's TOKEN
	res_header = request.headers
	if(res_header['Device-Token'] != TOKEN):
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

def test_mqtt():
	with requests_mock.Mocker() as cur_mock:
		API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
		url = '{api_endpoint}/analysis/services/mqtt/publish'.format(api_endpoint=API_TAGO)
		cur_mock.post(url, json=mock_callback)

		# Empty values are not being tested as null error is thrown by mqtt 
		# class, so null values are not possible

		# Good case
		result = mqtt(TOKEN).publish('bucket', 'message')
		check_status(result, True)

		# Bad case
		result = mqtt('wrong_token').publish('bucket', 'message')
		check_status(result, False)