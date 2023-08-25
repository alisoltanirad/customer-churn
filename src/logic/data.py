# -*- coding: utf-8 -*-
"""Data processing

This module contains functions to load and process training data.

"""

import pandas as pd

from config import BQ_DATASET, BQ_PROJECT, BQ_TABLE


def load_training_data_from_bigquery():
    """Load training data from BigQuery

    This function makes a query to BigQuery to load customer churn training data
    and returns the data in the shape of a Pandas dataframe

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


if __name__ == "__main__":
    dataset: pd.DataFrame = load_training_data_from_bigquery()
    print(dataset.shape)
    print(dataset.columns)
    print(dataset.head())
