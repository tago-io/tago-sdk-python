from socketIO_client import SocketIO, LoggingNamespace
import logging
logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()

# options = {'reconnectionDelay': 10000, 'reconnection': true}

class TagoRealTime:

    def __init__(self, address, token):
        self.socket   = SocketIO(address, 443, LoggingNamespace)
        self.token    = token
        self.callback = callback

    def on_response(*arg):
        print arg

    def listening(self, wait):
        self.socket.on('register:analysis', on_response)
        self.socket.on('run:analysis', on_response)
        self.socket.emit('register:analysis', self.token)

        if wait:
            self.socket.wait(seconds=wait)
        else:
            self.socket.wait()

        return self.socket

    def get_socket():
        self.socket
