# To run it, you should have inside the example folder

import sys
sys.path.append('..')

import tago

ANALYSYS_TOKEN = 'a5da3fc5-3cd5-4ee4-9ab4-d781aab65ffd'

def my_analysis(context, scope):
  # Getting the account token from analysis environment variable
  account_token = list(filter(lambda account_token: account_token['key'] == 'account_token', context.environment))
  account_token = account_token[0]['value']

  # Instantiating run object from Account Class
  run = tago.Account(account_token).run

  # Creating user object with all info inside
  userObject = {
    'active': True,
    'company': 'companyNameHere',
    'created_at': 'null',
    'email': 'test2@tago.io',
    'language': 'en',
    'name': 'test',
    'phone': 'phoneNumberHere',
    'tags': [],
    'timezone': 'America / Sao_Paulo',
    'password': 'testing123',
  }

  # Creating the user with all info above on our own TagoIO RUN and getting the response
  print(run.createUser(userObject))

  # If you doesn't want to print response, use this line
  # run.createUser(userObject)

# Initializing TagoIO analysis
tago.Analysis(ANALYSYS_TOKEN).init(my_analysis)
