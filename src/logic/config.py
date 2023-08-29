# -*- coding: utf-8 -*-
"""ML Configurations

This module contains configs for training/testing the model.

"""
# pylint: disable=unused-variable

# Classifier
MODEL_VERSION: str = "1.0"
MODEL_FILENAME: str = "model.json"
PREPROCESSOR_FILENAME: str = "preprocessor.joblib"

# BigQuery (training dataset)
BQ_PROJECT: str = "customer-churn-1"
BQ_DATASET: str = "bank_customer_churn"
BQ_TABLE: str = "customer_data"

# Google Cloud Storage (saving models and preprocessors)
GCS_BUCKET: str = "customer-churn-classifier"
GCS_FOLDER: str = "v" + MODEL_VERSION

# Feature selection
FEATURES_TO_USE: list[str] = [
    "CreditScore",
    "Geography",
    "Gender",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary",
    "Complain",
    "Satisfaction_Score",
    "Card_Type",
    "Point_Earned"
]

# Numeric/Categorical features
NUMERIC_COLS: list[str] = [
    "CreditScore",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary",
    "Complain",
    "Satisfaction_Score",
    "Point_Earned",
]
CATEGORICAL_COLS: list[str] = [
    "Geography",
    "Gender",
    "Card_Type"
]

# XGBoost classifier parameters
XGB_PARAMS: dict = {
    "eta": 0.3,
    "max_depth": 6,
}
