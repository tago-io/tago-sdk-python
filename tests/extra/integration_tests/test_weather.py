import requests
import requests_mock
import json
from tago.extra.weather import Weather 
from promise import Promise

TOKEN = 'fe1b837fb8f31dc6'

def test_current():
	result = Weather(TOKEN).current('27606', False, 'EN')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False

def test_history():
	result = Weather(TOKEN).history('2017-02-21', '27606', False, 'EN')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False

def test_forecast():
	result = Weather(TOKEN).forecast('27606', False, 'EN')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False

def test_alerts():
	result = Weather(TOKEN).alerts('27606', False, 'EN')
	print result
	if type(result) == Promise:
		assert True
	else:
		assert False