from tago import Tago
import os

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def test_insert():
    result = Tago(TOKEN).services.send({'to': '+19199960103'}, 'message': 'test tago services')
    print result
    if result['status']:
        assert True
    else:
        assert False
