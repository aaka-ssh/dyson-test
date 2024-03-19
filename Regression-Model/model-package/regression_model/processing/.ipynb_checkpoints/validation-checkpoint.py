from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from regression_model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()
    new_vars_with_na = [
        var
        for var in config.model_config.features
        if var
        not in config.model_config.numerical_vars_with_na
        and validated_data[var].isnull().sum() > 0
    ]
    validated_data.dropna(subset=new_vars_with_na, inplace=True)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    relevant_data = input_data[config.model_config.features].copy()
    validated_data = drop_na_inputs(input_data=relevant_data)
    errors = None

    try:
        # replace numpy nans so that pydantic can validate
        MultipleCesDataInputs(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class CesDataInputSchema(BaseModel):
    longitude: Optional[float]
    latitude: Optional[float]
    housing_median_age: Optional[int]
    total_rooms: Optional[int]
    total_bedrooms: Optional[float]
    population: Optional[int]
    households: Optional[int]
    median_income: Optional[float]
    median_ces: Optional[int]
    ocean_proximity: Optional[object]
    total_rooms_per_person: Optional[float]
    bedrooms_per_room: Optional[float]
    income_per_person: Optional[float]
    ocean_proximity_<1H OCEAN: Optional[int]
    ocean_proximity_INLAND: Optional[int]
    ocean_proximity_ISLAND: Optional[int]
    ocean_proximity_NEAR BAY: Optional[int]
    ocean_proximity_NEAR OCEAN: Optional[int]


class MultipleCesDataInputs(BaseModel):
    inputs: List[CesDataInputSchema]
