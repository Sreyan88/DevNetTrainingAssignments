import unittest

from json_parsing import print_json
from xml_parsing import print_xml
from yaml_parsing import print_yaml
from parsing_dnac_devices import print_dnac_devices

class TestParse(unittest.TestCase):

    def json_test(self,result):
        expected_names = ["ACCT100","ACCT200","ACCT300"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)

    def xml_test(self,result):
        expected_names = ["ACCT400","ACCT500","ACCT600"]
        expected_paid = ["600","70","0"]
        expected_due = ["10000","40","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)

    def yaml_test(self,result):
        expected_names = ["ACCT700","ACCT800","ACCT900"]
        expected_paid = ["60","70","0"]
        expected_due = ["100","60","0"]

        expected_list = [expected_names,expected_paid,expected_due]

        self.assertEqual(result,expected_list)


    def dnac_test(self,result):
        expected_devids = ["1904ca0d-01be-4d13-88e5-4f4f9980b512","181a0fcb-e56e-4833-a92a-ec9932be427c","3ab79a68-4a3a-4cdc-b41e-eb98dabcdb84","7efadae4-0023-434f-8ae6-0bbc3c51ff2c","ea400390-f224-4587-a11e-a941c68bd141"]
        expected_family = ["Routers","None","None","None","None"]
        expected_softype = ["IOS-XE","None","None","None","None"]
        expected_management = ["10.10.22.253","192.0.2.2","192.0.2.1","192.0.2.3","192.0.2.4"]
        expected_list = [expected_devids,expected_family,expected_softype,expected_management]

        self.assertEqual(result,expected_list)


if __name__ == "__main__":
    Test = TestParse()

    json_out = print_json()
    Test.json_test(json_out)

    xml_out = print_xml()
    Test.xml_test(xml_out)

    json_out = print_yaml()
    Test.yaml_test(json_out)

    dnac_out = print_dnac_devices()
    Test.dnac_test(dnac_out)

    print("All outputs look good!")




    
