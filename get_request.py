import requests
import json

def get_key():
  url = "https://sandboxdnac2.cisco.com/api/system/v1/auth/token"
  payload = {}
  headers = {
  'Authorization': 'Basic ZG5hY2RldjpEM3Y5M1RAd0sh'
  }
  response = requests.request("POST", url, headers=headers, data = payload)
  response = json.loads(response.text)

  return(response["Token"])


def get_devices():


  url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

  key = get_key()

  payload = {}
  headers = {
  'x-auth-token': key
}

  response = requests.request("GET", url, headers=headers, data = payload)

  return (response.text)


