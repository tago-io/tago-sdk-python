import os
from tago import Tago
import sys
sys.path.append('../..')

TOKEN = '37dc5a45d8e2596727edfbedc2971ebb'


def print_result(result):
  for key, value in result.iteritems():
    print(key + " : ", value)


def test_convert():
  result = Tago(TOKEN).extra.currency().convert('USD', 'GBP')
  print("Convert USD to GBP:")
  print_result(result)


test_convert()
