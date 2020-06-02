import unittest

from json_parsing import JSON
from xml_parsing import XML
from yaml_parsing import YAML
from parsing_dnac_devices import DNAC

class TestParse(unittest.TestCase):

    def test_json_test(self):
        J = JSON()
        expected_names = ["ACCT100","ACCT200","ACCT300"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(J.testing(),expected_list)

    def test_xml_test(self):
        X = XML()
        expected_names = ["ACCT400","ACCT500","ACCT600"]
        expected_paid = ["600","70","0"]
        expected_due = ["10000","40","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(X.testing(),expected_list)

    def test_yaml_test(self):
        Y = YAML()
        expected_names = ["ACCT700","ACCT800","ACCT900"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(Y.testing(),expected_list)


    def test_dnac_test(self):
        D = DNAC()
        expected_devids = ["1904ca0d-01be-4d13-88e5-4f4f9980b512","181a0fcb-e56e-4833-a92a-ec9932be427c","3ab79a68-4a3a-4cdc-b41e-eb98dabcdb84","7efadae4-0023-434f-8ae6-0bbc3c51ff2c","ea400390-f224-4587-a11e-a941c68bd141"]
        expected_family = ["Routers","None","None","None","None"]
        expected_softype = ["IOS-XE","None","None","None","None"]
        expected_management = ["10.10.22.253","192.0.2.2","192.0.2.1","192.0.2.3","192.0.2.4"]
        expected_list = [expected_devids,expected_family,expected_softype,expected_management]

        self.assertEqual(D.testing(),expected_list)




if __name__ == "__main__":
    unittest.main()

    #Test = TestParse()
    #Test.dnac_test()

    #J = JSON()
    #json_out = J.testing()
    #Test.json_test(json_out)

    #X = XML()
    #xml_out = X.testing()
    #Test.xml_test(xml_out)

    #Y = YAML()
    #yaml_out = Y.testing()
    #Test.yaml_test(yaml_out)

    #D = DNAC()
    #dnac_out = D.testing()
    #Test.dnac_test(dnac_out)

    print("All outputs look good!")




    
