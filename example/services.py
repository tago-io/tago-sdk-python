import os
from tago import Tago
import sys
sys.path.append('..')


TOKEN = os.environ.get(
    'TAGO_TOKEN_ANALYSIS') or 'f0ba1f34-2bec-4cba-80ba-088624e37fb2'

to_phone = ''
to_email = ''
email_sub = 'Tago Service Test'
message = 'Tago test service object'


def test_sms():
  result = Tago(TOKEN).services.sms().send(to_phone, message)
  print("SmS test result:")
  print(result)


def test_email():
  result = Tago(TOKEN).services.email().send(
    to_email, email_sub, message, '', '')
  print("Email test result:")
  print(result)


test_sms()
test_email()
