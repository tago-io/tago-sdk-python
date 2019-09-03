import requests
import json
import os

def env_to_obj(environment):
  finalObj = {}
  for tag in environment:
    finalObj[tag.key] = tag.value
  return finalObj
