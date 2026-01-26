"""Data Transfer Objects for Recipe-related operations."""
"""A DTO is an object that carries data between processes. In this case, it is used to transfer recipe data in the application layer."""

from pydantic import BaseModel, Field, validator
from typing import List
from Domain.ValueObject.MeasurementUnit import MeasurementUnit

class IngredientDTO(BaseModel):
    name: str = Field(..., min_length = 2, max_length = 100 ,example="Sugar")
    amount: float = Field(..., gt=0, example=100.0)
    unit: MeasurementUnit = Field(..., example="kg")
    
class CreateRecepieRequest(BaseModel):
    name: str = Field(..., min_length = 2, max_length = 150 ,example="Chocolate Cake")
    description: str = Field(..., max_length = 1000 ,example="A delicious chocolate cake recipe.")
    ingredients: List[IngredientDTO] = Field(..., min_item = 1, example=[
        {"name": "Flour", "amount": 200.0, "unit": "g"},
        {"name": "Sugar", "amount": 100.0, "unit": "g"},
        {"name": "Cocoa Powder", "amount": 50.0, "unit": "g"}
    ])