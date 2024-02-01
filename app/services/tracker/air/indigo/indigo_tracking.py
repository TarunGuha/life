import logging
from .get_indigo_raw_track_data import call_get_indigo_raw_track_data


def track_indigo_awb(request):
    raw_data = call_get_indigo_raw_track_data(request)

    return {"payload": raw_data, "status": 200}
