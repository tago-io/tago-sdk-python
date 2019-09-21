import sys
sys.path.append('..')

from tago import Analysis
from tago import Utils
from tago import Services
import tago
import json

# The main function used by Tago to run the script.
# It sends a notification to the account and another one linked to a dashboard.
def send_notification(context, scope):
  message = list(filter(lambda message: message['key'] == 'message', context.environment))
  message = message[0]['value']

  title = list(filter(lambda title: title['key'] == 'title', context.environment))
  title = title[0]['value']

  ref_id = list(filter(lambda ref_id: ref_id['key'] == 'dashboard;_id', context.environment))
  if not ref_id:
    ref_id = list(filter(lambda ref_id: ref_id['key'] == 'bucket_id', context.environment))
    if not ref_id:
      ref_id = None
    else:
      ref_id = ref_id[0]['value']
  else:
    ref_id = ref_id[0]['value']

  notification = Services(context.token).notification
  notification.send(title, message, ref_id)

tago.Analysis('MY-ANALYSIS-TOKEN-HERE').init(send_notification)
