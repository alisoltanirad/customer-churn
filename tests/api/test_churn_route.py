# -*- coding: utf-8 -*-
"""API tests

This module contains test cases for the FastAPI application.

"""

import pytest
from fastapi.testclient import TestClient

from src.api.app import application
from src.api.config import CHURN_URL


@pytest.mark.parametrize(
    "test_name,request_body,expected_code,expected_response",
    [
        (
            "valid_input_returns_success",
            {
                "customers": [
                    {
                        "CreditScore": 821,
                        "Geography": "France",
                        "Gender": "Male",
                        "Age": 50,
                        "Tenure": 7,
                        "Balance": 0,
                        "NumOfProducts": 2,
                        "HasCrCard": 1,
                        "IsActiveMember": 1,
                        "EstimatedSalary": 10022.8,
                        "Complain": 0,
                        "Satisfaction_Score": 2,
                        "Card_Type": "SILVER",
                        "Point_Earned": 205,
                    }
                ]
            },
            200,
            {"labels": [0]},
        ),
        (
            "null_input_returns_error",
            None,
            422,
            {
                "detail": [
                    {
                        "loc": ["body"],
                        "msg": "field required",
                        "type": "value_error.missing",
                    }
                ]
            },
        ),
        (
            "empty_input_returns_error",
            {},
            422,
            {
                "detail": [
                    {
                        "loc": ["body", "customers"],
                        "msg": "field required",
                        "type": "value_error.missing",
                    }
                ]
            },
        ),
    ],
)
def test_api(
    test_name: str, request_body: dict, expected_code: int, expected_response: dict
):
    """Test API

    This module contains API integration test cases for
    customer churn prediction route.

    Args:
        test_name (str): Test case name
        request_body (dict): Request to the API (input)
        expected_code (int): Expected response code
        expected_response (dict): Expected response (output)

    """
    # Create a FastAPI test client
    client = TestClient(application)

    # Make the API request and get the response
    response = client.post(
        url=CHURN_URL,
        json=request_body,
    )

    # Compare the expected response with actual response
    assert response.status_code == expected_code
    assert response.json() == expected_response
