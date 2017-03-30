from socket import TagoRealTime
import os

REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Analysis:
	def __init__(self, analysis, token):
		self.token = token
		self.analysis = analysis

	def run(environment, data , token):
		if data.empty():
			data = []

		context = {token, environment}
		this.analysis(context, data)

	def localRuntime(self, callback, wait):
		return TagoRealTime(REALTIME, self.token, callback).listening(wait)


