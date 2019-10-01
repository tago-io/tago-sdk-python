import requests # Used to make HTTP requests
import json # Used to parse JSON
import os # Used to infer environment variables
from ..internal import fixFilter

from.actions import Actions
from.analysis import Analysis
from.files import Files
from.buckets import Buckets
from.dashboards import Dashboards
from.devices import Devices
from.notifications import Notifications
from.middlewares import Middlewares
from.tags import Tags
from.paymentMethods import PaymentMethods
from.plan import Plan
from.paymentHistory import PaymentHistory
from.explore import Explore
from.connector import Connector
from.template import Template
from.accessManagement import AccessManagement
from.run import TagoIORUN
from.profiles import Profiles
from.service_authorization import ServiceAuth

API_TAGO=os.environ.get('TAGO_API') or 'https://api.tago.io'
REALTIME=os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'

class Account:
  def __init__(self, token):
    self.token=token
    self.default_headers={
      'content-type': 'application/json',
      'Account-Token': token
    }
    # self.devices = Devices(self.token)

  def info(self):
    return requests.get('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def summary(self, params=None):
    return requests.get('{api_endpoint}/account/summary'.format(api_endpoint=API_TAGO), headers=self.default_headers, params=params).json()

  def statistics(self, params):
    return requests.get('{api_endpoint}/statistics'.format(api_endpoint=API_TAGO), params=params, headers=self.default_headers).json()

  def edit(self, data):
    return requests.put('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def delete(self):
    return requests.delete('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def profileList(self):
    return requests.get('{api_endpoint}/account/profile'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def profileCreate(self, data):
    return requests.post('{api_endpoint}/account/profile'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def profileDelete(self, profile_id):
    return requests.delete('{api_endpoint}/account/profile/{profile_id}'.format(api_endpoint=API_TAGO, profile_id=profile_id), headers=self.default_headers).json()

  def tokenList(self, page=1, amount=20, filter={}, fields=['name', 'token', 'permission'], orderBy='created_at,desc'):
    params={
      'page': page,
      'filter': filter,
      'amount': amount,
      'orderBy': orderBy,
      'fields': fields,
    }
    params = fixFilter(params, filter)

    return requests.get('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=params).json()

  def tokenCreate(self, data):
    return requests.post('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def tokenDelete(self):
    return requests.delete('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

  def login(self, data):
    return requests.post('{api_endpoint}/account/profile/login'.format(api_endpoint=API_TAGO), headers=self.default_headers, json=data).json()

  def passwordRecover(self, email):
    return requests.get('{api_endpoint}/account/passwordreset/{email}'.format(api_endpoint=API_TAGO, email=email), headers=self.default_headers).json()

  def passwordChange(self, password):
    return requests.post('{api_endpoint}/account/passwordreset'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(password)).json()

  def create(self, name, email, password, cpassword, country, timezone, company, newsletter, developer):
    params={
      'name': name,
      'email': email,
      'password': password,
      'cpassword': cpassword,
      'country': country,
      'timezone': timezone,
      'company': company,
      'newsletter': newsletter,
      'developer': developer,
    }
    return requests.post('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=params).json()

  @staticmethod
  def resendConfirmation(self, email):
    return requests.get('{api_endpoint}/account/resend_confirmation/{email}'.format(api_endpoint=API_TAGO, email=email), headers=self.default_headers).json()

  def confirmAction(self, token):
    return requests.get('{api_endpoint}/account/confirm/{token}'.format(api_endpoint=API_TAGO, token=token), headers=self.default_headers).json()

  @property
  def actions(self):
    return Actions(self.token)

  @property
  def analysis(self):
    return Analysis(self.token)

  @property
  def buckets(self):
    return Buckets(self.token)

  @property
  def files(self):
    return Files(self.token)

  @property
  def dashboards(self):
    return Dashboards(self.token)

  @property
  def devices(self):
    return Devices(self.token)

  @property
  def notifications(self):
    return Notifications(self.token)

  @property
  def middlewares(self):
    return Middlewares(self.token)

  @property
  def tags(self):
    return Tags(self.token)

  @property
  def paymentMethods(self):
    return PaymentMethods(self.token)

  @property
  def plan(self):
    return Plan(self.token)

  @property
  def paymentHistory(self):
    return PaymentHistory(self.token)

  @property
  def explore(self):
    return Explore(self.token)

  @property
  def connector(self):
    return Connector(self.token)

  @property
  def template(self):
    return Template(self.token)

  @property
  def accessManagement(self):
    return AccessManagement(self.token)

  @property
  def run(self):
    return TagoIORUN(self.token)

  @property
  def ServiceAuthorization(self):
    return ServiceAuth(self.token)

  @property
  def profiles(self):
    return Profiles(self.token)
