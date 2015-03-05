from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def test_insert():
    result = Tago(TOKEN).device.insert({'variable': 'py', 'value': 2})
    if result['status']:
        assert True
    else:
        assert False
