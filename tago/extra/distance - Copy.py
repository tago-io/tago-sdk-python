from promise import Promise
from service_request import service_request as request
from default_headers import default_headers
from googlemaps import Client

#Google Distance API docs: https://developers.google.com/maps/documentation/distance-matrix/intro

class Distance:
    def __init__(self,key):
        self.key = key
        self.default_options = {'json':True,'headers': default_headers(self)}

    '''
     * Get a distance
     * @param  {STRING} to
     * @param  {STRING} message Message to be send
     * @return {Promise}
    '''
    def measure(self,origins, destinations, language, mode):
        def handle_locations(geolocation):
            if type(geolocation) == str:
                geoplited = geolocation.split(',')
                if len(geoplited) < 2:
                    return None
                else:
                    return geolocation
            elif geolocation and geolocation.coordinates:
                geolocation = geolocation.coordinates
                return str(geolocation[1])+","+str(geolocation[0])
            else:
                return None

        def make_string_togoogle(self, array_obj):
            if not type(array_obj) == list:
                array_obj = list(array_obj)

            array_obj_string = ""
            for x in array_obj:
                handled_loc = handle_locations(x)
                if handled_loc:
                    if not array_obj_string:
                        array_obj_string = handled_loc
                    else:
                        array_obj_string = array_obj_string|handled_loc

            return array_obj_string or ''

        if not origins:
            return Promise.reject('Invalid origin')
        if not destinations:
            return Promise.reject('Invalid destinations')

        origins_string      = make_string_togoogle(self,origins)
        destinations_string = make_string_togoogle(self,destinations)

        url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
        method = 'GET'
        params = {'origins':origins_string,'destinations': destinations_string,'mode': mode or 'car','language': language or 'en-US','key': self.key,}
        options = {} 
        self.default_options['url'] = url
        self.default_options['method'] = method
        self.default_options['params'] = params

        options = self.default_options

        return request(options)