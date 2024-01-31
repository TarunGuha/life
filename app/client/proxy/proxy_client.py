import random
import logging
import requests
from core.config import DIGITAL_OCEAN_FUNCTION_URI, DIGITAL_OCEAN_AUTH_KEY


class ProxyRequest:

    def call_proxy_client(self, request_specifications):
        headers = {
            "Content-Type": "application/json",
            "Authorization": DIGITAL_OCEAN_AUTH_KEY,
        }

        params = {
            "blocking": True,
            "result": True,
        }

        function_id = str(random.randint(1, 2))
        logging.info(
            "Proxy => Invoking Function ID -> {function_id}".format(
                function_id=function_id
            )
        )

        response = requests.post(
            url=DIGITAL_OCEAN_FUNCTION_URI + function_id,
            params=params,
            headers=headers,
            json=request_specifications,
        )

        return response

    def request(
        self,
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

        proxy_client_call = self.call_proxy_client(
            request_specifications=specifications
        )
        proxy_client_response = proxy_client_call.json()
        return proxy_client_response
