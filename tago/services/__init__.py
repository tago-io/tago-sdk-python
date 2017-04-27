import email
import sms
import socket
import console
import mqtt

class Services:
	def __init__(self, token):
		self.token = token

	def sms(self): 
		return SMS(self.token)

	def email(self): 
		return Email(self.token)

	def console(self):
		return Console(self.token)

	def socket(self):
		return Socket(self.token)

	def MQTT(self):
		return MQTT(self.token)


