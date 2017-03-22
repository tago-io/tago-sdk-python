from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def test_insert():
    result = Tago(TOKEN).device.edit({'variable': 'test', 'value': 3})
    print result
    if result['status']:
        assert True
    else:
        assert False
