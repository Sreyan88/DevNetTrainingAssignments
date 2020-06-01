import json

def print_dnac_devices():
    devids=[]
    family=[]
    softype=[]
    management=[]

    # Opening the file
    with open('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/dnac_devices.json') as f:
        devices = json.load(f)
    
    # Parsing the json
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

    print_dnac_devices()
