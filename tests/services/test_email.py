from tago import Tago
import os
from tago.services.email import Email as email

TOKEN = os.environ.get('TAGO_TOKEN_ANALYSIS') or 'TOKEN'

def test_email():
    result = email(TOKEN).send('xyz@ncsu.edu', 'tago test', 'test tago services', 'xyz@ncsu.edu', '')
    print result
    if result['status']:
        assert True
    else:
        assert False