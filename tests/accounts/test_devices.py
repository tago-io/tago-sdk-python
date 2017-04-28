from tago import Tago
from tago.account.devices import Devices  as Devices
import os

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'TOKEN'
DEBUG_MESSAGE = 'The response to {} \n{}'

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

    result = testDevices.factory()

    # print result

    # if true, the object was created
    if result['status']:
        assert True
    else:
        assert False


    #########################
    # Testing device info 
    #########################
    deviceInfo = testDevices.info(result['result']['device_id'])

    if deviceInfo['status']:
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

def test_device_token_create():

    testDevices = Devices(TOKEN)
    testDevice = testDevices.factory()

    print testDevice['result']['device_id']

    #########################
    # Testing device token creation
    #########################
    newToken = testDevices.tokenCreate(testDevice['result']['device_id'], {'name': 'NewDeviceToken', 'permission': 'full', 'device': ''})

    print 'The token create response'
    print newToken

    if newToken['status']:
        assert True
    else:
        assert False
    #########################
    # Testing device token listing
    #########################

    deviceList = testDevices.tokenList(testDevice['result']['device_id'])

    print 'The response to device list'
    print deviceList 

    if deviceList['status']:
        assert True
    else:
        assert False

    #########################
    # Testing deletion of a token
    #########################

    tokenDelete = testDevices.tokenDelete(newToken['result']['token'])

    print 'The response to token delete'
    print tokenDelete

    if tokenDelete['status']:
        assert True
    else:
        assert False

    # cleaning up the device we created for this test
    testDevices.delete(testDevice['result']['device_id'])

def test_device_param_set():
    testDevices = Devices(TOKEN)
    testDevice = testDevices.factory()

    ########################
    # Testing creation of params
    ########################
    testParam = testDevices.paramSet(testDevice['result']['device_id'], [{"key": "TestKey", "value": "TestValue"},{"key": "Test Key2", "value": "TestValue2"}])

    print DEBUG_MESSAGE.format('test_device_param_Set', testParam)

    if testParam['status']:
        assert True
    else:
        assert False

    # cleaning up the device we created for this test
    testDevices.delete(testDevice['result']['device_id'])

def test_param_list():
    testDevices = Devices(TOKEN)
    testDevice = testDevices.factory()

    paramListResult = testDevices.paramList(testDevice['result']['device_id'], str(True))

    print DEBUG_MESSAGE.format('test_device_param_list', paramListResult)

    if paramListResult['status']:
        assert True
    else:
        assert False

    # cleaning up the device we created for this test
    testDevices.delete(testDevice['result']['device_id'])
