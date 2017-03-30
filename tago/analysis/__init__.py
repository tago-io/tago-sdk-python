from socket import TagoRealTime
import os

REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Analysis:
	def __init__(self, analysis, token):
		self.token = token
		self.analysis = analysis

	def run_analysis(self, callback, wait):
		return TagoRealTime(REALTIME, self.token, callback).listening(wait)
