import requests
import requests_mock
import json
import re
import os
from tago.services.sms import SMS as sms

TOKEN = 'test_token'

def mock_callback(request, context):
	schema = {'to': '+11234567890', 'message': 'origin'}

	# Dictionary of params for the request
	res_dict = json.loads(request.body)

	# Check if the request has all the valid keys
	for key, value in schema.iteritems():
		if key not in res_dict: 
			return {'result': 'failure' }

	# Check if the request has all the valid params
	for key, value in schema.iteritems():
		if not res_dict[key]: 
			return {'result': 'failure'}

	# Check length of phone number
	if(len(res_dict['to']) > 15):
		return {'result': 'failure'}

	# regex for checking phone number
	# Check for sanity of phone number
	re_origin = re.match('\+\d', res_dict['to'])
	if(re_origin == None):
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

def test_sms():
	with requests_mock.Mocker() as cur_mock:
		API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
		url = '{api_endpoint}/analysis/services/sms/send'.format(api_endpoint=API_TAGO)
		cur_mock.post(url, json=mock_callback)

		# Empty values are not being tested as null error is thrown by sms 
		# class, so null values are not possible

		# Good case
		result = sms(TOKEN).send('+554498774411', 'test tago sms')
		check_status(result, True)

		# Bad case
		result = sms(TOKEN).send('+1234567890123456', 'test tago sms')
		check_status(result, False)

		# Bad case
		result = sms(TOKEN).send('1234567890', 'test tago sms')
		check_status(result, False)

		# Bad case
		result = sms('wrong_token').send('+554498774411', 'test tago sms')
		check_status(result, False)