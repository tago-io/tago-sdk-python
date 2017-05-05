from tago.extra.distance import Distance
import os

TOKEN = 'AIzaSyAJSOIe3c2vxYXa0YDtnf15JFkuRK-3tIk'

def test_measure():
	result = Distance(TOKEN).measure('35.7706256,-78.6952835', '35.7728213,-78.6865257', '', '')
	print result
	if result['status'] == 'OK':
		assert True
	else:
		assert False
