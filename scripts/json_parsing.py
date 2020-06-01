import json

def print_json():

    with open('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.json') as f:
        accounts = json.load(f)

    for account in accounts:
        print("Account name is :" + account)
        print("Paid amount for account is:" + str(accounts[account]["paid"]))
        print("Due amount for account is:" + str(accounts[account]["due"]))
        print("------------------------------------------------------------------------")


if __name__ == "__main__":

    print_json()