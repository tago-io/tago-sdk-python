from tago import Tago
import os
from tago.services.socket import Socket as socket

TOKEN = os.environ.get('TAGO_TOKEN_ANALYSIS') or 'f0ba1f34-2bec-4cba-80ba-088624e37fb2'

def test_socket():
    result = socket(TOKEN).send('588ff56e3a57780ce6ab7112', '{"variable":"temperature","value":27,"unit":"F"}')
    print result
    if result['status']:
        assert True
    else:
        assert False