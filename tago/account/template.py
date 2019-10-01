import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class Template:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def generateTemplate(self, templateObj):
    return requests.post('{api_endpoint}/template'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(templateObj)).json()

  def installTemplate(self, template_id, data={}):
    return requests.post('{api_endpoint}/template/{template_id}'.format(api_endpoint=API_TAGO, template_id=template_id), headers=self.default_headers, json=data).json()

  @staticmethod
  def getTemplateAnonymous(self, template_id):
    return requests.post('{api_endpoint}/template/{template_id}'.format(api_endpoint=API_TAGO, template_id=template_id), headers=self.default_headers).json()

  def getTemplate(self, template_id):
    return Template.getTemplateAnonymous(self, template_id)
