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
