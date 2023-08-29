# -*- coding: utf-8 -*-
"""Status route

This module contains logic for the status route.

"""

from fastapi import APIRouter

from api.config import STATUS_URL


router = APIRouter()

@router.get(STATUS_URL)
async def root():
    """Status route

    This route is used to check if the API is up and running.

    """
    return {"status": "alive"}
