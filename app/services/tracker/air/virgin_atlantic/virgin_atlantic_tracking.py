import logging
from .get_virgin_atlantic_token import call_get_virgin_atlantic_token
from .get_virgin_atlantic_raw_track_data import call_get_virgin_atlantic_raw_track_data
from .get_virgin_atlantic_booking_reference_number import (
    call_get_virgin_atlantic_booking_reference_number,
)


def track_virgin_atlantic_awb(request):
    bearer_token = call_get_virgin_atlantic_token()

    booking_reference_number = call_get_virgin_atlantic_booking_reference_number(
        request=request, bearer_token=bearer_token
    )

    raw_tracking_data = call_get_virgin_atlantic_raw_track_data(
        bearer_token=bearer_token, booking_reference_number=booking_reference_number
    )

    return {"payload": raw_tracking_data, "status": 200}
