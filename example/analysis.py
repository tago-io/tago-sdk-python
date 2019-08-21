import sys
sys.path.append('..')

from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or '8a8de9e3-b5f6-4077-89e3-ad728598aac5'

def func_callback(context, scope):
   print "context"
   print context
   print "scope"
   print scope

def test_socket():
   s =  Tago(TOKEN).analysis.run_analysis(func_callback, 0)

test_socket()