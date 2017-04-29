from promise import Promise
from service_request import service_request as request
from default_headers import default_headers
import urllib
import ast

class Currency:
    def __init__(self, key):
        self.key = key
        self.default_options = {'json': True, 'headers': default_headers(self)}

    def convert(self, c_from, c_to):
        def convert_result(result):
            result = ast.literal_eval(result)
            if not result['success']:
                return Promise.reject('Currency not found.')
            result_return = {'from': result['source'],'result': result['quotes']}
            return Promise.resolve(result_return)

        if not c_from:
            return Promise.reject('Missing params')
        if not c_from:
            return Promise.reject('Missing params')

        if type(c_to) == list:
            c_to = ','.join(c_to)
        url = 'http://apilayer.net/api/live/?asccess_key='+self.key
        method = 'get'
        params = {'access_key': self.key,'source': c_from,'currencies': c_to,'format': 1}
        options = {}
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options).then(lambda result: convert_result(result))