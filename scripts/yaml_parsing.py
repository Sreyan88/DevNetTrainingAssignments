import yaml

def print_yaml():

    names = []
    paid=[]
    due=[]

    # Opening the file
    yaml_file = open("C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.yml")
    accounts = yaml.load(yaml_file, Loader=yaml.FullLoader)
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

    print_yaml()