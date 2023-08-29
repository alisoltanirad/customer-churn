# -*- coding: utf-8 -*-
"""Churn route

This module contains logic for the churn route.

"""

import pandas as pd
from fastapi import APIRouter

from api.schemas import Request, Response
from logic.config import GCS_FOLDER
from logic.gc_utils import load_from_gcs
from logic.prediction import predict


router = APIRouter()
classifier, preprocessor = load_from_gcs(GCS_FOLDER)

@router.post(path="/churn", response_model=Response)
async def customer_churn(request: Request):
    """Customer churn route

    This route is used to predict if each customer churns.

    """
    # Transform input data for prediction
    customers: list[dict] = [c.dict() for c in request.customers]
    input_data: pd.DataFrame = pd.DataFrame(customers)

    # Run prediction pipeline (preprocessing, classification) and get the labels
    predictions: pd.Series = predict(classifier, preprocessor, input_data)

    # Transform predictions to be used as output
    labels: list[int] = predictions.tolist()

    # Return predictions
    return predictions
    
