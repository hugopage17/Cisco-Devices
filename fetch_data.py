import requests
import json
requests.packages.urllib3.disable_warnings()

class Fetch:
    def __init__(self):
        url = "https://sandboxapicem.cisco.com/api/v1/ticket"
        payload = "{\n\t\"username\":\"devnetuser\",\n\t\"password\":\"Cisco123!\"\n}"
        headers = {
          'Content-type': 'application/json',
          'Accept': 'application/json'
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            j = json.loads(response.text)
            token = j['response']['serviceTicket']
            self.token = token
            print('Token:',token)
        except Exception as e:
            print(e)

    def get_device_list(self):
        print('Accessing device list')
        url = "https://sandboxapicem.cisco.com/api/v1/network-device"
        headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'x-auth-token': self.token
        }
        response = requests.request("GET", url, headers=headers)
        j = json.loads(response.text)
        return j['response']
