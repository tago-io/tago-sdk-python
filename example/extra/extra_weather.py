import os
from tago import Tago
import sys
sys.path.append('../..')


TOKEN = 'fe1b837fb8f31dc6'


def print_result(result):
  for key, value in result.value.iteritems():
    print(key + " : ", value)


def test_current():
  result = Tago(TOKEN).extra.weather().current('27606', False, 'EN')
  print("Current Weather Test:")
  print_result(result)


def test_history():
  result = Tago(TOKEN).extra.weather().history(
    '2017-02-21', '27606', False, 'EN')
  print("Weather History Test:")
  print_result(result)


def test_forecast():
  result = Tago(TOKEN).extra.weather().forecast('27606', False, 'EN')
  print("Weather Forecast Test:")
  print_result(result)


def test_alerts():
  result = Tago(TOKEN).extra.weather().alerts('27606', False, 'EN')
  print("Weather Alert Test:")
  print_result(result)


test_current()
test_history()
test_forecast()
test_alerts()
