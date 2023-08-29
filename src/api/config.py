# -*- coding: utf-8 -*-
"""API Configurations

This module contains configs for the FastAPI application.

"""
# pylint: disable=unused-variable

# API configurations
API_TITLE = "Customer Churn Prediction"
API_VERSION: str = "1.0.0"
API_MAJOR_VERSION: str = API_VERSION.split(".")[0]
API_PREFIX: str = "v" + API_MAJOR_VERSION
STATUS_URL: str = "/"
CHURN_ROUTE: str = "churn"
CHURN_URL = "/" + API_MAJOR_VERSION + "/" + CHURN_ROUTE
