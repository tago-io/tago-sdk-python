from tago import Tago
import os
from tago.services.console import Console as console

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def test_console():
    result = console(TOKEN).send('test tago services', '')
    print result
    if result['status']:
        assert True
    else:
        assert False