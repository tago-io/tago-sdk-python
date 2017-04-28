from tago import Tago
import os
from tago.services.email import Email as email

TOKEN = os.environ.get('TAGO_TOKEN_ANALYSIS') or 'f0ba1f34-2bec-4cba-80ba-088624e37fb2'

def test_email():
    result = email(TOKEN).send('xyz@ncsu.edu', 'tago test', 'test tago services', 'xyz@ncsu.edu', '')
    print result
    if result['status']:
        assert True
    else:
        assert False