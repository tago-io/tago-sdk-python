import currency
import distance
import geocoding
import weather

class Services:
	def __init__(self, API_KEY):
		self.API_KEY = API_KEY

	def currency(self): 
		return Currency(self.API_KEY)

	def distance(self):
		return Distance(self.API_KEY)

	def geocoding(self):
		return Geocoding(self.API_KEY)

	def weather(self):
		return Weather(self.API_KEY)


