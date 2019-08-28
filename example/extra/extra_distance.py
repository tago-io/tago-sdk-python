import os
import sys
from tago import Tago
sys.path.append('../..')


TOKEN = 'AIzaSyAJSOIe3c2vxYXa0YDtnf15JFkuRK-3tIk'


def print_result(result):
    for key, value in result.iteritems():
        print(key + " : ", value)


def test_measure():
    result = Tago(TOKEN).extra.distance().measure(
        '35.7706256,-78.6952835', '35.7728213,-78.6865257', '', '')
    print("Distance Test:")
    print_result(result)


test_measure()
