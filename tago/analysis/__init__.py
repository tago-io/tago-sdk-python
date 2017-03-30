from socket import TagoRealTime

REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Analysis:
	def __init__(self, analysis, token):
		self.token = token
		self.analysis = analysis

	def run(environment, data = [], token):

		context = {token, environment}
		this.analysis(context, data)

	def on_response(*args):
		print args


	def localRuntime(self, callback):
		r_sock = TagoRealTime(REALTIME, this.token)

		r_sock.get_socket().emit('register:analysis', this.token)
		r_sock.get_socket().on('register:analysis', on_response)

		r_sock.get_socket().on('register:analysis', on_response)



