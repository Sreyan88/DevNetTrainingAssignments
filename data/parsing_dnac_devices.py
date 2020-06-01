import json

with open('dnac_devices.json') as f:
    devices = json.load(f)

for device in devices["response"]:
    print("Device ID is :" + str(device["id"]))
    print("Device Family is :" + str(device["family"]))
    print("Device Software Type is :" + str(device['softwareType']))
    print("Device Management IP Address  is :" + str(device['managementIpAddress']))
    print("------------------------------------------------------------------------")