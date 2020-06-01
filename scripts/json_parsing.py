import json

class JSON:
    def __init__(self):

        with open('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.json') as f:
            accounts = json.load(f)

        self.object = accounts

    def testing(self):
        accounts = self.object

        names = []
        paid=[]
        due=[]

        for account in accounts:
            names.append(account)
            paid.append(str(accounts[account]["paid"]))
            due.append(str(accounts[account]["due"]))

        return [names,paid,due]

    def print_json(self):
        accounts = self.object

        for account in accounts:
            print("Account name is :" + account)
            print("Paid amount for account is:" + str(accounts[account]["paid"]))
            print("Due amount for account is:" + str(accounts[account]["due"]))
            print("------------------------------------------------------------------------")



if __name__ == "__main__":

    J = JSON()
    J.print_json()






