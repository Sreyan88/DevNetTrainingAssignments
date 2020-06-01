import json

with open('db.json') as f:
    accounts = json.load(f)

for account in accounts:
    print("Account name is :" + account)
    print("Paid amount for account is:" + str(accounts[account]["paid"]))
    print("Due amount for account is:" + str(accounts[account]["due"]))