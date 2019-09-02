from socketIO_client import SocketIO, LoggingNamespace
# import logging
# logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
# logging.basicConfig()


class TagoRealTime:
  def __init__(self, address, token, callback):
    self.socket = SocketIO(address, 443, LoggingNamespace)
    self.token = token
    self.callback = callback

  def on_connect(self):
    self.socket.emit('register', self.token)

  def listening(self, channel, wait):
    self.socket.on('connect', self.on_connect)
    self.socket.on(channel, self.callback)

    if wait:
      self.socket.wait(seconds=wait)
    else:
      self.socket.wait()

    return self.socket

  def stopListening(self, channel):
    self.socket.off(channel)
