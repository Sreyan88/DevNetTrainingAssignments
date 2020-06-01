import json

def print_json():

    names = []
    paid=[]
    due=[]
    # Opening the file
    with open('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.json') as f:
        accounts = json.load(f)
    # Parsing
    for account in accounts:
        print("Account name is :" + account)
        print("Paid amount for account is:" + str(accounts[account]["paid"]))
        print("Due amount for account is:" + str(accounts[account]["due"]))
        print("------------------------------------------------------------------------")
        names.append(account)
        paid.append(str(accounts[account]["paid"]))
        due.append(str(accounts[account]["due"]))

    return [names,paid,due]


if __name__ == "__main__":

    print_json()







