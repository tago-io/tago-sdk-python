from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'f0ba1f34-2bec-4cba-80ba-088624e37fb2'

def func_callback(data):
   assert True

def test_socket():
   s =  Tago(TOKEN).analysis.localRuntime(func_callback, 1)

test_socket()