from tago import Tago
from tago.account.analysis import Analysis as Analysis 
import os
import requests
import json

API_TAGO = os.environ.get('TAGO_SERVER') or 'https://api.tago.io'
TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'a0030850-d585-4063-be6c-f59fdd7046c8'

DEBUG_MESSAGE = "The response to {} \n{}\n"

testAnalysis = Analysis(TOKEN)

def test_analysis_create_delete():
    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False
    
    ###########################
    # Deleting the new analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False


def test_analysis_edit():
    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

    ###########################
    # Editing the new analysis
    ###########################
    editResult = testAnalysis.edit(analysisResult['result']['id'], {"name": "A new analysis name"})

    if editResult['status']:
        assert True
    else:
        assert False
    
    ###########################
    # Deleting the new analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

def test_analysis_info():
    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

    ###########################
    #  Retrieving analysis info
    ###########################
    infoResult = testAnalysis.info(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis information', infoResult)

    if infoResult['status']:
        assert True
    else:
        assert False

    ###########################
    # Deleting the new analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

def test_analysis_tokenGenerate():
    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

    ###########################
    # Generating new token
    ###########################
    tokenResult = testAnalysis.tokenGenerate(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis token generation', tokenResult)

    if tokenResult:
        assert True
    else:
        assert False

    ###########################
    # Deleting up new token (is this even possible?)
    ###########################
    
    ###########################
    # Deleting the new analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

def test_analysis_uploadFile():
    test_file = 'Hello, world!'
    test_file_name = 'Testfile.txt'

    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

    fileResult = testAnalysis.uploadFile(analysisResult['result']['id'], test_file_name, test_file)

    print DEBUG_MESSAGE.format('analysis file upload', fileResult)

    if fileResult:
        assert True
    else:
        assert False

    ###########################
    # Deleting the new analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)
    
    if analysisResult['status']:
        assert True
    else:
        assert False

def test_analysis_run():
    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

    analysisRunResult = testAnalysis.run(analysisResult['result']['id'], {})

    print DEBUG_MESSAGE.format('analysis run', analysisRunResult)

    if analysisRunResult:
        assert True
    else:
        assert False

    ###########################
    # Deleting the new analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])

    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)
    
    if analysisResult['status']:
        assert True
    else:
        assert False

def func_callback():
    assert False

def test_analysis_listening():
    ###########################
    # Creating a new analysis
    ###########################
    analysisResult = testAnalysis.create({ "name": "Test Analysis" })

    print DEBUG_MESSAGE.format('analysis creation', analysisResult)

    if analysisResult['status']:
        assert True
    else:
        assert False

    ###########################
    # Start listening the analysis
    ###########################
    analyze_id = analysisResult['result']['id']
    analysis_token = analysisResult['result']['token']
    listeningResult = testAnalysis.listening(analyze_id, func_callback, 1)
    print DEBUG_MESSAGE.format('listening', listeningResult)

    check =  "Listening to Analyze "+analyze_id
    if check in listeningResult:
        assert True
    else:
        assert False


    #Create a LOG (extra/console.js) for this analysis using the token given from the create analysis response, now that it is listening, it should invoke the callback function
    default_headers = { 'content-type': 'application/json', 'Analysis-Token': analysis_token }
    data = {}
    data['message'] = 'Log Test!'
    LogRequest = requests.post('{api_endpoint}/analysis/services/console/send'.format(api_endpoint=API_TAGO), headers=default_headers, data=json.dumps(data)).json()
    print DEBUG_MESSAGE.format('Log Result', LogRequest)


    ###########################
    # Stop listening the analysis
    ###########################

    stopResult = testAnalysis.stopListening(analyze_id)
    print DEBUG_MESSAGE.format('listening stop', stopResult)

    check = "Stop listening to Analyze "+analyze_id
    if check in stopResult:
        assert True
    else:
        assert False   


    ###########################
    # Deleting the analysis
    ###########################
    analysisResult = testAnalysis.delete(analysisResult['result']['id'])
    print DEBUG_MESSAGE.format('analysis deletion', analysisResult)
    
    if analysisResult['status']:
        assert True
    else:
        assert False

