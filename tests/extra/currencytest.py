from tago import Tago
from currency import Currency
from promise import Promise
import os

TOKEN = '37dc5a45d8e2596727edfbedc2971ebb'

def test_convert():
	result = Currency(TOKEN).current('','','')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False
