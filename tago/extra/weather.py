from promise import Promise
from service_request import service_request as request
from default_headers import default_headers
from datetime import datetime
import urllib
import ast

# Wunderground docs: http://www.wunderground.com/weather/api/d/docs

class Weather:
    def __init__(self, key):
        self.key = key;
        self.default_options = {'json': True,'headers': default_headers(self)}

    def _setParams(self, params):
        self._query = params['query'] or None
        self._full = params['full'] or False
        self._lang = params['lang'] or 'EN'

    def geolocation_verify(geolocation):
        if type(geolocation) == 'string':
            geoplited = geolocation.split(',')
            if geolocation.length > 1:
                geolocation = [geoplited[0].strip(), geoplited[1].strip()]
            else:
                return None
        elif geolocation.coordinates:
            geolocation = geolocation.coordinates
        else:
            return None
        return ','.join([geolocation[0], geolocation[1]])

    def current(self, query, full, lang):
        def current_result(result):
            result = ast.literal_eval(result)
            if 'results' in result['response']:
	        if 'current_observation' not in result:
                    return Promise.reject('Invalid address, ' + str(len(result['response']['results'])) + ' match.')
            elif 'current_observation' not in result:
                return Promise.reject('Invalid address')
            result = result['current_observation']
            try:
                del result['image']
                del result['icon_url']
                del result['forecast_url']
                del result['history_url']
                del result['ob_url']
                del result['estimated']
            except Exception as e:
                return Promise.reject('weather system, '+ str(e))
            return Promise.resolve(result) 

        params = {'query':query, 'full':full, 'lang':lang, 'key':self.key}
        self._setParams(params)
        url = 'http://api.wunderground.com/api/'+self.key+'/lang:'+self._lang+'/conditions/q/'+urllib.quote(self._query.encode("utf-8"))+'.json'
        method = 'GET'

        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options).then(lambda result: current_result(result))

    def history(self, date, query, full, lang):
        def history_result(result):
            result = ast.literal_eval(result)
            result = result['history']
            return Promise.resolve(result)

        params = {'query':query, 'full':full, 'lang':lang}
        self._setParams(params)
        try: 
            date = datetime.strptime(date, '%Y-%m-%d')
            date = str(date.year) + str(format(date.month,'02')) + str(format(date.day,'02'))
        except Exception as e:
            return Promise.reject('Invalid date', + e)
        url = 'http://api.wunderground.com/api/'+self.key+'/lang:'+self._lang+'/history_'+str(date)+'/q/'+urllib.quote(self._query.encode("utf-8"))+'.json'
        method = 'GET'
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options).then(lambda result: history_result(result))

    def forecast(self, query, full, lang):
        def forecast_result(result):
            result = ast.literal_eval(result)
            print result
            try:
                result = result['forecast']
            except Exception as e:
                return Promise.reject('Error on parse weather forecast ' + str(e))
            return Promise.resolve(result)

        params = {'query':query, 'full':full, 'lang':lang, 'key':self.key}
        self._setParams(params)
        url    = 'http://api.wunderground.com/api/'+ self.key +'/forecast/q/'+urllib.quote(self._query.encode("utf-8"))+'.json'
        method = 'GET'
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options).then(lambda result: forecast_result(result))

    def alerts(self, query, full, lang):
        def alerts_result(result):
            result = ast.literal_eval(result)
            del result['response']
            return Promise.resolve(result)

        params = {'query':query, 'full':full, 'lang':lang}
        self._setParams(params)
        url    = 'http://api.wunderground.com/api/'+self.key+'/alerts/q/'+urllib.quote(self._query.encode("utf-8"))+'.json'
        method = 'GET'
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options).then(lambda result: alerts_result(result))
