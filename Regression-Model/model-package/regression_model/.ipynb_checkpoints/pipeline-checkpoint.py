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
        # ===== IMPUTATION =====
        # add missing indicator
        (
            "missing_indicator",
            AddMissingIndicator(variables=config.model_config.numerical_vars_with_na),
        ),
        # impute numerical variables with the mean
        (
            "mean_imputation",
            MeanMedianImputer(
                imputation_method="mean",
                variables=config.model_config.numerical_vars_with_na,
            ),
        ),
        # ==== VARIABLE TRANSFORMATION =====
        ("yjt", YeoJohnsonTransformer(variables=config.model_config.numericals_yjt_vars)),
        # == CATEGORICAL ENCODING
        # one hot encodinf of categorical variable
        (
            "ohe_enc",
            OneHotEncoder(
                encoding_method="ordered",
                variables=config.model_config.categorical_vars,
            ),
        ),
        ("drop_features", DropFeatures(features_to_drop=[config.model_config.categorical_vars])),
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
