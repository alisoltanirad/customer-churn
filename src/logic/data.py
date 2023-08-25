# -*- coding: utf-8 -*-
"""Data processing

This module contains functions to load and process training data.

"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from config import (
    BQ_DATASET,
    BQ_PROJECT,
    BQ_TABLE,
    CATEGORICAL_COLS,
    FEATURES_TO_USE,
    NUMERIC_COLS,
)


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
    return X[FEATURES_TO_USE]


def preprocess_features(X: pd.DataFrame) -> pd.DataFrame:
    """Feature preprocessing

    This function normalizes numeric features and encodes categorical features.

    Args:
        X (pd.DataFrame): Features to preprocess

    Returns:
        pd.DataFrame: Preprocessed features

    """
    # Define feature preprocessors
    standard_scaler = StandardScaler()
    one_hot_encoder = OneHotEncoder()
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", standard_scaler, NUMERIC_COLS),
            ("cat", one_hot_encoder, CATEGORICAL_COLS)
        ]
    )

    # Preprocess features
    preprocessed_data = preprocessor.fit_transform(X)
    X = pd.DataFrame(preprocessed_data)

    # Return preprocessed features
    return X


def get_x_y() -> tuple[pd.DataFrame, pd.Series]:
    """Get training data

    This function runs training dataset loading and preprocessing steps
    and returns final features and labels to be used in the model for training.

    Returns:
        pd.DataFrame: X (features)
        pd.Series: y (labels)

    """
    dataset: pd.DataFrame = load_training_data_from_bigquery()
    X, y = split_x_y(dataset)
    X = select_features(X)
    X = preprocess_features(X)
    return X, y


if __name__ == "__main__":
    X, y = get_x_y()
    print(X.shape)
    print(X.head())
    print(y.shape)
    print(y.head())
