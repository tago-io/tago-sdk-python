import requests
import requests_mock
import json
import re
import os
from tago.services.console import Console as console

TOKEN = 'test_token'

def mock_callback(request, context):
	schema = data = {'message':'message', 'timestamp': 'timestamp'}

	# Dictionary of params for the request
	res_dict = json.loads(request.body)

	print res_dict['timestamp']

	# Check if the request has all the valid keys
	for key, value in schema.iteritems():
		if key not in res_dict:
			return {'result': 'failure' }

	# Check if the request has all the valid params
	for key, value in schema.iteritems():
		if not res_dict[key]:
			return {'result': 'failure'}

	# regex for checking timestamp
	# Check for sanity of timestamp
	re_time = re.match('\d\.\d', str(res_dict['timestamp']))
	if(re_time == None):
		return {'result': 'failure'}

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

def test_console():
	with requests_mock.Mocker() as cur_mock:
		API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
		url = '{api_endpoint}/analysis/services/console/send'.format(api_endpoint=API_TAGO)
		cur_mock.post(url, json=mock_callback)

		# Empty values are not being tested as null error is thrown by console
		# class, so null values are not possible

		# Good case
		result = console(TOKEN).send('test tago services', '')
		check_status(result, True)

		# Bad case
		result = console(TOKEN).send('test tago services', 'wrong_timestamp')
		check_status(result, False)

		# Bad case
		result = console('wrong_token').send('test tago services', '')
		check_status(result, False)