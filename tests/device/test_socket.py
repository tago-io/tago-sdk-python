import sys
sys.path.append('../..')

from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def func_callback(data):
    assert True

def test_socket():
    s =  Tago(TOKEN).device.listening(func_callback, 1)
