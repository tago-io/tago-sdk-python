from tago import Tago
from distance import Distance
from promise import Promise
import os

TOKEN = ''

def test_measure():
	result = Distance(TOKEN).measure('23.434213,24.3233323')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False
