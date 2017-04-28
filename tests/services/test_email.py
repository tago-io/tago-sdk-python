from tago import Tago
import os
from tago.services.email import Email as email

TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'TOKEN'

def test_email():
    result = email(TOKEN).send('aapatel8@ncsu.edu', 'tago test', 'test tago services', 'kmishra@ncsu.edu', '')
    print result
    if result['status']:
        assert True
    else:
        assert False