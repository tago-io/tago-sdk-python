
from comum.tago_request import request
from config import config
from comum.default_headers import default_headers
from dasboards.widgets import Widgets
from utils import Realtime
from _share import share

class Dashboard:

	def __init__(self, acc_token):
		self.token = acc_token
		self.default_options = {"json":True,"headers":default_headers(self)}

	# List Dashboards
	def list:
		url = '{api_url}/dashbaord'.format(api_url=config.api_url)
		method = "GET"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return request(options)

	# Create a Dashboard
	def create(data):
		data = data if data else {}
		url = '{api_url}/dashbaord'.format(api_url=config.api_url)
		method = "POST"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		options["data"] = data
		return request(options)

	# Edit a Dashboard
	def edit(dashboard_id, data):
		data = data if data else {}
		url = '{api_url}/dashbaord/{dashboard_id}'.format(api_url=config.api_url, dashboard_id=dashboard_id)
		method = "PUT"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		options["data"] = data
		return request(options)

	# Delete a Dashboard
	def delete(dashboard_id):
		url = '{api_url}/dashbaord/{dashboard_id}'.format(api_url=config.api_url, dashboard_id=dashboard_id)
		method = "DELETE"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return request(options)

	# Get Information for a Dashboard
	def info(dashboard_id):
		if(!dashbaord or dashboard_id == ''):
			return new Promise...url
		url = '{api_url}/dashbaord/{dashboard_id}'.format(api_url=config.api_url, dashboard_id=dashboard_id)
		method = "GET"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return request(options)