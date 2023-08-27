# -*- coding: utf-8 -*-
"""FastAPI application

This module contains FastAPI main application.

"""

from fastapi import FastAPI

from .routers import status

# Initialize the FastAPI application
application = FastAPI()

# Add routers to the FastAPI application
application.include_router(status.router)
