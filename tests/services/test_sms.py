from tago import Tago
import os
from tago.services.sms import SMS as sms

TOKEN = os.environ.get('TAGO_TOKEN_ANALYSIS') or 'TOKEN'

def test_sms():
    result = sms(TOKEN).send('+11234567890', 'test tago services')
    print result
    if result['status']:
        assert True
    else:
        assert False