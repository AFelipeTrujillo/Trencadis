"""Data Transfer Objects for Recipe-related operations."""
"""A DTO is an object that carries data between processes. In this case, it is used to transfer recipe data in the application layer."""

from pydantic import BaseModel, Field, validator
from typing import List
from uuid import UUID
from Domain.ValueObject.MeasurementUnit import MeasurementUnit


class IngredientDTO(BaseModel):
    name: str = Field(
        ..., 
        min_length = 2, 
        max_length = 100 ,
        json_schema_extra={"example": "Sugar"}
    )
    amount: float = Field(
        ..., 
        gt=0,
        json_schema_extra={"example": 100.0}
    )
    unit: MeasurementUnit = Field(
        ..., 
        json_schema_extra={"example": "g"}
    )
    
class CreateRecepieRequest(BaseModel):
    name: str = Field(
        ..., 
        min_length = 2, 
        max_length = 150 ,
        json_schema_extra={"example": "Chocolate Cake"}
    )
    description: str = Field(
        ..., 
        max_length = 1000 ,
        json_schema_extra={"example": "A delicious chocolate cake recipe."}
    )
    ingredients: List[IngredientDTO] = Field(
        ..., 
        min_length = 1, 
        json_schema_extra={
            "example": [
                {
                    "name": "Flour",
                    "amount": 200.0,
                    "unit": "g"
                },
                {
                    "name": "Sugar",
                    "amount": 100.0,
                    "unit": "g"
                }
            ]
        }
    )

class RecipeListResponse(BaseModel):
    id: UUID = Field(
        ..., 
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"}
    )
    name: str = Field(
        ..., 
        json_schema_extra={"example": "Chocolate Cake"}
    )
    description: str = Field(
        ..., 
        json_schema_extra={"example": "A delicious chocolate cake recipe."}
    )