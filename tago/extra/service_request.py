from promise import Promise
import requests

def service_request(request_options):
    result = requests.get(request_options['url'], request_options['params'])
    if result.status_code != 200:
        return Promise.reject('Error on Third-Party service')       
    body = result.text
    try:
        body = JSON.parse(body);
    except:
        pass
    if result.status_code != requests.codes.ok:
        console.error(body)
        return Promise.reject('Error on Third-Party service')
    return Promise.resolve(body)