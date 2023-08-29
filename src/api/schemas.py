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
    CreditScore: int = Field(..., title="Credit Score", example=819)
    Geography: Country = Field(..., title="Geography (Country)", example="France")
    Gender: Sex = Field(..., title="Gender", example="Male")
    Age: int = Field(..., title="Age", example=50)
    Tenure: int = Field(..., title="Tenure (Household Size)", example=7)
    Balance: float = Field(..., title="Balance", exampe=10)
    NumOfProducts: int = Field(..., title="Number of Products", example=2)
    HasCrCard: int = Field(..., title="Has Credit Card?", example=1)
    IsActiveMember: int = Field(..., title="Is Active Member?", example=1)
    EstimatedSalary: float = Field(..., title="Estimated Salary", example=10022.8)
    Complain: int = Field(..., title="Has Complain?", example=0)
    Satisfaction_Score: int = Field(..., title="Satisfaction Score", example=2)
    Card_Type: CardType = Field(..., title="Card Type", example="SILVER")
    Point_Earned: int = Field(..., title="Points Earned", example=205)


class Request(BaseModel):
    """Request

    This model represents an API request.

    """
    customers: list[Customer] = Field(title="Customers")


class Response(BaseModel):
    """Response

    This model represents an API response.

    """
    labels: list[int] = Field(title="Customer Churn Predictions", example=[1])
