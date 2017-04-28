import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'

class DashboardsWidgets:
    def __init__(self, token):
        self.token = token
        self.default_headers = { 'content-type': 'application/json', 'Account-Token': token }
        return

    # Create a Dashboard Widget
    # @param  {String} dashboard id
    # @param  {JSON} data
    # @return {Promise}
    def create(self, dash_id, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/dashboard/{dash_id}/widget/'.format(api_endpoint=API_TAGO, dash_id=dash_id), headers=self.default_headers, data=json.dumps(data)).json()

    # Edit the Dashboard Widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @param  {Object} data
    # @return {Promise}
    def edit(self, dash_id, widget_id, data):
    	data = data if data else {}
    	return requests.put('{api_endpoint}/dashboard/{dash_id}/widget/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers, data=json.dumps(data)).json()

    # Delete the Dashboard Widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @return {Promise}
    def delete(self, dash_id, widget_id):
    	return requests.delete('{api_endpoint}/dashboard/{dash_id}/widget/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers).json()

    # Get Info of the Dashboard Widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @return {Promise}
    def info(self, dash_id, widget_id):
    	# if widget_id is null, then call list
    	if widget_id is None or widget_id == '':
	    return self.list()

    	return requests.get('{api_endpoint}/dashboard/{dash_id}/widget/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers).json()

    # Get all data for the current widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @return {Promise}
    def getData(self, dash_id, widget_id):
    	return requests.get('{api_endpoint}/data/{dash_id}/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers).json()

    # Update value of variable for the current widget
    # @param  {String} dashboard id
    # @param  {String} widget_id
    # @param  {JSON} data
    # @return {Promise}
    def sendData(self, dash_id, widget_id, data):
    	data = data if data else {}
    	return requests.post('{api_endpoint}/data/{dash_id}/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers, data=json.dumps(data)).json()
