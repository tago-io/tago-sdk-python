from .emailService import Email
from .sms import Sms
from .console import Console
from .mqtt import Mqtt
from .attachment import Attachment
from .notification import Notification


class Services:
  def __init__(self, token):
    self.token = token

  @property
  def sms(self):
    return Sms(self.token)

  @property
  def email(self):
    return Email(self.token)

  @property
  def console(self):
    return Console(self.token)

  @property
  def MQTT(self):
    return Mqtt(self.token)

  @property
  def notification(self):
    return Notification(self.token)

  @property
  def attachment(self):
    return Attachment(self.token)
