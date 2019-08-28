# To run it, you should have inside the example folder

import sys
sys.path.append('..')

from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'b125e477-067f-46f4-86c5-830b426d25e9'

def func_callback(context, scope):
  print('token:', context.token)
  print('environment:', context.environment)
  print('analysis_id:', context.analysis_id)
  print('\n')
  context.log(scope[0])
  context.log('teste')
  context.log(123)
  context.log(True)


Tago(TOKEN).analysis.init(func_callback)
