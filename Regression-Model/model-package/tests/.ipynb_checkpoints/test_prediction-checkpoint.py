import math
import warnings

import numpy as np

from regression_model.predict import make_prediction

warnings.filterwarnings("ignore", category=DeprecationWarning)


def test_make_prediction(sample_input_data):
    # Given
    expected_first_prediction_value = 193928
    expected_no_predictions = 4128

    # When
    result = make_prediction(input_data=sample_input_data)
    print("*************")
    print("result")

    # Then
    predictions = result.get("predictions")
    assert isinstance(predictions, list)
    assert isinstance(predictions[0], np.float64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert math.isclose(predictions[0], expected_first_prediction_value, abs_tol=100)
