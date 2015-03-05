### ignore this block if you don't know what is.
import sys
sys.path.append("..")
### ---

from tago import Tago

my_device = Tago('b61c4c00-b85b-11e4-b1a6-0f628ad58a3a').device

def func_callback_data(data):
    print data

    ''' Example output (data (python object))
    {
        u'variable': u'speed',
        u'origin': u'54e61b6624aaf6cd1d97613f',
        u'bucket': u'54e61b5024aaf6cd1d97613e',
        u'value': u'2',
        u'time': u'2015-03-05T18:09:03.197Z'
    }
    '''

my_device.listening(func_callback_data)
