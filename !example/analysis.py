# To run it, you should have inside the example folder

import os
import sys
sys.path.append('..')

from tago import Analysis

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'a5da3fc5-3cd5-4ee4-9ab4-d781aab65ffd'

def func_callback(context, scope):
  print('token:', context.token)
  print('environment:', context.environment)
  account_token = list(filter(lambda account_token: account_token['key'] == 'abc', context.environment))
  print(account_token[0]['value'])
  print('analysis_id:', context.analysis_id)
  print('\n')
  context.log(scope[0])
  context.log('teste')
  context.log(123)
  context.log(True)


Analysis(TOKEN).init(func_callback)
