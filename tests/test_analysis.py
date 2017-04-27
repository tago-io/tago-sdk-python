from tago import Tago
from tago.account.analysis import Analysis as Analysis 
import os

TOKEN = os.environ.get('TAGO_TOKEN_ACCOUNT') or 'TOKEN'
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

def test_analysis_listening():
    assert False
