import sys
sys.path.append('..')

from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'a5b992b1-0ad6-4752-893c-39969321417a'

def func_callback(context, scope):
   print "context"
   print context
   print "scope"
   print scope

def test_socket():
   s =  Tago(TOKEN).analysis.run_analysis(func_callback, 0)

test_socket()