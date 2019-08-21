import sys
sys.path.append('/Users/vitorfdl/Projects/tago-sdk-python')

from tago import Tago
import os

<<<<<<< HEAD
TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or '8a8de9e3-b5f6-4077-89e3-ad728598aac5'
=======
TOKEN = os.environ.get('TAGO_TOKEN_DEVICE') or 'e11a8e89-9923-4571-8202-55e6a017f76c'
>>>>>>> f74b5d3e855b3d4cc143a184efe8a2d857692fbe

def func_callback(context, scope):
   print "context"
   print context
   print "scope"
   print scope

def test_socket():
   s =  Tago(TOKEN).analysis.run_analysis(func_callback, 0)

test_socket()