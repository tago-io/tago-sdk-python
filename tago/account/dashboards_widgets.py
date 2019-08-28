import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'


class Widgets:
    def __init__(self, acc_token):
        self.token = acc_token
        self.default_headers = {
            'content-type': 'application/json', 'Account-Token': acc_token}
        return

    # TODO test it
    # Create a Dashboard Widget
    # @param  {String} dashboard id
    # @param  {JSON} data
    # @return {Promise}
    def create(self, dash_id, data):
        data = data if data else {}
        return requests.post('{api_endpoint}/dashboard/{dash_id}/widget/'.format(api_endpoint=API_TAGO, dash_id=dash_id), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO test it
    # Edit the Dashboard Widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @param  {Object} data
    # @return {Promise}
    def edit(self, dash_id, widget_id, data):
        data = data if data else {}
        return requests.put('{api_endpoint}/dashboard/{dash_id}/widget/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO test it
    # Delete the Dashboard Widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @return {Promise}
    def delete(self, dash_id, widget_id):
        return requests.delete('{api_endpoint}/dashboard/{dash_id}/widget/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers).json()

    # TODO review it
    # Get Info of the Dashboard Widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @return {Promise}
    # def info(self, dash_id, widget_id):
    # 	# if widget_id is null, then call list
    # 	if widget_id is None or widget_id == '':
        #     return self.list()

    # 	return requests.get('{api_endpoint}/dashboard/{dash_id}/widget/{widget_id}'.format(api_endpoint=API_TAGO, dash_id=dash_id, widget_id=widget_id), headers=self.default_headers).json()

    # TODO review it
    # Get all data for the current widget
    # @param  {String} dashboard id
    # @param  {String} widget id
    # @return {Promise}
    def getData(self, dashboard_id, widget_id, overwrite={}):
        params = {
            'overwrite': overwrite,
        }
        return requests.get('{api_endpoint}/data/{dashboard_id}/{widget_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id, widget_id=widget_id), headers=self.default_headers, params=json.dumps(params)).json()

    # TODO review it
    # Update value of variable for the current widget
    # @param  {String} dashboard id
    # @param  {String} widget_id
    # @param  {JSON} data
    # @return {Promise}
    def sendData(self, dashboard_id, widget_id, data, bypassBucket):
        data = data if data else {}
        params = {
            'bypass_bucket': bypassBucket or False,
        }
        return requests.post('{api_endpoint}/data/{dashboard_id}/{widget_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id, widget_id=widget_id), headers=self.default_headers, data=json.dumps(data), params=json.dumps(params)).json()

    # TODO review it
    def runAnalysis(self, dashboard_id, widget_id, data):
        return requests.post('{api_endpoint}/data/{dashboard_id}/{widget_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id, widget_id=widget_id), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO review it
    def deleteData(self, dashboard_id, widget_id, ids):
        params = {
            'ids': ids,
        }
        return requests.delete('{api_endpoint}/data/{dashboard_id}/{widget_id}'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id, widget_id=widget_id), headers=self.default_headers, params=json.dumps(params)).json()

    # TODO review it
    def tokenGenerate(self, dashboard_id, widget_id):
        return requests.get('{api_endpoint}/dashboard/{dashboard_id}/widget/{widget_id}/token'.format(api_endpoint=API_TAGO, dashboard_id=dashboard_id, widget_id=widget_id), headers=self.default_headers).json()
