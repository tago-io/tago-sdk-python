#	THESE METHODS IN SHARE.PY ARE ALL TESTED THROUGH TEST_BUCKETS.PY

# import os
# import sys
# sys.path.append(os.path.join('..', ''))
# import json
# from tago.account.dashboards import Dashboards
# import tago.account._share as share

# TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'a0030850-d585-4063-be6c-f59fdd7046c8'
# TYPE = 'dashboard'
# DATA = {'email':'vchawla3@ncsu.edu','permission':'read'}
# OPTIONS = {}
# ID = None
# test_dashboard = Dashboards(TOKEN)

# # def _create_test_dashboard():
# #     result = test_dashboard.create({'label':'test'})
# #     #global ID
# #     ID = test_dashboard.list()['result'][-1]['id']

# # def _delete_test_dashboard():
# #     #global ID
# #     test_dashboard.delete(ID)

# def test_invite():
#     result = test_dashboard.create({'label':'test'})
#     ID = test_dashboard.list()['result'][-1]['id']

#     #null = share.invite(TYPE,'',{},OPTIONS)
#     #assert null is None

#     #no_email = share.invite(TYPE,ID,{'email':None},OPTIONS)
#     #assert no_email is None

#     invite_result = test_dashboard.shareSendInvite(ID,DATA)
#     #print invite_result
#     assert invite_result is not None
#     print "invite passed"
#     if invite_result['status']:
#         assert True
#         print "invite passed"
#     else:
#        assert False
#        print "invite failed"

#     test_dashboard.delete(ID)

# def test_edit():
#     result = test_dashboard.create({'label':'test'})
#     ID = test_dashboard.list()['result'][-1]['id']
#     #null = share.edit(TYPE,'',{},OPTIONS)
#     #assert null is None

#     edit_result = test_dashboard.shareEdit(ID,DATA)
#     #print edit_result, ID
#     assert edit_result is not None
#     print "edit passed"
#     if edit_result['status']:
#         assert True
#         print "edit passed"
#     else:
#        assert False
#        print "edit failed"

#     test_dashboard.delete(ID)

# def test_list():
#     result = test_dashboard.create({'label':'test'})
#     ID = test_dashboard.list()['result'][-1]['id']
#     #null = share.list(TYPE,None,OPTIONS)
#     #assert null is None

#     list_result = test_dashboard.shareList(ID)
#     #print list_result
#     assert list_result is not None
#     print "list passed"
#     if list_result['status']:
#         assert True
#         print "list passed"
#     else:
#        assert False
#        print "list failed"

#     test_dashboard.delete(ID)

# def test_remove():
#     result = test_dashboard.create({'label':'test'})
#     ID = test_dashboard.list()['result'][-1]['id']
#     invite_result = test_dashboard.shareSendInvite(ID,DATA)
#     # null = share.remove(TYPE,'',OPTIONS)
#     # assert null is None

#     remove_result = share.remove(TYPE,invite_result['result']['share_id'],OPTIONS)
#     #assert remove_result is not None
#     print remove_result
#     if remove_result['status']:
#         assert True
#         print "remove passed"
#     else:
#        assert False
#        print "remove failed"

#     test_dashboard.delete(ID)

# # _create_test_dashboard()
# # test_invite()
# # test_edit()
# # test_list()
# # test_remove()
# # _delete_test_dashboard
