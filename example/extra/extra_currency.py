import sys
sys.path.append('../..')

from tago import Tago
import os

TOKEN = '37dc5a45d8e2596727edfbedc2971ebb'

def test_convert():
	result = Tago(TOKEN).extra.currency().convert('USD', 'GBP')
	print "Convert USD to GBP:"
	print result

test_convert()