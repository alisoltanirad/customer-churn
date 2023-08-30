# -*- coding: utf-8 -*-
"""Prediction

This module contains functions to take the input data,
transform features using preprocessing pipeline and
predict labels using the trained model.

"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier

from .config import GCS_FOLDER
from .gc_utils import load_from_gcs


def predict(
    classifier: XGBClassifier, preprocessor: ColumnTransformer, data: pd.DataFrame
) -> pd.Series:
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


if __name__ == "__main__":
    classifier, preprocessor = load_from_gcs(GCS_FOLDER)
    print(classifier)
    print(preprocessor)
    sample = pd.DataFrame(
        {
            "CreditScore": [821, 630],
            "Geography": ["France", "France"],
            "Gender": ["Male", "Female"],
            "Age": [50, 46],
            "Tenure": [7, 0],
            "Balance": [0, 0],
            "NumOfProducts": [2, 1],
            "HasCrCard": [1, 1],
            "IsActiveMember": [1, 1],
            "EstimatedSalary": [10022.8, 6294.84],
            "Complain": [0, 1],
            "Satisfaction_Score": [2, 3],
            "Card_Type": ["SILVER", "GOLD"],
            "Point_Earned": [205, 345],
        }
    )
    labels = predict(classifier, preprocessor, sample)
    print(labels)
