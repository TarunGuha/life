from typing import Union
from pydantic import BaseModel, root_validator


class AirTracking(BaseModel):
    airline_code: str
    document_number: str

    @root_validator(pre=True)
    def validate_air_tracking_payload(cls, values):
        if len(values.get("airline_code")) != 3:
            raise ValueError("Incorrect Airline Code")
        if len(values.get("document_number")) != 8:
            raise ValueError("Incorrect Document Number")
        return values
