#!/usr/bin/python3
#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

import requests

if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    response = response.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
