from currency import Currency
from distance import Distance
from geocoding import Geocoding
from weather import Weather

class Extra:
	def __init__(self, API_KEY):
		self.key = API_KEY

	def currency(self): 
		return Currency(self.key)

	def distance(self):
		return Distance(self.key)

	def geocoding(self):
		return Geocoding(self.key)

	def weather(self):
		return Weather(self.key)


