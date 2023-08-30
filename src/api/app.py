# -*- coding: utf-8 -*-
"""FastAPI application

This module contains FastAPI main application.

"""

from fastapi import FastAPI

from .config import API_TITLE, API_VERSION
from .routers import churn, status

# Initialize the FastAPI application
application = FastAPI(title=API_TITLE, version=API_VERSION)

# Add routers to the FastAPI application
application.include_router(churn.router)
application.include_router(status.router)
