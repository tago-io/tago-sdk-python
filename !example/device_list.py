import sys
sys.path.append('..')

from tago import Account

MY_ACCOUNT_TOKEN = 'Your-Account-Token'
my_account = Account(MY_ACCOUNT_TOKEN)

filters= {
    "tags": [{'key': 'City', 'value': 'PR'}],
    "name": "qweqwe"
}

# import urllib.parse

# aa = urllib.parse.parse_qs(filters)

# print(aa)
devices = my_account.devices.list(filter=filters)

print(devices)