# -*- coding: utf-8 -*-
"""Data processing

This module contains functions to load and process training data.

"""

import pandas as pd

from config import BQ_DATASET, BQ_PROJECT, BQ_TABLE


def load_training_data_from_bigquery() -> pd.DataFrame:
    """Load training data from BigQuery

    This function makes a query to BigQuery to load customer churn training data
    and returns the data in the shape of a Pandas dataframe.

    Returns:
        pd.DataFrame: Customer churn training data

    """
    # SQL query to retrieve training data from BigQuery
    query: str = f"""
        SELECT * FROM `{BQ_PROJECT}.{BQ_DATASET}.{BQ_TABLE}`
    """

    # Load data from BigQuery into Pandas dataframe
    dataset: pd.DataFrame = pd.read_gbq(query, project_id=BQ_PROJECT, dialect="standard")

    # Return training dataset
    return dataset


def split_x_y(dataset: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Split features and labels

    Args:
        dataset (pd.DataFrame): Training data

    Returns:
        pd.DataFrame: X (features)
        pd.Series: y (labels)

    """
    return dataset[dataset.columns.difference(["Exited"])], dataset["Exited"]


def select_features(X: pd.DataFrame) -> pd.DataFrame:
    """Feature selection

    This function selects features useful to train the model.

    Args:
        X (pd.DataFrame): Feature set containing all features

    Returns:
        pd.DataFrame: Feature set containing selected features

    """
    return X[[
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
    ]]


if __name__ == "__main__":
    dataset: pd.DataFrame = load_training_data_from_bigquery()
    X, y = split_x_y(dataset)
    X = select_features(X)
    print(X.shape)
    print(X.columns)
    print(X.head())
    print(y.head())
