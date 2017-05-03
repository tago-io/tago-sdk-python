from tago import Tago
from tago.account.actions import Actions as Actions 
import os

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'a0030850-d585-4063-be6c-f59fdd7046c8'
DEBUG_MESSAGE = "The response to {} \n{}"

def test_create_delete_action():
    testActions = Actions(TOKEN)

    newActionRequest = testActions.create({"name": "New Action"})

    print DEBUG_MESSAGE.format('action creation', newActionRequest)

    if newActionRequest['status']:
        assert True
    else:
        assert False

    newActionRequest = testActions.delete( newActionRequest['result']['action'] )

    print DEBUG_MESSAGE.format('action deletion', newActionRequest)

    if newActionRequest['status']:
        assert True
    else:
        assert False

def test_list_action():
    testActions = Actions(TOKEN)

    listActionsRequest = testActions.list()

    print DEBUG_MESSAGE.format('listing actions',  listActionsRequest)

    if listActionsRequest:
        assert True
    else:
        assert False

def test_edit_action():
    testActions = Actions(TOKEN)

    newActionRequest = testActions.create({"name": "New Action"})

    print DEBUG_MESSAGE.format('action creation', newActionRequest)

    if newActionRequest['status']:
        assert True
    else:
        assert False

    editActionRequest = testActions.edit(newActionRequest['result']['action'], {"name": "New Name For Action"})

    print DEBUG_MESSAGE.format('action editing', editActionRequest)

    newActionRequest = testActions.delete( newActionRequest['result']['action'] )

    print DEBUG_MESSAGE.format('action deletion', newActionRequest)

    if newActionRequest['status']:
        assert True
    else:
        assert False

def test_info_action():

    testActions = Actions(TOKEN)

    newActionRequest = testActions.create({"name": "New Action"})

    print DEBUG_MESSAGE.format('action creation', newActionRequest)

    if newActionRequest['status']:
        assert True
    else:
        assert False

    infoActionsRequest = testActions.info(newActionRequest['result']['action'])

    print DEBUG_MESSAGE.format('info actions',  infoActionsRequest)

    if infoActionsRequest:
        assert True
    else:
        assert False

    newActionRequest = testActions.delete( newActionRequest['result']['action'] )

    print DEBUG_MESSAGE.format('action deletion', newActionRequest)

    if newActionRequest['status']:
        assert True
    else:
        assert False
