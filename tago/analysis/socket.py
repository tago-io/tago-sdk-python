from socketIO_client import SocketIO, LoggingNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

options = {'reconnectionDelay': 10000, 'reconnection': true}

class TagoRealTime:

    def __init__(self, address, token):
        self.socket   = SocketIO(address, 443, options)
        self.token    = token
        self.callback = callback

    def on_connect(self):
        self.socket.emit('register', self.token)

    def on_data(self, data):
        self.callback(data)

    def listening(self, wait):
        self.socket.on('connect', self.on_connect)
        self.socket.on('data', self.on_data)

        if wait:
            self.socket.wait(seconds=wait)
        else:
            self.socket.wait()

        return self.socket

    def get_socket():
        self.socket
