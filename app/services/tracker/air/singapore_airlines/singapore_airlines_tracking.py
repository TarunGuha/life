import logging
from .get_singapore_airlines_raw_track_data import (
    call_get_singapore_airlines_raw_track_data,
)


def track_singapore_airlines_awb(request):
    raw_data = call_get_singapore_airlines_raw_track_data(request)
    return {"payload": raw_data, "status": 200}
