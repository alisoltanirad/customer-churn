# -*- coding: utf-8 -*-
"""Training

This module contains functions to train the classifer. To train a new model,
first set the model parameters in `config` module, then run this file.

Example:
    From the project's root, run:
        $ python src/logic/train.py

"""

import pandas as pd
from xgboost import XGBClassifier

from config import XGB_PARAMS

from data import get_x_y


def train(X: pd.DataFrame, y: pd.Series) -> XGBClassifier:
    """Train the classifer

    This function creates and trains a classifier using training data.

    Args:
        X (pd.DataFrame): Features
        y (pd.Series): Labels

    Returns:
        XGBClassifier: Classifier
    """
    classifier = XGBClassifier(**XGB_PARAMS)
    classifier.fit(X, y)

    return classifier


if __name__ == "__main__":
    X, y = get_x_y()
    classifier = train(X, y)
    print(classifier)
