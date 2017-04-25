import os
import sys
sys.path.append(os.path.join('..', ''))
from tago.account.dashboards import Dashboards
import tago.account._share as share

TOKEN = os.environ.get('TAGO_ACCOUNT_TOKEN') or 'TOKEN'
TYPE = 'dashboard'
DATA = {'email':'test@email.com'}
OPTIONS = {}
ID = None
test_dashboard = Dashboards(TOKEN)

def _create_test_dashboard():
    result = test_dashboard.create({'label':'test'})
    global ID
    ID = test_dashboard.list()['result'][-1]['id']
    print ID

def _delete_test_dashboard():
    global ID
    test_dashboard.delete(ID)

def test_invite():
    null = share.invite(TYPE,'',{},OPTIONS)
    assert null is None

    no_email = share.invite(TYPE,ID,{},OPTIONS)
    assert no_email is None

    invite_result = share.invite(TYPE,ID,DATA,OPTIONS)
    assert invite_result is not None
    if invite_result['status']:
        assert True
        print "invite passed"
    else:
       assert False
       print "invite failed"

def test_edit():
    null = share.edit(TYPE,'',{},OPTIONS)
    assert null is None

    edit_result = share.edit(TYPE,ID,DATA,OPTIONS)
    assert edit_result is not None
    if edit_result['status']:
        assert True
        print "edit passed"
    else:
       assert False
       print "edit failed"

def test_list():
    null = share.list(TYPE,None,OPTIONS)
    assert null is None

    list_result = share.list(TYPE,ID,OPTIONS)
    assert list_result is not None
    if list_result['status']:
        assert True
        print "list passed"
    else:
       assert False
       print "list failed"

def test_remove():
    null = share.remove(TYPE,'',OPTIONS)
    assert null is None

    remove_result = share.remove(TYPE,ID,OPTIONS)
    assert remove_result is not None
    if remove_result['status']:
        assert True
        print "remove passed"
    else:
       assert False
       print "remove failed"

_create_test_dashboard()
test_invite()
test_edit()
test_list()
test_remove()
_delete_test_dashboard
