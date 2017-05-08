import sys
sys.path.append('../..')

from tago import Tago
import os

TOKEN = 'AIzaSyAJSOIe3c2vxYXa0YDtnf15JFkuRK-3tIk'

def test_measure():
	result = Tago(TOKEN).extra.distance().measure('35.7706256,-78.6952835', '35.7728213,-78.6865257', '', '')
	print "Distance Test:"
	print result

test_measure()