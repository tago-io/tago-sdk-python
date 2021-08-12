import requests
import json
import os

API_TAGO = os.environ.get('TAGOIO_API') or 'https://api.tago.io'


class Email:
  def __init__(self, analysis_token):
    self.analysis_token = analysis_token
    self.default_headers = {
      'content-type': 'application/json', 'Device-Token': analysis_token}

  # Send email
  # to{string} : email address to which the message is to be sent
  # subject{string} : Subject of the email
  # message{string} : Message of the email
  # s_from{string} : email to receive reply (optional)
  # attachment{json} : attachment to be sent
  # return promise

  def send(self, to, subject, message, s_from, attachment, html, whitelabel_url):
    if not to or not message or not subject:
      raise ValueError("Empty or Bad arguments")

    data = {'to': to, 'subject': subject, 'message': message,
        'from': s_from, 'attachment': attachment, 'html': html, 'whitelabel_url': whitelabel_url}
    url = '{api_endpoint}/analysis/services/email/send'.format(
      api_endpoint=API_TAGO)
    return requests.post(url, json=data, headers=self.default_headers).json()
