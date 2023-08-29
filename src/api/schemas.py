# -*- coding: utf-8 -*-
"""FastAPI application

This module contains the I/O models for the API.

"""

from enum import Enum

from pydantic import BaseModel, Field


class Country(Enum):
    FRANCE: str = "France"
    GERMANY: str = "Germany"
    SPAIN: str = "Spain"


class Sex(Enum):
    MALE: str = "Male"
    FEMALE: str = "Female"


class CardType(Enum):
    DIAMOND: str = "DIAMOND"
    GOLD: str = "GOLD"
    SILVER: str = "SILVER"
    PLATINUM: str = "PLATINUM"


class Customer(BaseModel):
    """Customer

    This model represents a customer and provides features useful for
    predciting if the customer churns.

    """
    CreditScore: int = Field(..., title="Credit Score")
    Geography: Country = Field(..., title="Geography (Country)")
    Gender: Sex = Field(..., title="Gender")
    Age: int = Field(..., title="Age")
    Tenure: int = Field(..., title="Tenure (Household Size)")
    Balance: float = Field(..., title="Balance")
    NumOfProducts: int = Field(..., title="Number of Products")
    HasCrCard: int = Field(..., title="Has Credit Card?")
    IsActiveMember: int = Field(..., title="Is Active Member?")
    EstimatedSalary: float = Field(..., title="Estimated Salary")
    Complain: int = Field(..., title="Has Complain?")
    Satisfaction_Score: int = Field(..., title="Satisfaction Score")
    Card_Type: CardType = Field(..., title="Card Type")
    Point_Earned: int = Field(..., title="Points Earned")


class Request(BaseModel):
    """Request

    This model represents an API request.

    """
    customers: list[Customer] = Field(title="Customers")


class Response(BaseModel):
    """Response

    This model represents an API response.

    """
    labels: list[int] = Field(title="Customer Churn Predictions")
