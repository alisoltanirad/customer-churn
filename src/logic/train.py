# -*- coding: utf-8 -*-
"""Training

This module contains functions to train the classifer. To train a new model,
first set the model parameters in `config` module, then run this file.

Example:
    From the project's root, run:
        $ python src/logic/train.py

"""

import os

import pandas as pd
from google.cloud import storage
from xgboost import XGBClassifier

from config import GCS_BUCKET, GCS_FOLDER, MODEL_FILENAME, XGB_PARAMS
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


def save_classifier(classifier: XGBClassifier):
    """Save the classifier

    This function saves the classifier and uploads it to Google Cloud Storage.

    Args:
        classifier (XGBClassifier): XGBoost classifier

    """
    # Save the classifier to a local file
    classifier.save_model(MODEL_FILENAME)

    # Set up Google Cloud client and bucket
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)

    # Upload the classifier to Google Cloud Storage
    blob = bucket.blob(GCS_FOLDER + "/" + MODEL_FILENAME)
    blob.upload_from_filename(MODEL_FILENAME)

    # Remove the local file
    os.remove(MODEL_FILENAME)


if __name__ == "__main__":
    X, y = get_x_y()
    classifier = train(X, y)
    save_classifier(classifier)
    print(classifier)
