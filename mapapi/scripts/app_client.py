import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/getAddressDetails/"


headers = {
    "Content-Type": "application/json",
}

def get_address():
    new_data= {
        "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
        "output_format": "json"
        }
    r = requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_data),headers=headers)
    print(r.status_code)

    return r.text


get_address()