from tago import Tago
from tago.account.devices import Devices  as Devices
import os

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'TOKEN'

def test_device_list():
    # print dir(Devices)
    
    testDevices = Devices(TOKEN)

    result = testDevices.list()

    print result

    if result['status']:
        assert True
    else:
        assert False
