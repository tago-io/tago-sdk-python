from tago import Tago
import os
from tago.services.console import Console as console

TOKEN = os.environ.get('TAGO_TOKEN_ANALYSIS') or 'f0ba1f34-2bec-4cba-80ba-088624e37fb2'

def test_console():
    result = console(TOKEN).send('test tago services', '')
    print result
    if result['status']:
        assert True
    else:
        assert False