import json
import unittest

# Class defined for unittesting
class TestParse(unittest.TestCase):
    def test_parse(self,result):
        expected_names = ["ACCT100","ACCT200","ACCT300"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)


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

    result = print_json()

    test = TestParse()
    test.test_parse(result)

    print("Everything Good!")







