# To run it, you should have inside the example folder

import sys
sys.path.append('..')

import tago

ANALYSYS_TOKEN = 'your analysis token here'

def my_analysis(context, scope):
  # Getting the account token from analysis environment variables
  account_token = list(filter(lambda account_token: account_token['key'] == 'account_token', context.environment))
  account_token = account_token[0]['value']

  # Initializing account devices object
  account_devices = tago.Account(account_token).devices()

  # Creating an object with all device info
  new_device = {
    'name': 'My first device',
    'description': 'Creating my first device',
    'active': True,
    'visible': True,
    'tags': [{
      'key': 'client',
      'value': 'John',
    }],
    'configuration_params': [{
      'sent': 'false',
      'key': 'check_rate',
      'value': 600,
    }, {
      'sent': 'false',
      'key': 'measure_time',
      'value': 0,
    },],
  }

  # Printing response
  print(account_devices.create(new_device))

  # If you doesn't want to print response, use this line
  # account_devices.create(new_device)

tago.Analysis(ANALYSYS_TOKEN).init(my_analysis)
