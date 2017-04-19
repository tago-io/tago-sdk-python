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

def test_device_create():
    ######################### 
    # Testing device creation
    #########################
    testDevices = Devices(TOKEN)

    # TODO: Passing as JSON string for now.  Should that change?

    result = testDevices.create({'name': 'TestDeviceName'})

    # print result

    # if true, the object was created
    if result['status']:
        assert True
    else:
        assert False
    
    #########################
    # Testing device editing
    #########################
    editedResult = testDevices.edit(result['result']['device_id'], {'name': 'RenamedDevice'})

    # print editedResult
    
    # If true, the edit was successful
    if editedResult['status']:
        assert True
    else:
        assert False

    #########################
    # Testing device deletion
    #########################
    deletedResult = testDevices.delete(result['result']['device_id'])

    if deletedResult['status']:
        assert True
    else:
        assert False
