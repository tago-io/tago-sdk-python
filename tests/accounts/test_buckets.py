from tago import Tago
from tago.account.buckets import Buckets as Buckets
import os

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'a0030850-d585-4063-be6c-f59fdd7046c8'
DEBUG_MESSAGE = 'The response to {} \n{}'

testBuckets = Buckets(TOKEN)

def test_create_delete():
    #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Deleting a bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_list():
    listRequest = testBuckets.list(True)

    print(DEBUG_MESSAGE.format('bucket list', listRequest))

    if listRequest['status']:
        assert True
    else:
        assert False

def test_edit():
    #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # Editing a new bucket
    ######################

    editRequest = testBuckets.edit(createRequest['result']['bucket'], {'name': 'NewTestBucketName'})

    print(DEBUG_MESSAGE.format('bucket edit', editRequest))

    if editRequest:
        assert True
    else:
        assert False

    #######################
    # Cleaning up bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_info():
    #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # Getting bucket Info
    ######################

    infoRequest = testBuckets.info(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket info', infoRequest))

    if infoRequest:
        assert True
    else:
        assert False

    #######################
    # Cleaning up bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_backupList():
    backupListRequest = testBuckets.backupList()

    print(DEBUG_MESSAGE.format('bucket backup list', backupListRequest))

    if backupListRequest['status']:
        assert True
    else:
        assert False

def test_shareList():
    #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # testing shareList
    ######################

    shareListRequest = testBuckets.shareList(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket shareList', shareListRequest))

    if shareListRequest:
        assert True
    else:
        assert False

    #######################
    # Cleaning up bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_shareSendInvite_create_delete():
    #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # shareInvite create
    ######################

    shareSendInviteRequest = testBuckets.shareSendInvite(createRequest['result']['bucket'], {'email': 'rubybank517oodd@gmail.com', 'message': 'Lorem ipsum', 'copy_me': False, 'permission': 'full'})

    print(DEBUG_MESSAGE.format('bucket shareSendInvite', shareSendInviteRequest))

    if shareSendInviteRequest['status']:
        assert True
    else:
        assert False

    ######################
    # shareInvite delete
    ######################

    shareDeleteRequest = testBuckets.shareDelete(shareSendInviteRequest['result']['share_id'])

    print(DEBUG_MESSAGE.format('bucket shareInviteDelete', shareDeleteRequest))

    if shareSendInviteRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Cleaning up bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_shareEdit():
     #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # shareInvite create
    ######################

    shareSendInviteRequest = testBuckets.shareSendInvite(createRequest['result']['bucket'], {'email': 'rubybank517oodd@gmail.com', 'message': 'Lorem ipsum', 'copy_me': False, 'permission': 'full'})

    print(DEBUG_MESSAGE.format('bucket shareSendInvite', shareSendInviteRequest))

    if shareSendInviteRequest['status']:
        assert True
    else:
        assert False


    ######################
    # shareInvite edit
    ######################

    shareSendInviteEditRequest = testBuckets.shareEdit(shareSendInviteRequest['result']['share_id'], {'email': 'rubybank517oodd@gmail.com', 'message': 'ipsum Lorem', 'copy_me': False, 'permission': 'full'})

    print(DEBUG_MESSAGE.format('bucket shareSendInviteRequest', shareSendInviteEditRequest))

    if shareSendInviteRequest['status']:
        assert True
    else:
        assert False


    ######################
    # shareInvite delete
    ######################

    shareDeleteRequest = testBuckets.shareDelete(shareSendInviteRequest['result']['share_id'])

    print(DEBUG_MESSAGE.format('bucket shareInviteDelete', shareDeleteRequest))

    if shareSendInviteRequest['status']:
        assert True
    else:
        assert False

    #######################
    # Cleaning up bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False

def test_exportData():
    #######################
    # Creating a bucket
    ######################
    createRequest = testBuckets.create({'name':'Test Bucket'})

    print(DEBUG_MESSAGE.format('bucket create', createRequest))

    if createRequest['status']:
        assert True
    else:
        assert False

    ######################
    # Exporting a bucket
    ######################

    exportDataRequest = testBuckets.exportData('json', [{'id': createRequest['result']['bucket'], 'origin': [], 'variables': []}], {'start_date': '3/3/2017', 'end_date': '4/30/2017'})

    print(DEBUG_MESSAGE.format('bucket exportData', exportDataRequest))

    if exportDataRequest is not None:
        assert True
    else:
        assert False

    #######################
    # Deleting a bucket
    ######################

    deleteRequest = testBuckets.delete(createRequest['result']['bucket'])

    print(DEBUG_MESSAGE.format('bucket delete', deleteRequest))

    if deleteRequest['status']:
        assert True
    else:
        assert False
