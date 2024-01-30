import random
import requests
from core.config import DIGITAL_OCEAN_FUNCTION_URI, DIGITAL_OCEAN_AUTH_KEY


def call_proxy_client(request_specifications):
    headers = {
        "Content-Type": "application/json",
        "Authorization": DIGITAL_OCEAN_AUTH_KEY,
    }

    params = {
        "blocking": True,
        "result": True,
    }

    response = requests.post(
        url=DIGITAL_OCEAN_FUNCTION_URI + str(random.randint(1, 2)),
        params=params,
        headers=headers,
        json=request_specifications,
    )

    return response


def proxy_request(
    request_method,
    request_url,
    request_params={},
    request_data={},
    request_json={},
    request_headers={},
    request_cookies={},
):
    specifications = {
        "request_parameters": {
            "request_method": request_method,
            "request_url": request_url,
            "request_params": request_params,
            "request_data": request_data,
            "request_json": request_json,
            "request_headers": request_headers,
            "request_cookies": request_cookies,
        }
    }

    proxy_client_call = call_proxy_client(request_specifications=specifications)
    proxy_client_response = proxy_client_call.json()
    return proxy_client_response
