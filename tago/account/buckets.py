import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables
from ..internal import fixFilter

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'


class Buckets:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def list(self, page=1, fields=['id', 'name'], filter={}, amount=20, orderBy='name,asc'):
    params = {
      'page': page,
      'fields': fields,
      'filter': filter,
      'amount': amount,
      'orderBy': orderBy,
    }
    params = fixFilter(params, filter)

    return requests.get('{api_endpoint}/bucket'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=params).json()

  def create(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/bucket'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def edit(self, bkt_id, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/bucket/{bkt_id}'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers, json=data).json()

  def delete(self, bkt_id):
    return requests.delete('{api_endpoint}/bucket/{bkt_id}'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers).json()

  def deleteVariable(self, bkt_id, data):
    data = data if data else {}
    return requests.delete('{api_endpoint}/bucket/{bkt_id}/variable'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers, json=data).json()

  def listVariables(self, bkt_id, show_amount=False, show_deleted=False, resolveOriginName=False):
    params = {
      'amount': show_amount,
      'deleted': show_deleted,
      'resolveOriginName': resolveOriginName,
    }
    return requests.get('{api_endpoint}/bucket/{bkt_id}/variable'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers, params=params).json()

  def getDevicesAssociated(self, bkt_id):
    if bkt_id is None or bkt_id == '':
      raise ValueError('Bucket ID parameter is obrigatory.')
    return requests.get('{api_endpoint}/bucket/{bkt_id}/device'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers).json()

  def amount(self, bkt_id):
    if bkt_id is None or bkt_id == '':
      raise ValueError('Bucket ID parameter is obrigatory.')
    return requests.get('{api_endpoint}/bucket/{bkt_id}/data_amount'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers).json()

  def info(self, bkt_id):
    # if bkt_id is null, then call list
    if bkt_id is None or bkt_id == '':
      return self.list()

    return requests.get('{api_endpoint}/bucket/{bkt_id}'.format(api_endpoint=API_TAGO, bkt_id=bkt_id), headers=self.default_headers).json()

  def backupInfo(self, backup_id):
    # if backup_id is null, then error!
    if backup_id is None or backup_id == '':
      raise ValueError('backup_id must be set')

    return requests.get('{api_endpoint}/backup/{backup_id}'.format(api_endpoint=API_TAGO, backup_id=backup_id), headers=self.default_headers).json()

  def backupList(self):
    return requests.get('{api_endpoint}/backup'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def backupDelete(self, backup_id):
    # if bkt_id is null, then error!
    if backup_id is None or backup_id == '':
      raise ValueError('backup_id must be set')

    return requests.delete('{api_endpoint}/backup/{backup_id}'.format(api_endpoint=API_TAGO, backup_id=backup_id), headers=self.default_headers).json()

  def backupRecover(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/backup/recover'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def exportData(self, output, buckets, options):
    if output is None or output == '':
      raise ValueError('output must be set')
    elif buckets is None or buckets[0] is None:
      raise ValueError('bucket must be set')

    data = {}
    data['buckets'] = buckets
    data['start_date'] = options['start_date']
    data['end_date'] = options['end_date']

    return requests.post('{api_endpoint}/data/export?output={output}'.format(api_endpoint=API_TAGO, output=output), headers=self.default_headers, json=data).json()
