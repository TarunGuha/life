import logging
from .get_air_canada_basic_cookies import call_get_air_canada_basic_cookies
from .get_air_canada_auth_cookies import call_get_air_canada_auth_cookies
from .get_air_canada_bearer_token import call_get_air_canada_bearer_token
# from .get_air_canada_signature import call_get_air_canada_generate_signature
from .get_air_canada_raw_track_data import call_get_air_canada_raw_track_data


def track_air_canada_awb(request):
    basic_cookies = call_get_air_canada_basic_cookies()
    auth_cookies = call_get_air_canada_auth_cookies(basic_cookies)
    auth_tokens = call_get_air_canada_bearer_token()
    # signature = call_get_air_canada_generate_signature(auth_tokens)
    # raw_data = call_get_air_canada_raw_track_data(
    #     basic_cookies, auth_cookies, auth_tokens, signature, request
    # )

    return {"payload": auth_tokens, "status": 200}
