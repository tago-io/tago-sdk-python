from tago import Tago
from tago.extra.currency import Currency
from promise import Promise
import os

TOKEN = '37dc5a45d8e2596727edfbedc2971ebb'

def test_convert():
	result = Currency(TOKEN).convert('USD', 'GBP')
	print result
	if result['from'] == 'USD':
		assert True
	else:
		assert False
