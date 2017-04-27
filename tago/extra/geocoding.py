from promise import Promise
from service_request import service_request as request
from default_headers import default_headers
from googlemaps import Client

class Geocoding :
    def __init__(self,key):
	self.key = key
        self.default_options = {'json': True, 'headers':default_headers(self)}

    def getAddress(self, geolocation):
        if type(geolocation) == str:
            geoplited = geolocation.split(',')

            if len(geolocation) > 1:
                geolocation = [geoplited[0].strip(), geoplited[1].strip()]
            else: 
                return Promise.reject('Invalid geolocation')
        elif geolocation.coordinates:
            geolocation = geolocation.coordinates
        else:
            return Promise.reject('Invalid geolocation')

        geolocation = ','.join([geolocation[0], geolocation[1]])

        url    = 'https://maps.googleapis.com/maps/api/geocode/json'
        method = 'GET'
        params = {'latlng': geolocation, 'key':self.key}
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options)

    def getGeolocation(self, address):
        url    = 'https://maps.googleapis.com/maps/api/geocode/json'
        method = 'GET'
        params = { 'address':address, 'key': self.key }
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params
        options = self.default_options
        return request(options)

