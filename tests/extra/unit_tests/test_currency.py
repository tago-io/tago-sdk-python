import requests
import requests_mock
import json
from tago.extra.currency import Currency as currency


def has_key_callback(request, context):
    schema = {'access_key': '2bf1c721f5b33ea0977b79a832ac4640', 'source': 'c_src',
                            'currencies': 'c_to', 'format': 1}

    # Dictionary of params for the request
    res_dict = request.qs

    # Check if the request has all the valid params
    for key, value in schema.iteritems():
        if not res_dict[key][0]:
            return {'source': '', 'quotes': 'failure'}

    # Check if the request has all the valid keys
    for key, value in schema.iteritems():
        if key not in res_dict:
            return {'source': '', 'quotes': 'failure'}

    # Check if source currency has length 3
    if(len(res_dict['source'][0]) != 3):
        return {'source': res_dict['source'][0], 'quotes': 'failure'}

    # Check if currency to has length 3 or more
    if(len(res_dict['currencies'][0]) != 3):
        return {'source': res_dict['source'][0], 'quotes': 'failure'}

    # Check if API_KEY passed matches the header's API_KEY
    res_header = request.headers
    if(res_header['Device-Token'] != schema['access_key']):
        return {'source': res_dict['source'][0], 'quotes': 'failure'}

    # Return if all checks passed
    return {'source': 'USD', 'quotes': {'USDGBP': 0.77219}}


# Unit test HACK
# Check status of response request
# The convert function returns a json object with
# keys from and result. For unit test, quotes is being
# used as a means to mark failure.
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


def test_currency():
    with requests_mock.Mocker() as cur_mock:
        url = 'http://apilayer.net/api/live'
        cur_mock.get(url, json=has_key_callback)

        # Good case
        response = currency(
            '2bf1c721f5b33ea0977b79a832ac4640').convert('USD', 'EUR')
        check_status(response, True)

        # Bad case
        response = currency(
            '2bf1c721f5b33ea0977b79a832ac4640').convert('US', 'EUR')
        check_status(response, False)

        # Bad case
        response = currency(
            '2bf1c721f5b33ea0977b79a832ac4640').convert('USD', 'EU')
        check_status(response, False)

        # Bad case
        response = currency('wrong_key').convert('USD', 'EUR')
        check_status(response, False)
