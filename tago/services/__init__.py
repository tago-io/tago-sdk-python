from emailService import Email
from sms import Sms
from socket import Socket
from console import Console
from mqtt import Mqtt
from attachment import Attachment
from notification import Notification

class Services:
	def __init__(self, token):
		self.token = token

	def sms(self): 
		return Sms(self.token)

	def email(self):
		return Email(self.token)

	def console(self):
		return Console(self.token)

	def socket(self):
		return Socket(self.token)

	def MQTT(self):
		return Mqtt(self.token)

	def notification(self):
		return Notification(self.token)

	def attachment(self):
		return Attachment(self.token)


