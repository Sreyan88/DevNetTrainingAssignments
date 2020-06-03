import json

from get_request import get_devices

class DNAC:

    def __init__(self):
        
        devices = get_devices()
        self.object = json.loads(devices)
        
    def testing(self):
        devices= self.object

        devids=[]
        family=[]
        softype=[]
        management=[]

        for device in devices["response"]:
            devids.append(str(device["id"]))
            family.append(str(device["family"]))
            softype.append(str(device['softwareType']))
            management.append(str(device['managementIpAddress']))

        return [devids,family,softype,management]


    def print_dnac_devices(self):
        devices= self.object

        for device in devices["response"]:
            print("Device ID is :" + str(device["id"]))
            print("Device Family is :" + str(device["family"]))
            print("Device Software Type is :" + str(device['softwareType']))
            print("Device Management IP Address  is :" + str(device['managementIpAddress']))
            print("------------------------------------------------------------------------")


if __name__ == "__main__":

    D = DNAC()
    D.print_dnac_devices()
