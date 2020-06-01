import yaml
yaml_file = open("C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.yml")
accounts = yaml.load(yaml_file, Loader=yaml.FullLoader)

for account in accounts:
    print("Account name is :" + account)
    print("Paid amount for account is:" + str(accounts[account]["paid"]))
    print("Due amount for account is:" + str(accounts[account]["due"]))
    print("------------------------------------------------------------------------")