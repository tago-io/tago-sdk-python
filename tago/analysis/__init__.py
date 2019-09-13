from ..services import Services
import os

REALTIME_URL = os.environ.get('TAGO_REALTIME') or 'wss://realtime.tago.io'
TAGO_RUNTIME = os.environ.get('TAGO_RUNTIME') or False

if TAGO_RUNTIME == False:
  import socketio
  import asyncio
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)

class Analysis:
  def __init__(self, token):
    self._token = token

  def init(self, analysis):
    self._analysis = analysis
    if TAGO_RUNTIME is False:
      self.__localRuntime()
    else:
      return self.run

  def run(self, environment, data, analysis_id, token):
    def log(*args):
      print(*args)
      Services(token).console.log(str(args)[1:][:-2])

    def context():
      pass

    setattr(context, 'log', log)
    setattr(context, 'token', token)
    setattr(context, 'environment', environment)
    setattr(context, 'analysis_id', analysis_id)

    self._analysis(context, data or [])

  def __localRuntime(self):
    # logger=True, engineio_logger=True) #(reconnection=True, reconnection_delay=10000)
    sio = socketio.AsyncClient(reconnection=True, reconnection_delay=10000)

    async def connectSocket():
      def ready(analysisObj):
        print('Analysis [{AnalysisName}] Started\n'.format(AnalysisName=analysisObj['name']))

      def connect():
        print('Connected to TagoIO.')

      def disconnect():
        print('Disconnected from TagoIO.\n\n')

      def error(e):
        print('Connection error', e)

      def analysisTrigger(scope):
        self.run(scope['environment'], scope['data'], scope['analysis_id'], scope['token'])

      sio.on('ready', ready)
      sio.on('error', error)
      sio.on('connect', connect)
      sio.on('disconnect', disconnect)
      sio.on('analysis::trigger', analysisTrigger)

      await sio.connect(url=REALTIME_URL + '?token=' + self._token, transports=['websocket'])
      await sio.wait()

    loop.run_until_complete(connectSocket())
