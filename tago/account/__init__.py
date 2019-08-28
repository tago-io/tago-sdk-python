import requests  # Used to make HTTP requests
import json  # Used to parse JSON
import os  # Used to infer environment variables

from .actions import Actions
from .analysis import Analysis
from .files import Files
from .buckets import Buckets
from .dashboards import Dashboards
from .devices import Devices
from .notifications import Notifications
from .middlewares import Middlewares
from .tags import Tags
from .paymentMethods import PaymentMethods
from .plan import Plan
from .paymentHistory import PaymentHistory
from .explore import Explore
from .connector import Connector
from .template import Template
from .accessManagement import AccessManagement
from .run import TagoIORUN
from .profiles import Profiles
from .service_authorization import ServiceAuth

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
REALTIME = os.environ.get('TAGO_REALTIME') or 'https://realtime.tago.io'


class Account:
    def __init__(self, token):
        self.token = token
        self.default_headers = {
            'content-type': 'application/json', 'Account-Token': token}

    # TODO: test it
    def info(self):
        return requests.get('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: ask Vitor about params = undefined in javascript SDK
    def summary(self, params):
        return requests.get('{api_endpoint}/account/summary'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: test it
    def statistics(self, params):
        return requests.get('{api_endpoint}/statistics'.format(api_endpoint=API_TAGO), params=params, headers=self.default_headers).json()

    # TODO: test it
    def edit(self, data):
        return requests.put('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO: test it
    def delete(self):
        return requests.delete('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: test it
    def profileList(self):
        return requests.get('{api_endpoint}/account/profile'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: test it
    def profileCreate(self, data):
        return requests.post('{api_endpoint}/account/profile'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO: test it
    def profileDelete(self, profile_id):
        return requests.delete('{api_endpoint}/account/profile/{profile_id}'.format(api_endpoint=API_TAGO, profile_id=profile_id), headers=self.default_headers).json()

    # TODO: need review
    def tokenList(self, page=1, amount=20, filter={}, fields=['name', 'token', 'permission'], orderBy='created_at,desc'):
        params = {
            'page': page,
            'filter': filter,
            'amount': amount,
            'orderBy': orderBy,
            'fields': fields,
        }
        return requests.get('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(params)).json()

    # TODO: test it
    def tokenCreate(self, data):
        return requests.post('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    # TODO: test it
    def tokenDelete(self):
        return requests.delete('{api_endpoint}/account/profile/token'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: test it
    def login(self, data):
        return requests.post('{api_endpoint}/account/profile/login'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(data)).json()

    @staticmethod
    # TODO: test it
    def passwordRecover(self, email):
        return requests.get('{api_endpoint}/account/passwordreset/{email}'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: test it
    def passwordChange(self, password):
        return requests.post('{api_endpoint}/account/passwordreset'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(password)).json()

    # TODO: need review
    def create(self, name, email, password, cpassword, country, timezone, company, newsletter, developer):
        params = {
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
        return requests.post('{api_endpoint}/account'.format(api_endpoint=API_TAGO), headers=self.default_headers, data=json.dumps(params)).json()

    # TODO: test it
    @staticmethod
    def resendConfirmation(self, email):
        return requests.get('{api_endpoint}/account/resend_confirmation/{email}'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: test it
    def confirmAction(self, token):
        return requests.get('{api_endpoint}/account/confirm/{token}'.format(api_endpoint=API_TAGO), headers=self.default_headers).json()

    # TODO: verify if auditlog will be needed

    # TODO: create all sub-methods
    def getActions(self):
        return Actions(self.token)

    def getAnalysis(self):
        return Analysis(self.token)

    def getBuckets(self):
        return Buckets(self.token)

    def getFiles(self):
        return Files(self.token)

    def getDashboards(self):
        return Dashboards(self.token)

    def getDevices(self):
        return Devices(self.token)

    def getNotifications(self):
        return Notifications(self.token)

    def getMiddlewares(self):
        return Middlewares(self.token)

    def getTags(self):
        return Tags(self.token)

    def getPaymentMethods(self):
        return PaymentMethods(self.token)

    def getPlan(self):
        return Plan(self.token)

    def getPaymentHistory(self):
        return PaymentHistory(self.token)

    def getExplore(self):
        return Explore(self.token)

    def getConnector(self):
        return Connector(self.token)

    def getTemplate(self):
        return Template(self.token)

    def getAccessManagement(self):
        return AccessManagement(self.token)

    def getRun(self):
        return TagoIORUN(self.token)

    def getServiceAuthorization(self):
        return ServiceAuth(self.token)

    def getProfiles(self):
        return Profiles(self.token)
