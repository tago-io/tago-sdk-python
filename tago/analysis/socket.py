from socketIO_client_nexus import SocketIO, LoggingNamespace
from requests.exceptions import ConnectionError
import logging
# logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
# logging.basicConfig()
import json
import sys

# options = {'reconnectionDelay': 10000, 'reconnection': true}


class TagoRealTime:

    def __init__(self, address, token, callback):
        try:
            self.socket = SocketIO(address, 443, LoggingNamespace)
        except ConnectionError:
            print('The server is down. Try again later.')
            raise

        self.token = token
        self.callback = callback

    def run(self, environment, data, token):
        if len(data) == 0:
            data = []

        context = {"token": token, "environment": environment}
        self.callback(context, data)

    def on_connect(self, arg):
        print(arg['result'])

    def on_scope(self, arg):
        print('aaaa')
        for x in arg:
            self.run(x['environment'], x['data'], self.token)

    def on_register_analysis(self, analysis):
        print('Analysis', analysis['name'], 'Started.')

    def on_reconnect(self, arg):
        self.socket.emit('register', self.token)

    def listening(self, wait):
        self.socket.emit('register', self.token)
        self.socket.once('register', self.on_connect)
        self.socket.once('register:analysis', self.on_register_analysis)

        self.socket.on('run:analysis', self.on_scope)
        self.socket.on('reconnect', self.on_reconnect)

        if wait:
            self.socket.wait(seconds=wait)
        else:
            self.socket.wait()

        return self.socket

    def get_socket():
        self.socket
