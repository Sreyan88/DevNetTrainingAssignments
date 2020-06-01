import json
import unittest

class TestParse(unittest.TestCase):
    def test_parse(self,result):
        expected_devids = ["1904ca0d-01be-4d13-88e5-4f4f9980b512","181a0fcb-e56e-4833-a92a-ec9932be427c","3ab79a68-4a3a-4cdc-b41e-eb98dabcdb84","7efadae4-0023-434f-8ae6-0bbc3c51ff2c","ea400390-f224-4587-a11e-a941c68bd141"]
        expected_family = ["Routers","None","None","None","None"]
        expected_softype = ["IOS-XE","None","None","None","None"]
        expected_management = ["10.10.22.253","192.0.2.2","192.0.2.1","192.0.2.3","192.0.2.4"]
        expected_list = [expected_devids,expected_family,expected_softype,expected_management]

        self.assertEqual(result,expected_list)

def print_dnac_devices():
    devids=[]
    family=[]
    softype=[]
    management=[]

    with open('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/dnac_devices.json') as f:
        devices = json.load(f)

    for device in devices["response"]:
        print("Device ID is :" + str(device["id"]))
        print("Device Family is :" + str(device["family"]))
        print("Device Software Type is :" + str(device['softwareType']))
        print("Device Management IP Address  is :" + str(device['managementIpAddress']))
        print("------------------------------------------------------------------------")

        devids.append(str(device["id"]))
        family.append(str(device["family"]))
        softype.append(str(device['softwareType']))
        management.append(str(device['managementIpAddress']))

    return [devids,family,softype,management]

if __name__ == "__main__":

    result = print_dnac_devices()

    test = TestParse()
    test.test_parse(result)

    print("Everything Good!")