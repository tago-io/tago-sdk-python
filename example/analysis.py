import sys
sys.path.append('..')

from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'f0ba1f34-2bec-4cba-80ba-088624e37fb2'

def func_callback(context, scope):
   print "context"
   print context
   print "scope"
   print scope

def test_socket():
   s =  Tago(TOKEN).analysis.run_analysis(func_callback, 0)

test_socket()