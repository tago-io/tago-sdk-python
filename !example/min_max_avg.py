# Analysis Example
# Minimum, maximum, and average

# Get the minimum, maximum, and the average value of the variable temperature from your device,
# and save these values in new variables

# Instructions
# To run this analysis you need to add a device token to the environment variables,
# To do that, go to your device, then token and copy your token.
#* Go the the analysis, then environment variables, 
# type device_token on key, and paste your token on value
import sys
sys.path.append('..')

import functools
from tago import Device
from tago import Analysis

# The function myAnalysis will run when you execute your analysis
def myAnalysis(context, scope):
  # reads the value of device_token from the environment variable
  device_token = list(filter(lambda device_token: device_token['key'] == 'device_token', context.environment))
  device_token = device_token[0]['value']

  if not device_token:
    return context.log("Missing device_token Environment Variable.")
  
  my_device = Device(device_token)

  # This is a filter to get the minimum value of the variable temperature in the last day
  minFilter = {
    'variable': 'temperature',
    'qty': 1
  }

  # Now we use the filter for the device to get the data
  # check if the variable min has any value
  # if so, we crete a new object to send to Tago
  min_result = my_device.find({ 'variable': 'temperature', 'qty': 1 })
  if len(min_result["result"]) and min_result['status'] is True:
    # context.log(min_result["result"])
    min_result = min_result["result"][0]

    minValue = {
      'variable': 'temperature_minimum',
      'value': min_result["value"],
      'unit': 'F',
    }
  
    # now we insert the new object with the minimum value
    result = my_device.insert(minValue)
    if result['status'] is not True:
      return
      # context.log(result['result'])
    else:
      context.log('Temperature Minimum Updated')

  else:
    context.log('Minimum value not found')

  # This is a filter to get the maximum value of the variable temperature in the last day
  maxFilter = {
    'variable': 'temperature',
    'query': 'max',
    'start_date': '1 day',
  }

  max_result = my_device.find(minFilter)
  if len(max_result["result"]) and max_result['status'] is True:
    max_result = max_result["result"][0]

    minValue = {
      'variable': 'temperature_maximum',
      'value': max_result["value"],
      'unit': 'F',
    }
  
    # now we insert the new object with the Maximum value
    result = my_device.insert(minValue)
    if result['status'] is not True:
      context.log(result['result'])
    else:
      context.log('Temperature Maximum Updated')

  else:
    context.log('Maximum value not found')

  # This is a filter to get the last 1000 values of the variable temperature in the last day
  avgFilter = {
    'variable': 'temperature',
    'qty': 1000,
    'start_date': '1 day',
  }

  avg = device.find(avgFilter)
  if len(avg["result"]) and avg['status'] is True:
    temperatureSum = functools.reduce(lambda a,b : a+int(b["value"]),avg["result"])
    temperatureSum = temperatureSum / len(avg)
    context.log(temperatureSum)
  
    avgValue = {
      'variable': 'temperature_average',
      'value': temperatureSum,
      'unit': 'F',
    }

    result = my_device.insert(avgValue)
    if result['status'] is not True:
      context.log(result['result'])
    else:
      context.log('Temperature Average Updated')
  else:
    context.log('No result found for the avg calculation')

# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('Your-account-token').init(myAnalysis)
