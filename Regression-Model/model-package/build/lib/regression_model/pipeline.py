from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import (
    AddMissingIndicator,
    MeanMedianImputer,
)
from feature_engine.selection import DropFeatures
from feature_engine.transformation import YeoJohnsonTransformer
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from regression_model.config.core import config

ces_pipe = Pipeline(
    [
        # ==== VARIABLE TRANSFORMATION =====
        ("yjt", YeoJohnsonTransformer(variables=config.model_config.numericals_yjt_vars)),
        ("scaler", MinMaxScaler()),
        (
            "Lasso",
            Lasso(
                alpha=config.model_config.alpha,
                random_state=config.model_config.random_state,
            ),
        ),
    ]
)
