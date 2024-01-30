import logging
from .get_ana_cargo_cookies import call_get_ana_cargo_cookies
from .get_ana_cargo_bearer_token import call_get_ana_cargo_bearer_token
from .get_ana_cargo_raw_track_data import call_get_ana_cargo_raw_track_data
from .get_ana_cargo_raw_activity_data import call_get_ana_cargo_raw_activity_data


def track_ana_cargo_awb(request):
    cookies = call_get_ana_cargo_cookies()
    bearer_token = call_get_ana_cargo_bearer_token(cookies)
    tracking_data = call_get_ana_cargo_raw_track_data(cookies, bearer_token, request)
    activity_data = call_get_ana_cargo_raw_activity_data(cookies, bearer_token, request)

    return {"payload": activity_data, "status": 200}
