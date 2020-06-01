import xml.etree.ElementTree as ET
import unittest

class TestParse(unittest.TestCase):
    def test_parse(self,result):
        expected_names = ["ACCT400","ACCT500","ACCT600"]
        expected_paid = ["600","70","0"]
        expected_due = ["10000","40","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)



def print_xml():

    names = []
    paid=[]
    due=[]

    tree = ET.parse('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.xml')
    root = tree.getroot()

    count = 0
    for child in root:
        print ("Account name is:" + child.tag)
        print("Paid ammount is:"+ str(root[count][0].text))
        print("Due ammount is:"+ str(root[count][1].text))
        print("------------------------------------------------------------------------")
    
        names.append(child.tag)
        paid.append(str(root[count][0].text))
        due.append(str(root[count][1].text))

        count += 1

    return [names,paid,due]

if __name__ == "__main__":

    result = print_xml()

    test = TestParse()
    test.test_parse(result)

    print("Everything Good!")