# -*- coding: utf-8 -*-
"""Google Cloud Utilities

This module contains functions to read and write data to Google Cloud services.

"""

import os

from google.cloud import storage
from xgboost import XGBClassifier

from config import GCS_BUCKET, GCS_FOLDER, MODEL_FILENAME


def upload_to_gcs(filename: str):
    """Save to Google Cloud Storage

    This function uploads a local file to Google Cloud Storage.

    Args:
        filename (str): Name of the file (model or pipeline)

    """
    # Set up Google Cloud client and bucket
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)

    # Upload the classifier to Google Cloud Storage
    blob = bucket.blob(GCS_FOLDER + "/" + filename)
    blob.upload_from_filename(filename)


def save_classifier(classifier: XGBClassifier):
    """Save the classifier

    This function saves the classifier and uploads it to Google Cloud Storage.

    Args:
        classifier (XGBClassifier): XGBoost classifier

    """
    # Save the classifier to a local file
    classifier.save_model(MODEL_FILENAME)

    # Upload to Google Cloud Storage
    upload_to_gcs(MODEL_FILENAME)

    # Remove the local file
    os.remove(MODEL_FILENAME)
