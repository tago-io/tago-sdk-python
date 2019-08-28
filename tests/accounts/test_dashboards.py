from tago.account.dashboards import Dashboards
import os
import sys
sys.path.append(os.path.join('..', ''))

TOKEN = os.environ.get(
    'TAGO_TOKEN_ACCOUNT') or 'a0030850-d585-4063-be6c-f59fdd7046c8'
DEBUG_MESSAGE = 'The response to {} \n{}'

test_dashboard = Dashboards(TOKEN)


def test_create_delete():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label': 'Test Dash'})

    print(DEBUG_MESSAGE.format('dash create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Deleting a dash
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print(DEBUG_MESSAGE.format('dash delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False


def test_edit():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label': 'Test Dash'})

    print(DEBUG_MESSAGE.format('dash create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Editing a dashboard
    ######################

    editRequest = test_dashboard.edit(createRequest['result']['dashboard'], {
                                      'label': 'NewTestDashName'})

    print(DEBUG_MESSAGE.format('dash edit', editRequest))

    if editRequest:
        assert True
    else:
        assert False

    #######################
    # Deleting a dashboard
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print(DEBUG_MESSAGE.format('dash delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False


def test_info():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label': 'Test Dash'})

    print(DEBUG_MESSAGE.format('dash create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # Getting dashboard Info
    ######################

    infoRequest = test_dashboard.info(createRequest['result']['dashboard'])

    print(DEBUG_MESSAGE.format('dash info', infoRequest))

    if infoRequest:
        assert True
    else:
        assert False

    #######################
    # Deleting a dashboard
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print(DEBUG_MESSAGE.format('dash delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False


def test_list():
    listRequest = test_dashboard.list()

    print(DEBUG_MESSAGE.format('dash list', listRequest))

    if listRequest['status']:
        assert True
    else:
        assert False


def func_callback():
    assert True


def test_listening_stop_listening():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label': 'Test Dash'})

    print(DEBUG_MESSAGE.format('dash create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ###########################
    # Start listening the dash
    ###########################
    dashboard_id = createRequest['result']['dashboard']

    listeningResult = test_dashboard.listening(dashboard_id, func_callback, 1)
    print(DEBUG_MESSAGE.format('listening', listeningResult))

    check = "Listening to Dashboard "+dashboard_id
    if check in listeningResult:
        assert True
    else:
        assert False

    # Create a widget and pass data to it, should invoke the callback?

    ###########################
    # Stop listening the dash
    ###########################

    stopResult = test_dashboard.stopListening(dashboard_id)
    print(DEBUG_MESSAGE.format('listening stop', stopResult))

    check = "Stop listening to Dashboard "+dashboard_id
    if check in stopResult:
        assert True
    else:
        assert False

    #######################
    # Deleting a dashboard
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print(DEBUG_MESSAGE.format('dash delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False
