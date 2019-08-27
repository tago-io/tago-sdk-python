
import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables
import _share as share
from dashboards_widgets import Widgets

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Dashboards:
	def __init__(self, acc_token):
		self.token = acc_token
		self.default_headers = { 'content-type': 'application/json', 'Account-Token': acc_token }

	# TODO: need review
	def list(self, page = 1, fields = ['id', 'name'], filter = {}, amount = 20, orderBy = 'label,asc'):
		params = {
			'page': page,
			'filter': filter,
			'fields': fields,
			'amount': amount,
			'orderBy': orderBy,
		}
		return requests.get('{api_endpoint}/dashboard'.format(api_endpoint=API_TAGO), headers=self.default_headers, data = json.dumps(params)).json()

	# TODO test it
	# Create a Dashboard
	def create(self, data):
		data = data if data else {}
		return requests.post('{api_endpoint}/dashboard'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

	# TODO test it
	# Edit a Dashboard
	def edit(self, dashboard_id, data):
		data = data if data else {}
		return requests.put('{api_endpoint}/dashboard/{dashboard_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers, data=json.dumps(data)).json()

	# TODO test it
	# Delete a Dashboard
	def delete(self, dashboard_id):
		return requests.delete('{api_endpoint}/dashboard/{dashboard_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	# TODO test it
	# Get Information for a Dashboard
	def info(self, dashboard_id):
		if dashboard_id is None or dashboard_id == '':
		    #return None # Dashboard ID parameter is obligatory.
		    raise ValueError('Dashboard ID parameter is obrigatory.')

		return requests.get('{api_endpoint}/dashboard/{dashboard_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	# TODO test it
	def duplicate(self, dashboard_id, data):
		data = data if data else {}
		if dashboard_id is None or dashboard_id == '':
			raise ValueError('Dashboard ID parameter is obrigatory.')
		return requests.post('{api_endpoint}/dashboard/{dashboard_id}/duplicate'.format(api_endpoint = API_TAGO, dashboard_id = dashboard_id), headers = self.default_headers, data = json.dumps(data)).json()

	# TODO test it
	# Get share list of the dashboard
	def shareList(self, dashboard_id):
		if dashboard_id is None or dashboard_id == '':
			raise ValueError('dashboard_id must be set')
		return share.list("dashboard",dashboard_id,self.default_headers)

	# TODO test it
	# Share the dashboard with another person
	def shareSendInvite(self, dashboard_id, data):
		data = data if data else {}
		if dashboard_id is None or dashboard_id == '':
		    raise ValueError('dashboard_id must be set')
		elif data['email'] is None or data['email'] == '':
		    raise ValueError('email must be set in data')
		return share.invite("dashboard",dashboard_id,data,self.default_headers)

	# TODO test it
	# Change permssions of dashboard
	def shareEdit(self, share_id, data):
		data = data if data else {}
		if share_id is None or share_id == '':
		    raise ValueError('share_id must be set')
		elif data['email'] is None or data['email'] == '':
		    raise ValueError('email must be set in data')
		return share.edit(share_id, data, self.default_headers)

	# TODO test it
	# Remove share of a dashboard
	def shareDelete(self, share_id):
		if share_id is None or share_id == '':
		    raise ValueError('share_id must be set')
		return share.remove(share_id, self.default_headers)

	# TODO test it
	# Generate new public token for the dashboard
	def genPublicToken(self, dashboard_id):
		if dashboard_id is None or dashboard_id == '':
		    raise ValueError('dashboard_id must be set')

		return requests.get('{api_endpoint}/dashboard/{dashboard_id}/share/public'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	# TODO test it
	# Clone the dashboard with special parameters
	def shareClone(self, dashboard_id, data):
		if dashboard_id is None or dashboard_id == '':
		    raise ValueError('dashboard_id must be set')
		elif data.email is None:
		    raise ValueError('email must be set in data')

		return requests.post('{api_endpoint}/dashboard/{dashboard_id}/share/copy'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id), headers=self.default_headers).json()

	def listDevicesRelated(self, dashboard_id):
		return requests.get('{api_endpoint}/dashboard/{dashboard_id}/devices'.format(api_endpoint = API_TAGO, dashboard_id = dashboard_id), headers = self.default_headers).json()

	def getWidgets(self):
		return Widgets(self.token)
