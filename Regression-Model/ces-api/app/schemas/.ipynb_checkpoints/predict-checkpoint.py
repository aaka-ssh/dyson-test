from typing import Any, List, Optional

from pydantic import BaseModel
from regression_model.processing.validation import CesDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class MultipleCesDataInputs(BaseModel):
    inputs: List[CesDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "longitude": "-117.05",
                        "latitude": "32.58",
                        "housing_median_age": "22",
                        "total_rooms": "2101",
                        "total_bedrooms": "399",
                        "population": "1551",
                        "households": "371",
                        "median_income": "4.1518",
                        "median_ces": "136900",
                        "ocean_proximity": "NEAR OCEAN",
                        "total_rooms_per_person": "1.35460992907801",
                        "bedrooms_per_room": "0.189909566872917",
                        "income_per_person": "0.00267685364281108",
                        "ocean_proximity_less_than_1H_OCEAN": "0",
                        "ocean_proximity_INLAND": "0",
                        "ocean_proximity_ISLAND": "0",
                        "ocean_proximity_NEAR_BAY": "0",
                        "ocean_proximity_NEAR_OCEAN": "1",
                    }
                ]
            }
        }
