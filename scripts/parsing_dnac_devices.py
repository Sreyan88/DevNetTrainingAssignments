import json

class DNAC:

    def __init__(self):

        with open('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/dnac_devices.json') as f:
            devices = json.load(f)

        self.object = devices

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
