from fastapi import APIRouter
from fastapi.responses import JSONResponse
from actions.tracker.interactions.track_awb import air_tracker
from api.schema.tracker.air_tracking_schema import AirTracking

router = APIRouter(prefix="/tracker", tags=["Trackers"])


@router.post("/air_tracking")
async def call_air_tracking(request: AirTracking):
    response = air_tracker(request)
    return JSONResponse(
        status_code=response.get("status"), content=response.get("payload")
    )
