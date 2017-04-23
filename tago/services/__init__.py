import email
import sms
import socket
import console
import mqtt

class Services:
	def __init__(self, token):
		self.token = token

	def sms(self): 
		return new SMS(self.token)

	def email(self): 
		return new Email(self.token)

	def console(self):
		return new Console(self.token)

	def socket(self):
		return new Socket(self.token)

	def MQTT(self):
		return new MQTT(self.token)


