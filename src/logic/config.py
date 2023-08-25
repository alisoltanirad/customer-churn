# -*- coding: utf-8 -*-
"""Configurations

This module contains configs for training/testing the model

"""
# pylint: disable=unused-variable

# BigQuery
BQ_PROJECT: str = "customer-churn-1"
BQ_DATASET: str = "bank_customer_churn"
BQ_TABLE: str = "customer_data"

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
