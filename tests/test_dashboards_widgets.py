from tago import Tago
from tago.account.dashboards.widgets import DashboardsWidgets as DashboardsWidgets 
import os

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'TOKEN'
DEBUG_MESSAGE = "The response to {} \n{}\n"


testDashboardsWidgets = DashboardsWidgets(TOKEN)

def test_dashboards_widgets_create_delete():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    dashboardsWidgetsResult = testDashboardsWidgets.create('xyz', { "name": "Test DashboardsWidgets" })

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False
    
    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False



def test_dashboards_widgets_edit():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    dashboardsWidgetsResult = testDashboardsWidgets.create('xyz', { "name": "Test DashboardsWidgets" })

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    ####################################
    # Editing the new dashboards.widgets
    ####################################
    editResult = testDashboardsWidgets.edit('xyz', dashboardsWidgetsResult['result']['id'], {"name": "A new dashboards.widgets name"})

    print DEBUG_MESSAGE.format('dashboards.widgets editing', dashboardsWidgetsResult)

    if editResult['status']:
        assert True
    else:
        assert False
    
    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    

def test_dashboards_widgets_info():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    dashboardsWidgetsResult = testDashboardsWidgets.create('xyz', { "name": "Test DashboardsWidgets" })

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    ###########################
    #  Retrieving dashboards.widgets info
    ###########################
    infoResult = testDashboardsWidgets.info('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets information', infoResult)

    if infoResult['status']:
        assert True
    else:
        assert False
    
    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

        

def test_dashboards_widgets_getData():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    dashboardsWidgetsResult = testDashboardsWidgets.create('xyz', { "name": "Test DashboardsWidgets" })

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    #########################################
    #  Retrieving dashboards.widgets get data
    #########################################
    getDataResult = testDashboardsWidgets.getData('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets get data', getDataResult)

    if getDataResult['status']:
        assert True
    else:
        assert False
    
    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False



def test_dashboards_widgets_sendData():
    ###################################
    # Creating a new dashboards.widgets
    ###################################
    dashboardsWidgetsResult = testDashboardsWidgets.create('xyz', { "name": "Test DashboardsWidgets" })

    print DEBUG_MESSAGE.format('dashboards.widgets creation', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False

    #########################################
    #  Retrieving dashboards.widgets send data
    #########################################
    sendDataResult = testDashboardsWidgets.sendData('xyz', dashboardsWidgetsResult['result']['id'], {"name": "A new dashboards.widgets data"})

    print DEBUG_MESSAGE.format('dashboards.widgets get data', sendDataResult)

    if sendDataResult['status']:
        assert True
    else:
        assert False
    
    #####################################
    # Deleting the new dashboards.widgets
    #####################################
    dashboardsWidgetsResult = testDashboardsWidgets.delete('xyz', dashboardsWidgetsResult['result']['id'])

    print DEBUG_MESSAGE.format('dashboards.widgets deletion', dashboardsWidgetsResult)

    if dashboardsWidgetsResult['status']:
        assert True
    else:
        assert False