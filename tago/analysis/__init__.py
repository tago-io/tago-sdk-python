from socket import TagoRealTime
import os

REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Analysis:
	# need to check process.env.TAGO_RUNTIME with Vitor
	def __init__(self, analysis, token):
		self.token = token
		self.analysis = analysis

	# to do
	def run(self, callback, wait):
		return TagoRealTime(REALTIME, self.token, callback).listening(wait)

	# needs to be finished
	def localRuntime():
		if not self.token:
			raise Exception('To run locally, needs a token.')
		# run local 
