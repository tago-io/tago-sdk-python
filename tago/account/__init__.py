class Account:
	def __init__(self, token):
		self.token = token
		# Not sure about this next line..the 'default headers part'
		self.default_headers = { 'content-type': 'application/json', 'Account-Token': token }