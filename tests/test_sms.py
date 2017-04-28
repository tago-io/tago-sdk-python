from tago import Tago
import os
from tago.services.sms import SMS as sms

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def test_sms():
    result = sms(TOKEN).send('+19199960103', 'test tago services')
    print result
    if result['status']:
        assert True
    else:
        assert False