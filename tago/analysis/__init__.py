from ..services import Services
import os
import json
from typing import Callable

REALTIME_URL = os.environ.get('TAGOIO_REALTIME') or 'wss://realtime.tago.io'
T_ANALYSIS_CONTEXT = os.environ.get('T_ANALYSIS_CONTEXT') or False

if T_ANALYSIS_CONTEXT == False:
  import socketio
  import asyncio
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)

class Analysis:
  def __init__(self, token: str = 'unknown'):
    self._token = token

  def init(self, analysis: Callable):
    self._analysis = analysis

    if T_ANALYSIS_CONTEXT is False:
      self.__localRuntime()
    else:
      self.__runOnTagoIO()

  def __runOnTagoIO(self):
    def context():
      pass

    setattr(context, 'log', print)
    setattr(context, 'token', os.environ['T_ANALYSIS_TOKEN'])
    setattr(context, 'analysis_id', os.environ['T_ANALYSIS_ID'])
    try:
      setattr(context, 'environment', json.loads(os.environ['T_ANALYSIS_ENV']))
    except:
      setattr(context, 'environment', [])

    try:
      data = json.loads(os.environ['T_ANALYSIS_DATA'])
    except:
      data = []

    self._analysis(context, data)

  def __runLocal(self, environment, data, analysis_id, token):
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
        print('Analysis [{AnalysisName}] Started.\n'.format(AnalysisName=analysisObj['name']))

      def connect():
        print('Connected to TagoIO, Getting analysis information...')

      def disconnect():
        print('\nDisconnected from TagoIO.\n\n')

      def error(e):
        print('Connection error', e)

      def analysisTrigger(scope):
        self.__runLocal(scope['environment'], scope['data'], scope['analysis_id'], scope['token'])

      sio.on('ready', ready)
      sio.on('error', error)
      sio.on('connect', connect)
      sio.on('disconnect', disconnect)
      sio.on('analysis::trigger', analysisTrigger)

      URLRealtime = '{}{}{}'.format(REALTIME_URL, '?token=', self._token)
      await sio.connect(url=URLRealtime, transports=['websocket'])
      await sio.wait()

    try:
      loop.run_until_complete(connectSocket())
    except RuntimeError:
      pass

  @staticmethod
  def use(analysis: Callable, token: str = 'unknown'):
    Analysis(token).init(analysis)
