# -*- coding: utf-8 -*-
"""Churn route

This module contains logic for the churn route.

"""

import pandas as pd
from fastapi import APIRouter

from api.config import CHURN_URL
from api.schemas import Request, Response
from logic.config import CATEGORICAL_COLS, GCS_FOLDER
from logic.gc_utils import load_from_gcs
from logic.prediction import predict


router = APIRouter()
classifier, preprocessor = load_from_gcs(GCS_FOLDER)

@router.post(path=CHURN_URL, response_model=Response)
async def customer_churn(request: Request):
    """Customer churn route

    This route is used to predict if each customer churns.

    """
    # Transform input data to feed into a pandas dataframe
    customers: list[dict] = [c.dict() for c in request.customers]

    # Unpack enum values for categorical features
    for customer in customers:
        for feature in CATEGORICAL_COLS:
            customer[feature] = customer[feature].value

    # Create pandas dataframe to feed into the preprocessor
    input_data: pd.DataFrame = pd.DataFrame(customers)

    # Run prediction pipeline (preprocessing, classification) and get the labels
    predictions: pd.Series = predict(classifier, preprocessor, input_data)

    # Transform predictions to be used as output
    labels: list[int] = predictions.tolist()

    # Return predictions
    return {"labels": labels}
