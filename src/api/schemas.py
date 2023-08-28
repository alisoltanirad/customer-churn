# -*- coding: utf-8 -*-
"""FastAPI application

This module contains the I/O models for the API.

"""

from pydantic import BaseModel, Field


class Customer(BaseModel):
    """Customer

    This model represents a customer and provides features useful for
    predciting if the customer churns.

    """
    CreditScore: int = Field(title="Credit Score")
    Geography: str = Field(title="Geography (Country)")
    Gender: str = Field(title="Gender")
    Age: int = Field(title="Age")
    Tenure: int = Field(title="Tenure (Household Size)")
    Balance: float = Field(title="Balance")
    NumOfProducts: int = Field(title="Number of Products")
    HasCrCard: int = Field(title="Has Credit Card?")
    IsActiveMember: int = Field(title="Is Active Member?")
    EstimatedSalary: float = Field(title="Estimated Salary")
    Complain: int = Field(title="Has Complain?")
    Satisfaction_Score: int = Field(title="Satisfaction Score")
    Card_Type: str = Field(title="Card Type")
    Point_Earned: int = Field(title="Points Earned")


class Request(BaseModel):
    """Request

    This model represents an API request.

    """
    customers: list[Customer] = Field(title="Customers")


class Response(BaseModel):
    """Response

    This model represents an API response.

    """
    result: list[int] = Field(title="Customer Churn Predictions")
