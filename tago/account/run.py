import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGOIO_REALTIME') or 'https://realtime.tago.io'
from ..internal import fixFilter

class TagoIORUN:
  def __init__(self, acc_token):
    self.token = acc_token
    self.default_headers = {
      'content-type': 'application/json', 'Account-Token': acc_token}
    return

  def edit(self, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/run'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def info(self):
    return requests.get('{api_endpoint}/run'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def listUsers(self, page=1, fields=['id', 'name'], filter={}, amount=20, orderBy='name,asc'):
    params = {
      'page': page,
      'filter': filter,
      'fields': fields,
      'amount': amount,
      'orderBy': orderBy,
    }
    params = fixFilter(params, filter)

    return requests.get('{api_endpoint}/run/users'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=params).json()

  def getUserInfo(self, userID):
    return requests.get('{api_endpoint}/run/users/{userID}'.format(api_endpoint=API_TAGO, userID=userID), headers=self.default_headers).json()

  def loginAsUser(self, userID):
    return requests.get('{api_endpoint}/run/users/{userID}/login'.format(api_endpoint=API_TAGO, userID=userID), headers=self.default_headers).json()

  def userEdit(self, userID, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/run/users/{userID}'.format(api_endpoint=API_TAGO, userID=userID), headers=self.default_headers, json=data).json()

  def createUser(self, data):
    data = data if data else {}
    return requests.post('{api_endpoint}/run/users'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def deleteUser(self, userID):
    return requests.delete('{api_endpoint}/run/users/{userID}'.format(api_endpoint=API_TAGO, userID=userID), headers=self.default_headers).json()

  def emailTest(self, dataObj):
    data = {
      'subject': dataObj.subject,
      'body': dataObj.body
    }
    return requests.post('{api_endpoint}/run/email_test'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def notificationCreate(self, user_id, data):
    data = data if data else {}
    data['run_user'] = user_id
    return requests.post('{api_endpoint}/run/notification'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def notificationEdit(self, notification_id, data):
    data = data if data else {}
    return requests.put('{api_endpoint}/run/notification/{notification_id}'.format(api_endpoint=API_TAGO, notification_id=notification_id), headers=self.default_headers, json=data).json()

  def notificationDelete(self, notification_id):
    return requests.delete('{api_endpoint}/run/notification/{notification_id}'.format(api_endpoint=API_TAGO, notification_id=notification_id), headers=self.default_headers).json()

  def notificationList(self, user_id):
    return requests.get('{api_endpoint}/run/notification/{user_id}'.format(api_endpoint=API_TAGO, user_id=user_id), headers=self.default_headers).json()
