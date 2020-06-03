import json

class JSON:
    def __init__(self):

        with open('data/db.json') as f:
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
            print("<h3>Printing Device Details</h3>")
            print("<h3>Account name is</h3><br><br>{}".format(account))
            print("<h3>Paid amount for account is</h3><br><br>{}".format(str(accounts[account]["paid"])))
            print("<h3>Due amount for account is</h3><br><br>{}".format(str(accounts[account]["due"])))
            print("------------------------------------------------------------------------")
            print("<h3>Device Details Printed</h3>")



if __name__ == "__main__":

    J = JSON()
    J.print_json()






