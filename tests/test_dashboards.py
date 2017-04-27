import os
import sys
sys.path.append(os.path.join('..', ''))
from tago.account.dashboards import Dashboards
import unittest

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'TOKEN'
DEBUG_MESSAGE = 'The response to {} \n{}'

test_dashboard = Dashboards(TOKEN)

def test_create_delete():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label':'Test Dash'})

    print DEBUG_MESSAGE.format('dash create', createRequest)

    if createRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Deleting a dash
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print DEBUG_MESSAGE.format('dash delete', deleteRequest)

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_edit():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label':'Test Dash'})

    print DEBUG_MESSAGE.format('dash create', createRequest)

    if createRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Editing a dashboard
    ######################

    editRequest = test_dashboard.edit(createRequest['result']['dashboard'], {'label': 'NewTestDashName'})

    print DEBUG_MESSAGE.format('dash edit', editRequest)

    if editRequest:
        assert True
    else:
        assert False

    #######################
    # Deleting a dashboard
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print DEBUG_MESSAGE.format('dash delete', deleteRequest)

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_info():
    #######################
    # Creating a dashboard
    ######################
    createRequest = test_dashboard.create({'label':'Test Dash'})

    print DEBUG_MESSAGE.format('dash create', createRequest)

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # Getting dashboard Info 
    ######################

    infoRequest = test_dashboard.info(createRequest['result']['dashboard'])

    print DEBUG_MESSAGE.format('dash info', infoRequest)

    if infoRequest:
        assert True
    else:
        assert False

    #######################
    # Deleting a dashboard
    ######################

    deleteRequest = test_dashboard.delete(createRequest['result']['dashboard'])

    print DEBUG_MESSAGE.format('dash delete', deleteRequest)

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_list():
    listRequest = test_dashboard.list()

    print DEBUG_MESSAGE.format('dash list', listRequest)

    if listRequest['status']:
        assert True
    else:
        assert False



# def test_dashboards_list():
#     list = test_dashboard.list()
#     # print result
#     assert list is not None
#     if list['status']:
#         assert True
#         print "list passed"
#     else:
#         assert False
#         print "list failed"

# def test_dashboards_create():
#     test_dashboard = Dashboards(TOKEN)
#     list = test_dashboard.list()
#     before = len(list['result'])
#     result = test_dashboard.create({'label':'test'})
#     assert len(test_dashboard.list()['result']) == before + 1
#     # print result
#     assert result is not None
#     assert list['result'] != result['result']
#     if result['status']:
#         assert True
#         print "create passed"
#     else:
#         assert False
#         print "create failed"

# def test_dashboards_edit():
#     assert test_dashboard.list()['result'][-1]['label'] == "test"
#     edit_result = test_dashboard.edit(test_dashboard.list()['result'][-1]['id'],{'label':'test2'})
#     assert edit_result is not None
#     assert test_dashboard.list()['result'][-1]['label'] == 'test2'
#     if edit_result['status']:
#         assert True
#         assert edit_result['result'] == 'Successfully Updated'
#         print "edit passed"
#     else:
#         assert False
#         print "edit failed"

# def test_dashboards_info():
#     #unittest.assertRaises(ValueError, test_dashboard.info(''))
#      #null = test_dashboard.info('')
#      #assert null is None

#     invalid = test_dashboard.info('invalid')
#      # print result
#     assert invalid is not None
#     assert invalid['status'] == False
#     assert invalid['message'] == 'Invalid Dashboard ID'

#     info_result = test_dashboard.info(test_dashboard.list()['result'][-1]['id'])
#     if info_result['status']:
#         assert True
#         assert info_result['result']['dashboard']['label'] == 'test2'
#         print "info passed"
#     else:
#        assert False
#        print "info failed"

# def test_dashboards_delete():
#     before = len(test_dashboard.list()['result'])
#     delete_result = test_dashboard.delete(test_dashboard.list()['result'][-1]['id'])
#     assert delete_result is not None
#     assert len(test_dashboard.list()['result']) == before - 1
#     if delete_result['status']:
#         assert True
#         assert delete_result['result'] == 'Successfully Removed'
#         print "delete passed"
#     else:
#        assert False
#        print "delete failed"
