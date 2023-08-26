# -*- coding: utf-8 -*-
"""Prediction

This module contains functions to take the input data,
transform features using preprocessing pipeline and
predict labels using the trained model.

"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier


def predict(
    classifier: XGBClassifier,
    preprocessor: ColumnTransformer, 
    data: pd.DataFrame
):
    """Prediction

    This function takes and preprocess the input data
    and predicts a label for each observation.

    Args:
        classifier (XGBClassifier): Classifer for prediction
        preprocessor (ColumnTransformer): Preprocessing pipeline
        data (pd.DataFrame): Input data to predict

    Returns:
        pd.Series: Predicted labels

    """
    # Preprocess the input data
    preprocessed_data = preprocessor.transform(data)
    X = pd.DataFrame(preprocessed_data)

    # Run the classifier and predict the labels
    labels: pd.Series = pd.Series(classifier.predict(X))

    # Return the labels
    return labels
