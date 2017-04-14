
import requests
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
		return requests(options)

	# Create a Dashboard
	def create(data):
		data = data if data else {}
		url = '{api_url}/dashbaord'.format(api_url=config.api_url)
		method = "POST"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		options["data"] = data
		return requests(options)

	# Edit a Dashboard
	def edit(dashboard_id, data):
		data = data if data else {}
		url = '{api_url}/dashbaord/{dashboard_id}'.format(api_url=config.api_url, dashboard_id=dashboard_id)
		method = "PUT"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		options["data"] = data
		return requests(options)

	# Delete a Dashboard
	def delete(dashboard_id):
		url = '{api_url}/dashbaord/{dashboard_id}'.format(api_url=config.api_url, dashboard_id=dashboard_id)
		method = "DELETE"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return requests(options)

	# Get Information for a Dashboard
	def info(dashboard_id):
		if(!dashbaord or dashboard_id == ''):
			return Promise
		url = '{api_url}/dashbaord/{dashboard_id}'.format(api_url=config.api_url, dashboard_id=dashboard_id)
		method = "GET"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return requests(options)

	# Get Information for a Dashboard
	def listeneing(dashboard_id, func, realtime):
		if(!dashbaord or dashboard_id == ''):
			return Promise

		if(!this.realtime and !realtime):
			self.realtime = Realtime(self.token)
		realtime =  realtime if realtime or self.realtime
		realtime.get_socket.on('{dashboard:{dashboard_id}'.format(dashboard_id=dashboard_id), func)
		
		return Promise


	# Stop listening to a dashboard by its ID
	def stopListening(id, realtime):
		if(!self.realtime and !realtime):
			return None

		realtime =  realtime if realtime or self.realtime
		realtime.get_socket.off("dashboard:{id}".format(id=id))

	# Get share list of the dashboard
	def shareList(dashboard_id):
		if(!dashboard_id or dashboard_id == ''):
			return Promise
		return share.list("dashboard",dashboard_id,self.default_options)

	# Share the dashboard with another person
	def shareSendInvite(dashboard_id, data):
		data = data if data else {}
		if(!dashboard_id or dashboard_id == ''):
			return Promise
		elif !data.email:
			return Promise
		return share.invite("dashboard",dashboard_id,this.default_options)


	# Change permssions of bucket
	def shareEdit(share_id, data):
		data = data if data else {}
		if(!share_id or share_id == ''):
			return Promise
		elif !data.email:
			return Promise
		return share.edit("dashboard",share_id,this.default_options)

	# Remove share of a bucket
	def shareDelete(share_id):
		if(!share_id or share_id == ''):
			return Promise
		return share.remove("dashboard",share_id,this.default_options)

	# Generate new public token for the dashboard
	def genPublicToken(dashboard_id):
		if(!dashboard_id or dashboard_id == ''):
			return Promise

		url = "{api_url}/dashboard/{dashboard_id}/share/public".format(api_url=config.api_url,dashboard_id=dashboard_id)
		method = "GET"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return requests(options)


	# Clone the dashboard with special parameters
	def shareClone(dashboard_id, data):
		if (!dashboard_id or dashboard_id == ''):
			return Promise
		elif !data.email:
			return Promise

		url = "{api_url}/dashboard/{dashboard_id}/share/copy".format(api_url=config.api_url,dashboard_id=dashboard_id)
		method = "POST"

		options = this.default_options
		options["url"] = url
		options["method"] = method
		return requests(options)

	def get_widgets():
		return Widgets(self.token)



