##### Created By:       Sandhya Dodiya
##### Created Date:     8/02/2021
##### Last Modified:    9/02/2021

# Google Map API

Quick Setup
 * Create python3 virtual environment.
 ```bash
$ python3 -m venv env
$ source env/bin/activate
$ mkdir mapapi
$ cd mapapi
```
 * Install packages from requirements.txt.
 ```bash
 $ pip install -r requirements.txt
 ```
### Initial configuration

##### Required Details in configuration File.

Please go to  /etc/mapapi/ dir  and open config.yaml file.
Replace YOUR_API_KEY with actual key.

### How to run?
```bash
cd mapapi
$ python manage.py runserver
```
### Modules:
```
1.mapapi
```
### Backend API
##### Endpoints
Local http://127.0.0.1:8000/
##### A. :
```
1.  GET /api/getAddressDetails/
    Description: Returns data related to geolocation. Please make post request with address and output format
```   
```
2.  POST /api/getAddressDetails/
    Description : Returns data related to geolocation.
    Content-Type: application/json, text/xml

    Sample Requests
    Content-Type: application/json
    {
    "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008",
    "output_format": "json" [:options -- json, xml]
    }

    Request Parameters
    Property        |  Type    |   Description          |  Required
    ---------------------------------------------------------------
    address         |  String  |   Address              |  Yes
    output_format   |  String  |   Output Format Flag   |  Yes

    Response
    JSON : 
    {
        "status_code": 200,
        "data": {
            "coordinates": {
                "lat": 12.9658286,
                "lng": 77.63948169999999
            },
            "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008"
        }
    }

    XML : 
    <root>
        <status_code>200</status_code>
        <address># 3582,13 G Main Road, 4th Cross Rd, Indiranagar,Bengaluru, Karnataka 560008</address>
        <cordinates>
            <lat>12.9658286</lat>
            <lng>77.6394817</lng>
        </cordinates>
        <status>OK</status>
    </root>
  
    Error Response  
    Operational Errors
    JSON : 
    {
        "status_code": 201,
        "errors": {
            "message": "Please enter valid address and output format"
        }
    }

    XML : 
    <root>
        <status_code>201</status_code>
        <GeocodeResponse>
            <status>REQUEST_DENIED</status>
            <error_message>The provided API key is invalid.</error_message>
        </GeocodeResponse>
    </root>

    Field Errors 
    {
        "status_code": 400,
        "errors": {
            "message": "Address and output format field is required"
        }
    }



