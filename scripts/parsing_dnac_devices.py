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
            print("<h3>Printing Device Details</h3>")
            print("<h3>Device ID is </h3><br><br>{}".format((str(device["id"]))))
            print("<h3>Device Family is </h3><br><br>{}".format(str(device["family"])))
            print("<h3>Device Software Type is </h3><br><br>{}".format(str(device['softwareType'])))
            print("<h3>Device Management IP Address  is </h3><br><br>{}".format(str(device['managementIpAddress'])))
            print("------------------------------------------------------------------------")


if __name__ == "__main__":

    D = DNAC()
    D.print_dnac_devices()
