
import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables
import _share as share
from socket import TagoRealTime
from dashboards_widgets import DashboardsWidgets

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Dashboards:

	def __init__(self, acc_token):
		self.token = acc_token
		self.default_headers = { 'content-type': 'application/json', 'Account-Token': acc_token }

	# List Dashboards
	def list(self):
		return requests.get('{api_endpoint}/dashboard'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

	# Create a Dashboard
	def create(self, data):
		data = data if data else {}
		return requests.post('{api_endpoint}/dashboard'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

	# Edit a Dashboard
	def edit(self, dashboard_id, data):
		data = data if data else {}
		return requests.put('{api_endpoint}/dashboard/{dashboard_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers, data=json.dumps(data)).json()

	# Delete a Dashboard
	def delete(self, dashboard_id):
		return requests.delete('{api_endpoint}/dashboard/{dashboard_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	# Get Information for a Dashboard
	def info(self, dashboard_id):
		if dashboard_id is None or dashboard_id == '':
		    #return None # Dashboard ID parameter is obligatory.
		    raise ValueError('dashboard_id must be set')

		return requests.get('{api_endpoint}/dashboard/{dashboard_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()


	def listening(self, dashboard_id, func, wait):
		if dashboard_id is None or dashboard_id == '':
			raise ValueError('dashboard_id must be set')

		self.realtime = TagoRealTime(REALTIME, self.token, func)
		self.realtime.listening(dashboard_id, wait)

		return "Listening to Dashboard "+dashboard_id


	def stopListening(self, dashboard_id):
		if self.realtime is None:
			raise ValueError('realtime has not been initialized')

		self.realtime.stopListening(dashboard_id)

		return "Stop listening to Dashboard "+dashboard_id

	# Get share list of the dashboard
	def shareList(self, dashboard_id):
		if dashboard_id is None or dashboard_id == '':
			raise ValueError('dashboard_id must be set')
		return share.list("dashboard",dashboard_id,self.default_headers)

	# Share the dashboard with another person
	def shareSendInvite(self, dashboard_id, data):
		data = data if data else {}
		if dashboard_id is None or dashboard_id == '':
		    raise ValueError('dashboard_id must be set')
		elif data['email'] is None or data['email'] == '':
		    raise ValueError('email must be set in data')
		return share.invite("dashboard",dashboard_id,data,self.default_headers)

	# Change permssions of dashboard
	def shareEdit(self, share_id, data):
		data = data if data else {}
		if share_id is None or share_id == '':
		    raise ValueError('share_id must be set')
		elif data['email'] is None or data['email'] == '':
		    raise ValueError('email must be set in data')
		return share.edit("dashboard",share_id,data,self.default_headers)

	# Remove share of a dashboard
	def shareDelete(self, share_id):
		if share_id is None or share_id == '':
		    raise ValueError('share_id must be set')
		return share.remove("dashboard",share_id,self.default_headers)

	# Generate new public token for the dashboard
	def genPublicToken(self, dashboard_id):
		if dashboard_id is None or dashboard_id == '':
		    raise ValueError('dashboard_id must be set')

		return requests.get('{api_endpoint}/dashboard/{dashboard_id}/share/public'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	# Clone the dashboard with special parameters
	def shareClone(self, dashboard_id, data):
		if dashboard_id is None or dashboard_id == '':
		    raise ValueError('dashboard_id must be set')
		elif data.email is None:
		    raise ValueError('email must be set in data')

		return requests.post('{api_endpoint}/dashboard/{dashboard_id}/share/copy'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	def get_widgets(self):
		return DashboardsWidgets(self.token)
