import logging
from client.proxy.proxy_client import call_proxy_client


def track_virgin_atlantic_awb(request):
    specifications = {
        "request_parameters": {
            "request_type": "GET",
            "request_url": "https://api.ipify.org?format=json",
            "request_params": {},
            "request_data": {},
            "request_json": {"hello": "ok"},
        }
    }

    proxy_client_call = call_proxy_client(request_specifications=specifications)
    proxy_client_response = proxy_client_call.json()

    return {"payload": {"response": proxy_client_response}, "status": 200}
