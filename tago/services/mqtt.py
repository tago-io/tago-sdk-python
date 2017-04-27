
API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

class Console:
	def __init__(self, analysis_token):
		self.analysis_token = analysis_token
        self.default_headers = { 'content-type': 'application/json', 'Device-Token': analysis_token }

    # publish MQTT
    # message{string} : Message
    # bucket{string} : Bucket to recive message 
    # returns promise

    def publish(self, message, bucket):
    	data = {'message':message, 'bucket': bucket}
    	url = '{api_endpoint}/analysis/services/mqtt/publish'.format(api_endpoint=API_TAGO)
        return requests.post(self.url(id=False), data=json.dumps(data), headers=self.default_headers).json()
