import sys
sys.path.append('/Users/vitorfdl/Projects/tago-sdk-python')

from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'e11a8e89-9923-4571-8202-55e6a017f76c'

def func_callback(context, scope):
   print "context"
   print context
   print "scope"
   print scope

def test_socket():
   s =  Tago(TOKEN).analysis.run_analysis(func_callback, 0)

test_socket()