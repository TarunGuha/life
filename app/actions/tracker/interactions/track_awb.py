from services.tracker.air.air_india import track_air_india_awb
from services.tracker.air.virgin_atlantic import track_virgin_atlantic_awb


def air_tracker(request):
    match request.airline_code:
        case "098":
            response = track_air_india_awb(request)
        case "932":
            response = track_virgin_atlantic_awb(request)
        case _:
            response = {
                "payload": {"response": "not_found", "success": False},
                "status": 501,
            }
    return response
