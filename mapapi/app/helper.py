import json
from django.http import JsonResponse

def success_response(data=None):
    response = {"status_code": 200,}
    if data:
        response["data"] = data
    return JsonResponse(response, status=200)


def error_response(errors=None, status_code=202):
    response = {"status_code": status_code,}
    if errors:
        response["errors"] = errors
    return JsonResponse(response, status=status_code)


