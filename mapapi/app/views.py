import requests
import json
import xml.etree.ElementTree as ET

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from app.mixins import CSRFExemptMixin
from app.helper import success_response, error_response
from mapapi.settings import GOOGLE_MAP_API_BASE_URL, GOOGLE_MAP_KEY


class GetAddressDetails(CSRFExemptMixin, View):
    def get(self, request, *args, **kwargs):

        data = {
            "message": "Returns data related to geolocation. Please check REDME.md"
        }

        return JsonResponse(data)

    def post(self, request, *args, **kwargs):

        request_data = json.loads(request.body)
        output_format = request_data.get('output_format', None)
        address = request_data.get('address', None)
        data = {}
        if output_format is not None and address is not None:
            params_data = {
                "address": address,
                "key":  GOOGLE_MAP_KEY,
            }
            try:
                r = requests.get(GOOGLE_MAP_API_BASE_URL+output_format, params=params_data)
                if r.status_code == 200:
                    if output_format == "json":
                        response_data = r.json()
                        if response_data['status'] == "OK":
                            data['coordinates'] = response_data['results'][0]['geometry']['location']
                            data['address'] = address
                            return success_response(data)
                        else:
                            return error_response(response_data,201)
                    elif output_format == "xml":
                        response_data = ET.fromstring(r.text)
                        response_data_status = response_data.findall(".//status")
                        if response_data_status[0].text == "OK":
                            location_lat = response_data.findall(".//result//location/lat")
                            location_lng = response_data.findall(".//result//location/lng")
                            root = ET.Element("root")
                            address_tag = ET.Element("address")
                            cordinates = ET.Element("cordinates")
                            status_code = ET.Element("status_code")
                            root.append(status_code)
                            status_code.text = '200'
                            cordinates.append(location_lat[0])
                            cordinates.append(location_lng[0])
                            root.append(address_tag)
                            root.append(cordinates)
                            root.append(response_data_status[0])
                            address_tag.text = address
                            tree = ET.tostring(root).decode()
                            return HttpResponse(tree)
                        else:
                            root = ET.Element("root")
                            status_code = ET.Element("status_code")
                            root.append(status_code)
                            status_code.text = '201'
                            root.append(ET.fromstring(r.text))
                            tree = ET.tostring(root).decode()
                            return HttpResponse(tree)
                else:
                    data["message"] = "Please enter valid address and output format"
                    return error_response(data,201)
            except Exception as exe:
                return self.render_response(str(exe), output_format)
        else:
            data["message"] = "Address and output format field is required"
            return error_response(data,400)

    @staticmethod
    def render_response(message, output_format):

        if output_format == "xml":
            root = ET.Element("root")
            error_message = ET.Element("address")
            root.append(error_message)
            error_message.text = message
            tree = ET.tostring(root).decode()
            return HttpResponse(tree)
        else:
            data = {}
            data["error_message"] = message
            return JsonResponse(data)