from socketIO_client import SocketIO, LoggingNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()
import json

# options = {'reconnectionDelay': 10000, 'reconnection': true}

class TagoRealTime:

    def __init__(self, address, token, callback):
        self.socket   = SocketIO(address, 443, LoggingNamespace)
        self.token    = token
        self.callback = callback

    def run(self, environment, data, token):
        if len(data) == 0:
            data = []

        context = {"token":token, "environment":environment}
        self.callback(context, data)

    def on_connect(self, arg):
        print arg['result']

    def on_scope(self, arg):
        for x in arg:
            self.run(x['environment'], x['data'], self.token)

    def listening(self, wait):
        self.socket.emit('register:analysis', self.token)
        self.socket.on('register:analysis', self.on_connect)

        self.socket.on('run:analysis', self.on_scope)
        
        if wait:
            self.socket.wait(seconds=wait)
        else:
            self.socket.wait()

        return self.socket

    def get_socket():
        self.socket
