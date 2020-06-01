import yaml
import unittest



class TestParse(unittest.TestCase):
    def test_parse(self,result):
        expected_names = ["ACCT700","ACCT800","ACCT900"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)


def print_yaml():

    names = []
    paid=[]
    due=[]


    yaml_file = open("C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.yml")
    accounts = yaml.load(yaml_file, Loader=yaml.FullLoader)

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

    result = print_yaml()

    test = TestParse()
    test.test_parse(result)

    print("Everything Good!")