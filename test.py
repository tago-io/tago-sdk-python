#
# Analysis Example
# Get Device List
#
# This analysis retrieves the device list of your account and print to the console.
# There are examples on how to apply filter.
#
# Environment Variables
# In order to use this analysis, you must setup the Environment Variable table.
#
# account_token: Your account token
#
# Steps to generate an account_token:
# 1 - Enter the following link: https://admin.tago.io/account/
# 2 - Select your Profile.
# 3 - Enter Tokens tab.
# 4 - Generate a new Token with Expires Never.
# 5 - Press the Copy Button and place at the Environment Variables tab of this analysis.

from tago import Account
from tago import Analysis


# The function myAnalysis will run when you execute your analysis
def myAnalysis(context, scope):
  # reads the value of account_token from the environment variable
  breakpoint()
  account_token = list(
      filter(
          lambda account_token: account_token["key"] == "account_token",
          context.environment,
      )
  )
  account_token = account_token[0]["value"]

  if not account_token:
      return context.log("Missing account_token Environment Variable.")

  my_account = Account(account_token)

  # Example of filtering devies by Tag.
  # You can filter by: name, last_input, last_output, bucket, etc.
  my_filter = {
      "tags": [
          {
              "key": "keyOfTagWeWantToSearch",
              "value": "valueOfTagWeWantToSearch",
          }
      ],
      # 'bucket': '55d269211a2e236c25bb9859',
      # 'name': 'My Device'
      # 'name': 'My Dev*
  }
  # Searching all devices with tag we want
  devices = my_account.devices.list(page=1, fields=["id", "tags"], amount=10000)
  if devices["status"] is True:
      context.log(devices["result"])  # Array with dataz
  else:
      context.log(devices["message"])  # Error (if status is False)


# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('7f52b0eb-b5dc-405a-a965-0cdfee9e97a4').init(myAnalysis)
