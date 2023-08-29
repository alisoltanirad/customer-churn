# -*- coding: utf-8 -*-
"""Status route test

This module contains test cases for the API status route.

"""

from fastapi.testclient import TestClient

from src.api.app import application
from src.api.config import STATUS_URL


def test_status():
    """Test status route

    This module contains a test case for the API status route.


    """
    # Create a FastAPI test client
    client = TestClient(application)

    # Make the API request and get the response
    response = client.get(url=STATUS_URL)

    # Compare the expected response with actual response
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
