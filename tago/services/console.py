import time

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

class Console:
	def __init__(self, analysis_token):
		self.analysis_token = analysis_token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': analysis_token }

    def send(self, message, timestamp):
        if not timestamp:
            timestamp = time.time() * 1000 # Time from epoch in sec*1000

    	data = {'message':message, 'timestamp': timestamp}
    	url = '{api_endpoint}/analysis/services/console/send'.format(api_endpoint=API_TAGO)
        return requests.post(self.url(id=False), data=json.dumps(data), headers=self.default_headers).json()
