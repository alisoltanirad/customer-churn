# -*- coding: utf-8 -*-
"""FastAPI application

This module contains logic for the status route.

"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    """Status route

    This route is used to check if the API is up and running.

    """
    return {"status": "alive"}
