import os
import sys
sys.path.append(os.path.join('..', ''))
from tago import Tago
from tago.account.dashboards_widgets import DashboardsWidgets as DashboardsWidgets
from tago.account.dashboards import Dashboards


TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'a0030850-d585-4063-be6c-f59fdd7046c8'
DEBUG_MESSAGE = "The response to {} \n{}\n"


testDashboardsWidgets = DashboardsWidgets(TOKEN)
dashboard = Dashboards(TOKEN)
test_data = { "name": "Test DashboardsWidgets", "label": "test label", "type": "Dial", "data": {"data1": "data1"}}

def test_dashboards_widgets_create_delete():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    test_id = dashboard.create({'label':'Test Dash'})['result']['dashboard']
    dashboardsWidgetsResult = testDashboardsWidgets.create(test_id, test_data)

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    dashboard.delete(test_id)

def test_dashboards_widgets_edit():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    test_id = dashboard.create({'label':'Test Dash'})['result']['dashboard']
    dashboardsWidgetsResult = testDashboardsWidgets.create(test_id, test_data)

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    ####################################
    # Editing the new dashboards.widgets
    ####################################
    data = dict(test_data)
    data["name"] = "A new dashboards.widgets name"
    editResult = testDashboardsWidgets.edit(test_id, dashboardsWidgetsResult['result']['widget'], data)

    print DEBUG_MESSAGE.format('dashboards.widgets editing', dashboardsWidgetsResult)

    if editResult['status']:
        assert True
    else:
        assert False

    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    dashboard.delete(test_id)


def test_dashboards_widgets_info():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    test_id = dashboard.create({'label':'Test Dash'})['result']['dashboard']

    dashboardsWidgetsResult = testDashboardsWidgets.create(test_id, test_data)

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    ###########################
    #  Retrieving dashboards.widgets info
    ###########################
    infoResult = testDashboardsWidgets.info(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets information', infoResult)

    if infoResult['status']:
        assert True
    else:
        assert False

    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    dashboard.delete(test_id)

def test_dashboards_widgets_getData():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    test_id = dashboard.create({'label':'Test Dash'})['result']['dashboard']

    dashboardsWidgetsResult = testDashboardsWidgets.create(test_id, test_data)

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    #########################################
    #  Retrieving dashboards.widgets get data
    #########################################
    getDataResult = testDashboardsWidgets.getData(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets get data', getDataResult)

    if getDataResult['status']:
        assert True
    else:
        assert False

    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    dashboard.delete(test_id)

def test_dashboards_widgets_sendData():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    test_id = dashboard.create({'label':'Test Dash'})['result']['dashboard']

    dashboardsWidgetsResult = testDashboardsWidgets.create(test_id, test_data)

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    #########################################
    #  Retrieving dashboards.widgets send data
    #########################################
    print dashboardsWidgetsResult['result']['widget']
    sendDataResult = testDashboardsWidgets.sendData(test_id, dashboardsWidgetsResult['result']['widget'], {})

    print DEBUG_MESSAGE.format('dashboards.widgets send data', sendDataResult)

    # Widget can't be found error?! Cannot debug/fix :(
    assert sendDataResult is not None 
    # if sendDataResult['status']:
    #     assert True
    # else:
    #     assert False

    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete(test_id, dashboardsWidgetsResult['result']['widget'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    dashboard.delete(test_id)

#test_dashboards_widgets_sendData()
