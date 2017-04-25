import os
import sys
sys.path.append(os.path.join('..', ''))
from tago.account.dashboards import Dashboards

TOKEN = os.environ.get('TAGO_ACCOUNT_TOKEN') or 'TOKEN'
test_dashboard = Dashboards(TOKEN)

def test_dashboards_list():
    list = test_dashboard.list()
    # print result
    assert list is not None
    if list['status']:
        assert True
        print "list passed"
    else:
        assert False
        print "list failed"

def test_dashboards_create():
    test_dashboard = Dashboards(TOKEN)
    list = test_dashboard.list()
    before = len(list['result'])
    result = test_dashboard.create({'label':'test'})
    assert len(test_dashboard.list()['result']) == before + 1
    # print result
    assert result is not None
    assert list['result'] != result['result']
    if result['status']:
        assert True
        print "create passed"
    else:
        assert False
        print "create failed"

def test_dashboards_edit():
    assert test_dashboard.list()['result'][-1]['label'] == "test"
    edit_result = test_dashboard.edit(test_dashboard.list()['result'][-1]['id'],{'label':'test2'})
    assert edit_result is not None
    assert test_dashboard.list()['result'][-1]['label'] == 'test2'
    if edit_result['status']:
        assert True
        assert edit_result['result'] == 'Successfully Updated'
        print "edit passed"
    else:
        assert False
        print "edit failed"

def test_dashboards_info():
     null = test_dashboard.info('')
     assert null is None

     invalid = test_dashboard.info('invalid')
     # print result
     assert invalid is not None
     assert invalid['status'] == False
     assert invalid['message'] == 'Invalid Dashboard ID'

     info_result = test_dashboard.info(test_dashboard.list()['result'][-1]['id'])
     if info_result['status']:
         assert True
         assert info_result['result']['dashboard']['label'] == 'test2'
         print "info passed"
     else:
        assert False
        print "info failed"

def test_dashboards_delete():
    before = len(test_dashboard.list()['result'])
    delete_result = test_dashboard.delete(test_dashboard.list()['result'][-1]['id'])
    assert delete_result is not None
    assert len(test_dashboard.list()['result']) == before - 1
    if delete_result['status']:
        assert True
        assert delete_result['result'] == 'Successfully Removed'
        print "delete passed"
    else:
       assert False
       print "delete failed"

test_dashboards_list()
test_dashboards_create()
test_dashboards_edit()
test_dashboards_info()
test_dashboards_delete()
