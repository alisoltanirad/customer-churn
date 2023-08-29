# -*- coding: utf-8 -*-
"""Google Cloud Utilities

This module contains functions to read and write data to Google Cloud services.

"""

import json
import os

import joblib
from google.cloud import storage
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier

from .config import GCS_BUCKET, GCS_FOLDER, MODEL_FILENAME, PREPROCESSOR_FILENAME


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


def save_preprocessor(preprocessor: ColumnTransformer):
    """Save the preprocessor

    This function saves the Preprocessing pipeline and uploads it to Google Cloud Storage.

    Args:
        preprocessor (ColumnTransformer): Preprocessing pipeline

    """
    # Save the preprocessor to a local file
    joblib.dump(preprocessor, PREPROCESSOR_FILENAME)

    # Upload to Google Cloud Storage
    upload_to_gcs(PREPROCESSOR_FILENAME)

    # Remove the local file
    os.remove(PREPROCESSOR_FILENAME)


def load_from_gcs(folder_name: str) -> tuple[XGBClassifier, ColumnTransformer]:
    """Load from Google Cloud Storage

    This function downloads the classifier and preprocessor
    from Google Cloud Storage.

    Args:
        folder_name (str): Folder name within the bucket

    Returns:
        XGBClassifier: Classifier
        ColumnTransformer: Preprocessing pipeline

    """
    # Set up Google Cloud client and bucket
    client = storage.Client()
    bucket = client.bucket(GCS_BUCKET)

    # Set the path to the files within the bucket
    classifier_path: str = os.path.join(folder_name, MODEL_FILENAME)
    preprocessor_path: str = os.path.join(folder_name, PREPROCESSOR_FILENAME)

    # Download the model file
    blob = bucket.blob(classifier_path)
    blob.download_to_filename(MODEL_FILENAME)

    # Load XGBoost classifier
    classifier: XGBClassifier = XGBClassifier()
    classifier.load_model(MODEL_FILENAME)

    # Download the preprocessor file
    blob = bucket.blob(preprocessor_path)
    blob.download_to_filename(PREPROCESSOR_FILENAME)

    # Load preprocessing pipeline
    preprocessor = joblib.load(PREPROCESSOR_FILENAME)

    # Remove local files
    os.remove(MODEL_FILENAME)
    os.remove(PREPROCESSOR_FILENAME)

    # Return the classifier and preprocessor
    return classifier, preprocessor
